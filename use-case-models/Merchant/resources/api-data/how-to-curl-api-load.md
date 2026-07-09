# How to: populate the accelerator model with init demo data, using a curl call

## Prerequisites
A job INTEGRATE_ALL must have been created under <model>/model_jobs/

## curl cmd
curl.exe --location "https://<your-tenant-url>/dm/api/rest/loads/<your-data-location>" `
  --header "Content-Type: application/json" `
  --header "API-Key: <your-personal-API-key>" `
  --data "@<your-file-location>\merchant_api_load_payload.json"