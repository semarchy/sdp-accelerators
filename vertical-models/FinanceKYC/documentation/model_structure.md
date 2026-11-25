## Finance KYC Model Structure

Below is a summary table of all entities in the Finance KYC model, including their label, documentation, references, and attribute count.

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|-------------|--------------|----------------------|------------------------|--------------------|---------------------|
| Address | Address |  | (none) | Customer | 12 |
| BankAccount | Bank Account |  | (none) | Customer | 9 |
| BankingContract | Banking Contract |  | BankingContractRole | BankingProduct, Customer | 8 |
| BankingContractRole | Banking Contract Role |  | (none) | BankingContract, Customer | 6 |
| BankingProduct | Banking Product |  | BankingContract | BankingProductCategory | 8 |
| BankingProductCategory | Banking Product Category |  | BankingProduct | (none) | 5 |
| ContactInformation | Contact Information |  | (none) | Customer | 9 |
| CorporateEntity | Corporate Entity |  | UBO | Customer | 13 |
| Customer | Customer |  | Address, BankAccount, BankingContract, BankingContractRole, ContactInformation, CorporateEntity, CustomerRiskProfile, IdDocument, IndividualPerson, InsuranceContract, InsuranceContractRole, KYCCheck, KYCReview, Relationship | (none) | 8 |
| CustomerRiskProfile | Customer Risk Profile |  | (none) | Customer | 9 |
| Employment | Employment |  | (none) | IndividualPerson | 7 |
| IdDocument | Id Document |  | (none) | Customer | 9 |
| IndividualPerson | Individual Person |  | Employment | Customer | 14 |
| InsuranceContract | Insurance Contract |  | InsuranceContractRole | Customer, InsuranceProduct | 8 |
| InsuranceContractRole | Insurance Contract Role |  | (none) | Customer, InsuranceContract | 6 |
| InsuranceProduct | Insurance Product |  | InsuranceContract | InsuranceProductCategory | 8 |
| InsuranceProductCategory | Insurance Product Category |  | InsuranceProduct | (none) | 5 |
| KYCCheck | KYCCheck |  | (none) | Customer | 9 |
| KYCReview | KYCReview |  | (none) | Customer | 8 |
| Relationship | Relationship |  | (none) | Customer | 6 |
| UBO | UBO |  | (none) | CorporateEntity | 7 |
---

# Detailed Model Structure

Below are markdown tables for each entity in the model. Each table lists the attributes and their metadata.

## Address

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| AddressID | Address ID | LongInteger | Yes |  |
| AddressType | Address Type | String | No |  |
| Street | Street | String | No |  |
| City | City | String | Yes |  |
| PostalCode | Postal Code | String | No |  |
| Country | Country | String | Yes |  |
| State | State | String | No |  |
| FullAddress | Full Address | String | No |  |
| EnrichedAddress | Enriched Address | String | No |  |
| ValidFrom | Valid From | Date | No |  |
| ValidTo | Valid To | Date | No |  |
| IsCurrent | Is Current | Boolean | No |  |

---

## BankAccount

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| BankAccountID | Bank Account ID | String | Yes |  |
| BankName | Bank Name | String | Yes |  |
| AccountNumber | Account Number | String | Yes |  |
| IBAN | IBAN | String | Yes |  |
| AccountType | Account Type | String | No |  |
| Currency | Currency | String | No |  |
| OpenDate | Open Date | Date | No |  |
| CloseDate | Close Date | Date | No |  |
| IsActive | Is Active | Boolean | No |  |

---

## BankingContract

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| BankingContractID | Banking Contract ID | String | Yes | Unique identifier for the banking contract |
| ContractName | Contract Name | String | Yes | Name of the contract |
| StartDate | Start Date | Date | No | Contract start date |
| EndDate | End Date | Date | No | Contract end date |
| Status | Status | String | No | Contract status |
| Amount | Amount | Decimal | No | Contract amount |
| Currency | Currency | String | No | Currency |
| Notes | Notes | String | No | Additional notes |

---

## BankingContractRole

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| ContractRoleID | Banking Contract Role ID | String | Yes | Unique identifier for the contract role |
| Role | Role | String | Yes | Role in the contract |
| StartDate | Start Date | Date | No | Start date |
| EndDate | End Date | Date | No | End date |
| IsActive | Is Active | Boolean | No | Active flag |
| Notes | Notes | String | No | Additional notes |

---

## BankingProduct

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| BankingProductID | Banking Product ID | String | Yes | Unique identifier for the banking product |
| ProductName | Product Name | String | Yes | Name of the banking product |
| ProductType | Product Type | String | Yes | Type of product |
| Currency | Currency | String | Yes | Currency |
| IsActive | Is Active | Boolean | No | Active flag |
| StartDate | Start Date | Date | Yes | Start date |
| EndDate | End Date | Date | No | End date |
| Notes | Notes | String | No | Additional notes |

---

## BankingProductCategory

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| CategoryID | Banking Product Category ID | String | Yes | Unique identifier for the product category |
| CategoryName | Category Name | String | Yes | Name of the product category |
| Description | Description | String | Yes | Category description |
| IsActive | Is Active | Boolean | No | Active flag |
| Notes | Notes | String | No | Additional notes |

---

## ContactInformation

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| ContactID | Contact Information ID | String | Yes |  |
| ContactType | Contact Type | String | Yes |  |
| ContactValue | Contact Value | String | Yes |  |
| IsPrimary | Is Primary | Boolean | No |  |
| IsVerified | Is Verified | Boolean | No |  |
| ValidFrom | Valid From | Date | No |  |
| ValidTo | Valid To | Date | No |  |
| Notes | Notes | String | No |  |
| Preferred | Preferred | Boolean | No |  |

---

## CorporateEntity

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| EntityID | Corporate Entity ID | LongInteger | Yes |  |
| EntityName | Entity Name | String | Yes |  |
| NormalizedCorpName | Normalized Corporate Name | String | No | The normalized name of the corporate entity. |
| PhonetizedCorpName | Phonetized Corporate Name | String | No | The phonetized name of the corporate entity. |
| RegistrationNumber | Registration Number | String | Yes |  |
| NormalizedRegistrationNum | Registration Number | String | No | The normalized registration number of the corporate entity. |
| IncorporationDate | Incorporation Date | Date | No |  |
| CountryOfIncorporation | Country Of Incorporation | String | No |  |
| TaxID | Tax ID | String | No |  |
| NormalizedTaxID | Tax ID | String | No | The normalized tax ID of the corporate entity. |
| Industry | Industry | String | No |  |
| LegalForm | Legal Form | String | No |  |
| IsListed | Is Listed | Boolean | No |  |

---

## Customer

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| CustomerID | Customer ID | String | Yes | Unique identifier for the customer |
| CustomerType | Customer Type | String | Yes | Type of customer (Individual/Corporate) |
| Status | Status | String | No | Current status of the customer |
| SourceSystem | Source System | String | No | System where the customer was onboarded |
| Segment | Segment | String | No | Customer segment |
| CommunicationLanguage | Communication Language | String | No | Preferred communication language |
| Notes | Notes | String | No | Additional notes |
| IsActive | Is Active | Boolean | No | Active flag |

---

## CustomerRiskProfile

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| RiskProfileID | Customer Risk Profile ID | String | Yes |  |
| RiskLevel | Risk Level | String | Yes |  |
| AssessmentDate | Assessment Date | Date | No |  |
| AssessedBy | Assessed By | String | No |  |
| Score | Score | Decimal | No |  |
| IsSanctioned | Is Sanctioned | Boolean | No |  |
| SanctionReason | Sanction Reason | String | No |  |
| ReviewFrequency | Review Frequency | String | No |  |
| NextReviewDate | Next Review Date | Date | No |  |

---

## Employment

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| EmploymentID | Employment ID | String | Yes |  |
| EmployerName | Employer Name | String | Yes |  |
| JobTitle | Job Title | String | Yes |  |
| EmploymentType | Employment Type | String | No |  |
| StartDate | Start Date | Date | Yes |  |
| EndDate | End Date | Date | No |  |
| IsCurrent | Is Current | Boolean | No |  |

---

## IdDocument

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| DocumentID | Id Document ID | String | Yes |  |
| DocumentType | Document Type | String | Yes |  |
| DocumentNumber | Document Number | String | No |  |
| IssueDate | Issue Date | Date | No |  |
| ExpiryDate | Expiry Date | Date | No |  |
| IssuingCountry | Issuing Country | String | No |  |
| IssuingAuthority | Issuing Authority | String | No |  |
| IsPrimary | Is Primary | Boolean | No |  |
| IsVerified | Is Verified | Boolean | No |  |

---

## IndividualPerson

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| PersonID | Person ID | LongInteger | Yes |  |
| FirstName | First Name | String | Yes |  |
| NormalizedFirstName | Normalized First Name | String | No |  |
| PhonetizedFirstName | Phonetized First Name | String | No |  |
| LastName | Last Name | String | Yes |  |
| NormalizedLastName | Normalized Last Name | String | No |  |
| PhonetizedLastName | Phonetized Last Name | String | No |  |
| DateOfBirth | Date of Birth | Date | No |  |
| Nationality | Nationality | String | No |  |
| Gender | Gender | String | No |  |
| MaritalStatus | Marital Status | String | No |  |
| Occupation | Occupation | String | No |  |
| TaxID | Tax ID | String | No |  |
| IsPEP | Is PEP | Boolean | No |  |

---

## InsuranceContract

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| InsuranceContractID | Insurance Contract ID | String | Yes | Unique identifier for the insurance contract |
| ContractName | Contract Name | String | Yes | Name of the contract |
| StartDate | Start Date | Date | No | Contract start date |
| EndDate | End Date | Date | No | Contract end date |
| Status | Status | String | No | Contract status |
| Amount | Amount | Decimal | No | Contract amount |
| Currency | Currency | String | No | Currency |
| Notes | Notes | String | No | Additional notes |

---

## InsuranceContractRole

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| ContractRoleID | Insurance Contract Role ID | String | Yes | Unique identifier for the contract role |
| Role | Role | String | Yes | Role in the contract |
| StartDate | Start Date | Date | No | Start date |
| EndDate | End Date | Date | No | End date |
| IsActive | Is Active | Boolean | No | Active flag |
| Notes | Notes | String | No | Additional notes |

---

## InsuranceProduct

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| InsuranceProductID | Insurance Product ID | String | Yes | Unique identifier for the insurance product |
| ProductName | Product Name | String | Yes | Name of the insurance product |
| ProductType | Product Type | String | Yes | Type of product |
| Currency | Currency | String | Yes | Currency |
| IsActive | Is Active | Boolean | No | Active flag |
| StartDate | Start Date | Date | Yes | Start date |
| EndDate | End Date | Date | No | End date |
| Notes | Notes | String | No | Additional notes |

---

## InsuranceProductCategory

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| CategoryID | Insurance Product Category ID | String | Yes | Unique identifier for the Insurance product category |
| CategoryName | Category Name | String | Yes | Name of the product category |
| Description | Description | String | Yes | Category description |
| IsActive | Is Active | Boolean | No | Active flag |
| Notes | Notes | String | No | Additional notes |

---

## KYCCheck

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| KYCCheckID | KYCCheck ID | String | Yes |  |
| CheckType | Check Type | String | Yes |  |
| CheckDate | Check Date | Date | Yes |  |
| Result | Result | String | Yes |  |
| PerformedBy | Performed By | String | Yes |  |
| Notes | Notes | String | No |  |
| IsAutomated | Is Automated | Boolean | No |  |
| IsPassed | Is Passed | Boolean | No |  |
| NextCheckDate | Next Check Date | Date | No |  |

---

## KYCReview

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| KYCReviewID | KYCReview ID | String | Yes |  |
| ReviewDate | Review Date | Date | Yes |  |
| ReviewerName | Reviewer Name | String | Yes |  |
| ReviewResult | Review Result | String | Yes |  |
| Notes | Notes | String | No |  |
| IsAutomated | Is Automated | Boolean | No |  |
| IsPassed | Is Passed | Boolean | No |  |
| NextReviewDate | Next Review Date | Date | No |  |

---

## Relationship

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| RelationshipID | Relationship ID | String | Yes |  |
| RelationshipType | Relationship Type | String | Yes |  |
| StartDate | Start Date | Date | No |  |
| EndDate | End Date | Date | No |  |
| IsActive | Is Active | Boolean | No |  |
| Notes | Notes | String | No |  |

---

## UBO

| Attribute name | Attribute label | Data type | Mandatory? | Description |
|----------------|-----------------|-----------|------------|-------------|
| UBOID | UBOID | String | Yes |  |
| UBOName | UBO Name | String | No |  |
| OwnershipPercentage | Ownership Percentage | Decimal | Yes |  |
| CountryOfResidence | Country Of Residence | String | No |  |
| DateOfBirth | Date Of Birth | Date | No |  |
| IsPEP | Is PEP | Boolean | No |  |
| Notes | Notes | String | No |  |

---
