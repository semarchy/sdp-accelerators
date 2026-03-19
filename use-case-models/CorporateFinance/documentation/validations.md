# Corporate Finance Accelerator - Validations

Validations enforce required fields and business rules at ingestion or during authoring. Use this page to understand what is currently enforced in the Corporate Finance Accelerator and where additional controls may be needed.

Notes:
- Validation names and labels reflect the model configuration.
- Rules are applied per entity; failures typically block load or authoring depending on workflow configuration.

Related pages:
- [model structure](./model_structure.md)
- [user guide](./user_guide.md)

This table summarizes the explicit validations defined in the Corporate Finance model, including their entity, name, label, description, and condition.

| Entity | Name | Label | Description | Condition |
|---|---|---|---|---|
| Supplier | LeadTimePositive | Lead time must be positive | Ensures supplier lead time is either blank or greater than zero. | `LeadTimeDays IS NULL OR LeadTimeDays > 0` |
| SplitAllocation | SplitPercentMax | Split Percent must be 0-100 | Ensures a split allocation percentage does not exceed 100. | `SplitPercent <= 100` |

## Additional Built-in Validation Behavior

In addition to the explicit validation artifacts above, the model also relies on built-in authoring and reference validation behavior:

- `OrgUnit` stepper includes mandatory-field and foreign-key checks during authoring.
- `AccountMapping` stepper includes mandatory-field and foreign-key checks for mapping creation and split-allocation authoring.
- Model references are configured with pre-consolidation validation behavior to enforce referential integrity across related entities.

You can extend these validations to apply your specific business rules. For a full list of mandatory fields and restrictions, refer to the [model structure page](./model_structure.md).
