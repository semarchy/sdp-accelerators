## SAP Business Partner 360 Model Structure

Below is a summary table of all entities in the model, including their label, documentation, references, and attribute count.

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|-------------|-------------|---------------------|-----------------------|--------------------|---------------------|
| BusinessPartner | Business Partner | Trusted business partner golden record consolidating SAP and CRM party information. | BPAddress, BPBank, BPContact, BPIdentification, BPIndustry, BPRelationship, BPRole, BPTaxNumber, Supplier, SupplierPartnerFunc | BPStatus, BusinessPartnerCategory, BusinessPartnerGrouping, Language | 17 |
| Supplier | Supplier | Trusted supplier golden record extending a business partner in the vendor role. | SupplierCompany, SupplierPurchasingOrg, SupplierText | AlternativePayee, AuthorizationGroup, BusinessPartner, Industry, ResponsibleType, SupplierAccountGroup, SupplierCorporateGroup, TradingPartner | 13 |
| SupplierPurchasingOrg | Supplier Purchasing Org | Purchasing-organization-level data for a supplier. | SupplierPartnerFunc | ABCClassification, Currency, IncotermsClassification, PaymentTerms, PlanningCycle, PricingDateControl, PurchasingGroup, PurchasingOrganization, Supplier, ShippingCondition | 11 |
| BPAddress | BP Address | Postal address golden record for a business partner with geocoding enrichment. | BPAddressEmail, BPAddressPhone, BPAddressUsage | BusinessPartner, Country, Language, Region, TaxJurisdiction, TransportZone | 31 |
| BPContact | BP Contact | Contact person relationship linking an organization and a person business partner. | (none) | BusinessPartner, ContactPersonDepartment, ContactPersonFunction, RelationshipCategory | 4 |
| BPBank | BP Bank | Bank account golden record for a business partner. | (none) | BusinessPartner, Country | 11 |
| BPAddressEmail | BP Address Email | Email address associated with a business partner address. | (none) | BPAddress | 4 |
| BPAddressPhone | BP Address Phone | Phone number associated with a business partner address. | (none) | BPAddress, Country, PhoneNumberType | 4 |
| BPAddressUsage | BP Address Usage | Usage assignment for an address such as default, billing, or ship-to. | (none) | AddressUsage, BPAddress | 3 |
| BPIdentification | BP Identification | External identification numbers such as passports, national IDs, and D-U-N-S numbers. | (none) | BusinessPartner, BpIdentificationType, Country | 5 |
| BPIndustry | BP Industry | Industry classifications assigned to a business partner. | (none) | BusinessPartner, Industry, IndustrySector | 2 |
| BPRelationship | BP Relationship | Relationship between two business partners such as parent, headquarter, or affiliate. | (none) | BusinessPartner, RelationshipCategory | 3 |
| BPRole | BP Role | Roles assigned to a business partner such as customer, vendor, or contact person. | (none) | BusinessPartner, BusinessPartnerRole | 3 |
| BPTaxNumber | BP Tax Number | Tax registration numbers for a business partner. | (none) | BPTaxType, BusinessPartner, TaxNumberCategory | 5 |
| SupplierCompany | Supplier Company | Company-code-level financial data for a supplier. | (none) | AlternativePayee, CashPlanningGroup, CompanyCode, Country, HouseBank, InterestCalculationCode, PaymentBlockingReason, PaymentTerms, ReconciliationAccount, Supplier, SortKey, ToleranceGroup | 8 |
| SupplierPartnerFunc | Supplier Partner Function | Partner functions assigned within a supplier purchasing organization. | (none) | BusinessPartner, PartnerFunction, SupplierPurchasingOrg | 3 |
| SupplierText | Supplier Text | Long text notes associated with a supplier. | (none) | Language, LongTextID, Supplier | 2 |
| ABCClassification | ABC Classification | ABC Classification reference data used by the SAP Business Partner 360 model. | SupplierPurchasingOrg | (none) | 5 |
| AddressUsage | Address Usage | Address Usage reference data used by the SAP Business Partner 360 model. | BPAddressUsage | (none) | 5 |
| AlternativePayee | Alternative Payee | Alternative Payee reference data used by the SAP Business Partner 360 model. | Supplier, SupplierCompany | (none) | 5 |
| AuthorizationGroup | Authorization Group | Authorization Group reference data used by the SAP Business Partner 360 model. | Supplier | (none) | 5 |
| BPStatus | BP Status | BP Status reference data used by the SAP Business Partner 360 model. | BusinessPartner | (none) | 5 |
| BPTaxType | BP Tax Type | BP Tax Type reference data used by the SAP Business Partner 360 model. | BPTaxNumber | (none) | 5 |
| BpIdentificationType | BP Identification Type | BP Identification Type reference data used by the SAP Business Partner 360 model. | BPIdentification | (none) | 5 |
| BusinessPartnerCategory | Business Partner Category | Business Partner Category reference data used by the SAP Business Partner 360 model. | BusinessPartner | (none) | 5 |
| BusinessPartnerGrouping | Business Partner Grouping | Business Partner Grouping reference data used by the SAP Business Partner 360 model. | BusinessPartner | (none) | 5 |
| BusinessPartnerRole | Business Partner Role | Business Partner Role reference data used by the SAP Business Partner 360 model. | BPRole | (none) | 5 |
| CashPlanningGroup | Cash Planning Group | Cash Planning Group reference data used by the SAP Business Partner 360 model. | SupplierCompany | (none) | 5 |
| CompanyCode | Company Code | Company Code reference data used by the SAP Business Partner 360 model. | SupplierCompany | (none) | 5 |
| ContactPersonDepartment | Contact Person Department | Contact Person Department reference data used by the SAP Business Partner 360 model. | BPContact | (none) | 5 |
| ContactPersonFunction | Contact Person Function | Contact Person Function reference data used by the SAP Business Partner 360 model. | BPContact | (none) | 5 |
| Country | Country | Country reference data used by the SAP Business Partner 360 model. | BPAddress, BPAddressPhone, BPBank, BPIdentification, SupplierCompany | (none) | 5 |
| Currency | Currency | Currency reference data used by the SAP Business Partner 360 model. | SupplierPurchasingOrg | (none) | 5 |
| HouseBank | House Bank | House Bank reference data used by the SAP Business Partner 360 model. | SupplierCompany | (none) | 5 |
| IncotermsClassification | Incoterms Classification | Incoterms Classification reference data used by the SAP Business Partner 360 model. | SupplierPurchasingOrg | (none) | 5 |
| Industry | Industry | Industry reference data used by the SAP Business Partner 360 model. | BPIndustry, Supplier | (none) | 5 |
| IndustrySector | Industry Sector | Industry Sector reference data used by the SAP Business Partner 360 model. | BPIndustry | (none) | 5 |
| InterestCalculationCode | Interest Calculation Code | Interest Calculation Code reference data used by the SAP Business Partner 360 model. | SupplierCompany | (none) | 5 |
| Language | Language | Language reference data used by the SAP Business Partner 360 model. | BPAddress, BusinessPartner, SupplierText | (none) | 5 |
| LongTextID | Long Text ID | Long Text ID reference data used by the SAP Business Partner 360 model. | SupplierText | (none) | 5 |
| PartnerFunction | Partner Function | Partner Function reference data used by the SAP Business Partner 360 model. | SupplierPartnerFunc | (none) | 5 |
| PaymentBlockingReason | Payment Blocking Reason | Payment Blocking Reason reference data used by the SAP Business Partner 360 model. | SupplierCompany | (none) | 5 |
| PaymentTerms | Payment Terms | Payment Terms reference data used by the SAP Business Partner 360 model. | SupplierCompany, SupplierPurchasingOrg | (none) | 5 |
| PhoneNumberType | Phone Number Type | Phone Number Type reference data used by the SAP Business Partner 360 model. | BPAddressPhone | (none) | 5 |
| PlanningCycle | Planning Cycle | Planning Cycle reference data used by the SAP Business Partner 360 model. | SupplierPurchasingOrg | (none) | 5 |
| PricingDateControl | Pricing Date Control | Pricing Date Control reference data used by the SAP Business Partner 360 model. | SupplierPurchasingOrg | (none) | 5 |
| PurchasingGroup | Purchasing Group | Purchasing Group reference data used by the SAP Business Partner 360 model. | SupplierPurchasingOrg | (none) | 5 |
| PurchasingOrganization | Purchasing Organization | Purchasing Organization reference data used by the SAP Business Partner 360 model. | SupplierPurchasingOrg | (none) | 5 |
| ReconciliationAccount | Reconciliation Account | Reconciliation Account reference data used by the SAP Business Partner 360 model. | SupplierCompany | (none) | 5 |
| Region | Region | Region reference data used by the SAP Business Partner 360 model. | BPAddress | (none) | 5 |
| RelationshipCategory | Relationship Category | Relationship Category reference data used by the SAP Business Partner 360 model. | BPContact, BPRelationship | (none) | 5 |
| ResponsibleType | Responsible Type | Responsible Type reference data used by the SAP Business Partner 360 model. | Supplier | (none) | 5 |
| ShippingCondition | Shipping Condition | Shipping Condition reference data used by the SAP Business Partner 360 model. | SupplierPurchasingOrg | (none) | 5 |
| SortKey | Sort Key | Sort Key reference data used by the SAP Business Partner 360 model. | SupplierCompany | (none) | 5 |
| SourceSystem | Source System | Source System reference data used by the SAP Business Partner 360 model. | (none) | (none) | 5 |
| SupplierAccountGroup | Supplier Account Group | Supplier Account Group reference data used by the SAP Business Partner 360 model. | Supplier | (none) | 5 |
| SupplierCorporateGroup | Supplier Corporate Group | Supplier Corporate Group reference data used by the SAP Business Partner 360 model. | Supplier | (none) | 5 |
| TaxJurisdiction | Tax Jurisdiction | Tax Jurisdiction reference data used by the SAP Business Partner 360 model. | BPAddress | (none) | 5 |
| TaxNumberCategory | Tax Number Category | Tax Number Category reference data used by the SAP Business Partner 360 model. | BPTaxNumber | (none) | 5 |
| ToleranceGroup | Tolerance Group | Tolerance Group reference data used by the SAP Business Partner 360 model. | SupplierCompany | (none) | 5 |
| TradingPartner | Trading Partner | Trading Partner reference data used by the SAP Business Partner 360 model. | Supplier | (none) | 5 |
| TransportZone | Transport Zone | Transport Zone reference data used by the SAP Business Partner 360 model. | BPAddress | (none) | 5 |

# Detailed Model Structure

Below are markdown tables for each entity in the model. Each table lists the attributes and their metadata. The **Used in matching** column indicates attributes referenced by the entity's match rules.

## BusinessPartner (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BPGoldenID | BP Golden ID | LongInteger | Yes | System generated golden identifier for the trusted business partner record. | No |
| BusinessPartner | Business Partner | String | No | SAP business partner number kept for traceability. | Yes |
| BusinessPartnerFullName | Business Partner Full Name | String | No | Concatenated full name of the business partner. | No |
| NormalizedName | Normalized Name | String | No | Standardized business partner name used for matching and search. | Yes |
| OrganizationBPName1 | Organization BP Name 1 | String | No | Organization name line 1. | Yes |
| OrganizationBPName2 | Organization BP Name 2 | String | No | Organization name line 2. | No |
| LastName | Last Name | String | No | Person surname. | No |
| FirstName | First Name | String | No | Person first name. | No |
| MiddleName | Middle Name | String | No | Person middle name. | No |
| BirthDate | Birth Date | Date | No | Date of birth for a natural person business partner. | No |
| BusinessPartnerIsBlocked | Business Partner Is Blocked | Boolean | No | Central block flag for the business partner. | No |
| IsNaturalPerson | Is Natural Person | Boolean | No | Indicates whether the business partner is a natural person. | No |
| SearchTerm1 | Search Term 1 | String | No | Search term used for matching and deduplication. | Yes |
| SearchTerm2 | Search Term 2 | String | No | Secondary search term. | No |
| GoldenRecordFlag | Golden Record Flag | Boolean | No | Indicates the surviving golden record. | No |
| CreatedDate | Created Date | Timestamp | No | Creation timestamp of the business partner record. | No |
| LastModifiedDate | Last Modified Date | Timestamp | No | Last change timestamp of the business partner record. | No |

---

## Supplier (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SupplierGoldenID | Supplier Golden ID | LongInteger | Yes | System generated golden identifier for the supplier record. | No |
| Supplier | Supplier | String | No | SAP vendor number. | Yes |
| SupplierFullName | Supplier Full Name | String | No | Full name of the supplier. | No |
| SupplierName | Supplier Name | String | No | Supplier name. | No |
| NormalizedName | Normalized Name | String | No | Standardized supplier name used for matching and search. | Yes |
| VATRegistration | VAT Registration | String | No | VAT registration number. | Yes |
| BirthDate | Birth Date | Date | No | Date of birth for individual suppliers. | No |
| InternationalLocationNumber1 | International Location Number 1 | String | No | Global location number. | No |
| PurchasingIsBlocked | Purchasing Is Blocked | Boolean | No | Purchasing block flag. | No |
| SupplierProcurementBlock | Supplier Procurement Block | Boolean | No | Procurement block flag. | No |
| PaymentIsBlockedForSupplier | Payment Is Blocked For Supplier | Boolean | No | Payment block flag. | No |
| DeletionIndicator | Deletion Indicator | Boolean | No | Deletion indicator. | No |
| ConcatenatedInternationalLocNo | Concatenated International Loc No | String | No | Concatenated international location number. | No |

---

## SupplierPurchasingOrg (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SupplierPurchOrgGoldenID | Supplier Purch Org Golden ID | LongInteger | Yes | System generated golden identifier for the supplier purchasing org record. | No |
| IncotermsLocation1 | Incoterms Location 1 | String | No | Incoterms location. | No |
| SupplierPhoneNumber | Supplier Phone Number | String | No | Supplier purchasing phone number. | No |
| SupplierRespSalesPersonName | Supplier Resp Sales Person Name | String | No | Responsible sales person name. | No |
| NormalizedRespName | Normalized Resp Name | String | No | Standardized responsible sales person name used for matching. | Yes |
| SupplierIsBlockedForPurchasing | Supplier Is Blocked For Purchasing | Boolean | No | Purchasing block flag. | No |
| MinimumOrderAmount | Minimum Order Amount | LongInteger | No | Minimum order amount. | No |
| PurchaseOrderIsAckRequired | Purchase Order Is Ack Required | Boolean | No | Purchase order acknowledgment required flag. | No |
| InvoiceIsGoodsReceiptBased | Invoice Is Goods Receipt Based | Boolean | No | Goods-receipt-based invoice verification flag. | No |
| InvoiceIsMMServiceEntryBased | Invoice Is MM Service Entry Based | Boolean | No | Service-entry-based invoice verification flag. | No |
| ReturnsSupplier | Returns Supplier | Boolean | No | Returns supplier flag. | No |

---

## BPAddress (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AddressGoldenID | Address Golden ID | LongInteger | Yes | System generated golden identifier for the address record. | No |
| AddressID | Address ID | String | No | SAP internal address number. | No |
| CareOfName | Care of Name | String | No | Care-of name. | No |
| StreetName | Street Name | String | No | Street name. | Yes |
| HouseNumber | House Number | String | No | House number. | Yes |
| StreetPrefixName | Street Prefix Name | String | No | Street prefix. | No |
| StreetSuffixName | Street Suffix Name | String | No | Street suffix. | No |
| District | District | String | No | District. | No |
| CityName | City Name | String | No | City name. | Yes |
| County | County | String | No | County. | No |
| PostalCode | Postal Code | String | No | Postal code. | Yes |
| POBox | PO Box | String | No | PO box. | No |
| POBoxPostalCode | PO Box Postal Code | String | No | PO box postal code. | No |
| ValidityStartDate | Validity Start Date | Date | No | Address validity start date. | No |
| InpAddressLine | Input Address Line | String | No | Street address line used as input for geocoding. | No |
| InpCity | Input City | String | No | City used as input for geocoding. | No |
| InpState | Input State | String | No | State or region used as input for geocoding. | No |
| InpPostalCode | Input Postal Code | String | No | Postal code used as input for geocoding. | No |
| InpCountry | Input Country | String | No | Country used as input for geocoding. | No |
| GeoStreetNumber | Geocoded Street Number | String | No | Street number returned by the Google Maps geocoding enricher. | No |
| GeoStreetName | Geocoded Street Name | String | No | Street or route returned by the Google Maps geocoding enricher. | No |
| GeoLocality | Geocoded Locality | String | No | Locality or city returned by the Google Maps geocoding enricher. | No |
| GeoState | Geocoded State | String | No | Administrative area returned by the Google Maps geocoding enricher. | No |
| GeoPostalCode | Geocoded Postal Code | String | No | Postal code returned by the Google Maps geocoding enricher. | No |
| GeoCountry | Geocoded Country | String | No | Country long name returned by the Google Maps geocoding enricher. | No |
| GeoCountryShort | Geocoded Country Short | String | No | Country short code returned by the Google Maps geocoding enricher. | No |
| GeoLatitude | Geocoded Latitude | String | No | Latitude returned by the Google Maps geocoding enricher. | No |
| GeoLongitude | Geocoded Longitude | String | No | Longitude returned by the Google Maps geocoding enricher. | No |
| GeoStatus | Geocoded Status | String | No | Geocoding status returned by the Google Maps geocoding enricher. | No |
| GeoQuality | Geocoded Quality | String | No | Geocoding quality returned by the Google Maps geocoding enricher. | No |
| NormalizedCity | Normalized City | String | No | Standardized city name in upper case used for search and matching. | No |

---

## BPContact (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ContactGoldenID | Contact Golden ID | LongInteger | Yes | System generated golden identifier for the contact record. | No |
| ContactFullName | Contact Full Name | String | No | Full name of the contact person. | No |
| NormalizedName | Normalized Name | String | No | Standardized contact name used for matching. | Yes |
| ValidityEndDate | Validity End Date | Date | No | Contact relationship validity end date. | No |

---

## BPBank (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BankGoldenID | Bank Golden ID | LongInteger | Yes | System generated golden identifier for the bank record. | No |
| BankIdentification | Bank Identification | String | No | SAP bank key. | Yes |
| BankAccount | Bank Account | String | No | Bank account number. | Yes |
| BankControlKey | Bank Control Key | String | No | Bank routing or control key. | No |
| IBAN | IBAN | String | No | International bank account number. | Yes |
| IBANValidityStartDate | IBAN Validity Start Date | Date | No | IBAN validity start date. | No |
| SWIFTCode | SWIFT Code | String | No | SWIFT or BIC code. | No |
| BankAccountHolderName | Bank Account Holder Name | String | No | Bank account holder name. | No |
| CollectionAuthInd | Collection Auth Ind | Boolean | No | Direct debit collection authorization indicator. | No |
| ValidityStartDate | Validity Start Date | Date | No | Bank record validity start date. | No |
| ValidityEndDate | Validity End Date | Date | No | Bank record validity end date. | No |

---

## BPAddressEmail (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| EmailID | Email ID | String | Yes | Unique identifier for the email record. | No |
| EmailAddress | Email Address | String | Yes | Email address value. | No |
| IsDefaultEmailAddress | Is Default Email Address | Boolean | No | Indicates whether this is the default email address. | No |
| SearchEmailAddress | Search Email Address | String | No | Normalized email address used for search. | No |

---

## BPAddressPhone (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PhoneID | Phone ID | String | Yes | Unique identifier for the phone record. | No |
| PhoneNumber | Phone Number | String | Yes | Phone number value. | No |
| PhoneNumberExtension | Phone Number Extension | String | No | Phone number extension. | No |
| IsDefaultPhoneNumber | Is Default Phone Number | Boolean | No | Indicates whether this is the default phone number. | No |

---

## BPAddressUsage (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AddressUsageID | Address Usage ID | String | Yes | Unique identifier for the address usage assignment. | No |
| ValidFrom | Valid From | Date | No | Usage validity start date. | No |
| ValidTo | Valid To | Date | No | Usage validity end date. | No |

---

## BPIdentification (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| IdentificationID | Identification ID | String | Yes | Unique identifier for the identification record. | No |
| BpIdentificationNumber | BP Identification Number | String | Yes | External identification number value. | No |
| IdentificationEntryDate | Identification Entry Date | Date | No | Date the identification was recorded. | No |
| InstitutionName | Institution Name | String | No | Issuing authority for the identification. | No |
| NormalizedIdNumber | Normalized Identification Number | String | No | Identification number in upper case with spaces removed used for search and comparison. | No |

---

## BPIndustry (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| IndustryID | Industry ID | String | Yes | Unique identifier for the industry assignment. | No |
| IsStandardIndustry | Is Standard Industry | Boolean | No | Indicates whether this is the standard industry. | No |

---

## BPRelationship (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RelationshipID | Relationship ID | String | Yes | Unique identifier for the relationship. | No |
| ValidFrom | Valid From | Date | No | Relationship validity start date. | No |
| ValidTo | Valid To | Date | No | Relationship validity end date. | No |

---

## BPRole (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RoleID | Role ID | String | Yes | Unique identifier for the business partner role assignment. | No |
| ValidFrom | Valid From | Date | No | Date from which the role is valid. | No |
| ValidTo | Valid To | Date | No | Date through which the role is valid. | No |

---

## BPTaxNumber (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| TaxID | Tax ID | String | Yes | Unique identifier for the tax number record. | No |
| BPTaxNumber | BP Tax Number | String | Yes | Tax number value. | No |
| TaxNumberValidityDate | Tax Number Validity Date | Date | No | Tax number validity date. | No |
| TaxNumberIsCanceled | Tax Number Is Canceled | Boolean | No | Indicates whether the tax number is canceled. | No |
| NormalizedTaxNumber | Normalized Tax Number | String | No | Tax number in upper case with spaces removed used for search and comparison. | No |

---

## SupplierCompany (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SupplierCompanyID | Supplier Company ID | String | Yes | Unique identifier for the supplier company assignment. | No |
| SupplierAccountNote | Supplier Account Note | String | No | Supplier account note. | No |
| PaymentMethodsList | Payment Methods List | String | No | Allowed payment methods. | No |
| PaymentIsBlockedForSupplier | Payment Is Blocked For Supplier | Boolean | No | Company-code payment block flag. | No |
| CheckPaidDuringPaymentRun | Check Paid During Payment Run | Boolean | No | Check paid during payment run flag. | No |
| PostingIsBlocked | Posting Is Blocked | Boolean | No | Posting block flag. | No |
| DeletionIndicator | Deletion Indicator | Boolean | No | Deletion indicator. | No |
| SupplierClerk | Supplier Clerk | String | No | Supplier accounting clerk. | No |

---

## SupplierPartnerFunc (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PartnerFuncID | Partner Func ID | String | Yes | Unique identifier for the partner function assignment. | No |
| PartnerCounter | Partner Counter | String | No | Partner counter. | No |
| DefaultPartner | Default Partner | Boolean | No | Indicates whether this is the default partner. | No |

---

## SupplierText (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| TextID | Text ID | String | Yes | Unique identifier for the supplier text. | No |
| LongText | Long Text | String | No | Long text content. | No |

---

## ABCClassification (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ABCClassificationID | ABC Classification ID | String | Yes | Unique identifier for the abc classification. | No |
| ABCClassificationCode | ABC Classification Code | String | Yes | Code for the abc classification. | No |
| ABCClassificationName | ABC Classification Name | String | Yes | Name of the abc classification. | No |
| Description | Description | String | No | Description for the abc classification. | No |
| Active | Active | Boolean | No | Indicates whether the abc classification is active. | No |

---

## AddressUsage (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AddressUsageID | Address Usage ID | String | Yes | Unique identifier for the address usage. | No |
| AddressUsageCode | Address Usage Code | String | Yes | Code for the address usage. | No |
| AddressUsageName | Address Usage Name | String | Yes | Name of the address usage. | No |
| Description | Description | String | No | Description for the address usage. | No |
| Active | Active | Boolean | No | Indicates whether the address usage is active. | No |

---

## AlternativePayee (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AlternativePayeeID | Alternative Payee ID | String | Yes | Unique identifier for the alternative payee. | No |
| AlternativePayeeCode | Alternative Payee Code | String | Yes | Code for the alternative payee. | No |
| AlternativePayeeName | Alternative Payee Name | String | Yes | Name of the alternative payee. | No |
| Description | Description | String | No | Description for the alternative payee. | No |
| Active | Active | Boolean | No | Indicates whether the alternative payee is active. | No |

---

## AuthorizationGroup (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AuthorizationGroupID | Authorization Group ID | String | Yes | Unique identifier for the authorization group. | No |
| AuthorizationGroupCode | Authorization Group Code | String | Yes | Code for the authorization group. | No |
| AuthorizationGroupName | Authorization Group Name | String | Yes | Name of the authorization group. | No |
| Description | Description | String | No | Description for the authorization group. | No |
| Active | Active | Boolean | No | Indicates whether the authorization group is active. | No |

---

## BPStatus (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BPStatusID | BP Status ID | String | Yes | Unique identifier for the bp status. | No |
| BPStatusCode | BP Status Code | String | Yes | Code for the bp status. | No |
| BPStatusName | BP Status Name | String | Yes | Name of the bp status. | No |
| Description | Description | String | No | Description for the bp status. | No |
| Active | Active | Boolean | No | Indicates whether the bp status is active. | No |

---

## BPTaxType (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BPTaxTypeID | BP Tax Type ID | String | Yes | Unique identifier for the bp tax type. | No |
| BPTaxTypeCode | BP Tax Type Code | String | Yes | Code for the bp tax type. | No |
| BPTaxTypeName | BP Tax Type Name | String | Yes | Name of the bp tax type. | No |
| Description | Description | String | No | Description for the bp tax type. | No |
| Active | Active | Boolean | No | Indicates whether the bp tax type is active. | No |

---

## BpIdentificationType (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BpIdentificationTypeID | BP Identification Type ID | String | Yes | Unique identifier for the bp identification type. | No |
| BpIdentificationTypeCode | BP Identification Type Code | String | Yes | Code for the bp identification type. | No |
| BpIdentificationTypeName | BP Identification Type Name | String | Yes | Name of the bp identification type. | No |
| Description | Description | String | No | Description for the bp identification type. | No |
| Active | Active | Boolean | No | Indicates whether the bp identification type is active. | No |

---

## BusinessPartnerCategory (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BusinessPartnerCategoryID | Business Partner Category ID | String | Yes | Unique identifier for the business partner category. | No |
| BusinessPartnerCategoryCode | Business Partner Category Code | String | Yes | Code for the business partner category. | No |
| BusinessPartnerCategoryName | Business Partner Category Name | String | Yes | Name of the business partner category. | No |
| Description | Description | String | No | Description for the business partner category. | No |
| Active | Active | Boolean | No | Indicates whether the business partner category is active. | No |

---

## BusinessPartnerGrouping (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BusinessPartnerGroupingID | Business Partner Grouping ID | String | Yes | Unique identifier for the business partner grouping. | No |
| BusinessPartnerGroupingCode | Business Partner Grouping Code | String | Yes | Code for the business partner grouping. | No |
| BusinessPartnerGroupingName | Business Partner Grouping Name | String | Yes | Name of the business partner grouping. | No |
| Description | Description | String | No | Description for the business partner grouping. | No |
| Active | Active | Boolean | No | Indicates whether the business partner grouping is active. | No |

---

## BusinessPartnerRole (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BusinessPartnerRoleID | Business Partner Role ID | String | Yes | Unique identifier for the business partner role. | No |
| BusinessPartnerRoleCode | Business Partner Role Code | String | Yes | Code for the business partner role. | No |
| BusinessPartnerRoleName | Business Partner Role Name | String | Yes | Name of the business partner role. | No |
| Description | Description | String | No | Description for the business partner role. | No |
| Active | Active | Boolean | No | Indicates whether the business partner role is active. | No |

---

## CashPlanningGroup (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CashPlanningGroupID | Cash Planning Group ID | String | Yes | Unique identifier for the cash planning group. | No |
| CashPlanningGroupCode | Cash Planning Group Code | String | Yes | Code for the cash planning group. | No |
| CashPlanningGroupName | Cash Planning Group Name | String | Yes | Name of the cash planning group. | No |
| Description | Description | String | No | Description for the cash planning group. | No |
| Active | Active | Boolean | No | Indicates whether the cash planning group is active. | No |

---

## CompanyCode (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CompanyCodeID | Company Code ID | String | Yes | Unique identifier for the company code. | No |
| CompanyCodeCode | Company Code Code | String | Yes | Code for the company code. | No |
| CompanyCodeName | Company Code Name | String | Yes | Name of the company code. | No |
| Description | Description | String | No | Description for the company code. | No |
| Active | Active | Boolean | No | Indicates whether the company code is active. | No |

---

## ContactPersonDepartment (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ContactPersonDepartmentID | Contact Person Department ID | String | Yes | Unique identifier for the contact person department. | No |
| ContactPersonDepartmentCode | Contact Person Department Code | String | Yes | Code for the contact person department. | No |
| ContactPersonDepartmentName | Contact Person Department Name | String | Yes | Name of the contact person department. | No |
| Description | Description | String | No | Description for the contact person department. | No |
| Active | Active | Boolean | No | Indicates whether the contact person department is active. | No |

---

## ContactPersonFunction (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ContactPersonFunctionID | Contact Person Function ID | String | Yes | Unique identifier for the contact person function. | No |
| ContactPersonFunctionCode | Contact Person Function Code | String | Yes | Code for the contact person function. | No |
| ContactPersonFunctionName | Contact Person Function Name | String | Yes | Name of the contact person function. | No |
| Description | Description | String | No | Description for the contact person function. | No |
| Active | Active | Boolean | No | Indicates whether the contact person function is active. | No |

---

## Country (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CountryID | Country ID | String | Yes | Unique identifier for the country. | No |
| CountryCode | Country Code | String | Yes | Code for the country. | No |
| CountryName | Country Name | String | Yes | Name of the country. | No |
| Description | Description | String | No | Description for the country. | No |
| Active | Active | Boolean | No | Indicates whether the country is active. | No |

---

## Currency (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CurrencyID | Currency ID | String | Yes | Unique identifier for the currency. | No |
| CurrencyCode | Currency Code | String | Yes | Code for the currency. | No |
| CurrencyName | Currency Name | String | Yes | Name of the currency. | No |
| Description | Description | String | No | Description for the currency. | No |
| Active | Active | Boolean | No | Indicates whether the currency is active. | No |

---

## HouseBank (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| HouseBankID | House Bank ID | String | Yes | Unique identifier for the house bank. | No |
| HouseBankCode | House Bank Code | String | Yes | Code for the house bank. | No |
| HouseBankName | House Bank Name | String | Yes | Name of the house bank. | No |
| Description | Description | String | No | Description for the house bank. | No |
| Active | Active | Boolean | No | Indicates whether the house bank is active. | No |

---

## IncotermsClassification (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| IncotermsClassificationID | Incoterms Classification ID | String | Yes | Unique identifier for the incoterms classification. | No |
| IncotermsClassificationCode | Incoterms Classification Code | String | Yes | Code for the incoterms classification. | No |
| IncotermsClassificationName | Incoterms Classification Name | String | Yes | Name of the incoterms classification. | No |
| Description | Description | String | No | Description for the incoterms classification. | No |
| Active | Active | Boolean | No | Indicates whether the incoterms classification is active. | No |

---

## Industry (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| IndustryID | Industry ID | String | Yes | Unique identifier for the industry. | No |
| IndustryCode | Industry Code | String | Yes | Code for the industry. | No |
| IndustryName | Industry Name | String | Yes | Name of the industry. | No |
| Description | Description | String | No | Description for the industry. | No |
| Active | Active | Boolean | No | Indicates whether the industry is active. | No |

---

## IndustrySector (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| IndustrySectorID | Industry Sector ID | String | Yes | Unique identifier for the industry sector. | No |
| IndustrySectorCode | Industry Sector Code | String | Yes | Code for the industry sector. | No |
| IndustrySectorName | Industry Sector Name | String | Yes | Name of the industry sector. | No |
| Description | Description | String | No | Description for the industry sector. | No |
| Active | Active | Boolean | No | Indicates whether the industry sector is active. | No |

---

## InterestCalculationCode (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| InterestCalculationCodeID | Interest Calculation Code ID | String | Yes | Unique identifier for the interest calculation code. | No |
| InterestCalculationCodeCode | Interest Calculation Code Code | String | Yes | Code for the interest calculation code. | No |
| InterestCalculationCodeName | Interest Calculation Code Name | String | Yes | Name of the interest calculation code. | No |
| Description | Description | String | No | Description for the interest calculation code. | No |
| Active | Active | Boolean | No | Indicates whether the interest calculation code is active. | No |

---

## Language (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| LanguageID | Language ID | String | Yes | Unique identifier for the language. | No |
| LanguageCode | Language Code | String | Yes | Code for the language. | No |
| LanguageName | Language Name | String | Yes | Name of the language. | No |
| Description | Description | String | No | Description for the language. | No |
| Active | Active | Boolean | No | Indicates whether the language is active. | No |

---

## LongTextID (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| LongTextIDID | Long Text ID ID | String | Yes | Unique identifier for the long text id. | No |
| LongTextIDCode | Long Text ID Code | String | Yes | Code for the long text id. | No |
| LongTextIDName | Long Text ID Name | String | Yes | Name of the long text id. | No |
| Description | Description | String | No | Description for the long text id. | No |
| Active | Active | Boolean | No | Indicates whether the long text id is active. | No |

---

## PartnerFunction (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PartnerFunctionID | Partner Function ID | String | Yes | Unique identifier for the partner function. | No |
| PartnerFunctionCode | Partner Function Code | String | Yes | Code for the partner function. | No |
| PartnerFunctionName | Partner Function Name | String | Yes | Name of the partner function. | No |
| Description | Description | String | No | Description for the partner function. | No |
| Active | Active | Boolean | No | Indicates whether the partner function is active. | No |

---

## PaymentBlockingReason (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PaymentBlockingReasonID | Payment Blocking Reason ID | String | Yes | Unique identifier for the payment blocking reason. | No |
| PaymentBlockingReasonCode | Payment Blocking Reason Code | String | Yes | Code for the payment blocking reason. | No |
| PaymentBlockingReasonName | Payment Blocking Reason Name | String | Yes | Name of the payment blocking reason. | No |
| Description | Description | String | No | Description for the payment blocking reason. | No |
| Active | Active | Boolean | No | Indicates whether the payment blocking reason is active. | No |

---

## PaymentTerms (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PaymentTermsID | Payment Terms ID | String | Yes | Unique identifier for the payment terms. | No |
| PaymentTermsCode | Payment Terms Code | String | Yes | Code for the payment terms. | No |
| PaymentTermsName | Payment Terms Name | String | Yes | Name of the payment terms. | No |
| Description | Description | String | No | Description for the payment terms. | No |
| Active | Active | Boolean | No | Indicates whether the payment terms is active. | No |

---

## PhoneNumberType (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PhoneNumberTypeID | Phone Number Type ID | String | Yes | Unique identifier for the phone number type. | No |
| PhoneNumberTypeCode | Phone Number Type Code | String | Yes | Code for the phone number type. | No |
| PhoneNumberTypeName | Phone Number Type Name | String | Yes | Name of the phone number type. | No |
| Description | Description | String | No | Description for the phone number type. | No |
| Active | Active | Boolean | No | Indicates whether the phone number type is active. | No |

---

## PlanningCycle (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PlanningCycleID | Planning Cycle ID | String | Yes | Unique identifier for the planning cycle. | No |
| PlanningCycleCode | Planning Cycle Code | String | Yes | Code for the planning cycle. | No |
| PlanningCycleName | Planning Cycle Name | String | Yes | Name of the planning cycle. | No |
| Description | Description | String | No | Description for the planning cycle. | No |
| Active | Active | Boolean | No | Indicates whether the planning cycle is active. | No |

---

## PricingDateControl (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PricingDateControlID | Pricing Date Control ID | String | Yes | Unique identifier for the pricing date control. | No |
| PricingDateControlCode | Pricing Date Control Code | String | Yes | Code for the pricing date control. | No |
| PricingDateControlName | Pricing Date Control Name | String | Yes | Name of the pricing date control. | No |
| Description | Description | String | No | Description for the pricing date control. | No |
| Active | Active | Boolean | No | Indicates whether the pricing date control is active. | No |

---

## PurchasingGroup (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PurchasingGroupID | Purchasing Group ID | String | Yes | Unique identifier for the purchasing group. | No |
| PurchasingGroupCode | Purchasing Group Code | String | Yes | Code for the purchasing group. | No |
| PurchasingGroupName | Purchasing Group Name | String | Yes | Name of the purchasing group. | No |
| Description | Description | String | No | Description for the purchasing group. | No |
| Active | Active | Boolean | No | Indicates whether the purchasing group is active. | No |

---

## PurchasingOrganization (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PurchasingOrganizationID | Purchasing Organization ID | String | Yes | Unique identifier for the purchasing organization. | No |
| PurchasingOrganizationCode | Purchasing Organization Code | String | Yes | Code for the purchasing organization. | No |
| PurchasingOrganizationName | Purchasing Organization Name | String | Yes | Name of the purchasing organization. | No |
| Description | Description | String | No | Description for the purchasing organization. | No |
| Active | Active | Boolean | No | Indicates whether the purchasing organization is active. | No |

---

## ReconciliationAccount (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ReconciliationAccountID | Reconciliation Account ID | String | Yes | Unique identifier for the reconciliation account. | No |
| ReconciliationAccountCode | Reconciliation Account Code | String | Yes | Code for the reconciliation account. | No |
| ReconciliationAccountName | Reconciliation Account Name | String | Yes | Name of the reconciliation account. | No |
| Description | Description | String | No | Description for the reconciliation account. | No |
| Active | Active | Boolean | No | Indicates whether the reconciliation account is active. | No |

---

## Region (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RegionID | Region ID | String | Yes | Unique identifier for the region. | No |
| RegionCode | Region Code | String | Yes | Code for the region. | No |
| RegionName | Region Name | String | Yes | Name of the region. | No |
| Description | Description | String | No | Description for the region. | No |
| Active | Active | Boolean | No | Indicates whether the region is active. | No |

---

## RelationshipCategory (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RelationshipCategoryID | Relationship Category ID | String | Yes | Unique identifier for the relationship category. | No |
| RelationshipCategoryCode | Relationship Category Code | String | Yes | Code for the relationship category. | No |
| RelationshipCategoryName | Relationship Category Name | String | Yes | Name of the relationship category. | No |
| Description | Description | String | No | Description for the relationship category. | No |
| Active | Active | Boolean | No | Indicates whether the relationship category is active. | No |

---

## ResponsibleType (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ResponsibleTypeID | Responsible Type ID | String | Yes | Unique identifier for the responsible type. | No |
| ResponsibleTypeCode | Responsible Type Code | String | Yes | Code for the responsible type. | No |
| ResponsibleTypeName | Responsible Type Name | String | Yes | Name of the responsible type. | No |
| Description | Description | String | No | Description for the responsible type. | No |
| Active | Active | Boolean | No | Indicates whether the responsible type is active. | No |

---

## ShippingCondition (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ShippingConditionID | Shipping Condition ID | String | Yes | Unique identifier for the shipping condition. | No |
| ShippingConditionCode | Shipping Condition Code | String | Yes | Code for the shipping condition. | No |
| ShippingConditionName | Shipping Condition Name | String | Yes | Name of the shipping condition. | No |
| Description | Description | String | No | Description for the shipping condition. | No |
| Active | Active | Boolean | No | Indicates whether the shipping condition is active. | No |

---

## SortKey (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SortKeyID | Sort Key ID | String | Yes | Unique identifier for the sort key. | No |
| SortKeyCode | Sort Key Code | String | Yes | Code for the sort key. | No |
| SortKeyName | Sort Key Name | String | Yes | Name of the sort key. | No |
| Description | Description | String | No | Description for the sort key. | No |
| Active | Active | Boolean | No | Indicates whether the sort key is active. | No |

---

## SourceSystem (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SourceSystemID | Source System ID | String | Yes | Unique identifier for the source system. | No |
| SourceSystemCode | Source System Code | String | Yes | Code for the source system. | No |
| SourceSystemName | Source System Name | String | Yes | Name of the source system. | No |
| Description | Description | String | No | Description for the source system. | No |
| Active | Active | Boolean | No | Indicates whether the source system is active. | No |

---

## SupplierAccountGroup (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SupplierAccountGroupID | Supplier Account Group ID | String | Yes | Unique identifier for the supplier account group. | No |
| SupplierAccountGroupCode | Supplier Account Group Code | String | Yes | Code for the supplier account group. | No |
| SupplierAccountGroupName | Supplier Account Group Name | String | Yes | Name of the supplier account group. | No |
| Description | Description | String | No | Description for the supplier account group. | No |
| Active | Active | Boolean | No | Indicates whether the supplier account group is active. | No |

---

## SupplierCorporateGroup (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SupplierCorporateGroupID | Supplier Corporate Group ID | String | Yes | Unique identifier for the supplier corporate group. | No |
| SupplierCorporateGroupCode | Supplier Corporate Group Code | String | Yes | Code for the supplier corporate group. | No |
| SupplierCorporateGroupName | Supplier Corporate Group Name | String | Yes | Name of the supplier corporate group. | No |
| Description | Description | String | No | Description for the supplier corporate group. | No |
| Active | Active | Boolean | No | Indicates whether the supplier corporate group is active. | No |

---

## TaxJurisdiction (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| TaxJurisdictionID | Tax Jurisdiction ID | String | Yes | Unique identifier for the tax jurisdiction. | No |
| TaxJurisdictionCode | Tax Jurisdiction Code | String | Yes | Code for the tax jurisdiction. | No |
| TaxJurisdictionName | Tax Jurisdiction Name | String | Yes | Name of the tax jurisdiction. | No |
| Description | Description | String | No | Description for the tax jurisdiction. | No |
| Active | Active | Boolean | No | Indicates whether the tax jurisdiction is active. | No |

---

## TaxNumberCategory (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| TaxNumberCategoryID | Tax Number Category ID | String | Yes | Unique identifier for the tax number category. | No |
| TaxNumberCategoryCode | Tax Number Category Code | String | Yes | Code for the tax number category. | No |
| TaxNumberCategoryName | Tax Number Category Name | String | Yes | Name of the tax number category. | No |
| Description | Description | String | No | Description for the tax number category. | No |
| Active | Active | Boolean | No | Indicates whether the tax number category is active. | No |

---

## ToleranceGroup (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ToleranceGroupID | Tolerance Group ID | String | Yes | Unique identifier for the tolerance group. | No |
| ToleranceGroupCode | Tolerance Group Code | String | Yes | Code for the tolerance group. | No |
| ToleranceGroupName | Tolerance Group Name | String | Yes | Name of the tolerance group. | No |
| Description | Description | String | No | Description for the tolerance group. | No |
| Active | Active | Boolean | No | Indicates whether the tolerance group is active. | No |

---

## TradingPartner (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| TradingPartnerID | Trading Partner ID | String | Yes | Unique identifier for the trading partner. | No |
| TradingPartnerCode | Trading Partner Code | String | Yes | Code for the trading partner. | No |
| TradingPartnerName | Trading Partner Name | String | Yes | Name of the trading partner. | No |
| Description | Description | String | No | Description for the trading partner. | No |
| Active | Active | Boolean | No | Indicates whether the trading partner is active. | No |

---

## TransportZone (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| TransportZoneID | Transport Zone ID | String | Yes | Unique identifier for the transport zone. | No |
| TransportZoneCode | Transport Zone Code | String | Yes | Code for the transport zone. | No |
| TransportZoneName | Transport Zone Name | String | Yes | Name of the transport zone. | No |
| Description | Description | String | No | Description for the transport zone. | No |
| Active | Active | Boolean | No | Indicates whether the transport zone is active. | No |

---

