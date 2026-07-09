# PrivateEquity Curl Import

This folder contains a generated Semarchy REST load package for the `AL_PrivateEquity` data location.

The payloads are derived from:

- `src/PrivateEquity/entities/*.Entity.seml`
- `src/PrivateEquity/references/*.Reference.seml`
- old xDM SQL files under `demo data`

Runtime conventions mirror the Automative curl import package:

- `action`: `CREATE_LOAD_AND_SUBMIT`
- `programName`: `curl`
- `jobName`: `INTEGRATE_ALL`
- `persistOptions.responsePayload`: `SUMMARY`
- `persistOptions.persistMode`: `ALWAYS`
- `persistOptions.missingIdBehavior`: `GENERATE`

The new model job expected by these payloads is `src/PrivateEquity/model_jobs/INTEGRATE_ALL.ModelJob.seml`.

## Phase Payloads

| Phase | File | Records | Entities |
| --- | --- | ---: | --- |
| 01 | `Phase01_NameType_Load.json` | 3 | `NameType` |
| 02 | `Phase02_FoundationalReferenceData_Load.json` | 682 | `InvestmentStructure`, `Industry`, `GroupType`, `GeographyType`, `EntityType`, `Currency`, `Country`, `Region`, `AccountType`, `Bank`, `EntityRole`, `EntityStructure`, `Status`, `Category`, `Relationship`, `Startegy` |
| 03 | `Phase03_DependentReferenceData_Load.json` | 102 | `State`, `Subcategory`, `Form` |
| 04 | `Phase04_FundPortfolio_Load.json` | 240 | `Fund`, `Portfolio` |
| 05 | `Phase05_LegalEntity_Load.json` | 602 | `LegalEntity` |
| 06 | `Phase06_LegalEntityRelationships_Load.json` | 600 | `LERelationship`, `ParentChild` |
| 07 | `Phase07_FundPortfolioLegalEntityLinks_Load.json` | 2 | `FundLE`, `PortfolioLegalEntity` |
| 08 | `Phase08_LEGroupHierarchy_Load.json` | 85 | `LEGroup`, `GroupHierarchy`, `GroupLegalEntity` |
| 09 | `Phase09_NamesOfficesContacts_Load.json` | 576 | `Name`, `Office`, `Contact` |
| 10 | `Phase10_Documents_Load.json` | 1,192 | `Document` |
| 11 | `Phase11_Accounts_Load.json` | 200 | `Account` |

## Run Order

Run the phase payloads in numeric order. Later phases contain references to records loaded by earlier phases.

`LegalEntity` is the FUZZY entity in this model. Its payload uses `PublisherID` and `SourceID` from `sd_legal_entity`.
Child references to `LegalEntity` use the Semarchy REST fuzzy-reference pattern: `PublisherID_<role>`, `SourceID_<role>`, and `FID_<role>: null`.

Complex address attributes use Semarchy REST dot notation, for example `InputAddress.AddressLine` and `SourceAddress.City`.

`Fund` and `Portfolio` are intentionally loaded in one phase. The model has references in both directions, although the current xDM SQL has null `Fund.Portfolio` values and populated `Portfolio.Fund` values.

## Files

- `DemoDataInfo.csv`: model inventory in entity-name order.
- `DemoDataInfo.sorted-by-dependency.csv`: same inventory ordered by the generated phase sequence.
- `Phase*_Load.json`: REST load payloads.
- `RM-temp_CallInitDataloadCurl.md`: PowerShell curl commands using the sandbox tenant and `AL_PrivateEquity` data location.
- `run_all_curl.ps1`: convenience loader that runs all phases in order.
- `generate_curl_import.py`: generator used to rebuild this package from SEML and SQL sources.
- `SourceValueRepairs.md`: inferred values applied to incomplete SQL source rows.
- `SkippedRecords.md`: source records skipped because they could not satisfy mandatory references after source-reference resolution.

## Reference Repairs

The generator nulls source foreign IDs that do not resolve to records present in the generated payloads, then skips any records left without a mandatory reference. Skipped records are listed separately.

- `GroupLegalEntity` row 9: `FID_LEGroup` source value `5` did not resolve to `LEGroup` and was set to null.
- `GroupLegalEntity` row 10: `FID_LEGroup` source value `5` did not resolve to `LEGroup` and was set to null.
- `GroupLegalEntity` row 11: `FID_LEGroup` source value `4` did not resolve to `LEGroup` and was set to null.
- `GroupLegalEntity` row 12: `FID_LEGroup` source value `4` did not resolve to `LEGroup` and was set to null.
- `GroupLegalEntity` row 13: `FID_LEGroup` source value `4` did not resolve to `LEGroup` and was set to null.
- `GroupLegalEntity` row 14: `FID_LEGroup` source value `3` did not resolve to `LEGroup` and was set to null.
- `GroupLegalEntity` row 15: `FID_LEGroup` source value `3` did not resolve to `LEGroup` and was set to null.

## Skipped Source Records

The generator skipped source records that could not satisfy mandatory references after source-reference resolution. See `SkippedRecords.md` for the full list.

- `GroupLegalEntity` ID 13: skipped because mandatory reference(s) `LEGroup` were missing after source-reference resolution.
- `GroupLegalEntity` ID 12: skipped because mandatory reference(s) `LEGroup` were missing after source-reference resolution.
- `GroupLegalEntity` ID 10: skipped because mandatory reference(s) `LEGroup` were missing after source-reference resolution.
- `GroupLegalEntity` ID 9: skipped because mandatory reference(s) `LEGroup` were missing after source-reference resolution.
- `GroupLegalEntity` ID 8: skipped because mandatory reference(s) `LEGroup` were missing after source-reference resolution.
- `GroupLegalEntity` ID 5: skipped because mandatory reference(s) `LEGroup` were missing after source-reference resolution.
- `GroupLegalEntity` ID 4: skipped because mandatory reference(s) `LEGroup` were missing after source-reference resolution.

## Mandatory Data Checks

No missing mandatory attributes/references were detected in the generated payloads.
