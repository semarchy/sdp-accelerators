# Validations Documentation

This table summarizes the validations defined in the model, including their entity, name, label, description, and condition.

| Entity      | Name                 | Label                | Description                                   | Condition                                      |
|-------------|----------------------|----------------------|-----------------------------------------------|------------------------------------------------|
| Account     | AccountNumber        | Account Numner       | Account Number must be between 8 and 12 digits| REGEXP_LIKE(AccountNumber, '^[0-9]{8,12}$')    |
| Account     | RoutingNumber        | Routing Numner       | Routing Number must be between 8 and 12 digits| REGEXP_LIKE(RoutingNumber, '^[0-9]{8,12}$')    |
| Contact     | SSNFormat            | SSN Format           | SSN must be in the format XXX-XX-XXXX         | REGEXP_LIKE(SSN, '^[0-9]{3}-[0-9]{2}-[0-9]{4}$')|
| LegalEntity | DetectSpecialCharacter| Detect Special Character | Name must not start with special characters | REGEXP_LIKE(Name, '^[^a-zA-Z0-9].*')           |
| LegalEntity | USFEIN               | Detect Special Character | USFEIN must be in the format XX-XXXXXXX      | REGEXP_LIKE(USFEIN, '^[^a-zA-Z0-9].*')         |
