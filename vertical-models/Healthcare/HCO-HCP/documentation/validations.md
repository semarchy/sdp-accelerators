# Validations Documentation

Validations enforce required fields and business rules at ingestion or during authoring. Use this page to understand what is currently enforced and where additional controls may be needed.

Notes:
- Validation names and labels reflect the model configuration (spelling preserved).
- Rules are applied per entity; failures typically block load or authoring depending on workflow configuration.

This table summarizes the validations defined in the HCO-HCP model, including their entity, name, label, description, and condition.

| Entity | Name | Label | Description | Condition |
|---|---|---|---|---|
| HCO | RejectNotAvailableData | Reject N/A Data | Reject N/A Data | HospitalCCN != '#N/A' |
| HCP | CheckName | Check Name | Check Name | FirstName IS NOT NULL AND LastName IS NOT NULL |
| HCP | RejectNotAvailableData | Reject N/A Data | Reject N/A Data | FullName != '#N/A' |

You can extend these validations to apply your specific business rules. For a full list of mandatory fields and restrictions, refer to the [model structure page](./model_structure.md).
