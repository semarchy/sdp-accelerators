```markdown
# Model structure

This document lists entities in the Merchant model and shows attribute metadata. The last column marks whether an attribute is referenced by the entity's matcher (if present).

---

## ContactRole
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| ContactRoleID | Contact Role ID | LongInteger | Yes | Primary key for the ContactRole entity | No |
| Role | Role | String(50) | Yes | Name of the contact role (for example: Billing, Technical, Primary) | No |

---

## Country
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| CountryCode | ISO Alpha 2 Code | String(2) | Yes | ISO 3166-1 alpha-2 country code (e.g., US, GB) | No |
| Alpha3Code | ISO 3166-1 3-Letter Code | String(3) | No | ISO 3166-1 alpha-3 country code (e.g., USA, GBR) | No |
| NumericCode | Numeric Code | String(3) | No | ISO numeric country code | No |
| URLWikipedia | URL Wikipedia | String(128) | No | Link to the country's Wikipedia page for reference | No |
| LocalShortName | Local Short Name | String(128) | No | Short name of the country in the local language | No |
| EnglishShortName | English Short Name | String(128) | No | Short name of the country in English | No |
| EnglishShortNameCAPS | English Short Name ALLCAPS | String(128) | No | Uppercase English short name (for legacy or matching needs) | No |
| EnglishFullName | English Full Name | String(128) | No | Full official country name in English | No |
| FlagURL | Flag URL | String(128) | No | URL pointing to an image of the country's flag | No |

---

## Currency
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| CurrencyCode | Currency Code | String(3) | Yes | ISO 4217 alphabetic currency code (e.g., USD, EUR) | No |
| Name | Name | String(100) | Yes | Official name of the currency | No |
| CurrencyNumber | Currency Number | String(3) | No | ISO 4217 numeric currency code | No |
| CountryAlpha3 | Country Alpha3 Code | String(3) | No | ISO 3166-1 alpha-3 country code | No |
| IsCurrent | Is Current | Boolean | No | Flag if the currency is currently in use | No |

---

## Industry
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| IndustryName | Industry Name | String(100) | Yes | Name of the industry sector | No |

---

## Merchant
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| MerchantID | Merchant ID | LongInteger | Yes | Primary key for the Merchant entity | No |
| MerchantName | Merchant Name | String(200) | Yes | Official name of the merchant as registered in the system | No |
| EnrichedMerchantName | Enriched Merchant Name | String(200) | No | Enriched official name of the merchant | No |
| MerchantType | Merchant Type | LOV (Merchant.list_of_values.MerchantType) | No | Classification of merchant using a list-of-values | No |
| Status | Status | LOV (Merchant.list_of_values.MerchantStatus) | No | Current lifecycle or verification status of the merchant | No |
| OnboardingDate | Onboarding Date | Date | No | Date the merchant was onboarded into the system | No |
| ActivationDate | Activation Date | Date | No | Date the merchant record was activated in the system | No |
| TerminationDate | Termination Date | Date | No | Date the merchant was terminated from the system | No |
| MerchantCode | Merchant Code | String(50) | No | Internal merchant identifier (business key) | No |

---

## Party
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| PartyID | Party ID | LongInteger | Yes | Master key for the Party entity | No |
| PartyType | Party Type | LOV (Merchant.list_of_values.PartyType) | No | High-level type: ORGANIZATION or PERSON | No |
| PartyRoleType | Party Role Type | LOV (Merchant.list_of_values.PartyRoleType) | No | Optional role type (Merchant, Supplier, Customer, Partner) | No |
| PartyStatus | Party Status | LOV (Merchant.list_of_values.PartyStatus) | No | Lifecycle status: Active, Inactive, Suspended | No |
| DisplayName | Display Name | String(200) | Yes | Primary UI / business name | No |
| NormalizedName | Normalized Name | String(200) | No | Uppercase, cleaned name for matching | Yes |
| AlternateName | Alternate Name | String(128) | No | DBA / Trade name | No |
| LegalName | Legal Name | String(128) | No | Registered legal name (if applicable) | Yes |

---

## PartyAddress
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| AddressID | Address ID | LongInteger | Yes | Primary key for the PartyAddress entity | No |
| AddressType | Address Type | LOV (AddressType) | No | Classification of address (e.g., billing, shipping) | No |
| Street | Street | String(128) | Yes | First line of street address | No |
| City | City | String(64) | No | City or locality name for the address | No |
| State | State | String(64) | No | State, province or region for the address | No |
| PostalCode | Postal Code | String(20) | No | Postal or ZIP code for the address | No |
| EnrichedStreet | Enriched Street | String(128) | No | Standardized/enriched street value produced by geocoding or normalization | No |
| EnrichedCity | Enriched City | String(64) | No | Standardized/enriched city value | No |
| EnrichedState | Enriched State | String(64) | No | Standardized/enriched state value | No |
| EnrichedPostalCode | Enriched Postal Code | String(20) | No | Standardized/enriched postal code | No |
| EnrichedLatitude | Enriched Latitude | Decimal(10,6) | No | Geocoded latitude coordinate for the address | No |
| EnrichedLongitude | Enriched Longitude | Decimal(10,6) | No | Geocoded longitude coordinate for the address | No |

---

## PartyContact
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| PartyContactID | Party Contact ID | LongInteger | Yes | Primary key for the PartyContact entity | No |
| ContactType | Contact Type | LOV (Party.list_of_values.PartyContactType) | No | Type of contact (e.g., Billing, Support) | No |
| FirstName | First Name | String(100) | Yes | Contact's first name | No |
| LastName | Last Name | String(100) | Yes | Contact's last name | No |
| EnrichedFirstName | Enriched First Name | String(100) | No | Enriched first name, if available | Yes |
| EnrichedLastName | Enriched Last Name | String(100) | No | Enriched last name, if available | Yes |
| Email | Email | String(255) | No | Contact's email address | Yes |
| PhoneNumber | Phone Number | String(50) | No | Contact's phone number | No |

---

## Product
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| ProductID | Product ID | LongInteger | Yes | Unique master identifier for the Product | No |
| ProductName | Product Name | String(255) | Yes | Official name of the product or service | No |
| Description | Description | String(500) | No | Description of the product | No |
| ProductStatus | Product Status | LOV (Merchant.list_of_values.ProductStatus) | Yes | Current status of the product (e.g., Active, Inactive) | No |

---

## ProductCategory
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| ProductCategoryID | Product Category ID | LongInteger | Yes | Unique identifier for product category | No |
| CategoryName | Category Name | String(100) | Yes | Name of the product category | No |
| IsActive | Is Active | Boolean | Yes | Flag indicating if category is currently in use | No |

---

## SubIndustry
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| SubIndustryName | Sub Industry Name | String(128) | Yes | Name of the sub-industry (more specific classification under Industry) | No |

---

## Individual
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| IndividualID | Individual ID | LongInteger | Yes | Surrogate key for Individual | No |
| FirstName | First Name | String(128) | No | Given name | No |
| MiddleName | Middle Name | String(128) | No | Optional middle name | No |
| LastName | Last Name | String(128) | No | Family name | No |
| DateOfBirth | Date Of Birth | Date | No | DOB | Yes |
| Gender | Gender | LOV (Merchant.list_of_values.Gender) | No | Gender LOV: MALE, FEMALE, OTHER | No |
| IdentificationNumber | Identification Number | String(64) | No | Aadhaar / Passport / SSN | No |
| FirstNameEnriched | First Name (Enriched) | String(128) | No | Enriched/normalized first name | Yes |
| LastNameEnriched | Last Name (Enriched) | String(128) | No | Enriched/normalized last name | Yes |

---

## LegalEntity
| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---:|---:|---|---:|
| LegalEntityID | Legal Entity ID | LongInteger | Yes | Surrogate key for LegalEntity | No |
| LegalEntityType | Legal Entity Type | LOV (Merchant.list_of_values.LegalEntityType) | No | Legal entity legal form (Corporation, LLP, Partnership, Sole Proprietor, Trust) | No |
| LegalName | Legal Name | String(256) | No | Official registered name of the legal entity | No |
| NormalizedLegalName | Normalized Legal Name | String(256) | No | Standardized name used for matching and deduplication | No |
| AlternateLegalName | Alternate Legal Name | String(256) | No | Previous or alternate registered/legal name | No |
| RegistrationNumber | Registration Number | String(128) | No | Company or registration number assigned by the registrar | No |
| RegistrationAuthority | Registration Authority | String(128) | No | Registrar or issuing authority for the registration number | No |
| TaxIdentifier | Tax Identifier | String(128) | No | Tax identifier such as PAN, EIN, UTR, etc. | Yes |
| TaxIdentifierType | Tax Identifier Type | LOV (Merchant.list_of_values.TaxIdentifierType) | No | Type of tax identifier (PAN, EIN, VAT, GSTIN, etc.) | No |
| RegulatoryIdentifier | Regulatory Identifier | String(128) | No | Sector-specific regulatory identifier if applicable | No |
| RegulatoryAuthority | Regulatory Authority | String(128) | No | Issuing regulator for the regulatory identifier | No |
| IncorporationDate | Incorporation Date | Date | No | Date of legal formation/incorporation | No |

```