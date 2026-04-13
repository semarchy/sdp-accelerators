```markdown
# Enrichers

Enrichers apply transformations to populate derived/enriched attributes. They are used to standardize, normalize, and compute derived values that should be stored alongside source values to preserve provenance.

Key enricher example

- `NormalizeShortName` (Country)
  - Type: `SemQLEnricher`
  - Purpose: set `EnglishShortNameCAPS` = UPPER(`EnglishShortName`).
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/Country/enrichers/NormalizeShortName.SemQLEnricher.seml`

Guidelines

- Use `PRE_CONSO` for cleanses that should run before consolidation.
- Preserve source values; write transforms to `Enriched*` attributes to keep provenance.
- Keep enrichers focused and idempotent so they can be safely re-run during processing.
- Document the expected inputs and outputs in the enricher `description`.

Location

- Per-entity enrichers are stored under `src/Merchant/entities/<Entity>/enrichers/`.

Additional newly added enrichers

- `EnrichedMerchantName` (Merchant)
  - Type: `SemQLEnricher`
  - Purpose: populate `EnrichedMerchantName` = UPPER(`MerchantName`).
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/Merchant/enrichers/EnrichedMerchantName.SemQLEnricher.seml`

- `AddressEnricher` (PartyAddress)
  - Type: `SemQLEnricher`
  - Purpose: populate standardized/enriched address attributes (`EnrichedStreet`, `EnrichedCity`, `EnrichedState`, `EnrichedPostalCode`) using normalization.
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/PartyAddress/enrichers/AddressEnricher.SemQLEnricher.seml`

  - Type: `SemQLEnricher`
  - Purpose: populate `NormalizedName` from `DisplayName` (e.g. `NormalizedName` = UPPER(`DisplayName`)).
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/Party/enrichers/NormalizedName.SemQLEnricher.seml`

- `NormalizeShortName` (Country)
  - Type: `SemQLEnricher`
  - Purpose: set `EnglishShortNameCAPS` = UPPER(`EnglishShortName`).
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/Country/enrichers/NormalizeShortName.SemQLEnricher.seml`

- `Wikipedia` (Country)
  - Type: `SemQLEnricher`
  - Purpose: populate `WikipediaUrl` (adds a canonical Wikipedia link or identifier for the country from a lookup mapping).
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/Country/enrichers/Wikipedia.SemQLEnricher.seml`

- `IsCurrent` (Currency)
  - Type: `SemQLEnricher`
  - Purpose: set `IsCurrent` flag when the currency `ValidTo`/`EndDate` is null or in the future (indicates current currencies).
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/Currency/enrichers/IsCurrent.SemQLEnricher.seml`

- `EnrichedName` (Individual)
  - Type: `SemQLEnricher`
  - Purpose: populate `EnrichedName` (e.g. concatenation and normalization of `FirstName` / `MiddleName` / `LastName`, UPPER-cased for matching).
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/Individual/enrichers/EnrichedName.SemQLEnricher.seml`

- `NormalizeLegalName` (LegalEntity)
  - Type: `SemQLEnricher`
  - Purpose: normalize and populate `EnrichedLegalName` = UPPER(`LegalName`) and remove legal suffixes for matching.
  - Execution scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/LegalEntity/enrichers/NormalizeLegalName.SemQLEnricher.seml`
```
