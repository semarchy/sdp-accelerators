# This readme.md file contains the plugin enrichers for which the parameter values  needs to  be udpated in plugin parameters.
### example: 
pluginParams:
  - paramName: PARAM_CLIENT_ID
    value: &lt;GoogleAPIKey&gt;


|Entity Name | Enricher | ParamName | Value|
|------------|---------------|-----------|------|
|Account     |\src\sales360\entities\Account\enrichers\GeocodedBillingAddress.JavaPluginEnricher.seml|PARAM_CLIENT_ID| GoogleAPIKey |
|Account     |\src\sales360\entities\Account\enrichers\GeocodedShippingAddress.JavaPluginEnricher.seml|PARAM_CLIENT_ID| GoogleAPIKey |
|Contact     |\src\sales360\entities\Account\enrichers\GeocodedMailingAddress.JavaPluginEnricher.seml|PARAM_CLIENT_ID| GoogleAPIKey |
|Contact     |\src\sales360\entities\Account\enrichers\GeocodedOtherAddress.JavaPluginEnricher.seml|PARAM_CLIENT_ID| GoogleAPIKey |
|Leads       |\src\sales360\entities\Account\enrichers\GeoCodedAddress.JavaPluginEnricher.seml|PARAM_CLIENT_ID| GoogleAPIKey |

# Value for Google API Key needs to be updated in forms using the Google Map APIs.
### example:
 http://google.com/api/js?key= &lt;GoogleAPIKey&gt;

|Entity Name | FormName | Section | Key |
|------------|------------|-----------|------|
|Account     |\src\sales360\entities\Account\forms\AccountBrowsingForm.Form.seml| GMapBilling |Google API Key |
|Account     |\src\sales360\entities\Account\forms\AccountBrowsingForm.Form.seml| GMapShipping |Google API Key|