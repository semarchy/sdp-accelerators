## How to: populate the SAP Business Partner 360 model with init demo data, using a cURL call

# Prerequisites

- A job `INTEGRATE_ALL` must exist under `/model_jobs/` (it does, as `sapbp360.model_jobs.INTEGRATE_ALL`).
- The model must be deployed to a data location, and you need an API key with load privileges.

# What the payload does

`SAPBusinessPartner360.json` is a single `CREATE_LOAD_AND_SUBMIT` request that:
- loads every entity (reference/code lists first, then the fuzzy hubs, then their children) with `defaultPublisherId: CRM`;
- uses `persistMode: ALWAYS` so records that fail validations are still loaded and surface in the **Manage > Source Errors** views;
- lets Semarchy generate golden/master ids (`missingIdBehavior: GENERATE`).

Foreign keys to fuzzy entities (Business Partner, Supplier, Supplier Purchasing Org, BP Address) are expressed with `SourceID_<role>` + `PublisherID_<role>`; foreign keys to reference/basic entities use `FID_<role>`.

# cURL cmd

```
curl.exe --location "https://<TenantURL>/dm/api/rest/loads/<DataLocationName>" `
  --header "Content-Type: application/json" `
  --header "API-Key: <APIKey>" `
  --data "@<pathtojson>\SAPBusinessPartner360.json"
```

# Notes

- The JSON is generated from the CSV files in `../` (the numbered `NN-<Entity>.csv` files) and is kept consistent with them. If the CSVs are regenerated, regenerate this JSON too.
- The fuzzy entities contain ~10% intentional duplicates that consolidate through the match rules, and each validated entity contains 3-5 intentionally bad records for testing the validations and the Source Errors views.
