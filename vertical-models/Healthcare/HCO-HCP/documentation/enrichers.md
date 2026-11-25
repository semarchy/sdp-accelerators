# Enrichers Documentation

This page summarizes the enrichers defined in the HCO-HCP model. Use it to understand what is automated, which attributes are enriched, and which plugins or expressions are required.

Notes:
- Labels and descriptions reflect the model configuration (spelling preserved).
- Java plugin and REST enrichers typically require external configuration (API keys, endpoints, or plugin deployment).
- SemQL enrichers execute in the model pipeline and do not require external services.

This table summarizes the enrichers defined in the HCO-HCP model, including their entity, name, type, label, description, enriched attribute, and expression or plugin.

| Entity name | Enricher name | Enricher type | Enricher label | Enricher description | Enriched attribute | Enricher expression / Plugin |
|---|---|---|---|---|---|---|
| HCO | GoogleMapEnricher | JavaPluginEnricher | Google Map Enricher | Google Map Enricher | GeocodedAddress.PostalCode, GeocodedAddress.StreetNumber, GeocodedAddress.State, GeocodedAddress.CoordLatitude, GeocodedAddress.Locality, GeocodedAddress.StreetName, GeocodedAddress.CoordLongitude, GeocodedAddress.Country | plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher |
| HCO | NormalizeName | SemQLEnricher | Normalize Name | Normalize Name | HospitalNameNormalized | HospitalNameNormalized = REGEXP_REPLACE( REPLACE( REPLACE( UPPER(HospitalName), '''', '' ), '&', ' AND ' ), '[[:punct:][:blank:]]+', /* find one or more spaces or punctuation marks */ ' ', /* replace with a single space */ 'g' /* replace all occurences */ ) |
| HCO | RemoveBusinessEntityType | SemQLEnricher | Remove Business Entity Type | Remove Business Entity Type | HospitalNameNormalized | HospitalNameNormalized = REGEXP_REPLACE ( HospitalNameNormalized, '[[:blank:]]+(' /* find spaces preceding the business entity type */ || 'COMPANY|COMPANY[[:blank:]]*INC|CORPORATION|CORP|AND[[:blank:]]*CO|CO|CO[[:blank:]]*INC|INCORPORATED|INC|LIMITED|LTD|ASSOCIATION|ASSOC|' /* Anglo entities */ || 'L[[:blank:]]*P|L[[:blank:]]*L[[:blank:]]*P|L[[:blank:]]*L[[:blank:]]*L[[:blank:]]*P|L[[:blank:]]*L[[:blank:]]*C|P[[:blank:]]*L[[:blank:]]*C|' /* More Anglo entities */ || 'S[[:blank:]]*A[[:blank:]]*R[[:blank:]]*L|S[[:blank:]]*A[[:blank:]]*S|' /* French entities */ || 'A[[:blank:]]*G|G[[:blank:]]*M[[:blank:]]*B[[:blank:]]*H|' /* German entities */ || 'S[[:blank:]]*A|S[[:blank:]]*L|' /* Spanish entities */ || 'K[[:blank:]]*K|G[[:blank:]]*K|' /* Japanese entities */ || ')[[:blank:]]*$', '' /* replace the business entity type with an empty string */ ) |
| HCP | AddressCleansing | JavaPluginEnricher | Address Cleansing | Address Cleansing | GeocodedAddress.CoordLongitude, GeocodedAddress.CoordLatitude, GeocodedAddress.State, GeocodedAddress.CountryShort, GeocodedAddress.Quality, GeocodedAddress.PostalCode, GeocodedAddress.Country, GeocodedAddress.StreetNumber, GeocodedAddress.Locality, GeocodedAddress.StreetName, GeocodedAddress.StatusReturned | plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher |
| HCP | GoogleMapEnricher | JavaPluginEnricher | Google Map Enricher | Google Map Enricher | GeocodedAddress.StreetName, GeocodedAddress.Country, GeocodedAddress.CoordLatitude, GeocodedAddress.StreetNumber, GeocodedAddress.Locality, GeocodedAddress.PostalCode, GeocodedAddress.State, GeocodedAddress.CoordLongitude | plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher |
| HCP | NPINumber | RestClientEnricher | NPI Number | NPI Number | Specialties, ZipCode, City, StreetAddressLine1, State, FirstName, LastName | plugin: NPPESRestAPI |
| HCP | NPPESGetNPI | RestClientEnricher | NPPES Get NPI | NPPES Get NPI | NPI | plugin: NPPESGetNPI |
| HCP | Phoneticize | SemQLEnricher | Phoneticize | Phoneticize | LastNamePhonetic, FirstNamePhonetic | LastNamePhonetic = METAPHONE( LastName, 128 ); FirstNamePhonetic = METAPHONE( FirstName, 128 ) |
| HCP | SplitName | JavaPluginEnricher | Split Name | Split Name | LastName, FirstName | plugin: com.semarchy.engine.plugins.convergence.personname.personNameEnricher |
| InsuranceCompany | AddressEnricher | JavaPluginEnricher | Address Enricher | Address Enricher | GeocodedAddress.StreetNumber, GeocodedAddress.PostalCode, GeocodedAddress.StreetName, GeocodedAddress.Country, GeocodedAddress.CoordLatitude, GeocodedAddress.CoordLongitude, GeocodedAddress.Locality, GeocodedAddress.State | plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher |
| InsuranceCompany | NormalizeWebsite | SemQLEnricher | Normalize Websie | Normalize Websie | NormalizedWebsite | NormalizedWebsite = CASE WHEN URL = '(none)' THEN NULL ELSE RTRIM( REGEXP_REPLACE( LOWER(URL) , '^(https?://)?(www\.)?' ,'' ) , '/' ) END /* Regex notes: get rid of http or https and get rid of leading www and get rid of trailing slash. */ |
| Member | CleanseEmail | JavaPluginEnricher | Cleanse Email | Cleanse Email | ValidEmailDomain, CleansedEmail | plugin: com.semarchy.engine.plugins.convergence.email |
| Member | FindPCPPubID | JavaPluginEnricher | Find PCP PublisherID | Find PCP PublisherID | PublisherID_HCP | plugin: com.semarchy.engine.plugins.convergence.lookup |
| Member | FindPCPSourceID | JavaPluginEnricher | Find PCP Source ID | Find PCP Source ID | SourceID_HCP | plugin: com.semarchy.engine.plugins.convergence.lookup |
| Member | Gender | JavaPluginEnricher | Gender | Gender | Gender | plugin: com.semarchy.engine.plugins.convergence.personname.personNameEnricher |
| Member | GeocodeUsingGoogle | JavaPluginEnricher | Geocode Using Google | Geocode Using Google | GeocodedAddress.StreetNumber, GeocodedAddress.Country, GeocodedAddress.PostalCode, GeocodedAddress.State, GeocodedAddress.CoordLatitude, GeocodedAddress.StreetName, GeocodedAddress.CoordLongitude, GeocodedAddress.Locality | plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher |
| Member | Phoneticize | SemQLEnricher | Phoneticize | Phoneticize | FirstNamePhonetic, LastNamePhonetic | FirstNamePhonetic = METAPHONE( FirstName, 128 ); LastNamePhonetic = METAPHONE( LastName, 128 ) |
| Member | StandardizeCellPhone | JavaPluginEnricher | Standardize Cell Phone | Standardize Cell Phone | StarndardizedCellPhone | plugin: com.semarchy.engine.plugins.convergence.phone |
| Member | StandardizeHomePhone | JavaPluginEnricher | Standardize Home Phone | Standardize Home Phone | StandardizedHomePhone | plugin: com.semarchy.engine.plugins.convergence.phone |
| Products | Definition | SemQLEnricher | Definition | Definition | Definition | Definition = SEM_CONCAT('', '', 'https://en.wikipedia.org/wiki/', SPLIT_PART(TradeName, ' ', 1) ) |
| Products | GenAIDescriptionProducts | JavaPluginEnricher | Gen AI Description Products | Gen AI Description Products | GEN_AIDescription | plugin: com.semarchy.engine.plugins.genai.openai.simple |
| Products | UpperAttributes | SemQLEnricher | Upper Attributes | Upper Attributes | EnrichForm, EnrichAdministration | EnrichForm = UPPER(FDN_Form); EnrichAdministration = UPPER(FDN_Administration) |
| Products | url | SemQLEnricher | url | url | url | url = "'https://' || TradeName || '.com'" |
