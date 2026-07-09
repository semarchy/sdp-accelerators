## How to: populate the accelerator model with init demo data, using a cURL call

# Prerequisites

A job INTEGRATE_ALL must have been created under /model_jobs/

## cURL cmd

curl.exe --location "https://&lt;TenantURL&gt;/dm/api/rest/loads/" --header "Content-Type: application/json" --header "API-Key:&lt;APIKey&gt; " ` --data "@&lt;pathtojson&gt;\SalesforceAccelerator.json"