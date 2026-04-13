
# Validations Documentation

This table summarizes the validations defined in the FinanceKYC model, including their entity, label, scope, and condition.

| Entity              | Name             | Label                         | Validation label      | Validation scope | Description                                         | Condition                                      |
|---------------------|------------------|-------------------------------|-----------------------|------------------|-----------------------------------------------------|------------------------------------------------|
| IndividualPerson    | ValidDoB         | Date of Birth must be valid   |                       | PRE_CONSO        | Date of Birth must be in the past, but not too far in the past | DateOfBirth > MAKE_DATE(1900, 01, 01) AND DateOfBirth < CURRENT_DATE() |
| BankingProduct      | ValidateCategory | Validate Category             | Category is required  | NONE             |                                                     | FID_Category is not null                       |
| InsuranceProduct    | ValidateCategory | Validate Category             | Category is required  | NONE             |                                                     | FID_Category is not null                       |

You can extend these validations to apply your specific business rules. For a full list of mandatory fields and restrictions, refer to the [model structure page](./model_structure.md).
