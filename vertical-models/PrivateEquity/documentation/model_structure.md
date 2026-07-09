# Private Equity Accelerator - Model Structure

This page documents the Private Equity model entities and their attributes. The summary table gives a quick overview, and the detailed sections list attribute metadata as configured in the accelerator.

Notes:
- Entity names, labels, descriptions, and documentation are taken from the model configuration under `src/PrivateEquity`.
- The delivered application is `Private Equity`, focused on private-equity legal entity governance, fund and portfolio context, workflow, relationship, office, contact, document, and account use cases.
- `Used in matching` is inferred from the configured SemQL matcher expressions on the `LegalEntity` entity.
- The validated demo is portfolio-forward: `Asia Growth Fund`, `Apex Data Services LLC`, `Asia Growth Fund Software Development`, `Asia Growth Fund Healthcare`, and the `Portfolio Change Approval` workflow.

Related pages:
- [user guide](./user_guide.md)
- [enrichers](./enrichers.md)
- [validations](./validations.md)

## Model Diagrams

- [Groups](../src/PrivateEquity/model_diagrams/Groups.ModelDiagram.seml)
- [Relationships](../src/PrivateEquity/model_diagrams/Relationships.ModelDiagram.seml)
- [Account](../src/PrivateEquity/model_diagrams/Account.ModelDiagram.seml)
- [All Domains](../src/PrivateEquity/model_diagrams/AllDomains.ModelDiagram.seml)
- [Legal Entity](../src/PrivateEquity/model_diagrams/LegalEntity.ModelDiagram.seml)

## Current Demo-Relevant Structures

| Area | Model Support |
| --- | --- |
| Fund hierarchy | `Fund` and `Portfolio` connect `Asia Growth Fund` to industry-focused portfolios. |
| Fund manager context | `FundLE` links funds to legal entities with an `EntityRole`, such as manager. |
| Portfolio assignment | `PortfolioLegalEntity` links portfolios to investment vehicles/legal entities with an `EntityRole`. |
| Investment vehicle 360 | `LegalEntity` is enriched with offices, contacts, names, documents, accounts, parent-child links, and relationship context. |
| Source consolidation | `LegalEntity` matching uses FEIN, name, and address rules to create golden records from source records. |
| Portfolio change approval | `PortfolioChangeApproval` governs changes to `PortfolioLegalEntity` records and publishes through `INTEGRATE_ALL`. |

Below is a summary table of all entities in the Private Equity model, grouped by sub-model and linked to their detailed sections.

| Sub-model | Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|---|---|---|---|---|---|---|
| Legal Entity Core | [LegalEntity](#legalentity) | Legal Entity | In the context of a private equity company, a legal entity refers to a distinct and formal organization established to conduct business activities and hold assets. It is a separate legal entity from its owners and is typically structured as a limited partnership or a limited liability company. Private equity firms often establish multiple legal entities to manage their operations and investments effectively. | Account, Contact, Document, FundLE, GroupLegalEntity, LERelationship, Name, Office, ParentChild, PortfolioLegalEntity | Category, Country, Currency, EntityStructure, EntityType, GeographyType, Industry, Region, Startegy, State, Status, Subcategory | 17 |
| Legal Entity Core | [Office](#office) | Office | Captures office names, phone numbers, and geocoded address details used by contacts and legal entities. | Contact | LegalEntity | 7 |
| Legal Entity Core | [Contact](#contact) | Contact | Captures contact details, professional registrations, email, phone, and address information used to manage people associated with offices and legal entities. | (none) | LegalEntity, Office | 22 |
| Legal Entity Core | [Name](#name) | Name | Join table for LE Names | (none) | LegalEntity, NameType | 2 |
| Legal Entity Core | [NameType](#nametype) | Name Type | Reference Table for Name Types | Name | (none) | 1 |
| Legal Entity Core | [Document](#document) | Document | Join table for the Tax forms of the Legal Entity | (none) | Form, LegalEntity | 3 |
| Legal Entity Core | [Form](#form) | Form | A list of Tax Forms from the IRS | Document | EntityType | 3 |
| Relationships and Hierarchies | [ParentChild](#parentchild) | Parent Child | Join table for Parent Child LE Relationship | (none) | LegalEntity | 1 |
| Relationships and Hierarchies | [LERelationship](#lerelationship) | LE Relationship | Join table for LE Relationships | (none) | LegalEntity, Relationship | 1 |
| Relationships and Hierarchies | [Relationship](#relationship) | Relationship | Reference table for Relationship types | LERelationship | (none) | 1 |
| Relationships and Hierarchies | [LEGroup](#legroup) | LE Group | Information about a LE Group | GroupHierarchy, GroupLegalEntity | Currency, GroupType, InvestmentStructure, Startegy | 6 |
| Relationships and Hierarchies | [GroupType](#grouptype) | Group Type | Maintains controlled values for classifying legal entity groups. | LEGroup | (none) | 1 |
| Relationships and Hierarchies | [GroupHierarchy](#grouphierarchy) | Group Hierarchy | Join table for Group Parent and Child | (none) | Currency, LEGroup | 1 |
| Relationships and Hierarchies | [GroupLegalEntity](#grouplegalentity) | Group Legal Entity | Join table for Grouping LEs, One group has multiple entities and one entity can be in multiple groups | (none) | LEGroup, LegalEntity | 1 |
| Relationships and Hierarchies | [InvestmentStructure](#investmentstructure) | Investment Structure | Maintains controlled values for classifying the investment structure associated with a legal entity group. | LEGroup | (none) | 1 |
| Funds, Portfolios, and Accounts | [Fund](#fund) | Fund | Private equity companies offer various investment products to their investors, with the most common being funds. A fund is a pooled investment vehicle that allows investors to pool their capital together, which is then managed by the private equity firm. These funds serve as investment vehicles through which the firm invests in various assets such as private companies, real estate, or other alternative investments. | Account, FundLE, Portfolio | Portfolio | 4 |
| Funds, Portfolios, and Accounts | [Portfolio](#portfolio) | Portfolio | Within a private equity fund, there are portfolios. A portfolio represents a collection of investments held by the fund. Private equity firms typically manage multiple portfolios within a fund, each comprising a set of investments with common characteristics or objectives. Portfolios can be segmented based on factors such as industry, geographic location, risk profile, or investment stage. | Account, Fund, PortfolioLegalEntity | Fund, Industry | 4 |
| Funds, Portfolios, and Accounts | [FundLE](#fundle) | Fund LE | Join table for Fund's Legal Entities | (none) | EntityRole, Fund, LegalEntity | 2 |
| Funds, Portfolios, and Accounts | [PortfolioLegalEntity](#portfoliolegalentity) | Portfolio Legal Entity | Links portfolios to legal entities and records each entity role so portfolio participation can be governed consistently. | (none) | EntityRole, LegalEntity, Portfolio | 1 |
| Funds, Portfolios, and Accounts | [EntityRole](#entityrole) | Entity Role | Maintains controlled values describing the business role a legal entity has in relationship tables. | FundLE, PortfolioLegalEntity | (none) | 1 |
| Funds, Portfolios, and Accounts | [Account](#account) | Account | Captures bank account identifiers and derived account keys used to link accounts to legal entities, funds, portfolios, and banks in operational and reporting workflows. | (none) | AccountType, Bank, Fund, LegalEntity, Portfolio | 6 |
| Funds, Portfolios, and Accounts | [AccountType](#accounttype) | Account Type | Maintains the controlled list of account type values used to categorize bank accounts during stewardship and integration. | Account | (none) | 2 |
| Funds, Portfolios, and Accounts | [Bank](#bank) | Bank | Maintains the list of banks used when assigning and validating account records. | Account | (none) | 1 |
| Reference Data and Classification | [Category](#category) | Category | Deal Related, Fund Related, etc. Reference Oaktree model | LegalEntity, Subcategory | (none) | 1 |
| Reference Data and Classification | [Subcategory](#subcategory) | Subcategory | Reference for Subcategories | LegalEntity | Category | 2 |
| Reference Data and Classification | [EntityType](#entitytype) | Entity Type | Individual or Organization, filters the Forms and Attributes | Form, LegalEntity | (none) | 1 |
| Reference Data and Classification | [EntityStructure](#entitystructure) | Entity Structure | Legal Structure like LLC, INC, Corp, etc. | LegalEntity | (none) | 2 |
| Reference Data and Classification | [Status](#status) | Status | Reference Table for LE Statuses | LegalEntity | (none) | 1 |
| Reference Data and Classification | [Startegy](#startegy) | Startegy | Reference Table for Strategies | LEGroup, LegalEntity | (none) | 2 |
| Reference Data and Classification | [Industry](#industry) | Industry | Maintains controlled industry values used to classify portfolios and legal entities. | LegalEntity, Portfolio | (none) | 1 |
| Reference Data and Classification | [GeographyType](#geographytype) | Geography Type | Domestic or International | LegalEntity | (none) | 2 |
| Reference Data and Classification | [Region](#region) | Region | Maintains regional reference values used with countries and legal entities for geographic reporting. | LegalEntity | (none) | 1 |
| Reference Data and Classification | [Country](#country) | Country | Maintains ISO and local country identifiers used by address, region, tax, and reporting workflows. | LegalEntity, State | (none) | 10 |
| Reference Data and Classification | [State](#state) | State | Reference table for States | LegalEntity | Country | 4 |
| Reference Data and Classification | [Currency](#currency) | Currency | Maintains currency codes, effective dates, symbols, and minor units used for financial classification and reporting. | GroupHierarchy, LEGroup, LegalEntity | (none) | 9 |

## Legal Entity Core

### LegalEntity

Represents a formal legal organization or individual managed for tax, accounting, relationship, and investment workflows.

References: `Category`, `Country`, `Currency`, `EntityStructure`, `EntityType`, `GeographyType`, `Industry`, `Region`, `Startegy`, `State`, `Status`, `Subcategory`
Referenced by: `Account`, `Contact`, `Document`, `FundLE`, `GroupLegalEntity`, `LERelationship`, `Name`, `Office`, `ParentChild`, `PortfolioLegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the legal entity record. | No |
| Name | Name | String | No | Business name used to identify the legal entity record in stewardship screens and integrations. | Yes |
| NormalizedName | Normalized Name | String | No | Uppercased and trimmed legal entity name used for matching and validation. | Yes |
| Website | Website | String | No | Website URL associated with the legal entity. | No |
| SSN | SSN | String | No | Social Security Number captured when the legal entity is an individual. | No |
| USFEIN | USFEIN | String | No | United States Federal Employer Identification Number used for tax identification. | Yes |
| NewInTY22 | New In TY22 | PrivateEquity.list_of_values.YesNo | No | Indicates whether the legal entity was newly included in tax year 2022 processing. | No |
| EnableTaxSoftware | Enable Tax Software | PrivateEquity.list_of_values.YesNo | No | Indicates whether the legal entity should be enabled in tax software integrations. | No |
| K1DueJune30 | K1 Due June30 | PrivateEquity.list_of_values.YesNo | No | Indicates whether Schedule K-1 is due by June 30 for the legal entity. | No |
| FiscalYearEnd | Fiscal Year End | PrivateEquity.list_of_values.FiscalYearEnd | No | Fiscal year-end value used for tax and reporting timelines. | No |
| Revenue | Revenue | Integer | No | Revenue amount associated with legal entity reporting. | No |
| FormADVPF | Form ADV / PF | PrivateEquity.list_of_values.YesNo | No | Indicates whether Form ADV or Form PF applies to the legal entity. | No |
| FinalInTY22 | Final In TY22 | PrivateEquity.list_of_values.YesNo | No | Indicates whether the legal entity was final in tax year 2022 processing. | No |
| FiscalYear | Fiscal Year | Boolean | No | Indicates whether the legal entity follows a fiscal year basis. | No |
| ChainID | Chain ID | String | No | Source chain identifier used to align the legal entity with upstream private equity systems. | No |
| GeocodedAddress | Geocoded Address | PrivateEquity.complex_types.GeocodedAddressType | No | Geocoded address generated from legal entity address inputs. | Yes |
| InputAddress | Input Address | PrivateEquity.complex_types.InputAddressType | No | Source address captured for geocoding and legal entity location management. | No |

---

### Office

Represents an office location associated with legal entities and contacts, including phone and address data.

References: `LegalEntity`
Referenced by: `Contact`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the office record. | No |
| Phone | Phone | String | No | Phone number supplied for the office. | No |
| StandarizedPhone | Standarized Phone | String | No | Standardized office phone number generated for consistent contact and office communication. | No |
| Name | Name | String | Yes | Business name used to identify the office record in stewardship screens and integrations. | No |
| NormalizedName | Normalized Name | String | No | Uppercased and trimmed office name used for matching and validation. | No |
| GeocodedAddress | Geocoded Address | PrivateEquity.complex_types.GeocodedAddressType | No | Geocoded address generated from office address inputs. | No |
| SourceAddress | Source Address | PrivateEquity.complex_types.InputAddressType | No | Source address captured for office geocoding and location management. | No |

---

### Contact

Represents a person or business contact associated with a legal entity or office.

References: `LegalEntity`, `Office`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the contact record. | No |
| Series7 | Series 7 | Boolean | No | Indicates whether the contact holds the FINRA Series 7 registration. | No |
| MiddleName | Middle Name | String | No | Middle name or initial used to distinguish the contact when needed. | No |
| Series82 | Series 82 | Boolean | No | Indicates whether the contact holds the FINRA Series 82 registration. | No |
| Series62 | Series 62 | Boolean | No | Indicates whether the contact holds the FINRA Series 62 registration. | No |
| StandarizedMobile | Standarized Mobile | String | No | Standardized mobile phone number generated for consistent contact matching and communication. | No |
| Mobile | Mobile | String | No | Mobile phone number supplied for the contact. | No |
| FullName | Full Name | String | No | Derived full name built from the contact first and last name values. | No |
| FirstName | First Name | String | Yes | Given name used to identify and communicate with the contact. | No |
| Phone | Office Phone | String | No | Office phone number associated with the contact. | No |
| CleansedEmail | Cleansed Email | String | No | Standardized email value generated from the contact email address. | No |
| Series22 | Series 22 | Boolean | No | Indicates whether the contact holds the FINRA Series 22 registration. | No |
| Series66 | Series 66 | Boolean | No | Indicates whether the contact holds the FINRA Series 66 registration. | No |
| Series65 | Series 65 | Boolean | No | Indicates whether the contact holds the FINRA Series 65 registration. | No |
| Email | Email | String | No | Email address supplied for the contact. | No |
| Series6 | Series 6 | Boolean | No | Indicates whether the contact holds the FINRA Series 6 registration. | No |
| SSN | SSN | String | No | Social Security Number captured for contact identification where required. | No |
| LastName | Last Name | String | Yes | Family name used to identify and sort the contact. | No |
| JobTitle | Job Title | String | No | Job title or business role held by the contact. | No |
| MobileGeocodingData | Mobile Geocoding Data | String | No | Geocoding metadata returned during mobile phone standardization. | No |
| ValidEmailDomain | Valid Email Domain | String | No | Indicator showing whether the email domain passed validation. | No |
| Address | Address | PrivateEquity.complex_types.InputAddressType | No | Input address associated with the contact for location and phone standardization context. | No |

---

### Name

Join table for LE Names

References: `LegalEntity`, `NameType`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the name record. | No |
| Name | Name | String | Yes | Business name used to identify the name record in stewardship screens and integrations. | No |

---

### NameType

Reference Table for Name Types

References: `(none)`
Referenced by: `Name`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| NameType | Name Type | String | Yes | Controlled reference value used to classify name type records. | No |

---

### Document

Join table for the Tax forms of the Legal Entity

References: `Form`, `LegalEntity`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the document record. | No |
| URL | URL | String | No | URL pointing to the document or form resource. | No |
| DueDate | Due Date | Date | No | Due date by which the document or tax form is expected. | No |

---

### Form

A list of Tax Forms from the IRS

References: `EntityType`
Referenced by: `Document`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | Unique identifier for the form record. | No |
| Name | Name | String | Yes | Business name used to identify the form record in stewardship screens and integrations. | No |
| Description | Description | String | No | Free-text explanation that clarifies the meaning or business use of the form value. | No |

---


## Relationships and Hierarchies

### ParentChild

Join table for Parent Child LE Relationship

References: `LegalEntity`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the parent child record. | No |

---

### LERelationship

Join table for LE Relationships

References: `LegalEntity`, `Relationship`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the LE relationship record. | No |

---

### Relationship

Reference table for Relationship types

References: `(none)`
Referenced by: `LERelationship`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Relationship | Relationship | String | Yes | Controlled reference value used to classify relationship records. | No |

---

### LEGroup

Information about a LE Group

References: `Currency`, `GroupType`, `InvestmentStructure`, `Startegy`
Referenced by: `GroupHierarchy`, `GroupLegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the LE group record. | No |
| Name | Name | String | No | Business name used to identify the LE group record in stewardship screens and integrations. | No |
| InceptionDate | Inception Date | Date | No | Date on which the legal entity group was established. | No |
| InheritedCurrency | Inherited Currency | String | No | Currency inherited by the legal entity group from related configuration or parent context. | No |
| StartDate | Start Date | Date | No | Start date for the legal entity group assignment or validity period. | No |
| EndDate | End Date | Date | No | End date for the legal entity group assignment or validity period. | No |

---

### GroupType

Defines reference values used to classify legal entity groups.

References: `(none)`
Referenced by: `LEGroup`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| GroupType | Group Type | String | Yes | Controlled reference value used to classify group type records. | No |

---

### GroupHierarchy

Join table for Group Parent and Child

References: `Currency`, `LEGroup`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the group hierarchy record. | No |

---

### GroupLegalEntity

Join table for Grouping LEs, One group has multiple entities and one entity can be in multiple groups

References: `LEGroup`, `LegalEntity`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the group legal entity record. | No |

---

### InvestmentStructure

Defines reference values that classify investment structures used by legal entity groups.

References: `(none)`
Referenced by: `LEGroup`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| InvestmentStructure | Investment Structure | String | Yes | Controlled reference value used to classify investment structure records. | No |

---


## Funds, Portfolios, and Accounts

### Fund

Represents an investment fund used to organize portfolios and related legal entities.

References: `Portfolio`
Referenced by: `Account`, `FundLE`, `Portfolio`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | Integer | Yes | Unique identifier for the fund record. | No |
| Name | Name | String | Yes | Business name used to identify the fund record in stewardship screens and integrations. | No |
| ChainID | Chain ID | Integer | Yes | Source chain identifier used to align the fund with upstream private equity systems. | No |
| Description | Description | String | No | Free-text explanation that clarifies the meaning or business use of the fund value. | No |

---

### Portfolio

Represents a portfolio within a fund used to group investments and related legal entities.

References: `Fund`, `Industry`
Referenced by: `Account`, `Fund`, `PortfolioLegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the portfolio record. | No |
| ChainID | Chain ID | String | Yes | Source chain identifier used to align the portfolio with upstream private equity systems. | No |
| Description | Description | String | No | Free-text explanation that clarifies the meaning or business use of the portfolio value. | No |
| Name | Name | String | Yes | Business name used to identify the portfolio record in stewardship screens and integrations. | No |

---

### FundLE

Join table for Fund's Legal Entities

References: `EntityRole`, `Fund`, `LegalEntity`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the fund LE record. | No |
| Code | Code | String | No | Business code used to identify the fund-to-legal-entity association. | No |

---

### PortfolioLegalEntity

Associates portfolios with legal entities and captures the role of each entity in a portfolio context.

References: `EntityRole`, `LegalEntity`, `Portfolio`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the portfolio legal entity record. | No |

---

### EntityRole

Defines the role a legal entity plays in a fund, portfolio, group, or relationship.

References: `(none)`
Referenced by: `FundLE`, `PortfolioLegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| EntityRole | Entity Role | String | Yes | Controlled reference value used to classify entity role records. | No |

---

### Account

Represents a bank account associated with a legal entity, fund, portfolio, and banking institution.

References: `AccountType`, `Bank`, `Fund`, `LegalEntity`, `Portfolio`
Referenced by: `(none)`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Unique identifier for the account record. | No |
| RoutingNumber | Routing Number | String | No | Bank routing number used to identify the financial institution for account validation and payments. | No |
| Name | Name | String | No | Business name used to identify the account record in stewardship screens and integrations. | No |
| AccountKey | Account Key | String | No | Derived composite key combining fund, portfolio, and chain identifiers to identify an account across integrations. | No |
| AccountNumber | Account Number | String | No | Bank account number used to identify the account at the servicing bank. | No |
| ChainID | Chain ID | String | Yes | Source chain identifier used to align the account with upstream private equity systems. | No |

---

### AccountType

Defines reference values used to classify bank accounts by business purpose or account category.

References: `(none)`
Referenced by: `Account`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AccountType | Account Type | String | Yes | Controlled reference value used to classify account type records. | No |
| Description | Description | String | No | Free-text explanation that clarifies the meaning or business use of the account type value. | No |

---

### Bank

Defines banking institutions used to associate accounts with their servicing bank.

References: `(none)`
Referenced by: `Account`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Bank | Bank | String | Yes | Controlled reference value used to classify bank records. | No |

---


## Reference Data and Classification

### Category

Deal Related, Fund Related, etc. Reference Oaktree model

References: `(none)`
Referenced by: `LegalEntity`, `Subcategory`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Category | Category | String | Yes | Controlled reference value used to classify category records. | No |

---

### Subcategory

Reference for Subcategories

References: `Category`
Referenced by: `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Subcategory | Subcategory | String | Yes | Controlled reference value used to classify subcategory records. | No |
| Description | Description | String | No | Free-text explanation that clarifies the meaning or business use of the subcategory value. | No |

---

### EntityType

Individual or Organization, filters the Forms and Attributes

References: `(none)`
Referenced by: `Form`, `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| EntityType | Entity Type | String | Yes | Controlled reference value used to classify entity type records. | No |

---

### EntityStructure

Legal Structure like LLC, INC, Corp, etc.

References: `(none)`
Referenced by: `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| EntityStructure | Entity Structure | String | Yes | Controlled reference value used to classify entity structure records. | No |
| Description | Description | String | No | Free-text explanation that clarifies the meaning or business use of the entity structure value. | No |

---

### Status

Reference Table for LE Statuses

References: `(none)`
Referenced by: `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Status | Status | String | Yes | Controlled reference value used to classify status records. | No |

---

### Startegy

Reference Table for Strategies

References: `(none)`
Referenced by: `LEGroup`, `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Startegy | Startegy | String | Yes | Controlled reference value used to classify strategy records. | No |
| Description | Description | String | No | Free-text explanation that clarifies the meaning or business use of the strategy value. | No |

---

### Industry

Defines industry reference values used to classify portfolios and legal entities.

References: `(none)`
Referenced by: `LegalEntity`, `Portfolio`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Industry | Industry | String | Yes | Controlled reference value used to classify industry records. | No |

---

### GeographyType

Domestic or International

References: `(none)`
Referenced by: `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| GeographyType | Geography Type | String | Yes | Controlled reference value used to classify geography type records. | No |
| Description | Description | String | No | Free-text explanation that clarifies the meaning or business use of the geography type value. | No |

---

### Region

Defines regional reference values used for geographic classification and reporting.

References: `(none)`
Referenced by: `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Region | Region | String | Yes | Controlled reference value used to classify region records. | No |

---

### Country

Defines country reference data used for addresses, tax reporting, and geographic classification.

References: `(none)`
Referenced by: `LegalEntity`, `State`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | Unique identifier for the country record. | No |
| GEC | GEC | String | No | Geopolitical Entities, Names, and Codes identifier for the country. | No |
| EnglishShortName | English Short Name | String | No | Short English country name used in user-facing lists and search. | No |
| EnglishFullName | English Full Name | String | No | Full English country name used for formal reporting and reference. | No |
| FlagURL | Flag URL | String | No | URL for the country flag image used in reference displays. | No |
| URLWikipedia | URL Wikipedia | String | No | Wikipedia URL used as an external country reference. | No |
| Alpha3Code | ISO 3166-1 3-Letter Code | String | No | Three-letter ISO 3166-1 country code used for country identification and integration. | No |
| Alpha2Code | ISO 3166-1 2-Letter Code | String | No | Two-letter ISO 3166-1 country code used for country identification and integration. | No |
| NumericCode | Numeric Code | String | No | Numeric ISO 3166-1 country code used for standards-based integration. | No |
| LocalShortName | Local Short Name | String | No | Local short country name used for regional display and reference. | No |

---

### State

Reference table for States

References: `Country`
Referenced by: `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | Unique identifier for the state record. | No |
| Name | Name | String | Yes | Business name used to identify the state record in stewardship screens and integrations. | No |
| Code | Code | String | No | State or province code used for address and geographic reference. | No |
| FIPSCode | FIPS Code | String | No | Federal Information Processing Standards code used for state reference and integration. | No |

---

### Currency

Defines currency reference data used for financial classification and reporting.

References: `(none)`
Referenced by: `GroupHierarchy`, `LEGroup`, `LegalEntity`

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | Unique identifier for the currency record. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the currency reference value is valid. | No |
| NumericCode | Numeric Code | Integer | No | Numeric ISO currency code used for standards-based integration. | No |
| AlphabeticCode | Alphabetic Code | String | No | Three-letter ISO currency code used for financial reporting and integration. | No |
| CommonSymbols | Common Symbols | String | No | Common currency symbols used for display and recognition. | No |
| IsCurrent | Is Current | Boolean | No | Indicates whether the currency is currently active for business use. | No |
| EffectiveTo | Effective To | Date | No | Date through which the currency reference value is valid. | No |
| MinorUnit | Minor Unit | ShortInteger | No | Number of decimal places used by the currency minor unit. | No |
| Name | Name | String | No | Currency name used in reference lists and stewardship screens. | No |

---
