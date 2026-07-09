# Automotive Manufacturing API Import

This folder contains the deployment-ready API import payload for the Automotive / Manufacturing accelerator demo dataset.

## Payload

| File | Purpose |
| --- | --- |
| `AutoManufInitDataLoad.json` | Combined 3,517-record story demo dataset. |
| `StoryDemo_DataGenerationReport.md` | Data generation summary and scenario anchors. |

## Import Command

Run this command from the accelerator workspace root.

```powershell
$env:SEMARCHY_API_KEY = "<your-api-key>"

curl.exe --location "https://<your-instance-url>/dm/api/rest/loads/AL_AutoManuf" `
  --header "Content-Type: application/json" `
  --header "API-Key: $env:SEMARCHY_API_KEY" `
  --data "@resources\demo-data\API Import-curl\AutoManufInitDataLoad.json"
```

Replace:

- `<your-api-key>` with your personal or integration API key.
- `<your-instance-url>` with the target Semarchy Data Platform instance URL.

Do not commit personal API keys into this file.
