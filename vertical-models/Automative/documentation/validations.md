# Manufacturing and Automotive Accelerator - Validations

Validations enforce required fields and business rules at ingestion or during authoring. Use this page to understand what is currently enforced in the Manufacturing model and where additional controls may be needed.

Notes:
- Validation names and labels reflect the model configuration.
- Rules are applied per entity; failures typically block load or authoring depending on workflow and validation-scope configuration.

Related pages:
- [model structure](./model_structure.md)
- [user guide](./user_guide.md)
- [enrichers](./enrichers.md)

This table summarizes the explicit validations defined in the Manufacturing model, including their entity, name, label, description, failure label, scope, and condition.

| Entity | Name | Label | Description | Failure label | Scope | Condition |
|---|---|---|---|---|---|---|
| Customer | OlderThan18Years | Older Than18 Years | Ensures customers are at least 18 years old before they can purchase an automobile. | Minors cannot purchase a car. Please come back once you turn 18 | PRE_CONSO | `AGE(CURRENT_DATE(), DateOfBirth) >= MAKE_INTERVAL (18,0,0,0,0,0,0)` |
| ItemSpecificAttribute | MandatoryAttribute | Mandatory Attribute | Ensures mandatory item attributes have either a constrained value or an unconstrained value before consolidation. | A value is mandatory for this attribute | PRE_CONSO | `Attribute.Mandatory ='0' or ( Attribute.Mandatory ='1' and ( FID_AttributeValue is not null or UnconstrainedValue is not null ) )` |
| Supplier | FoundedYear | Founded Year | Ensures the supplier founding year is later than 1700 before consolidation. | Founding Year cannot be before 1700 AC | PRE_CONSO | `FoundedYear > 1700` |

## Additional Built-in Validation Behavior

In addition to the explicit validation artifacts above, the model also relies on built-in authoring and reference validation behavior:

- Entity attributes marked as mandatory are enforced through the model and authoring steppers.
- Model references use pre-consolidation validation behavior to enforce referential integrity across related entities.
- The onboarding workflows for customers, dealers, items, and suppliers use stepper-based authoring flows with mandatory-field and foreign-key checks.
- Fuzzy-matched entities such as customers, suppliers, manufacturers, product vehicles, contacts, and addresses include match and duplicate-review behavior in addition to validation rules.

You can extend these validations to apply more specific business rules. For a full list of mandatory fields and restrictions, refer to the [model structure page](./model_structure.md).
