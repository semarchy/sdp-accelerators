## Rest Client Deployment

Use the following commands to deploy the NPPES REST client configurations into the SEM DM admin service. Run them from a terminal with access to the target environment and authenticate your Platform CLI .

```cmd
sem dm admin rest-client set NPPESGetNPI -i "HCO-HCP RestClient_NPPESGetNPI.json"
sem dm admin rest-client set NPPESRestAPI -i "HCO-HCP RestClient_NPPESRestAPI.json"
```
