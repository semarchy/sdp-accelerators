#!/usr/bin/env python3
"""Validate the GovernanceRules demo data against the data product model (SEML).

Purpose
    Checks, before anything is loaded, that the generated test dataset
    (../data-files/*.csv and ../API Import-curl/GovernanceRules-demo-data.json)
    will load into the GovernanceRules data product and give the documented
    outcome. The model is read from the SEML files of src/GovernanceRules, so a
    model change that the data does not follow is reported here.

What is checked
    Files     the nine CSVs exist with their NN- load-order prefix, parents numbered
              before children, UTF-8 without BOM, each file < 1 MB; the generated
              files are up to date with ../source (build_demo_data.py --check).
    Model     entity and attribute names, FID_<role> columns of the references,
              no column for a SEQUENCE-generated ID or an enricher output (InForce),
              LOV codes, string lengths, numbers, dates (yyyy-MM-dd), mandatory
              attributes and mandatory references, referential integrity, code
              uniqueness, the INTEGRATE_ALL job and the SEED publisher exist.
    Payload   CREATE_LOAD_AND_SUBMIT header, every entity in optionsPerEntity, and
              the same records as the CSVs.
    Outcome   the SemQL validations RetirementAfterEffective and
              ApprovedRuleHasScope evaluated in Python, the in-force logic of the
              ComputeInForce enricher and of the GovernanceAgent row filter, and the
              expected counts below: only the three deliberate DQ-BAD rows fail,
              one per check, and nothing references them.
    Corpus    rule code format and prefix vs category, statement contains its
              requirement level keyword, every rule cites a regulation, approval
              fields of approved and retired rules, retired rules have a retirement
              date and reason, format patterns compile and match their example,
              pharma extension (POL-GXP) rules scoped only to pharma domains or
              attribute types and generic rules never to them.
    Privacy   e-mail addresses only @example.com; none of the project-specific
              terms given with --deny or --deny-file (company, project, tenant or
              person names that must not ship) in any demo-data file.

Usage
    python validate_demo_data.py                  validate (in-force as of today)
    python validate_demo_data.py --as-of 2026-12-31
    python validate_demo_data.py --seml-root PATH  model folder (default: ../../../src/GovernanceRules)
    python validate_demo_data.py --deny-file PATH  one term per line that must not appear in the data

Standard library only; PyYAML is used when installed, otherwise a minimal
parser that reads the subset of YAML used by the SEML files this validator
reads (entities, references, lists of values, validations, enrichers, jobs,
publishers; not forms or workflows). Paths are relative to
this script. Exit code 0 when clean, 1 on any error.
"""
import argparse
import csv
import io
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DATA_FILES = os.path.join(ROOT, "data-files")
PAYLOAD = os.path.join(ROOT, "API Import-curl", "GovernanceRules-demo-data.json")
DEFAULT_SEML = os.path.normpath(os.path.join(ROOT, "..", "..", "src", "GovernanceRules"))

LOAD_ORDER = ["GovernanceBody", "DataDomain", "DataClassification", "Regulation", "BusinessAttributeType",
              "GovernancePolicy", "GovernanceRule", "RuleScope", "RuleCitation"]
JOB, PUBLISHER = "INTEGRATE_ALL", "SEED"
MAX_BYTES = 1024 * 1024

# Expected outcome. Update together with README.md when the source changes.
EXPECTED_ROWS = {"GovernanceBody": 5, "DataDomain": 11, "DataClassification": 6, "Regulation": 26,
                 "BusinessAttributeType": 27, "GovernancePolicy": 6, "GovernanceRule": 74,
                 "RuleScope": 133, "RuleCitation": 146}
EXPECTED_DELIBERATE = {"RetirementAfterEffective": ["DQ-BAD1"], "ApprovedRuleHasScope": ["DQ-BAD2"],
                       "mandatory Statement": ["DQ-BAD3"]}
EXPECTED_STATUS = {"APPROVED": 65, "DRAFT": 2, "IN_REVIEW": 2, "RETIRED": 2}  # certified rules only
EXPECTED_IN_FORCE = 65
EXPECTED_AGENT = {"GovernanceRule": 65, "RuleScope": 126, "RuleCitation": 139}

CODE_FORMAT = re.compile(r"[A-Z]{2,4}-[0-9]{3}")
BAD_FORMAT = re.compile(r"[A-Z]{2,4}-BAD[0-9]")
PREFIX = {"DQ": "DATA_QUALITY", "PRIV": "PRIVACY", "SEC": "SECURITY_ACCESS", "RET": "RETENTION",
          "REF": "REFERENCE_DATA", "MDM": "IDENTITY_MATCHING", "META": "METADATA_DOCUMENTATION",
          "AI": "AI_USAGE", "STW": "STEWARDSHIP", "MOD": "MODELING_CONVENTIONS"}
PHARMA_POLICY = "POL-GXP"
PHARMA_DOMAINS = {"MEDICINAL_PRODUCT", "HCP", "CLINICAL_SITE"}
PHARMA_TYPES = {"NDC", "NPI", "HCP_LICENSE_NUMBER", "MPID", "PHPID", "TRANSFER_OF_VALUE"}
FORBIDDEN = []  # filled from --deny / --deny-file: keep project-specific names out of this file
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,})")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")

errors = []


def err(msg):
    errors.append(msg)


# --------------------------------------------------------------------------- YAML
def _scalar(text):
    t = text.strip()
    if t in ("", "~", "null"):
        return None
    if t[0] == "'" and t.endswith("'") and len(t) > 1:
        return t[1:-1].replace("''", "'")
    if t[0] == '"' and t.endswith('"') and len(t) > 1:
        return t[1:-1].replace('\\"', '"')
    if t in ("[]", "{}"):
        return [] if t == "[]" else {}
    if t in ("true", "false"):
        return t == "true"
    if re.fullmatch(r"-?\d+", t):
        return int(t)
    return t


def mini_yaml(text):
    """Parse the YAML subset used by SEML: block maps, block lists of maps or
    scalars, plain / single / double quoted scalars that may span lines,
    full-line comments. Enough for the attributes this validator reads."""
    lines = [l.rstrip("\r\n") for l in text.splitlines()]
    lines = [l for l in lines if l.strip() and not l.lstrip().startswith("#")]
    pos = [0]

    def indent(l):
        return len(l) - len(l.lstrip(" "))

    def read_value(first, own_indent):
        # Gather a scalar that may continue on more-indented lines.
        val = first.strip()
        if val[:1] in ("'", '"'):
            q = val[0]
            def closed(v):
                body = v[1:]
                if q == "'":
                    body = body.replace("''", "")
                else:
                    body = body.replace('\\"', "")
                return q in body
            while not closed(val) and pos[0] < len(lines):
                val += " " + lines[pos[0]].strip()
                pos[0] += 1
        else:
            while pos[0] < len(lines) and indent(lines[pos[0]]) > own_indent \
                    and not lines[pos[0]].lstrip().startswith("- "):
                val += " " + lines[pos[0]].strip()
                pos[0] += 1
        return _scalar(val)

    def block(ind):
        if pos[0] >= len(lines):
            return None
        if lines[pos[0]].lstrip().startswith("- ") or lines[pos[0]].strip() == "-":
            return seq(ind)
        return mapping(ind)

    def seq(ind):
        out = []
        while pos[0] < len(lines) and indent(lines[pos[0]]) == ind and lines[pos[0]].lstrip().startswith("-"):
            line = lines[pos[0]]
            rest = line[ind + 1:].lstrip(" ")
            if re.match(r"^[A-Za-z_][\w.]*:(\s|$)", rest):
                # map item: rewrite "- key: v" as "  key: v" and parse a map at ind+2
                lines[pos[0]] = " " * (ind + 2) + rest
                out.append(mapping(ind + 2))
            else:
                pos[0] += 1
                out.append(read_value(rest, ind))
        return out

    def mapping(ind):
        out = {}
        while pos[0] < len(lines) and indent(lines[pos[0]]) == ind and not lines[pos[0]].lstrip().startswith("- "):
            line = lines[pos[0]]
            m = re.match(r"^\s*([^:]+?):(?:\s+(.*))?$", line)
            if not m:
                pos[0] += 1
                continue
            key, val = m.group(1).strip(), m.group(2)
            pos[0] += 1
            if val is None or val.strip() == "":
                if pos[0] < len(lines):
                    nxt = indent(lines[pos[0]])
                    if nxt > ind or (nxt == ind and lines[pos[0]].lstrip().startswith("- ")):
                        out[key] = block(nxt)
                        continue
                out[key] = None
            else:
                out[key] = read_value(val, ind)
        return out

    return block(0) or {}


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    try:
        import yaml  # optional
        return yaml.safe_load(text) or {}
    except ImportError:
        return mini_yaml(text)


# --------------------------------------------------------------------------- model
# The only SEML files read (the minimal parser is checked against PyYAML on these).
MODEL_FILES = (".Entity.seml", ".Reference.seml", ".LOVType.seml", ".SemQLValidation.seml",
               ".SemQLEnricher.seml", ".CertificationJob.seml", ".Publisher.seml")

class Model:
    def __init__(self, root):
        self.entities, self.refs, self.lovs, self.validations, self.enricher_outputs = {}, [], {}, {}, {}
        self.jobs, self.publishers = {}, set()
        for dirpath, _, names in os.walk(root):
            for n in sorted(names):
                if not n.endswith(MODEL_FILES):
                    continue
                d = load_yaml(os.path.join(dirpath, n))
                t = d.get("_type")
                if t == "Entity":
                    self.entities[d["_name"]] = d
                elif t == "Reference":
                    self.refs.append(d)
                elif t == "LOVType":
                    self.lovs[d["_name"]] = {v["code"] for v in d.get("lovValues") or []}
                elif t == "SemQLValidation":
                    self.validations.setdefault(short(d["entity"]), []).append(d["_name"])
                elif t == "SemQLEnricher" and d.get("enricherExecutionScope") not in (None, "NONE"):
                    outs = {e["attributeName"] for e in d.get("semQlEnricherExpressions") or []}
                    self.enricher_outputs.setdefault(short(d["entity"]), set()).update(outs)
                elif t == "CertificationJob":
                    self.jobs[d["_name"]] = d
                elif t == "Publisher":
                    self.publishers.add(d.get("code") or d["_name"])

    def attrs(self, entity):
        return {a["_name"]: a for a in self.entities[entity].get("attributes") or []}

    def refs_from(self, entity):
        """{FID_<role>: (target entity, mandatory)} for references leaving entity."""
        return {"FID_" + r["toRoleName"]: (short(r["toEntity"]), bool(r.get("oneToMany")))
                for r in self.refs if short(r["fromEntity"]) == entity}

    def pk(self, entity):
        return short(self.entities[entity]["primaryKey"])

    def generated_id(self, entity):
        gen = self.entities[entity].get("sourceIdGeneration") or {}
        return gen.get("mode") == "SEQUENCE"


def short(qualified):
    return str(qualified).rsplit(".", 1)[-1]


# --------------------------------------------------------------------------- data
def read_csv(path):
    with open(path, "rb") as f:
        raw = f.read()
    if raw.startswith(b"\xef\xbb\xbf"):
        err(f"{os.path.basename(path)}: starts with a UTF-8 BOM")
        raw = raw[3:]
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        err(f"{os.path.basename(path)}: not UTF-8 ({e})")
        text = raw.decode("utf-8", "replace")
    rows = list(csv.reader(io.StringIO(text, newline="")))
    header, body = rows[0], rows[1:]
    out = []
    for i, r in enumerate(body, 2):
        if len(r) != len(header):
            err(f"{os.path.basename(path)} line {i}: {len(r)} cells for {len(header)} columns")
            continue
        out.append({h: (v if v != "" else None) for h, v in zip(header, r)})
    return header, out, len(raw)


def as_date(v):
    if v is None:
        return None
    if not ISO_DATE.fullmatch(v):
        return "bad"
    try:
        return date.fromisoformat(v)
    except ValueError:
        return "bad"


def check_value(entity, key, attr, model, v):
    dt = attr.get("dataType")
    where = f"{entity} {key}: {attr['_name']}"
    if v is None:
        return
    if dt == "String":
        if attr.get("length") and len(v) > attr["length"]:
            err(f"{where} is {len(v)} characters, longer than {attr['length']}")
    elif dt == "Date":
        if as_date(v) == "bad":
            err(f"{where} = {v!r} is not a yyyy-MM-dd date")
    elif dt == "Boolean":
        if v not in ("true", "false"):
            err(f"{where} = {v!r} is not true/false")
    elif dt in ("Integer", "LongInteger", "Decimal"):
        if not re.fullmatch(r"-?\d+(\.\d+)?", v):
            err(f"{where} = {v!r} is not a number")
        elif attr.get("precision") and len(v.lstrip("-").split(".")[0]) > attr["precision"]:
            err(f"{where} = {v} exceeds precision {attr['precision']}")
    elif dt and short(dt) in model.lovs:
        if v not in model.lovs[short(dt)]:
            err(f"{where} = {v!r} is not a code of LOV {short(dt)}")


def norm_json(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    return None if v is None else str(v)


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seml-root", default=DEFAULT_SEML, help="data product folder (default: %(default)s)")
    ap.add_argument("--as-of", default=None, help="date of the in-force evaluation, yyyy-MM-dd (default: today)")
    ap.add_argument("--deny", action="append", default=[], help="term that must not appear in the demo data (repeatable)")
    ap.add_argument("--deny-file", default=None, help="file with one denied term per line (# for comments)")
    args = ap.parse_args()
    FORBIDDEN.extend(t.lower() for t in args.deny)
    if args.deny_file:
        with open(args.deny_file, encoding="utf-8") as f:
            FORBIDDEN.extend(t.strip().lower() for t in f if t.strip() and not t.startswith("#"))
    as_of = date.fromisoformat(args.as_of) if args.as_of else date.today()

    if not os.path.isdir(args.seml_root):
        print(f"ERROR: model folder not found: {args.seml_root}")
        return 1
    model = Model(args.seml_root)

    # ---- build is up to date
    sys.path.insert(0, HERE)
    sys.dont_write_bytecode = True  # leave no __pycache__ in the accelerator folder
    try:
        import build_demo_data as build
        for path, text in build.build().items():
            current = open(path, encoding="utf-8", newline="").read() if os.path.exists(path) else None
            if current != text:
                err(f"{os.path.relpath(path, ROOT)} is out of date with source/: run build_demo_data.py")
    except Exception as e:  # noqa: BLE001 - report any build failure as a finding
        err(f"build_demo_data.py could not run: {e}")

    # ---- model-level prerequisites
    if JOB not in model.jobs:
        err(f"certification job {JOB} not found in the model")
    else:
        job_text = json.dumps(model.jobs[JOB])
        for e in LOAD_ORDER:
            if e not in job_text:
                err(f"job {JOB} does not certify {e}")
    if PUBLISHER not in model.publishers:
        err(f"publisher {PUBLISHER} not found in the model")
    for e in model.entities:
        if e not in LOAD_ORDER:
            err(f"model entity {e} has no demo data file")

    # ---- files
    files = sorted(f for f in os.listdir(DATA_FILES) if f.endswith(".csv")) if os.path.isdir(DATA_FILES) else []
    expected_files = [f"{i:02d}-{e}.csv" for i, e in enumerate(LOAD_ORDER, 1)]
    if files != expected_files:
        err(f"data-files/ holds {files}, expected {expected_files}")
    data, headers = {}, {}
    for i, e in enumerate(LOAD_ORDER, 1):
        path = os.path.join(DATA_FILES, f"{i:02d}-{e}.csv")
        if not os.path.exists(path):
            continue
        headers[e], data[e], size = read_csv(path)
        if size >= MAX_BYTES:
            err(f"{os.path.basename(path)}: {size} bytes, not under 1 MB")
    if os.path.exists(PAYLOAD) and os.path.getsize(PAYLOAD) >= MAX_BYTES:
        err("payload is not under 1 MB")

    # ---- columns, values, keys
    keys = {}
    for e in LOAD_ORDER:
        if e not in data:
            continue
        if e not in model.entities:
            err(f"{e}: not an entity of the model")
            continue
        ent = model.entities[e]
        if ent.get("entityType") != "BASIC":
            err(f"{e}: entity type {ent.get('entityType')}, the FID_ convention assumes BASIC")
        attrs, refs = model.attrs(e), model.refs_from(e)
        pk = model.pk(e)
        computed = model.enricher_outputs.get(e, set())
        for col in headers[e]:
            if col.startswith("FID_"):
                if col not in refs:
                    err(f"{e}: column {col} is not a reference role of the entity (roles: {sorted(refs)})")
            elif col not in attrs:
                err(f"{e}: column {col} is not an attribute of the entity")
            elif col in computed:
                err(f"{e}: column {col} is computed by an enricher and must not be loaded")
            elif col == pk and model.generated_id(e):
                err(f"{e}: column {col} is generated by a SEQUENCE and must not be loaded")
        for col in refs:
            if col not in headers[e]:
                err(f"{e}: reference column {col} is missing")
        for a, spec in attrs.items():
            if spec.get("mandatory") and a not in headers[e] and not (a == pk and model.generated_id(e)) \
                    and a not in computed:
                err(f"{e}: mandatory attribute {a} has no column")
        # parent files numbered before child files
        for col, (target, _) in refs.items():
            if target in LOAD_ORDER and LOAD_ORDER.index(target) > LOAD_ORDER.index(e):
                err(f"{e}: references {target}, which is loaded after it")
        if not model.generated_id(e):
            codes = [r.get(pk) for r in data[e]]
            dup = sorted({c for c in codes if codes.count(c) > 1 and c is not None})
            if dup:
                err(f"{e}: duplicate {pk} {dup}")
            keys[e] = set(codes)

    mandatory_failures = {}
    for e in LOAD_ORDER:
        if e not in data or e not in model.entities:
            continue
        attrs, refs, pk = model.attrs(e), model.refs_from(e), model.pk(e)
        for i, r in enumerate(data[e], 1):
            key = r.get(pk) or f"row {i}"
            for a, v in r.items():
                if a in attrs:
                    check_value(e, key, attrs[a], model, v)
                    if attrs[a].get("mandatory") and v is None:
                        mandatory_failures.setdefault(f"mandatory {a}", []).append(key)
                elif a in refs:
                    target, mandatory = refs[a]
                    if v is None:
                        if mandatory:
                            mandatory_failures.setdefault(f"mandatory reference {a}", []).append(key)
                    elif v not in keys.get(target, set()):
                        err(f"{e} {key}: {a} = {v!r} not found in {target}")

    rules = {r["Code"]: r for r in data.get("GovernanceRule", [])}
    bad = {c for c in rules if "BAD" in c}

    # ---- children never reference a deliberate failure
    for e in ("RuleScope", "RuleCitation"):
        for i, r in enumerate(data.get(e, []), 1):
            if r.get("FID_Rule") in bad:
                err(f"{e} row {i}: references the deliberate failure {r['FID_Rule']}")
    scopes, cites = {}, {}
    for r in data.get("RuleScope", []):
        scopes.setdefault(r["FID_Rule"], []).append(r)
    for r in data.get("RuleCitation", []):
        cites.setdefault(r["FID_Rule"], []).append(r)
    seen = set()
    for r in data.get("RuleScope", []):
        t = tuple(r.values())
        if t in seen:
            err(f"RuleScope: duplicate scope row {t}")
        seen.add(t)

    # ---- SemQL validations evaluated in Python
    failing = dict(mandatory_failures)
    for code, r in rules.items():
        eff, ret = as_date(r.get("EffectiveDate")), as_date(r.get("RetirementDate"))
        # RetirementDate IS NULL OR EffectiveDate IS NULL OR RetirementDate > EffectiveDate
        if eff not in (None, "bad") and ret not in (None, "bad") and not ret > eff:
            failing.setdefault("RetirementAfterEffective", []).append(code)
        # LifecycleStatus <> 'APPROVED' OR any Scopes have (1 = 1)
        if r.get("LifecycleStatus") == "APPROVED" and not scopes.get(code):
            failing.setdefault("ApprovedRuleHasScope", []).append(code)
    for v in ("RetirementAfterEffective", "ApprovedRuleHasScope"):
        if v not in model.validations.get("GovernanceRule", []):
            err(f"validation {v} not found on GovernanceRule in the model: update this validator")
    if {k: sorted(v) for k, v in failing.items()} != EXPECTED_DELIBERATE:
        err(f"records failing a check {dict(sorted(failing.items()))}, expected {EXPECTED_DELIBERATE}")
    failed_codes = {c for v in failing.values() for c in v}
    if failed_codes != bad:
        err(f"rows marked BAD {sorted(bad)} differ from rows that fail {sorted(failed_codes)}")
    for code in bad:
        if not BAD_FORMAT.fullmatch(code):
            err(f"{code}: a deliberate failure code must look like DQ-BAD1")
        if not (rules[code].get("Title") or "").startswith("[DELIBERATE FAILURE]"):
            err(f"{code}: title must start with [DELIBERATE FAILURE]")
    if bad and list(rules)[-len(bad):] != sorted(bad):
        err("the deliberate failures must be the trailing GovernanceRule rows")

    # ---- certified result: counts, status, in force, agent view
    good = {c: r for c, r in rules.items() if c not in failed_codes}
    counts = {e: len(rows) for e, rows in data.items()}
    if counts != EXPECTED_ROWS:
        err(f"row counts {counts}, expected {EXPECTED_ROWS}")
    status = {}
    for r in good.values():
        status[r["LifecycleStatus"]] = status.get(r["LifecycleStatus"], 0) + 1
    if status != EXPECTED_STATUS:
        err(f"certified rules by status {status}, expected {EXPECTED_STATUS}")

    def in_force(r):  # ComputeInForce enricher and GovernanceAgent row filter
        eff, ret = as_date(r.get("EffectiveDate")), as_date(r.get("RetirementDate"))
        return (r.get("LifecycleStatus") == "APPROVED" and eff not in (None, "bad") and eff <= as_of
                and (ret is None or (ret != "bad" and ret > as_of)))
    force = {c for c, r in good.items() if in_force(r)}
    agent = {"GovernanceRule": len(force),
             "RuleScope": sum(len(scopes.get(c, [])) for c in force),
             "RuleCitation": sum(len(cites.get(c, [])) for c in force)}
    if len(force) != EXPECTED_IN_FORCE:
        err(f"{len(force)} rules in force on {as_of}, expected {EXPECTED_IN_FORCE}")
    if agent != EXPECTED_AGENT:
        err(f"GovernanceAgent sees {agent} on {as_of}, expected {EXPECTED_AGENT}")

    # ---- corpus consistency (certified rules)
    for code, r in good.items():
        if not CODE_FORMAT.fullmatch(code):
            err(f"{code}: code format, expected for example DQ-001")
        if PREFIX.get(code.split("-")[0]) != r.get("Category"):
            err(f"{code}: prefix does not match category {r.get('Category')}")
        if r.get("RequirementLevel") and not re.search(r"\b" + r["RequirementLevel"] + r"\b", r.get("Statement") or ""):
            err(f"{code}: statement does not contain {r['RequirementLevel']}")
        for a in ("Title", "Rationale", "ImplementationGuidance", "Example", "ImplementationPattern", "EffectiveDate"):
            if not r.get(a):
                err(f"{code}: empty {a}")
        st = r.get("LifecycleStatus")
        if st in ("APPROVED", "RETIRED") and not (r.get("ApprovedOn") and r.get("ApprovedBy")):
            err(f"{code}: {st} without ApprovedOn / ApprovedBy")
        if st in ("DRAFT", "IN_REVIEW") and (r.get("ApprovedOn") or r.get("ApprovedBy")):
            err(f"{code}: {st} with approval fields")
        if st == "RETIRED" and not (r.get("RetirementDate") and r.get("RetirementReason")):
            err(f"{code}: RETIRED without RetirementDate and RetirementReason")
        if st == "APPROVED" and code not in force:
            err(f"{code}: APPROVED but not in force on {as_of}")
        if not cites.get(code):
            err(f"{code}: no citation")
        pharma = r.get("FID_Policy") == PHARMA_POLICY
        for s in scopes.get(code, []):
            is_ph = s.get("FID_DataDomain") in PHARMA_DOMAINS or s.get("FID_AttributeType") in PHARMA_TYPES
            if pharma and not is_ph:
                err(f"{code}: pharma rule has a scope row reaching non-pharma designs {s}")
            if not pharma and is_ph:
                err(f"{code}: generic rule scoped to a pharma domain or attribute type {s}")
    for r in data.get("RuleCitation", []):
        if not r.get("Clause"):
            err(f"RuleCitation of {r.get('FID_Rule')}: empty Clause")
    for a in data.get("BusinessAttributeType", []):
        if a.get("FormatPattern"):
            try:
                if a.get("Example") and not re.match(a["FormatPattern"], a["Example"]):
                    err(f"BusinessAttributeType {a['Code']}: example does not match FormatPattern")
            except re.error as e:
                err(f"BusinessAttributeType {a['Code']}: invalid regex ({e})")
    for c in data.get("DataClassification", []):
        if c.get("SensitivityRank") and not 1 <= int(c["SensitivityRank"]) <= 5:
            err(f"DataClassification {c['Code']}: SensitivityRank out of 1..5")

    # ---- payload
    if not os.path.exists(PAYLOAD):
        err("API payload not found")
    else:
        with open(PAYLOAD, encoding="utf-8") as f:
            p = json.load(f)
        po = p.get("persistOptions", {})
        for k, v in {"action": "CREATE_LOAD_AND_SUBMIT", "jobName": JOB}.items():
            if p.get(k) != v:
                err(f"payload {k} = {p.get(k)!r}, expected {v!r}")
        for k, v in {"defaultPublisherId": PUBLISHER, "missingIdBehavior": "GENERATE",
                     "persistMode": "ALWAYS", "responsePayload": "SUMMARY"}.items():
            if po.get(k) != v:
                err(f"payload persistOptions.{k} = {po.get(k)!r}, expected {v!r}")
        recs = p.get("persistRecords", {})
        if list(recs) != LOAD_ORDER:
            err(f"payload entities {list(recs)}, expected {LOAD_ORDER}")
        if set(po.get("optionsPerEntity") or {}) != set(recs):
            err("payload optionsPerEntity must list every entity of persistRecords")
        for e, rows in recs.items():
            csv_rows = data.get(e, [])
            if len(rows) != len(csv_rows):
                err(f"payload {e}: {len(rows)} records, CSV has {len(csv_rows)}")
                continue
            for i, (j, c) in enumerate(zip(rows, csv_rows), 1):
                jn = {k: norm_json(v) for k, v in j.items() if v is not None}
                cn = {k: v for k, v in c.items() if v is not None}
                if jn != cn:
                    err(f"payload {e} record {i} differs from the CSV row")
                    break
                if any(v is not None and not isinstance(v, str) for k, v in j.items() if k.startswith("FID_")):
                    err(f"payload {e} record {i}: FID_ values of Code keys must be strings")

    # ---- privacy
    for dirpath, _, names in os.walk(ROOT):
        for n in names:
            if not n.endswith((".csv", ".json", ".md", ".py")) or n == os.path.basename(__file__):
                continue
            path = os.path.join(dirpath, n)
            with open(path, encoding="utf-8", errors="replace") as f:
                text = f.read()
            low = text.lower()
            for word in FORBIDDEN:
                if word in low:
                    err(f"{os.path.relpath(path, ROOT)}: contains the project-specific name {word!r}")
            for m in EMAIL.finditer(text):
                if m.group(1).lower() != "example.com":
                    err(f"{os.path.relpath(path, ROOT)}: e-mail address {m.group(0)!r} is not @example.com")

    # ---- report
    if errors:
        print(f"NOT OK - {len(errors)} error(s):")
        for e in errors:
            print(" -", e)
        return 1
    print(f"OK - {sum(counts.values())} rows in {len(counts)} files; "
          + ", ".join(f"{e} {n}" for e, n in counts.items()))
    print(f"     deliberate failures: " + ", ".join(f"{k} -> {', '.join(v)}" for k, v in sorted(failing.items())))
    print(f"     certified rules by status {status}; in force on {as_of}: {len(force)}; "
          f"GovernanceAgent sees {agent}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
