# Private Equity Accelerator - Validations

Validations enforce required fields, relationship integrity, duplicate detection, and business rules at ingestion or during authoring. Use this page to understand what is currently enforced in the Private Equity model and where additional controls may be needed.

Notes:
- Validation names and labels reflect the model configuration.
- Rules are applied per entity; failures typically block or warn during load, authoring, workflow completion, or consolidation depending on validation scope and stepper configuration.
- The model also uses match rules, unique keys, duplicate management, and survivorship rules as part of the broader data-quality control surface.
- In the validated demo, two Apex source records consolidate automatically into one golden `Apex Data Services LLC` record.

Related pages:
- [model structure](./model_structure.md)
- [user guide](./user_guide.md)
- [enrichers](./enrichers.md)

This table summarizes the explicit validation artifacts defined in the Private Equity model, including their entity, name, label, description, failure label, scope, and condition.

| Entity | Name | Label | Description | Failure label | Scope | Condition |
|---|---|---|---|---|---|---|
| Account | AccountNumber | Account Number | Ensures account numbers contain 8 to 12 digits before consolidation. | Account Number has to between 8-12 Digits (Ex: 12345678XXXX) | PRE_CONSO | `REGEXP_LIKE(AccountNumber, '^[0-9]{8,12}$')` |
| Account | RoutingNumber | Routing Number | Ensures routing numbers contain exactly 9 digits before consolidation. | Routing Number has to be 9 digits (Ex: 123456789) | PRE_CONSO | `REGEXP_LIKE(RoutingNumber, '[0-9]{9}')` |
| Contact | SSNFormat | SSN Format | Ensures contact Social Security Numbers follow the 123-12-1234 format before consolidation. | SSN Format Error (Ex: 123-12-1234) | PRE_CONSO | `REGEXP_LIKE(SSN, '[0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{4}')` |
| LegalEntity | DetectSpecialCharacter | Detect Special Character | Ensures legal entity names do not start with configured special characters before consolidation. | Legal Entity Name cannot start with a Special Character | PRE_CONSO | `SUBSTR(Name, 1, 1) != '?' AND SUBSTR(Name, 1, 1) != '!' AND SUBSTR(Name, 1, 1) != '@' AND SUBSTR(Name, 1, 1) != '#' AND SUBSTR(Name, 1, 1) != '$' AND SUBSTR(Name, 1, 1) != '%' AND SUBSTR(Name, 1, 1) != '^' AND SUBSTR(Name, 1, 1) != '&' AND SUBSTR(Name, 1, 1) != '*' AND SUBSTR(Name, 1, 1) != ')' AND SUBSTR(Name, 1, 1) != '+' AND SUBSTR(Name, 1, 1) != '=' AND SUBSTR(Name, 1, 1) != '\' AND SUBSTR(Name, 1, 1) != '~'` |
| LegalEntity | USFEIN | USFEIN | Ensures US FEIN values follow the 12-1234567 format before consolidation. | US FEIN Format Error (Ex: 12-1234567) | PRE_CONSO | `REGEXP_LIKE(USFEIN, '[0-9]{2}[-]{1}[0-9]{7}')` |

## Matching and Duplicate Review

The `LegalEntity` entity is fuzzy matched and includes a duplicate manager for steward review. The matcher is configured with auto-confirm and merge thresholds, multi-iteration grouping, and transitive match score support.

Current matcher settings include `autoConfirmGoldenThreshold: 99`, so a rule scoring 100 can automatically confirm a golden record.

| Entity | Match rule | Label | Score | Condition |
|---|---|---|---|---|
| LegalEntity | ExactEIN | Exact EIN | 100 | `Record1.USFEIN = Record2.USFEIN` |
| LegalEntity | ExactNameAddress | Exact Name & Address | 90 | `Record1.NormalizedName = Record2.NormalizedName AND Record1.GeocodedAddress = Record2.GeocodedAddress` |
| LegalEntity | ExactName | Exact Name | 75 | `Record1.Name = Record2.Name` |

Validated demo example:

- `Apex Data Services LLC` and `Apex Data Services, LLC` use the same FEIN.
- The `ExactEIN` rule scores 100.
- Because the auto-confirm threshold is 99, the golden Apex record is automatically approved/clean in the demo environment.

Duplicate review is exposed through `ManageDuplicatesOnLegalEntity`, which configures the duplicate management workspace used to review and resolve potential legal entity matches.

## Unique Keys

| Entity | Unique key | Label | Scope | Key attributes |
|---|---|---|---|---|
| Contact | UniqueSSN | Unique SSN | PRE_CONSO | `SSN` |
| Fund | ChainID | Chain ID | PRE_CONSO | `ChainID` |
| LegalEntity | ChainID | Chain ID | POST_CONSO | `ChainID` |
| LegalEntity | NormalizedName | Normalized Name | POST_CONSO | `NormalizedName` |
| LegalEntity | USFEIN | US-FEIN | POST_CONSO | `USFEIN` |
| Portfolio | ChainID | Chain ID | PRE_CONSO | `ChainID` |

## Survivorship

The Legal Entity entity includes survivorship rules that decide which source value survives during consolidation. Publishers configured in the model are `Salesforce`, `Investran`, `EntityHub`, `GENEVA`, and `TAX`.

| Rule | Type | Strategy | Default? | Attributes | Publisher ranking | Description |
|---|---|---|---|---|---|---|
| ChainID | StandardSurvivorshipRule | PREFERRED_PUBLISHER | false | `ChainID` | `Salesforce`, `Investran`, `EntityHub`, `GENEVA` | Selects the surviving Chain ID from preferred publishers, prioritizing Salesforce, Investran, EntityHub, and GENEVA. |
| DefaultRule | StandardSurvivorshipRule | PREFERRED_PUBLISHER | true | (default scope) | `Salesforce`, `Investran`, `EntityHub`, `GENEVA` | Applies the default preferred-publisher survivorship strategy for legal entity attributes not handled by a specific rule. |
| IdSurvivorshipRule | IDSurvivorshipRule | CUSTOM_RANKING | (none) | (default scope) | (none) | Selects the surviving legal entity identifier using custom ranking during consolidation. |
| MostFrequentValue | StandardSurvivorshipRule | MOST_FREQUENT_VALUE | false | `Category`, `Subcategory`, `Startegy` | (none) | Selects the most frequent category, subcategory, and strategy values during legal entity consolidation. |
| TAX | StandardSurvivorshipRule | PREFERRED_PUBLISHER | false | `K1DueJune30`, `EnableTaxSoftware`, `NewInTY22`, `FinalInTY22`, `FormADVPF` | `TAX`, `EntityHub`, `GENEVA`, `Investran`, `Salesforce` | Selects surviving tax workflow attributes from preferred publishers, prioritizing TAX before other source systems. |

## Additional Built-in Validation Behavior

In addition to the explicit validation artifacts above, the model relies on built-in authoring and reference validation behavior:

- Entity attributes and references marked as mandatory are enforced by the model and workflow steppers.
- References use pre-consolidation validation behavior to enforce valid relationships to countries, states, entity types, status, currency, category, subcategory, strategy, forms, name types, funds, portfolios, offices, banks, account types, and roles.
- Workflow steppers trigger validation warnings for legal entity type, US FEIN, leading special characters, duplicate detection, LOV fields, and foreign-key references before users submit tasks.
- State pickers are filtered by selected country, and subcategory pickers are filtered by selected category in the authoring forms.
- The create/edit workflow supports comments, attachments, due dates, and priority so approval context can be captured alongside data changes.
- The `Portfolio Change Approval` workflow uses the `ApprovePortfolioChange` stepper to separate `Current Assignment` from `Proposed Assignment`.
- The `New Portfolio` selector is sorted alphabetically and highlights the changed field for requester and approver review.
- The approval task can be claimed from `Team To Do`; publication runs through `INTEGRATE_ALL` and can be run in the background.

You can extend these validations to enforce additional private-equity requirements, such as mandatory tax documents for selected entity types, jurisdiction-specific identifiers, stricter portfolio-move eligibility, or stricter workflow transitions. For the full entity and attribute inventory, refer to the [model structure page](./model_structure.md).
