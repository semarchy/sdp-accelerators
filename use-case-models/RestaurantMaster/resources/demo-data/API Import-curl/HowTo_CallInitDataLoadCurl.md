# How to load the Restaurant Master demo data with one cURL call

## Prerequisites

- The data product is deployed to a data location. Its certification job is `INGEST_ALL`
  (`src/RestaurantMaster/certification_jobs/INGEST_ALL.CertificationJob.seml`), the job the payload names.
- An API key with the `semarchyAdmin` role. Its grant in this data product carries the loads-API right.
- The data location is empty: the payload is the first load (see [the demo-data README](../README.md)).

## cURL command

Run it from the accelerator folder (`RestaurantMaster`). PowerShell:

```powershell
$env:SEMARCHY_API_KEY = "<your-api-key>"

curl.exe --location "https://<your-instance-url>/dm/api/rest/loads/<your-data-location>" `
  --header "Content-Type: application/json" `
  --header "API-Key: $env:SEMARCHY_API_KEY" `
  --data "@resources\demo-data\API Import-curl\RestaurantMaster.json"
```

Bash:

```bash
export SEMARCHY_API_KEY="<your-api-key>"

curl --location "https://<your-instance-url>/dm/api/rest/loads/<your-data-location>" \
  --header "Content-Type: application/json" \
  --header "API-Key: $SEMARCHY_API_KEY" \
  --data "@resources/demo-data/API Import-curl/RestaurantMaster.json"
```

Replace:

- `<your-api-key>` with your API key;
- `<your-instance-url>` with the Semarchy Data Platform instance, without a trailing slash;
- `<your-data-location>` with the data location the data product is deployed to.

The call creates the load, stores the 2,066 records and submits them to `INGEST_ALL` in one step. It returns the
load ID straight away; the certification then runs on the platform for a few minutes. Follow it in the application
(*Data stewardship*) or with `GET https://<your-instance-url>/dm/api/rest/loads/<your-data-location>/<loadId>`.

Do not commit your API key into this file.
