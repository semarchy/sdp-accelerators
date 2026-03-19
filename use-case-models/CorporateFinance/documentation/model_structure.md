# Corporate Finance Accelerator - Model Structure

This page documents the model entities and their attributes. The summary table gives a quick overview, and the detailed sections list attribute metadata as configured in the Corporate Finance Accelerator.

Notes:
- Entity names and labels reflect the model configuration.
- If a label or description looks sparse, treat the model definition as the authoritative source until it is enriched in the model itself.

Related pages:
- [user guide](./user_guide.md)
- [enrichers](./enrichers.md)
- [validations](./validations.md)

## Model Diagrams

- [Full Corporate Finance Model](../resources-WIP/image-libraries/corpfin/corpfin_model.png)
- [Organizational Structure Sub-model](../resources-WIP/image-libraries/corpfin/corpfinOrg_model.png)
- [CoA and Mappings Sub-model](../resources-WIP/image-libraries/corpfin/corpfinCoA_model.png)
- [Counterparty Domain Sub-model](../resources-WIP/image-libraries/corpfin/corpfinCounterparty_model.png)
- [Reference and Time Sub-model](../resources-WIP/image-libraries/corpfin/corpfinRef_model.png)

Below is a summary table of all entities in the Corporate Finance model, grouped by sub-model and linked to their detailed sections.

| Sub-model | Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|---|---|---|---|---|---|---|
| Organizational Structure | [OrgUnit](#orgunit) | Org Unit | Master list of cost centers, profit centers, business units, and legal entities. | ChartOfAccounts, MappingSet, OrgHierarchyNode, OrgUnitCoAAssignment, OrgUnitMappingCoverage | Counterparty, OrgUnitType | 7 |
| Organizational Structure | [OrgUnitType](#orgunittype) | Org Unit Type |  | OrgUnit | (none) | 3 |
| Organizational Structure | [OrgHierarchy](#orghierarchy) | Org Hierarchy | Organizational hierarchy definition. | OrgHierarchyNode | (none) | 8 |
| Organizational Structure | [OrgHierarchyNode](#orghierarchynode) | Org Hierarchy Node | Nodes within an organizational hierarchy linked to org units. | OrgHierarchyNode | OrgHierarchy, OrgHierarchyNode, OrgUnit | 5 |
| Organizational Structure | [OrgUnitCoAAssignment](#orgunitcoaassignment) | Org Unit CoA Assignment | Associates organizational units with charts of accounts. | (none) | ChartOfAccounts, OrgUnit | 4 |
| Organizational Structure | [OrgUnitMappingCoverage](#orgunitmappingcoverage) | Org Unit Mapping Coverage | Specifies which mapping sets/versions apply to an org unit. | (none) | MappingSet, OrgUnit | 4 |
| CoA and Mappings | [ChartOfAccounts](#chartofaccounts) | Chart Of Accounts | Defines a chart of accounts for operational, statutory, or group reporting. | Account, MappingSet, OrgUnitCoAAssignment | Currency, OrgUnit | 6 |
| CoA and Mappings | [Account](#account) | Account | Chart of accounts entry. | Account, AccountMapping, SplitAllocation | Account, ChartOfAccounts | 7 |
| CoA and Mappings | [MappingSet](#mappingset) | Mapping Set | Defines mapping scopes between charts of accounts. | AccountMapping, OrgUnitMappingCoverage | ChartOfAccounts, OrgUnit | 4 |
| CoA and Mappings | [MappingType](#mappingtype) | Mapping Type |  | AccountMapping | (none) | 3 |
| CoA and Mappings | [MappingRule](#mappingrule) | Mapping Rule | Defines conditional or split logic for account mappings. | AccountMapping | (none) | 6 |
| CoA and Mappings | [AccountMapping](#accountmapping) | Account Mapping | Links source accounts to target accounts or rules. | SplitAllocation | Account, MappingRule, MappingSet, MappingType | 4 |
| CoA and Mappings | [SplitAllocation](#splitallocation) | Split Allocation | Breaks mapping amounts across multiple target accounts. | (none) | Account, AccountMapping | 4 |
| Counterparty Domain | [CounterpartyGroup](#counterpartygroup) | Counterparty Group | Hierarchy of related counterparties. | Counterparty, CounterpartyGroup | CounterpartyGroup, Country | 8 |
| Counterparty Domain | [Counterparty](#counterparty) | Counterparty | Golden record for any customer or supplier organization. | BankAccount, ContactInformation, CounterpartyAddress, Customer, OrgUnit, RiskComplianceProfile, Supplier | CounterpartyGroup, Country, Currency | 9 |
| Counterparty Domain | [CounterpartyAddress](#counterpartyaddress) | Counterparty Address | Associates a counterparty to a mastered address. | (none) | Address, Counterparty | 2 |
| Counterparty Domain | [Address](#address) | Address |  | CounterpartyAddress | Country | 9 |
| Counterparty Domain | [ContactInformation](#contactinformation) | Contact Information | Named contacts for a counterparty. | (none) | Counterparty | 7 |
| Counterparty Domain | [BankAccount](#bankaccount) | Bank Account | Banking coordinates associated with a counterparty. | Supplier | Counterparty, Currency | 8 |
| Counterparty Domain | [Customer](#customer) | Customer | Customer-specific view of the counterparty. | (none) | Counterparty, Currency | 6 |
| Counterparty Domain | [Supplier](#supplier) | Supplier | Supplier-specific view of the counterparty. | (none) | BankAccount, Counterparty | 4 |
| Counterparty Domain | [RiskComplianceProfile](#riskcomplianceprofile) | Risk Compliance Profile | Captures sanction and AML monitoring details. | (none) | Counterparty | 8 |
| Reference and Time | [Region](#region) | Region | Geographical region or location. | Country | (none) | 6 |
| Reference and Time | [Country](#country) | Country |  | Address, Counterparty, CounterpartyGroup, TaxCode | Currency, Region | 11 |
| Reference and Time | [Currency](#currency) | Currency |  | BankAccount, ChartOfAccounts, Counterparty, Country, Customer | (none) | 8 |
| Reference and Time | [FiscalCalendar](#fiscalcalendar) | Fiscal Calendar |  | FiscalPeriod | (none) | 8 |
| Reference and Time | [FiscalPeriod](#fiscalperiod) | Fiscal Period | Fiscal period for accounting and reporting. | (none) | FiscalCalendar | 7 |
| Reference and Time | [TaxCode](#taxcode) | Tax Code |  | (none) | Country | 5 |
| Reference and Time | [CostType](#costtype) | Cost Type |  | CostType | CostType | 5 |
| Reference and Time | [StatusCode](#statuscode) | Status Code |  | (none) | (none) | 5 |

---

# Detailed Model Structure

Below are markdown tables for each entity in the model. Each table lists the attributes and their metadata.

## Organizational Structure

### OrgUnit

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OrgUnitID | Org Unit ID | String | Yes | Surrogate identifier for organizational unit | No |
| OrgUnitBusinessCode | Org Unit Business Code | String | Yes | External or ERP code for the unit | No |
| NormalizedOrgUnitBusinessCode | Normalized Org Unit Business Code | String | No | Trimmed and uppercased business code for matching | No |
| OrgUnitName | Org Unit Name | String | Yes | Display name of the organizational unit | No |
| NormalizedOrgUnitName | Normalized Org Unit Name | String | No | Trimmed and uppercased organizational unit name for matching | No |
| PhonetizedOrgUnitName | Phonetized Org Unit Name | String | No | Phonetic representation of the org unit name for fuzzy matching | No |
| Description | Description | String | No | Narrative description of responsibilities or scope | No |

---

### OrgUnitType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OrgUnitTypeID | Org Unit Type ID | String | Yes | Surrogate identifier for org unit type | No |
| Type | Type | String | Yes | Org unit type | No |
| Description | Description | String | No | Description of the org unit type | No |

---

### OrgHierarchy

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OrgHierarchyID | Org Hierarchy ID | String | Yes | Surrogate identifier for an organizational hierarchy | No |
| Name | Name | String | Yes | Hierarchy name (e.g., FY2026 Managerial) | No |
| EffectiveStartDate | Effective Start Date | Date | Yes | Effective start date | No |
| EffectiveEndDate | Effective End Date | Date | No | Effective end date | No |
| NormalizedName | Normalized Name | String | No | Trimmed and uppercased hierarchy name | No |
| HierarchyType | Hierarchy Type | String | Yes | Type of hierarchy (Operational, Managerial, Statutory, Group) | No |
| NormalizedHierarchyType | Normalized Hierarchy Type | String | No | Trimmed and uppercased hierarchy type | No |
| Description | Description | String | No | Additional context for the hierarchy | No |

---

### OrgHierarchyNode

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OrgHierarchyNodeID | Org Hierarchy Node ID | String | Yes | Surrogate identifier for a hierarchy node | No |
| EffectiveStartDate | Effective Start Date | Date | Yes | Effective start date | No |
| EffectiveEndDate | Effective End Date | Date | No | Effective end date | No |
| RelationshipType | Relationship Type | String | Yes | Relationship to the parent (ReportsTo, Owns, Consolidates) | No |
| Sequence | Sequence | Integer | No | Ordering of siblings under the same parent | No |

---

### OrgUnitCoAAssignment

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CoAAssignmentID | CoA Assignment ID | String | Yes | Surrogate identifier for CoA usage | No |
| UsageScope | Usage Scope | String | Yes | Purpose of the assignment (Operational, Managerial, Statutory, Group) | No |
| NormalizedUsageScope | Normalized Usage Scope | String | No | Trimmed and uppercased usage scope | No |
| Notes | Notes | String | No | Additional context or restrictions | No |

---

### OrgUnitMappingCoverage

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| MappingCoverageID | Mapping Coverage ID | String | Yes | Surrogate identifier linking units to mappings | No |
| CoverageScope | Coverage Scope | String | Yes | Description of source->target scope (Local->Group, BU->Legal) | No |
| NormalizedCoverageScope | Normalized Coverage Scope | String | No | Trimmed and uppercased coverage scope | No |
| Comments | Comments | String | No | Business notes or approvals | No |

---

## CoA and Mappings

### ChartOfAccounts

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ChartOfAccountsID | Chart Of Accounts ID | String | Yes | Surrogate identifier for the chart of accounts | No |
| Name | Name | String | Yes | Chart of accounts display name | No |
| NormalizedName | Normalized Name | String | No | Trimmed and uppercased chart of accounts name | No |
| Description | Description | String | No | Description or usage context | No |
| AccountingStandard | Accounting Standard | String | No | Accounting framework (Local GAAP, IFRS, etc.) | No |
| IsGroupCoA | Is Group CoA | Boolean | No | Indicates if this is the corporate/group CoA | No |

---

### Account

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AccountID | Account ID | String | Yes | Surrogate identifier for account | No |
| AccountCode | Account Code | String | Yes | Unique code within the CoA | No |
| NormalizedAccountCode | Normalized Account Code | String | No | Trimmed and uppercased account code | No |
| AccountName | Account Name | String | Yes | Account label | No |
| NormalizedAccountName | Normalized Account Name | String | No | Trimmed and uppercased account name | No |
| AccountType | Account Type | String | Yes | Classification (Asset, Liability, etc.) | No |
| IsPosting | Is Posting | Boolean | Yes | Indicates if postings are allowed | No |

---

### MappingSet

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| MappingSetID | Mapping Set ID | String | Yes | Surrogate identifier for mapping scope | No |
| MappingSetName | Mapping Set Name | String | Yes | Mapping set name (e.g., FY2026 Group) | No |
| NormalizedMappingSetName | Normalized Mapping Set Name | String | No | Trimmed and uppercased mapping set name | No |
| Purpose | Purpose | String | Yes | Purpose (Consolidation, Migration, Reporting) | No |

---

### MappingType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| MappingTypeID | Mapping Type ID | String | Yes | Surrogate identifier for mapping type | No |
| Type | Type | String | Yes | Mapping type | No |
| Description | Description | String | No | Description of the mapping type | No |

---

### MappingRule

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RuleID | Rule ID | String | Yes | Surrogate identifier for mapping rule | No |
| RuleName | Rule Name | String | Yes | Rule label | No |
| NormalizedRuleName | Normalized Rule Name | String | No | Trimmed and uppercased rule name | No |
| RuleType | Rule Type | String | Yes | Rule classification (Split, Conditional, Override) | No |
| NormalizedRuleType | Normalized Rule Type | String | No | Trimmed and uppercased rule type | No |
| RuleDescription | Rule Description | String | No | Plain-language description of the split or condition | No |

---

### AccountMapping

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AccountMappingID | Account Mapping ID | String | Yes | Surrogate identifier for account mapping | No |
| Priority | Priority | Integer | No | Order to evaluate when overlaps exist | No |
| Justification | Justification | String | No | Business justification or notes | No |
| ReportingPnLCategoryCode | Reporting PnL Category Code | String | No | BI/reporting category to assign when applying this mapping | No |

---

### SplitAllocation

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SplitAllocationID | Split Allocation ID | String | Yes | Surrogate identifier for split allocation | No |
| SplitPercent | Split Percent | Decimal | Yes | Percentage of amount routed to the target | No |
| NormalizedSplitPercent | Normalized Split Percent | Decimal | No | Cleaned percentage for validation and capping | No |
| Sequence | Sequence | Integer | No | Order of allocation evaluation | No |

---

## Counterparty Domain

### CounterpartyGroup

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CounterpartyGroupID | Counterparty Group ID | String | Yes | Surrogate identifier for counterparty group | No |
| GroupName | Group Name | String | Yes | Counterparty group display name | No |
| NormalizedGroupName | Normalized Group Name | String | No | Trimmed and uppercased group name for matching | No |
| PhonetizedGroupName | Phonetized Group Name | String | No | Phonetic representation of group name for fuzzy matching | No |
| DUNSNumber | DUNS Number | String | No | Global DUNS or external registry number | No |
| NormalizedDUNSNumber | Normalized DUNS Number | String | No | Trimmed and uppercased DUNS/registration identifier | No |
| UltimateParentFlag | Ultimate Parent Flag | Boolean | No | Indicates whether the group is the top of hierarchy | No |
| Sector | Sector | String | No | Industry sector | No |

---

### Counterparty

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CounterpartyID | Counterparty ID | LongInteger | Yes | Surrogate identifier for the counterparty master | No |
| LegalName | Legal Name | String | Yes | Official registered name | Yes |
| NormalizedLegalName | Normalized Legal Name | String | No | Trimmed and uppercased legal name for matching | Yes |
| PhonetizedLegalName | Phonetized Legal Name | String | No | Phonetic representation of legal name for fuzzy matching | Yes |
| TaxID | Tax ID | String | No | Primary tax identification number | Yes |
| NormalizedTaxID | Normalized Tax ID | String | No | Trimmed and uppercased tax identifier | Yes |
| IsCustomer | Is Customer | Boolean | No | Flag indicating customer role | No |
| IsSupplier | Is Supplier | Boolean | No | Flag indicating supplier role | No |
| IsInternalEntity | Is Internal Entity | Boolean | No | Indicates the counterparty is part of our corporate group | No |

---

### CounterpartyAddress

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CounterpartyAddressID | Counterparty Address ID | String | Yes | Surrogate identifier for counterparty address | No |
| AddressType | Address Type | String | Yes | Usage classification (Billing, Shipping, Registered) | No |

---

### Address

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AddressID | Address ID | String | Yes | Surrogate identifier for the address record | No |
| Line1 | Line 1 | String | Yes | Primary address line | No |
| Line2 | Line 2 | String | No | Secondary address line | No |
| City | City | String | Yes | City name | No |
| NormalizedCity | Normalized City | String | No | Trimmed and uppercased city name for matching | No |
| PostalCode | Postal Code | String | No | Postal or ZIP code | No |
| NormalizedPostalCode | Normalized Postal Code | String | No | Trimmed and uppercased postal code for matching | No |
| Region | Region | String | No | State or region name | No |
| NormalizedRegion | Normalized Region | String | No | Trimmed and uppercased region/state value | No |

---

### ContactInformation

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ContactID | Contact ID | String | Yes | Surrogate identifier for contact record | No |
| ContactType | Contact Type | String | Yes | Role of the contact (Primary, Billing, Technical) | No |
| FullName | Full Name | String | Yes | Contact person full name | No |
| Email | Email | String | Yes | Email address | No |
| Phone | Phone | String | Yes | Primary phone number | No |
| Role | Role | String | No | Job role or title | No |
| PreferredLanguage | Preferred Language | String | No | Language preference for communications | No |

---

### BankAccount

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| BankAccountID | Bank Account ID | String | Yes | Surrogate identifier for bank account | No |
| BankName | Bank Name | String | Yes | Legal name of the bank | No |
| IBAN | IBAN | String | Yes | International Bank Account Number | No |
| NormalizedIBAN | Normalized IBAN | String | No | Trimmed and uppercased IBAN for validation | No |
| SWIFT | SWIFT | String | No | SWIFT/BIC code | No |
| NormalizedSWIFT | Normalized SWIFT | String | No | Trimmed and uppercased SWIFT/BIC code | No |
| AccountType | Account Type | String | No | Usage classification (AP, AR, Escrow) | No |
| DefaultFlag | Default Flag | Boolean | No | Indicates if this is the default payout account | No |

---

### Customer

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CustomerID | Customer ID | String | Yes | Source-system customer identifier | No |
| CustomerType | Customer Type | String | No | Business classification (B2B, B2C, etc.) | No |
| PaymentTerms | Payment Terms | String | No | Standard AR payment terms | No |
| NormalizedPaymentTerms | Normalized Payment Terms | String | No | Trimmed and uppercased payment terms for standardization | No |
| CreditLimit | Credit Limit | Decimal | No | Maximum credit exposure | No |
| CreditRating | Credit Rating | String | No | Internal or external credit score | No |

---

### Supplier

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SupplierID | Supplier ID | String | Yes | Source-system supplier identifier | No |
| PaymentTerms | Payment Terms | String | No | Standard AP payment terms | No |
| NormalizedPaymentTerms | Normalized Payment Terms | String | No | Trimmed and uppercased payment terms for standardization | No |
| LeadTimeDays | Lead Time Days | Integer | No | Average lead time in days for fulfillment | No |

---

### RiskComplianceProfile

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RiskProfileID | Risk Profile ID | String | Yes | Surrogate identifier for risk profile | No |
| ScreeningDate | Screening Date | Date | No | Date of latest sanction/AML screening | No |
| SanctionListFlag | Sanction List Flag | Boolean | No | Indicates presence on a sanction list | No |
| RiskScore | Risk Score | Decimal | No | Calculated compliance risk score | No |
| RiskCategory | Risk Category | String | No | Risk category (Low, Medium, High) | No |
| NormalizedRiskCategory | Normalized Risk Category | String | No | Trimmed and uppercased risk category | No |
| LastCheckedDate | Last Checked Date | Date | No | Date of last automated monitoring check | No |
| Notes | Notes | String | No | Additional review notes | No |

---

## Reference and Time

### Region

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RegionID | Region ID | String | Yes | Unique region identifier | No |
| RegionName | Region Name | String | Yes | Region or location name | No |
| NormalizedRegionName | Normalized Region Name | String | No | Trimmed and uppercased region name | No |
| ISOCode | ISO Code | String | No | Standardized ISO or internal region code | No |
| NormalizedISOCode | Normalized ISO Code | String | No | Trimmed and uppercased ISO/internal region code | No |
| ReportingZone | Reporting Zone | String | No | Internal reporting grouping | No |

---

### Country

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CountryID | Country ID | String | Yes | Unique identifier for country | No |
| CountryCode | Country Code | String | Yes | ISO Alpha-3 country code | No |
| NormalizedCountryCode | Normalized Country Code | String | No | Trimmed and uppercased country code | No |
| CountryName | Country Name | String | Yes | Official country name | No |
| NormalizedCountryName | Normalized Country Name | String | No | Trimmed and uppercased country name | No |
| ISOAlpha2 | ISO Alpha-2 | String | No | ISO Alpha-2 code | No |
| NormalizedISOAlpha2 | Normalized ISO Alpha-2 | String | No | Trimmed and uppercased ISO Alpha-2 code | No |
| ISOAlpha3 | ISO Alpha-3 | String | No | ISO Alpha-3 code | No |
| NormalizedISOAlpha3 | Normalized ISO Alpha-3 | String | No | Trimmed and uppercased ISO Alpha-3 code | No |
| GeoZone | Geographic Zone | String | No | Geographic region or continent | No |
| ReportingZone | Reporting Zone | String | No | Internal reporting grouping | No |

---

### Currency

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CurrencyID | Currency ID | String | Yes | Surrogate identifier for currency | No |
| CurrencyCode | Currency Code | String | Yes | ISO 4217 currency code | No |
| NormalizedCurrencyCode | Normalized Currency Code | String | No | Trimmed and uppercased currency code | No |
| CurrencyName | Currency Name | String | Yes | Currency full name | No |
| NormalizedCurrencyName | Normalized Currency Name | String | No | Trimmed and uppercased currency name | No |
| Symbol | Symbol | String | No | Currency symbol | No |
| DecimalPrecision | Decimal Precision | Integer | No | Number of decimals used | No |
| ExchangeRateSource | Exchange Rate Source | String | No | Source of exchange rate | No |

---

### FiscalCalendar

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CalendarID | Calendar ID | String | Yes | Surrogate identifier for fiscal calendar | No |
| CalendarCode | Calendar Code | String | Yes | Business key for the fiscal calendar | No |
| FiscalYear | Fiscal Year | String | Yes | Fiscal year represented | No |
| PeriodCount | Period Count | Integer | Yes | Number of periods in the fiscal year | No |
| StartDate | Start Date | Date | Yes | Fiscal year start date | No |
| EndDate | End Date | Date | Yes | Fiscal year end date | No |
| IsStandard | Is Standard | Boolean | No | Flag indicating the corporate standard calendar | No |
| Description | Description | String | No | Description of the fiscal calendar | No |

---

### FiscalPeriod

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PeriodID | Period ID | String | Yes | Surrogate identifier for the period | No |
| FiscalYear | Fiscal Year | String | Yes | Fiscal year number | No |
| PeriodNumber | Period Number | Integer | Yes | Period number in fiscal year | No |
| PeriodLabel | Period Label | String | Yes | Human-readable business label for the period | No |
| StartDate | Start Date | Date | Yes | Start date of the period | No |
| EndDate | End Date | Date | Yes | End date of the period | No |
| Quarter | Quarter | String | No | Quarter label (Q1, Q2, etc.) | No |

---

### TaxCode

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| TaxCodeID | Tax Code ID | String | Yes | Surrogate identifier for tax code | No |
| Name | Name | String | Yes | Name of the tax code | No |
| Description | Description | String | No | Description of the tax code | No |
| TaxRate | Tax Rate | Decimal | Yes | Tax rate percentage | No |
| JurisdictionType | Jurisdiction Type | String | No | Jurisdiction type (federal, state, etc.) | No |

---

### CostType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CostTypeID | Cost Type ID | String | Yes | Surrogate identifier for cost type | No |
| CostTypeCode | Cost Type Code | String | Yes | Business key or ERP cost type code | No |
| Description | Description | String | Yes | Description of the cost type | No |
| AccountType | Account Type | String | No | Account type the cost type belongs to | No |
| ExpenseGroup | Expense Group | String | No | Expense grouping | No |

---

### StatusCode

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| StatusCode | Status Code | String | Yes | Unique lifecycle code | No |
| Label | Label | String | Yes | Display label for the status | No |
| Description | Description | String | No | Status description | No |
| Category | Category | String | No | Category of entities using the status | No |
| Sequence | Sequence | Integer | No | Ordering sequence | No |

---
