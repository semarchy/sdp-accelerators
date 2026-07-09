## How to: populate the SAP Product Material 360 model with init demo data, using a cURL call

# Prerequisites
A job INTEGRATE_ALL must have been created under /model_jobs/

## cURL cmd
curl.exe --location "https://<TenantURL>/dm/api/rest/loads/" --header "Content-Type: application/json" --header "API-Key:<APIKey> " ` --data "@<pathtojson>\SAPProductMaterial360.json"

## Storage Location geocoding sample data

The `StorageLocation` records in `SAPProductMaterial360.json` include the source-provided geocoding input fields: `InpAddressLine`, `InpCity`, `InpState`, `InpPostalCode`, and `InpCountry`.

Do not populate the Google Maps `Geo*` output fields in the API payload. Those fields are produced by the `GeocodedStorageLocationAddress` Java plugin enricher during integration.
