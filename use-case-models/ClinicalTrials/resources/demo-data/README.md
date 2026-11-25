# Clinical Trials MDM — Demo Data

Sample data for the `CTMDM` model: one CSV per entity plus a single consolidated JSON
payload in `persistRecords` form.

| File | Purpose |
| --- | --- |
| `01_*.csv` … `21_*.csv` | One file per entity. The numeric prefix is the safe load order (parents before children). |
| `ClinicalTrialsMDM-demo-data.json` | The same 4,374 records as a single `persistRecords` payload for `CREATE_LOAD_AND_SUBMIT` (~2.1 MB). |

## Record counts

| # | Entity | Type | Rows | Of which deliberate |
| --- | --- | --- | --- | --- |
| 01 | Country | BASIC | 50 | 3 invalid |
| 02 | StudyPhase | BASIC | 10 | 3 invalid |
| 03 | TherapeuticArea | BASIC | 17 | 3 invalid |
| 04 | RegulatoryAuthority | BASIC | 19 | 3 invalid |
| 05 | SiteCapability | BASIC | 23 | 3 invalid |
| 06 | HealthcareOrganization | FUZZY_MATCHED | 145 | 11 duplicates, 4 invalid |
| 07 | ClinicalSite | FUZZY_MATCHED | 167 | 12 duplicates, 5 invalid |
| 08 | EthicsCommittee | FUZZY_MATCHED | 101 | 7 duplicates, 4 invalid |
| 09 | Vendor | FUZZY_MATCHED | 80 | 6 duplicates, 4 invalid |
| 10 | Investigator | FUZZY_MATCHED | 372 | 27 duplicates, 5 invalid |
| 11 | Study | ID_MATCHED | 69 | 5 multi-source, 4 invalid |
| 12 | Protocol | ID_MATCHED | 144 | 4 invalid |
| 13 | ProtocolAmendment | ID_MATCHED | 184 | 4 invalid |
| 14 | MedicalLicense | ID_MATCHED | 324 | 4 invalid |
| 15 | GcpCertification | ID_MATCHED | 304 | 4 invalid |
| 16 | StudyCountry | ID_MATCHED | 264 | 4 invalid |
| 17 | StudySite | ID_MATCHED | 525 | 5 invalid |
| 18 | StudyInvestigator | ID_MATCHED | 484 | 4 invalid |
| 19 | StudyVendor | ID_MATCHED | 164 | 4 invalid |
| 20 | SiteEthicsCommittee | ID_MATCHED | 304 | 4 invalid |
| 21 | SiteCapabilityAssignment | BASIC | 624 | 4 invalid |
| | **Total** | | **4,374** | |

All 27 references in the model are populated, and every foreign key resolves to a
validation-passing parent record.

## Column conventions

- **Enricher outputs are not supplied.** No `Normalized*` or `Phonetized*` column appears in
  any file — `NormalizeXxx` and `PhonetizeXxx` populate those at PRE_CONSO.
- **Fuzzy-matched entities** are keyed by `PublisherID` + `SourceID`. The `LongInteger`
  surrogate golden id (`SiteID`, `OrganizationID`, `InvestigatorID`, `EthicsCommitteeID`,
  `VendorID`) is hub-generated and therefore absent.
- **Foreign keys to a fuzzy entity** use `PublisherID_<role>` + `SourceID_<role>`; no
  `FID_<role>` column is used for those.
- **Foreign keys to BASIC / ID_MATCHED entities** use `FID_<role>`.
- **CSV** prefixes the ID_MATCHED golden id with `Gold_` (e.g. `Gold_StudyID`). **JSON** uses
  the raw attribute name (`StudyID`) so the payload can be posted to the API unmodified.
- Dates are `yyyy-MM-dd`; booleans are `true` / `false`; nulls are empty in CSV and `null`
  in JSON.
- Publisher codes are the model's own: `CTMS`, `CRM`, `CROSource`, `EDC`, `ERP`, `ETMF`,
  `ManualEntry`, `MedicalAffairs`, `RegulatorySystem`, `RIM`. Each entity only uses the
  publishers named in its survivorship rule's ranking.

## Duplicates (fuzzy entities)

Roughly 8% of each fuzzy entity's records are a second source record for an organisation,
site, committee, vendor or investigator that already exists, published by a different source
system. Each pair is built to clear the model's 85 merge threshold:

| Variant | How it differs | Rule that fires |
| --- | --- | --- |
| Case / whitespace | `"  RAVENGLASS TEACHING HOSPITAL …  "` vs `"Ravenglass Teaching Hospital …"` | Strong match, score 95 — the normalized values are identical |
| Punctuation | `"Ashcombe University Hospital Clinical Research-Center."` vs `"… Clinical Research Center"` | Phonetic match, score 88 — the metaphone key is unchanged but the normalized name differs |

`Investigator` duplicates use the same institution with a shortened or nickname first name
and a different email, which fires the institution-based rule at 88.

`Study` additionally carries 5 golden ids published by two source systems each, to exercise
ID-based consolidation and the preferred-publisher survivorship ranking.

## Deliberate validation failures

Every entity that carries validations has 3–5 records that fail them, so the error tables and
the steward workflows have something to show. They are always the trailing rows of each file
and use `-BAD-` in their business key. Coverage is spread across the two kinds of rule:

- **Missing mandatory-by-logic values** — null `SiteName`, `CountryCode`, `OrganizationName`,
  `CommitteeName`, `VendorName`, `VendorType`, `StudyNumber`, `ProtocolNumber`,
  `AmendmentNumber`, `LicenseNumber`, `CertificateNumber`, `CapabilityStatus`,
  `PhaseName`, `TherapeuticAreaName`, `AuthorityName`, `CapabilityName`, investigator
  name and email.
- **Inverted date ranges and negative counts** — deactivation before activation, expiry
  before issue, approval outside the submission/effective window, role end before role
  start, negative enrolment capacity and target, subjects enrolled above target.

Because these rules are `PRE_CONSO`, the failing rows are rejected before consolidation. No
child record references one of them, so a rejected parent never cascades into extra errors.

## Two model behaviours the data works around

1. **`InvestigatorPhoneticMatch`** matches on `NormalizedInstitution` alone at score 88, which
   is above the 85 merge threshold. Any two investigators sharing an institution string would
   auto-merge into one golden record. Each investigator therefore carries a unique
   `Institution` value (`"<organisation> <specialty> Unit <nn>"`), and only the intended
   duplicate pairs repeat it. Worth revisiting the rule — adding a name or licence predicate
   would let the data use realistic shared institution names.

2. **`ClinicalSitePhoneticMatch`** matches on `PhonetizedSiteName` + `NormalizedCity` at score
   88, with no unique identifier to anchor it. Metaphone keys are short, so two unrelated
   sites in the same city can collide and merge. Every genuine site is therefore placed in its
   own city (150 sites across 150 cities); only a deliberate duplicate shares a city with its
   twin. This makes accidental merges impossible regardless of how the metaphone key behaves,
   at the cost of not showing several sites in one metropolitan area.

After the first `INTEGRATE_ALL` run, the expected outcome is 130 golden organisations, 150
golden sites, 90 golden committees, 70 golden vendors and 340 golden investigators.

## Regenerating

`tools/ctmdm-demo-data/gen_demo_data.py` writes this folder; `validate_demo_data.py` checks the
result against the `.seml` model (business-key uniqueness, attribute names and lengths, data
types, publisher codes, referential integrity, validation-failure counts, and match-rule
grouping). Run the generator then the validator after any change to the model structure.
