# How to: load the GovernanceRules demo data with one cURL call

`GovernanceRules-demo-data.json` loads the whole test dataset (9 entities, 434 records, see
[../README.md](../README.md)) in **one** call to the REST loads API, under the publisher `SEED`,
and certifies it with the job `INTEGRATE_ALL`.

## Prerequisites

1. **The data product is deployed** to a data location, and the data location is ready
   (status `DL_READY` / *Ready*). Note its **name**: it is `<DataLocationName>` below.
2. **The certification job `INTEGRATE_ALL` exists.** It is part of the model
   (`src/GovernanceRules/jobs/INTEGRATE_ALL.CertificationJob.seml`) and certifies the nine
   entities in dependency order, so nothing to create: it is deployed with the data product.
3. **An API key whose roles include `semarchyConnect` and `GovernanceSteward`.**
   `GovernanceSteward` is the role of the data product that carries `integrationWsRole`
   (the right to load through the REST API); `semarchyConnect` lets the key sign in.
   Both roles must exist on the platform (see `../../platform-administration/`, which also
   holds a key definition, `semDMApiKey_config.json`). Create the key in
   *Configuration > API Keys*, copy its value once: it is `<APIKey>` below.
4. **The data location is empty**, or at least holds no RuleScope and RuleCitation records
   (see *Load once* below).
5. cURL: `curl.exe` ships with Windows 10 and later; on Linux and macOS use `curl`.

Placeholders:

| Placeholder | Example |
|---|---|
| `<TenantURL>` | `https://mytenant.example.com` (no trailing slash) |
| `<DataLocationName>` | `GovernanceRules` |
| `<APIKey>` | the value of the API key |
| `<PathToJson>` | full path to `GovernanceRules-demo-data.json` |

## Load call

### Windows PowerShell

Call `curl.exe`, not `curl` (in Windows PowerShell 5.1, `curl` is an alias of
`Invoke-WebRequest`). Each line ends with a backtick.

```powershell
curl.exe --location --request POST "<TenantURL>/dm/api/rest/loads/<DataLocationName>" `
  --header "Content-Type: application/json" `
  --header "API-Key: <APIKey>" `
  --data-binary "@<PathToJson>"
```

Example of `<PathToJson>`: `C:\accelerators\use-case-models\GovernanceRules\resources\demo-data\API Import-curl\GovernanceRules-demo-data.json`
(keep the double quotes: the folder name contains a space).

### bash (Linux, macOS, Git Bash, WSL)

```bash
curl --location --request POST "<TenantURL>/dm/api/rest/loads/<DataLocationName>" \
  --header "Content-Type: application/json" \
  --header "API-Key: <APIKey>" \
  --data-binary "@<PathToJson>"
```

Use `--data-binary` (not `--data`): it sends the file byte for byte, so the UTF-8 characters
and line breaks of the rule texts arrive unchanged.

## Expected response

The call returns at once, before certification, with HTTP 200 and a body like:

```json
{
  "status": "PERSISTED",
  "load": { "loadId": 42, "batchId": 17, "loadStatus": "PENDING", "...": "..." },
  "persistSummary": { "...": "records persisted per entity" }
}
```

Note the **`loadId`**. `persistSummary` counts the records written to the load, before
certification: it does not tell whether a record failed a validation.

## Check the load status

Poll every few seconds until the status is final:

```powershell
curl.exe --location "<TenantURL>/dm/api/rest/loads/<DataLocationName>/<loadId>" `
  --header "API-Key: <APIKey>"
```

```bash
curl --location "<TenantURL>/dm/api/rest/loads/<DataLocationName>/<loadId>" \
  --header "API-Key: <APIKey>"
```

Read `loadStatus`:

| `loadStatus` | Meaning |
|---|---|
| `PENDING`, `PROCESSING` | the INTEGRATE_ALL job is running: keep polling (it takes under a minute) |
| `DONE` | certified, no record in error |
| `WARNING` | certified, and some records failed a validation: **expected for this dataset**, which contains three deliberate failures (DQ-BAD1, DQ-BAD2, DQ-BAD3) |
| any other value (`ERROR`, `CANCELED`, ...) | the job failed: read the job log of the data location |

The status call can answer a transient HTTP 500: retry it. Then compare the result with the
expected outcome in [../README.md](../README.md#expected-outcome-after-the-first-integrate_all-run):
71 golden rules, 65 in force, 3 rules in error.

## Load once

**Run this load only once per data location.** The entities keyed by `Code` (rules, policies,
regulations, ...) are updated in place by a second load, but **RuleScope and RuleCitation
have generated IDs** (a sequence assigns them at load time): every reload adds 133 scope rows
and 146 citations again, so each rule ends up with duplicate scopes and citations.

To reload from a clean state, either:

- **reset the data location** (recommended): delete the data location and deploy the data
  product again into a new, empty one, then run the load; or
- **delete the child records**: in the GovernanceRules application, signed in with the
  `GovernanceSteward` role (the only role allowed to remove them), select all *Rule scopes*
  and delete them, then all *Citations* (both have a hard-delete action), then reload. Rules,
  policies and reference lists are updated in place. Governance rules themselves cannot be
  deleted (`enableDelete: false`; they are retired through the Rule review workflow).

Do not run the load while another load or job is running on the same data location.
