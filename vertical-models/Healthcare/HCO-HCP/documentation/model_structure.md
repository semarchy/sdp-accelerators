## HCO-HCP Model Structure

This page documents the model entities and their attributes. The summary table gives a quick overview, and the detailed sections list attribute metadata as configured in the model.

Notes:
- Entity names and labels reflect the model configuration (including any intentional naming).
- If a label looks inconsistent with internal standards, treat it as the authoritative configuration until updated in the model.

Below is a summary table of all entities in the HCO-HCP model, including their label, documentation, references, and attribute count.

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|---|---|---|---|---|---|
| Administration | Administration | Administration routes for products. | Products | (none) | 2 |
| Coverage | Coverage | Member insurance coverage details. | (none) | InsuranceCompany, Member | 7 |
| Encounter | Encounter | Clinical encounter facts linking members, providers, and organizations. | (none) | HCO, HCP, Member | 4 |
| Form | Form | Product form or dosage form reference. | Products | (none) | 2 |
| HCO | HCO | Health Care Organization master, including identifiers and location details. | Encounter, HCP | (none) | 12 |
| HCP | HCP | Health Care Provider master with identifiers, names, licenses, and address. | Encounter, HCPSpecialty, Member | HCO, TaxonomyClassificationSpecialization | 33 |
| HCPSpecialty | HCP Specialty | See MDM-6889 | (none) | HCP, Specialty | 1 |
| ICD10CM | ICD10CM | ICD-10-CM diagnosis codes reference. | ICD10CM, ICDMapping | ICD10CM | 5 |
| ICD9CM | ICD9CM | ICD-9-CM diagnosis codes reference. | ICD9CM, ICDMapping | ICD9CM | 4 |
| ICDMapping | ICD Mapping | Mapping between ICD-9 and ICD-10 codes. | (none) | ICD10CM, ICD9CM | 2 |
| InsuranceCompany | Insurance Company | Insurance company reference. | Coverage | (none) | 7 |
| Member | Member | Member or patient master with demographics and contact data. | Coverage, Encounter | HCP | 33 |
| Products | Products | Product catalog for healthcare or pharma products. | Strength | Administration, Form, Sponsor, TherapeauticArea | 13 |
| Specialty | Specialty | Medical specialty reference. | HCPSpecialty | (none) | 2 |
| Sponsor | Sponsor | Sponsor or manufacturer reference. | Products | (none) | 2 |
| Strength | Strength | Product strength reference. | (none) | Products | 2 |
| TaxonomyClassification | Taxonomy Classification | Taxonomy classification within a grouping. | TaxonomyClassificationSpecialization | TaxonomyGrouping | 3 |
| TaxonomyClassificationSpecialization | Taxonomy Classification Specialization | Links taxonomy classifications and specializations. | HCP | TaxonomyClassification, TaxonomySpecialization | 3 |
| TaxonomyGrouping | Taxonomy Grouping | Taxonomy grouping for specialty classification. | TaxonomyClassification | (none) | 3 |
| TaxonomySpecialization | Taxonomy Specialization | Taxonomy specialization reference. | TaxonomyClassificationSpecialization | (none) | 2 |
| TherapeauticArea | Therapeautic Area | Therapeutic areas for product classification. | Products | (none) | 3 |
---

# Detailed Model Structure

Below are markdown tables for each entity in the model. Each table lists the attributes and their metadata.

## Administration

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| RouteOfAdministration | Route Of Administration | String | No | Route Of Administration | No |

---

## Coverage

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| SubscriberID | Subscriber ID | String | No | Subscriber ID | No |
| GroupName | Group Name | String | No | Group Name | No |
| EffectiveDate | Effective Date | String | No | Effective Date | No |
| GroupNumber | Group Number | String | No | Group Number | No |
| ExpirationDate | Expiration Date | String | No | Expiration Date | No |
| Relationship | Relationship | String | No | Relationship | No |

---

## Encounter

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| EncounterID | Encounter ID | String | Yes | Encounter ID | No |
| Medication | Medication | String | No | Medication | No |
| Condition | Condition | String | No | Condition | No |
| EncounterDate | Encounter Date | String | No | Encounter Date | No |

---

## Form

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| Form | Form | String | No | Form | No |

---

## HCO

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| ACTIVECODE | ACTIVECODE | ACTIVECODE | No | ACTIVECODE | No |
| HospitalID | Hospital ID | String | No | Hospital ID | Yes |
| HospitalName | Hospital Name | String | No | Hospital Name | No |
| inpcity | City | String | No | City | No |
| inpstreet | Street | String | No | Street | No |
| inpstate | State | String | No | State | No |
| HospitalNameNormalized | Hospital Name Normalized | String | No | Hospital Name Normalized | Yes |
| HospitalCCN | Hospital CCN | String | No | Hospital CCN | No |
| inpcountry | Country | String | No | Country | No |
| inpzip | Zip | String | No | Zip | No |
| GeocodedAddress | Geocoded Address | GeocodedAddressType | No | Geocoded Address | Yes |

---

## HCP

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| FullName | Full Name | String | No | Full Name | No |
| State | State | String | No | State | Yes |
| FirstName | First Name | String | No | First Name | No |
| LicenseNumber3 | License Number 3 | String | No | License Number 3 | No |
| LicenseStateCode5 | License State Code 5 | String | No | License State Code 5 | No |
| EffectiveDate | Effective Date | Date | No | Effective Date | No |
| LicenseNumber1 | License Number 1 | String | No | License Number 1 | No |
| NewSpecialty | New Specialty | Boolean | No | New Specialty | No |
| Specialties | Specialties | String | No | Specialties | No |
| Country | Country | String | No | Country | No |
| MiddleName | Middle Name | String | No | Middle Name | No |
| City | City | String | No | City | No |
| ZipCode | Zip Code | String | No | Zip Code | Yes |
| LastName | Last Name | String | No | Last Name | No |
| LicenseStateCode4 | License State Code 4 | String | No | License State Code 4 | No |
| LastNamePhonetic | Last Name Phonetic | String | No | Last Name Phonetic | Yes |
| LicenseStateCode2 | License State Code 2 | String | No | License State Code 2 | No |
| LicenseNumber5 | License Number 5 | String | No | License Number 5 | No |
| NPI | NPI | String | No | NPI | Yes |
| Province | Province | String | No | Province | No |
| StreetAddressLine1 | Street Address Line1 | String | No | Street Address Line1 | No |
| NameSuffix | Name Suffix | String | No | Name Suffix | No |
| PrimaryType | Primary Type | String | No | Primary Type | No |
| LicenseNumber2 | License Number 2 | String | No | License Number 2 | No |
| LicenseStateCode3 | License State Code 3 | String | No | License State Code 3 | No |
| LicenseNumber4 | License Number 4 | String | No | License Number 4 | No |
| PhysicianProfileID | Physician Profile ID | String | No | Physician Profile ID | Yes |
| LicenseStateCode1 | License State Code 1 | String | No | License State Code 1 | No |
| StreetAddressLine2 | Street Address Line2 | String | No | Street Address Line2 | No |
| FirstNamePhonetic | First Name Phonetic | String | No | First Name Phonetic | Yes |
| PostalCode | Postal Code | String | No | Postal Code | No |
| GeocodedAddress | Geocoded Address | GeocodedAddressType | No | Geocoded Address | No |

---

## HCPSpecialty

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | ID | No |

---

## ICD10CM

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | ID | No |
| OrderNumber | Order Number | String | No | Order Number | No |
| LongDescription | Long Description | String | No | Long Description | No |
| FormattedICD10Code | Formatted ICD10 Code | String | No | Formatted ICD10 Code | No |
| ShortDescription | Short Description | String | No | Short Description | No |

---

## ICD9CM

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | ID | No |
| Description | Description | String | No | Description | No |
| RawICD9Code | Raw ICD9 Code | String | No | Raw ICD9 Code | No |
| IsIndustryStd | Is Industry Std | Boolean | No | Is Industry Std | No |

---

## ICDMapping

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ICDMappingID | ICD Mapping ID | String | Yes | ICD Mapping ID | No |
| Description | Description | String | No | Description | No |

---

## InsuranceCompany

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String | Yes | Code | No |
| NormalizedWebsite | Normalized Website | String | No | Normalized Website | No |
| Name | Name | String | No | Name | No |
| URL | URL | String | No | URL | No |
| TypeOfPayments | Type Of Payments | TypesOfPayments | No | Type Of Payments | No |
| InputAddress | Input Address | InputAddress | No | Input Address | No |
| GeocodedAddress | Geocoded Address | GeocodedAddressType | No | Geocoded Address | No |

---

## Member

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| CellPhone | Cell Phone | String | No | Cell Phone | No |
| LastNamePhonetic | Last Name Phonetic | String | No | Last Name Phonetic | Yes |
| PlaceOfBirth | Place Of Birth | String | No | Place Of Birth | No |
| GroupID | Group ID | String | No | Group ID | No |
| Street | Street | String | No | Street | No |
| DeathDate | Death Date | String | No | Death Date | No |
| BirthDate | Birth Date | String | No | Birth Date | Yes |
| Zip | Zip | String | No | Zip | Yes |
| SINumber | SI Number | String | No | SI Number | No |
| FirstNamePhonetic | First Name Phonetic | String | No | First Name Phonetic | Yes |
| Country | Country | String | No | Country | No |
| MaritalStatus | Marital Status | String | No | Marital Status | No |
| WorkPhone | Work Phone | String | No | Work Phone | No |
| StandardizedHomePhone | Standardized Home Phone | String | No | Standardized Home Phone | No |
| LastName | Last Name | String | No | Last Name | No |
| HomePhone | Home Phone | String | No | Home Phone | No |
| PrimaryPhysicianID | Primary Physician ID | String | No | Primary Physician ID | No |
| MemberIDX | Member IDX | String | No | Member IDX | Yes |
| FirstName | First Name | String | No | First Name | No |
| ValidEmailDomain | Valid Email Domain | String | No | Valid Email Domain | No |
| Gender | Gender | String | No | Gender | No |
| State | State | String | No | State | No |
| StarndardizedCellPhone | Starndardized Cell Phone | String | No | Starndardized Cell Phone | No |
| EmailAddress | Email Address | String | No | Email Address | No |
| GroupName | Group Name | String | No | Group Name | No |
| MiddleName | Middle Name | String | No | Middle Name | No |
| Suffix | Suffix | String | No | Suffix | No |
| City | City | String | No | City | No |
| CleansedEmail | Cleansed Email | String | No | Cleansed Email | Yes |
| SubscriberRelationship | Subscriber Relationship | String | No | Subscriber Relationship | No |
| MemberIDs | Member IDs | MemberIDs | No | Member IDs | No |
| GeocodedAddress | Geocoded Address | GeocodedAddressType | No | Geocoded Address | Yes |

---

## Products

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| TradeName | Trade Name | String | No | Trade Name | Yes |
| EnrichAdministration | Enrich Administration | String | No | Enrich Administration | No |
| Definition | Definition | String | No | Definition | No |
| ProductName | Product Name | String | No | Product Name | Yes |
| url | url | String | No | url | No |
| EnrichForm | Enrich Form | String | No | Enrich Form | No |
| GenericName | Generic Name | String | No | Generic Name | Yes |
| Price | Price | String | No | Price | No |
| Image | Image | Binary | No | Image | No |
| NDCCode | NDC Code | String | No | NDC Code | No |
| Indication | Indication | String | No | Indication | No |
| GEN_AIDescription | GEN AI Description | String | No | GEN AI Description | No |

---

## Specialty

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String | Yes | Code | No |
| Name | Name | String | Yes | Name | No |

---

## Sponsor

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| SponsorName | Sponsor Name | String | No | Sponsor Name | No |

---

## Strength

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | ID | No |
| Strength | Strength | String | No | Strength | No |

---

## TaxonomyClassification

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | ID | No |
| ClassificationCode | Classification Code | String | Yes | Classification Code | No |
| Name | Name | String | No | Name | No |

---

## TaxonomyClassificationSpecialization

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | Code | String | Yes | Code | No |
| Definition | Definition | String | No | Definition | No |
| Notes | Notes | String | No | Notes | No |

---

## TaxonomyGrouping

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | ID | No |
| Name | Name | String | Yes | Name | No |
| Role | Role | TaxonomyGrouping | Yes | Role | No |

---

## TaxonomySpecialization

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | String | Yes | ID | No |
| Name | Name | String | Yes | Name | No |

---

## TherapeauticArea

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String | Yes | Code | No |
| Description | Description | String | No | Description | No |
| Name | Name | String | No | Name | No |

---
