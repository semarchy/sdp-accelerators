# Validations Documentation

This table summarizes the validations defined in the model, including their entity, name, label, and condition. All validations run in the PRE_CONSO scope as logical (soft) constraints rather than database constraints.

| Entity | Name | Label | Condition |
|--------|------|-------|-----------|
| BPAddress | PostalCodeRequiresCity | City Name is required when a Postal Code is provided. | PostalCode is null or CityName is not null |
| BPAddressEmail | EmailFormat | Email Address must contain a valid pattern. | EmailAddress is null or EmailAddress like '%_@_%.__%' |
| BPAddressPhone | PhoneNumberLength | Phone Number must be between 5 and 30 characters. | PhoneNumber is null or (length(PhoneNumber) >= 5 and length(PhoneNumber) <= 30) |
| BPAddressUsage | UsageValidity | Valid To must not be before Valid From. | ValidTo is null or ValidFrom is null or ValidTo >= ValidFrom |
| BPBank | BankValidity | Validity End Date must not be before Validity Start Date. | ValidityEndDate is null or ValidityStartDate is null or ValidityEndDate >= ValidityStartDate |
| BPBank | IBANLength | IBAN length must be between 15 and 34 characters. | IBAN is null or (length(IBAN) >= 15 and length(IBAN) <= 34) |
| BPBank | SWIFTCodeLength | SWIFT/BIC code must be 8 or 11 characters. | SWIFTCode is null or length(SWIFTCode) = 8 or length(SWIFTCode) = 11 |
| BPContact | ContactNameRequired | Contact Full Name is required. | ContactFullName is not null |
| BPIdentification | IdentificationNumberRequired | BP Identification Number value is required. | BpIdentificationNumber is not null |
| BPRelationship | RelationshipValidity | Valid To must not be before Valid From. | ValidTo is null or ValidFrom is null or ValidTo >= ValidFrom |
| BPRole | RoleValidity | Valid To must not be before Valid From. | ValidTo is null or ValidFrom is null or ValidTo >= ValidFrom |
| BPTaxNumber | TaxNumberRequired | BP Tax Number value is required. | BPTaxNumber is not null |
| BusinessPartner | AuditDates | Last Modified Date must not be before Created Date. | CreatedDate is null or LastModifiedDate is null or LastModifiedDate >= CreatedDate |
| BusinessPartner | NaturalPersonLastName | Last Name is required for a natural person business partner. | COALESCE(SEM_BOOLEAN_TO_CHAR(IsNaturalPerson), 'false') = 'false' or LastName is not null |
| Supplier | SupplierNameRequired | Supplier Name or Full Name is required. | SupplierName is not null or SupplierFullName is not null |
| SupplierPurchasingOrg | MinimumOrderAmountPositive | Minimum Order Amount must not be negative. | MinimumOrderAmount is null or MinimumOrderAmount >= 0 |
