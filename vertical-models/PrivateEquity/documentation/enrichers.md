# Private Equity Accelerator - Enrichers

This page summarizes the enrichers defined in the Private Equity model. Use it to understand what is automated, which attributes are enriched, and which plugins or SemQL expressions are required.

Notes:
- Labels and descriptions reflect the model configuration.
- Java plugin enrichers require the relevant plugin and runtime configuration to be available.
- SemQL enrichers execute in the model pipeline and do not require external services.
- Plugin parameter values are intentionally not listed here.
- In the validated demo, enrichers support the Apex Legal Entity 360 view, location/map context, office context, portfolio names, and account keys used around the fund and portfolio story.

Related pages:
- [model structure](./model_structure.md)
- [user guide](./user_guide.md)
- [validations](./validations.md)

This table summarizes the enrichers defined in the Private Equity model, including their entity, name, type, label, description, enriched attribute, and expression or plugin.

| Entity name | Enricher name | Enricher type | Enricher label | Enricher description | Enriched attribute | Enricher expression / Plugin |
|---|---|---|---|---|---|---|
| Account | AccountKey | SemQLEnricher | Account Key | Derives the account key by concatenating fund chain ID, portfolio chain ID, and account chain ID for integration alignment. | `AccountKey` | `AccountKey = Fund.ChainID \|\| '~' \|\| Portfolio.ChainID \|\| '~' \|\| ChainID` |
| Account | AccountName | SemQLEnricher | Account Name | Populates missing account names from the related legal entity and bank names for easier account identification. | `Name` | `Condition: Name is null; Name = FDN_LegalEntity \|\| '~' \|\| FDN_Bank` |
| Contact | AutopopulateFullName | SemQLEnricher | Autopopulate Full Name | Builds the contact full name from first and last name values before consolidation. | `FullName` | `FullName = FirstName \|\| ' ' \|\| LastName` |
| Contact | AutopopulateOfficePhone | SemQLEnricher | Autopopulate Office Phone | Copies the standardized office phone number onto the contact phone field before consolidation. | `Phone` | `Phone = Office.StandarizedPhone` |
| Contact | CleanseEmail | JavaPluginEnricher | Cleanse Email | Validates and standardizes contact email values using the Semarchy email convergence plugin. | `CleansedEmail`, `ValidEmailDomain` | `plugin: com.semarchy.engine.plugins.convergence.email; inputs: Email` |
| Contact | StandardizeMobilePhone | JavaPluginEnricher | Standardize Mobile Phone | Standardizes contact mobile phone numbers using country context for consistent phone formatting. | `StandarizedMobile`, `MobileGeocodingData` | `plugin: com.semarchy.engine.plugins.convergence.phone; inputs: Mobile, 'NATIONAL', 'US', COALESCE( Address.Country, 'US' )` |
| LegalEntity | AutoPopulateCurrency | SemQLEnricher | Auto Populate Currency | Defaults legal entity currency to USD when the related country is the United States. | `FID_Currency` | `FID_Currency = case when FID_Country = 'US' then 'USD' else null end` |
| LegalEntity | GeocodeUsingGoogle | JavaPluginEnricher | Geocode Using Google | Geocodes address components using Google Maps and stores the resolved location details. | `GeocodedAddress.CoordLongitude`, `GeocodedAddress.StatusReturned`, `GeocodedAddress.Quality`, `GeocodedAddress.StreetName`, `GeocodedAddress.Country`, `GeocodedAddress.PostalCode`, `GeocodedAddress.Locality`, `GeocodedAddress.State`, `GeocodedAddress.CoordLatitude`, `GeocodedAddress.StreetNumber` | `plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher; inputs: InputAddress.City, InputAddress.AddressLine, InputAddress.ZipCode, InputAddress.Country` |
| LegalEntity | NormalizeEntityName | SemQLEnricher | Normalize Entity Name | Normalizes legal entity names by trimming whitespace and converting values to uppercase for matching and validation. | `NormalizedName` | `NormalizedName = RTRIM(LTRIM(UPPER(Name)))` |
| LegalEntity | PopulateType | SemQLEnricher | Populate Type | Classifies legal entities as Internal when the name matches the configured Northstar pattern, otherwise defaults the type to Investor. | `FID_EntityType` | `FID_EntityType = case when REGEXP_LIKE(Name, '<internal-sponsor-pattern>') then 'Internal' else 'Investor' end` |
| LegalEntity | ReplaceSingleQuotation | SemQLEnricher | Replace Single Quotation | Expands KKR legal entity names to Kohlberg Kravis Roberts in the normalized name field. | `NormalizedName` | `NormalizedName = REGEXP_REPLACE(Name, 'KKR', 'Kohlberg Kravis Roberts')` |
| LegalEntity | SetStatusActive | SemQLEnricher | Set Status Active | Sets the legal entity status to Active during pre-consolidation processing. | `FID_Status` | `FID_Status = 'Active'` |
| LegalEntity | SetStatusDraft | SemQLEnricher | Set Status Draft | Sets the legal entity status to Draft during pre-consolidation processing. | `FID_Status` | `FID_Status = 'Draft'` |
| LegalEntity | SetStatusPendingValidation | SemQLEnricher | Set Status Pending Validation | Sets the legal entity status to Pending Validation during pre-consolidation processing. | `FID_Status` | `FID_Status = 'Pending Validation'` |
| Office | GeocodeUsingGoogle | JavaPluginEnricher | Geocode Using Google | Geocodes address components using Google Maps and stores the resolved location details. | `GeocodedAddress.Quality`, `GeocodedAddress.Locality`, `GeocodedAddress.State`, `GeocodedAddress.StreetName`, `GeocodedAddress.CoordLatitude`, `GeocodedAddress.StatusReturned`, `GeocodedAddress.Country`, `GeocodedAddress.PostalCode`, `GeocodedAddress.CountryShort`, `GeocodedAddress.CoordLongitude`, `GeocodedAddress.StreetNumber` | `plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher; inputs: SourceAddress.AddressLine, SourceAddress.City, SourceAddress.Country, SourceAddress.ZipCode` |
| Office | NormalizedName | SemQLEnricher | Normalized Name | Normalizes office names by trimming whitespace and converting values to uppercase for matching and validation. | `NormalizedName` | `NormalizedName = RTRIM(LTRIM(UPPER(Name)))` |
| Office | StandarizePhone | JavaPluginEnricher | Standarize Phone | Standardizes office phone numbers using country context for consistent phone formatting. | `StandarizedPhone` | `plugin: com.semarchy.engine.plugins.convergence.phone; inputs: Phone, COALESCE( SourceAddress.Country, 'US' ), 'US', 'NATIONAL'` |
| Portfolio | PortfolioName | SemQLEnricher | Portfolio Name | Populates missing portfolio names from the related fund and industry names before consolidation. | `Name` | `Condition: Name is null; Name = FDN_Fund \|\| ' ' \|\| FDN_Industry` |

## How the enrichers support the use cases

- Legal entity onboarding uses status, type, currency, name normalization, quote replacement, and geocoding enrichers to improve data as users author and integrate records.
- The Apex demo uses legal entity name normalization and FEIN-based matching to support source consolidation into one golden record.
- Location and office context rely on geocoding enrichers so the Legal Entity 360 view can show map and operating-footprint proof points.
- Office and contact stewardship uses geocoding, phone standardization, email cleansing, and full-name derivation to improve operational contact data.
- Account and portfolio enrichers derive readable account and portfolio names and composite account keys for downstream integration.
- Portfolio name enrichment supports the fund hierarchy view used to validate the portfolio-change workflow.
- Java plugin enrichers should be validated in the target runtime because they depend on plugin availability and external configuration.
