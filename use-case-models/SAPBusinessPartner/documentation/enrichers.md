# Enrichers Documentation

This table summarizes the enrichers defined in the model, including their entity, name, type, label, description, enriched attribute(s), and expression. All enrichers run in the PRE_CONSO scope so that source values are preserved and enriched values are written to separate attributes.

| Entity name | Enricher name | Enricher type | Enricher label | Enricher description | Enriched attribute | Enricher expression |
|-------------|---------------|---------------|----------------|----------------------|--------------------|---------------------|
| BPAddress | GeocodedBPAddressAddress | JavaPluginEnricher | Geocoded BP Address Address | Use the Google Maps API plugin to geocode BP Address address fields. | GeoCountryShort, GeoLatitude, GeoStatus, GeoQuality, GeoLongitude, GeoLocality, GeoStreetName, GeoPostalCode, GeoCountry, GeoState, GeoStreetNumber | Plugin: com.semarchy.integration.rowTransformers.googleMapsEnricher |
| BPAddress | NormalizedCity | SemQLEnricher | Normalized city name for search and matching. | Normalized city name for search and matching. | NormalizedCity | LTRIM(RTRIM(UPPER(CityName))) |
| BPAddressEmail | NormalizedEmail | SemQLEnricher | Normalized email address for search. | Normalized email address for search. | SearchEmailAddress | UPPER(EmailAddress) |
| BPContact | NormalizedContactName | SemQLEnricher | Normalized contact name for matching. | Normalized contact name for matching. | NormalizedName | LTRIM(RTRIM(UPPER(ContactFullName))) |
| BPIdentification | NormalizedIdNumber | SemQLEnricher | Normalized identification number for search and comparison. | Normalized identification number for search and comparison. | NormalizedIdNumber | REPLACE(UPPER(BpIdentificationNumber), ' ', '') |
| BPTaxNumber | NormalizedTaxNumber | SemQLEnricher | Normalized tax number for search and comparison. | Normalized tax number for search and comparison. | NormalizedTaxNumber | REPLACE(UPPER(BPTaxNumber), ' ', '') |
| BusinessPartner | NormalizedBusinessPartnerName | SemQLEnricher | Normalized business partner name for matching. | Normalized business partner name for matching. | NormalizedName | LTRIM(RTRIM(UPPER(BusinessPartnerFullName))) |
| Supplier | NormalizedSupplierName | SemQLEnricher | Normalized supplier name for matching. | Normalized supplier name for matching. | NormalizedName | LTRIM(RTRIM(UPPER(SupplierName))) |
| SupplierPurchasingOrg | NormalizedRespName | SemQLEnricher | Normalized responsible sales person name for matching. | Normalized responsible sales person name for matching. | NormalizedRespName | LTRIM(RTRIM(UPPER(SupplierRespSalesPersonName))) |
