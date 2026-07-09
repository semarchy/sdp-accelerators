# Manufacturing and Automotive Accelerator - Enrichers

This page summarizes the enrichers defined in the Manufacturing model. Use it to understand what is automated, which attributes are enriched, and which plugins or expressions are required.

Notes:
- Labels reflect the model configuration.
- Java plugin enrichers require the relevant plugin and runtime configuration to be available.
- SemQL enrichers execute in the model pipeline and do not require external services.
- Plugin parameter values are intentionally not listed here.

Related pages:
- [model structure](./model_structure.md)
- [user guide](./user_guide.md)
- [validations](./validations.md)

This table summarizes the enrichers defined in the Manufacturing model, including their entity, name, type, label, description, enriched attribute, and expression or plugin.

| Entity name | Enricher name | Enricher type | Enricher label | Enricher description | Enriched attribute | Enricher expression / Plugin |
|---|---|---|---|---|---|---|
| Address | GeocodeUsingGoogle | JavaPluginEnricher | Geocode Using Google | Uses Google Maps geocoding to enrich address input fields with standardized location components and coordinates. | `GeocodedLattitude`, `GeocodedCountry`, `GeocodedLongitude`, `GeocodedStreetName`, `GeocodedPostalCode`, `GeocodedState`, `GeocodedStreetNumber`, `GeocodedLocality` | `plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher; inputs: InputAddressLine, FDN_InputCountry, InputZipCode, SEM_CONCAT( ', ','1', InputCity, FDN_InputState)` |
| Customer | CleanseEmail | JavaPluginEnricher | Cleanse Email | Cleanses and validates customer email addresses to produce standardized email and domain quality outputs. | `CleansedEmail`, `ValidEmailDomain` | `plugin: com.semarchy.engine.plugins.convergence.email; inputs: SourceEmail` |
| Customer | FillInUnknownNicknames | SemQLEnricher | Fill In Unknown Nicknames | Fills missing customer nickname values from the lowercased first name so matching logic has a usable fallback. | `Nickname` | `Condition: Nickname is null; Nickname = LOWER ( FirstName )` |
| Customer | GeocodeUsingGoogle | JavaPluginEnricher | Geocode Using Google | Uses Google Maps geocoding to enrich customer address inputs with standardized location components and coordinates. | `GeocodedCountry`, `GeocodedLocality`, `GeocodedLongitude`, `GeocodedState`, `GeocodedStreetNumber`, `GeocodedPostalCode`, `GeocodedLatitude`, `GeocodedStreetName` | `plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher; inputs: InputCountry, InputAddressLine, InputCity, InputZipCode` |
| Customer | Household | JavaPluginEnricher | Household | Looks up a household address from geocoded street information to group customers at the same household. | `HouseholdID` | `plugin: com.semarchy.engine.plugins.convergence.lookup; inputs: GeocodedStreetName` |
| Customer | HouseholdIDToInteger | SemQLEnricher | Household ID To Integer | Converts the household identifier returned by lookup into the numeric foreign key used for household relationships. | `FID_Household` | `FID_Household = SEM_CAST_NUMERIC(HouseholdID)` |
| Customer | LookupNickname | JavaPluginEnricher | Lookup Nickname | Looks up common nicknames for the customer first name to support household analysis and fuzzy matching. | `Nickname` | `plugin: com.semarchy.engine.plugins.convergence.lookup; inputs: LOWER( COALESCE( NormalizedFirstName, FirstName) )` |
| Customer | MelissaPersonatorEnricher | JavaPluginEnricher | Melissa Personator Enricher | This is the Semarchy-built Melissa plugin, not the legacy version built by Melissa. | `MDPersonator.AddressSuiteNumber`, `MDPersonator.PhonePrefix`, `MDPersonator.EmailAddress`, `MDPersonator.AddressPostDirection`, `MDPersonator.UrbanizationName`, `MDPersonator.NameLast`, `MDPersonator.CBSADivisionTitle`, `MDPersonator.CountyName`, `MDPersonator.AddressRouteService`, `MDPersonator.LengthOfResidence`, plus 83 more | `plugin: com.semarchy.engine.plugins.melissa.personator; inputs: SourcePhone, InputCity, InputCountry, InputZipCode, SourceEmail, InputState, plus 2 more` |
| Customer | NormalizeName | JavaPluginEnricher | Normalize Name | Normalizes customer full names into standardized first and last name components for matching and stewardship. | `NormalizedFirstName`, `NormalizedLastName` | `plugin: com.semarchy.engine.plugins.convergence.personname.personNameEnricher; inputs: COALESCE(GeocodedCountry, 'US'), FirstName \\|\\| ' ' \\|\\| LastName` |
| Customer | PhonetizeFirstName | JavaPluginEnricher | Phonetize First Name | Generates a phonetic representation of the customer first name to support fuzzy duplicate detection. | `PhoneticFirstName` | `plugin: com.semarchy.engine.plugins.convergence.text; inputs: FirstName` |
| Customer | PhonetizeLastName | JavaPluginEnricher | Phonetize Last Name | Generates a phonetic representation of the customer last name to support fuzzy duplicate detection. | `PhoneticLastName` | `plugin: com.semarchy.engine.plugins.convergence.text; inputs: LastName` |
| Customer | StandardizePhone | JavaPluginEnricher | Standardize Phone | Standardizes customer phone numbers and returns geocoding context for customer matching and contact quality. | `StandardizedPhone`, `PhoneGeocodingData` | `plugin: com.semarchy.engine.plugins.convergence.phone; inputs: 'US', SourcePhone, COALESCE( InputCountry, 'US' ), 'NATIONAL'` |
| Item | DefaultItemCondition | SemQLEnricher | Default Item Condition | Defaults missing item condition values to New so item records have a usable condition classification. | `FID_ItemCondition` | `Condition: FID_ItemCondition is null; FID_ItemCondition = 'New'` |
| Item | NormalizeSKU | SemQLEnricher | Normalize SKU | Normalizes SKU values by removing punctuation for item matching and standardization. | `NormalizedSKU` | `NormalizedSKU = REGEXP_REPLACE(SKU,'[[:punct:]]','', 'g')` |
| ItemBillOfMaterial | DefaultRelationshipType | SemQLEnricher | Default Relationship Type | Defaults missing bill of material relationship types to AssemblyComponent for component relationships. | `RelationshipType` | `Condition: RelationshipType is NULL; RelationshipType = 'AssemblyComponent'` |
| ItemBillOfMaterial | SetName | SemQLEnricher | Set Name | Sets a missing bill of material name from the parent item display name. | `Name` | `Condition: Name is null; Name = FDN_ParentItem` |
| SupplierManufacturerPlant | Manufacturer | SemQLEnricher | Manufacturer | Derives the manufacturer on a supplier-manufacturer-plant relationship from the related manufacturing plant. | `FID_Manufacturer` | `Condition: FID_Manufacturer is null and FID_ManufacturingPlant is not null /* If we have the MFG plant, Semarchy should automatically fill the Manufacturer*/; FID_Manufacturer = ManufacturingPlant.FID_Manufacturer` |

You can extend these enrichers to apply customer-specific standardization, geocoding, householding, contact cleansing, and item normalization rules. For a full list of entities and attributes, refer to the [model structure page](./model_structure.md).
