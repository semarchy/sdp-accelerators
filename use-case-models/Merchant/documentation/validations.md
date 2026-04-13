# Validations

Validation rules prevent bad data entering consolidation. This document describes the key validation patterns and notable validation rules in the model.

Examples

- `Industry` (SubIndustry entity)
  - Type: `SemQLValidation`
  - Condition: `FDN_Industry IS NOT NULL` when Sub Industry provided.
  - Scope: `PRE_CONSO`
  - Path: `src/Merchant/entities/SubIndustry/validations/Industry.SemQLValidation.seml`

 - `ValidEmail` (PartyContact)
  - Type: `PluginValidation` (plugin `Pcom.semarchy.engine.plugins.convergence.email`)
  - Purpose: validate email syntax and domain against accepted domains.
  - Retries: 3; on-error: `SKIP_RECORDS`; Scope: `PRE_CONSO`.
  - Path: `src/Merchant/entities/PartyContact/validations/ValidEmail.PluginValidation.seml`

- `MerchantName` (Merchant)
  - Type: `SemQLValidation`
  - Condition: `Name IS NOT NULL AND LENGTH(LTRIM(RTRIM(Name))) > 0`
  - Scope: `PRE_CONSO`
  - Path: `src/Merchant/entities/Merchant/validations/MerchantName.SemQLValidation.seml`

 - `Status` (Merchant)
  - Type: `SemQLValidation`
  - Condition: `Status IS NOT NULL AND LENGTH(LTRIM(RTRIM(Status))) > 0`
  - Scope: `PRE_CONSO`
  - Path: `src/Merchant/entities/Merchant/validations/Status.SemQLValidation.seml`

 - `TerminationDateAfterActivation` (Merchant)
  - Type: `SemQLValidation`
  - Condition: `TerminationDate IS NULL OR (ActivationDate IS NOT NULL AND TerminationDate >= ActivationDate)`
  - Scope: `PRE_CONSO`
  - Path: `src/Merchant/entities/Merchant/validations/TerminationDate.SemQLValidation.seml`

Best practices

- Prefer `PRE_CONSO` for validations that should block bad data before consolidation.
- Use plugin validations for complex checks that rely on external libraries or services; document plugin inputs and parameters inside the SEML `description` and `pluginParams`.
- Fail fast for data that must be corrected upstream; for non-critical checks consider `WARN` or `SKIP_RECORDS` behavior.

Location

- Per-entity validations are stored under `src/Merchant/entities/<Entity>/validations/`.
