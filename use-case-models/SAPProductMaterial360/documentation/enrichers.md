# Enrichers Documentation

This table summarizes the enrichers defined in the SAP Product / Material 360 model.

| Entity name | Enricher name | Enricher type | Enricher label | Enricher description | Enriched attribute | Enricher expression |
|---|---|---|---|---|---|---|
| Product | NormalizedProductName | SemQLEnricher | Normalized Product Name | Normalize the product name for product matching. | NormalizedProductName | NormalizedProductName: LTRIM(RTRIM(UPPER(ProductName))) |
| Material | NormalizedMaterialDescription | SemQLEnricher | Normalized Material Description | Normalize material descriptions for duplicate material detection. | NormalizedMaterialDesc | NormalizedMaterialDesc: LTRIM(RTRIM(UPPER(MaterialDescription))) |
| StorageLocation | GeocodedStorageLocationAddress | PluginEnricher | Geocoded Storage Location Address | Use the Google Maps API plugin to geocode storage location address fields. | GeoCountryShort, GeoLatitude, GeoStatus, GeoQuality, GeoLongitude, GeoLocality, GeoStreetName, GeoPostalCode, GeoCountry, GeoState, GeoStreetNumber | IN_COUNTRY: InpCountry; IN_CITY: InpCity; IN_ADDRESSLINE: InpAddressLine; IN_POSTALCODE: InpPostalCode |
