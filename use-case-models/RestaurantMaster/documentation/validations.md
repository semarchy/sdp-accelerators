# Validations

A record that fails a validation is not certified: it stays in the error views (*Data stewardship > Records in error*) with the message below, until it is corrected and loaded or saved again. Validations that run *after consolidation* check the golden record of an ID-matched entity.

## Validation rules

| Entity | Rule | Runs | Message shown |
|---|---|---|---|
| Restaurant | BrandRequired | After consolidation | A restaurant beyond the pipeline stage must have a brand. |
| Restaurant | LifecycleCoherence | After consolidation | Status and dates disagree: an open restaurant needs an opening date in the past, a temporarily closed one a closure date, a permanently closed or relocated one a permanent closure date, and the reason must belong to the status. |
| Restaurant | RestaurantIdFormat | After consolidation | The restaurant ID must be R followed by 7 digits (for example R0000123). |
| RestaurantHours | HoursComplete | Before consolidation | Regular hours need a day, special hours a date; open and close times are HH:MM (close after open unless it closes the next day) unless the channel is closed or open 24 hours; dates in order. |
| RestaurantHours | KeyConvention | Before consolidation | The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471). |
| RestaurantService | DeliveryPartnerRule | Before consolidation | A delivery service names its delivery partner, other services do not; dates in order. |
| RestaurantService | KeyConvention | Before consolidation | The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471). |
| RestaurantContactPoint | ContactFormat | Before consolidation | An email must look like name@domain.tld and a link must start with http. |
| RestaurantContactPoint | KeyConvention | Before consolidation | The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471). |
| RestaurantLocalizedName | KeyConvention | Before consolidation | The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471). |
| RestaurantStatusHistory | KeyConvention | Before consolidation | The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471). |
| RestaurantStatusHistory | ReasonFitsStatus | Before consolidation | The reason must belong to the selected status. |
| RestaurantOperator | AgreementRequired | Before consolidation | A franchised operator needs a franchise agreement number. |
| RestaurantOperator | KeyConvention | Before consolidation | The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471). |
| RestaurantOrgAssignment | KeyConvention | Before consolidation | The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471). |
| RestaurantOrgAssignment | UnitFitsHierarchy | Before consolidation | The organization unit must belong to the selected hierarchy. |
| RestaurantIdentifier | KeyConvention | Before consolidation | The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471). |
| RestaurantIdentifier | ValidityOrder | Before consolidation | Valid to must not be before valid from. |
| Franchisee | PrincipalEmailFormat | Before consolidation | The principal email must look like name@domain.tld. |
| LegalEntity | LegalEntityKeyFormat | After consolidation | The key must be US- or CA- followed by 9 digits. |
| OrganizationUnit | UnitIntegrity | Before consolidation | The parent must be in the same hierarchy and not create a loop; a market has a brand, other units none. |

## Unique keys

A unique key rejects a record when another record already has the same values for the listed attributes.

| Entity | Unique key | Attributes | Runs | Message shown |
|---|---|---|---|---|
| Restaurant | UkDuplicateAddress | DuplicateCheckKey | After consolidation | Another restaurant of the same brand exists at this address - possibly a mistyped restaurant ID. |
| Restaurant | UkSite | SiteCheckKey | After consolidation | Another restaurant already carries this Site ID. |
| RestaurantHours | UkHoursSlot | HoursSlotKey | Before consolidation | These hours are already defined for this channel, day or date and start date. |
| RestaurantLocalizedName | UkLanguage | NaturalKey | Before consolidation | This restaurant already has a name in this language. |
| RestaurantStatusHistory | UkStatusStart | NaturalKey | Before consolidation | This restaurant already has a status starting that day. |
| RestaurantOperator | UkOperatorStart | NaturalKey | Before consolidation | This restaurant already has an operator starting that day. |
| RestaurantOrgAssignment | UkAssignmentStart | NaturalKey | Before consolidation | This restaurant already has an assignment in this hierarchy starting that day. |
| RestaurantIdentifier | UkIdentifier | NaturalKey | Before consolidation | This system already uses this identifier from this date. |

## Mandatory attributes

Every attribute marked *Mandatory* in [model_structure.md](model_structure.md) is checked too: a record without it is rejected.

## Rule conditions (SemQL)

The condition each rule tests. A record passes when the condition is true.

### Restaurant (`Restaurant`)

**BrandRequired**: A restaurant beyond the pipeline stage must have a brand.

```sql
FID_Brand IS NOT NULL OR FID_LifecycleStatus IS NULL OR FID_LifecycleStatus IN ('PIPELINE', 'CANCELLED')
```

**LifecycleCoherence**: Status and dates disagree: an open restaurant needs an opening date in the past, a temporarily closed one a closure date, a permanently closed or relocated one a permanent closure date, and the reason must belong to the status.

```sql
(FID_LifecycleStatus IS NULL OR FID_LifecycleStatus <> 'OPEN' OR (OriginalOpenDate IS NOT NULL AND OriginalOpenDate <= CURRENT_DATE())) AND (FID_LifecycleStatus IS NULL OR FID_LifecycleStatus <> 'TEMP_CLOSED' OR TemporaryClosureDate IS NOT NULL) AND (FID_LifecycleStatus IS NULL OR FID_LifecycleStatus NOT IN ('PERM_CLOSED', 'RELOCATED') OR PermanentClosureDate IS NOT NULL) AND (FID_LifecycleStatusReason IS NULL OR LifecycleStatusReason.FID_LifecycleStatus = FID_LifecycleStatus)
```

**RestaurantIdFormat**: The restaurant ID must be R followed by 7 digits (for example R0000123).

```sql
REGEXP_REPLACE(RestaurantID, '^R[0-9]{7}$', 'X') = 'X'
```

### Opening hours (`RestaurantHours`)

**HoursComplete**: Regular hours need a day, special hours a date; open and close times are HH:MM (close after open unless it closes the next day) unless the channel is closed or open 24 hours; dates in order.

```sql
(HoursType <> 'REGULAR' OR DayOfWeek IS NOT NULL) AND (HoursType <> 'SPECIAL' OR SpecialDate IS NOT NULL) AND (COALESCE(Closed, 'N') = 'Y' OR COALESCE(Open24Hours, 'N') = 'Y' OR (REGEXP_REPLACE(COALESCE(OpenTime, ''), '^([01][0-9]|2[0-3]):[0-5][0-9]$', 'X') = 'X' AND REGEXP_REPLACE(COALESCE(CloseTime, ''), '^([01][0-9]|2[0-3]):[0-5][0-9]$', 'X') = 'X' AND (CloseTime > OpenTime OR COALESCE(ClosesNextDay, 'N') = 'Y'))) AND (EffectiveTo IS NULL OR EffectiveTo >= EffectiveFrom)
```

**KeyConvention**: The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471).

```sql
SUBSTR(RestaurantHoursID, 1, LENGTH(FID_Restaurant) + 1) = FID_Restaurant || '-'
```

### Service (`RestaurantService`)

**DeliveryPartnerRule**: A delivery service names its delivery partner, other services do not; dates in order.

```sql
((FID_ServiceType = 'DELIVERY' AND FID_DeliveryPartner IS NOT NULL) OR (FID_ServiceType <> 'DELIVERY' AND FID_DeliveryPartner IS NULL)) AND (EffectiveTo IS NULL OR EffectiveTo >= EffectiveFrom)
```

**KeyConvention**: The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471).

```sql
SUBSTR(RestaurantServiceID, 1, LENGTH(FID_Restaurant) + 1) = FID_Restaurant || '-'
```

### Contact point (`RestaurantContactPoint`)

**ContactFormat**: An email must look like name@domain.tld and a link must start with http.

```sql
(ContactPointType <> 'EMAIL' OR ContactValue LIKE '%_@_%._%') AND (ContactPointType NOT IN ('WEBSITE', 'ORDERING', 'SOCIAL') OR ContactValue LIKE 'http%')
```

**KeyConvention**: The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471).

```sql
SUBSTR(RestaurantContactPointID, 1, LENGTH(FID_Restaurant) + 1) = FID_Restaurant || '-'
```

### Localized name (`RestaurantLocalizedName`)

**KeyConvention**: The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471).

```sql
SUBSTR(RestaurantLocalizedNameID, 1, LENGTH(FID_Restaurant) + 1) = FID_Restaurant || '-'
```

### Status history (`RestaurantStatusHistory`)

**KeyConvention**: The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471).

```sql
SUBSTR(RestaurantStatusHistoryID, 1, LENGTH(FID_Restaurant) + 1) = FID_Restaurant || '-'
```

**ReasonFitsStatus**: The reason must belong to the selected status.

```sql
FID_LifecycleStatusReason IS NULL OR LifecycleStatusReason.FID_LifecycleStatus = FID_LifecycleStatus
```

### Operator (`RestaurantOperator`)

**AgreementRequired**: A franchised operator needs a franchise agreement number.

```sql
OwnershipType <> 'FRANCHISED' OR AgreementNumber IS NOT NULL
```

**KeyConvention**: The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471).

```sql
SUBSTR(RestaurantOperatorID, 1, LENGTH(FID_Restaurant) + 1) = FID_Restaurant || '-'
```

### Organization assignment (`RestaurantOrgAssignment`)

**KeyConvention**: The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471).

```sql
SUBSTR(RestaurantOrgAssignmentID, 1, LENGTH(FID_Restaurant) + 1) = FID_Restaurant || '-'
```

**UnitFitsHierarchy**: The organization unit must belong to the selected hierarchy.

```sql
OrganizationUnit.HierarchyType = HierarchyType
```

### Restaurant identifier (`RestaurantIdentifier`)

**KeyConvention**: The key must start with the restaurant ID followed by a dash (for example R0000123-POS-4471).

```sql
SUBSTR(RestaurantIdentifierID, 1, LENGTH(FID_Restaurant) + 1) = FID_Restaurant || '-'
```

**ValidityOrder**: Valid to must not be before valid from.

```sql
ValidTo IS NULL OR ValidTo >= ValidFrom
```

### Franchisee (`Franchisee`)

**PrincipalEmailFormat**: The principal email must look like name@domain.tld.

```sql
PrincipalEmail IS NULL OR PrincipalEmail LIKE '%_@_%._%'
```

### Legal entity (`LegalEntity`)

**LegalEntityKeyFormat**: The key must be US- or CA- followed by 9 digits.

```sql
REGEXP_REPLACE(LegalEntityKey, '^(US|CA)-[0-9]{9}$', 'X') = 'X'
```

### Organization unit (`OrganizationUnit`)

**UnitIntegrity**: The parent must be in the same hierarchy and not create a loop; a market has a brand, other units none.

```sql
(FID_ParentUnit IS NULL OR (FID_ParentUnit <> UnitCode AND (ParentUnit.HierarchyType IS NULL OR ParentUnit.HierarchyType = HierarchyType) AND (ParentUnit.FID_ParentUnit IS NULL OR ParentUnit.FID_ParentUnit <> UnitCode) AND (ParentUnit.ParentUnit.FID_ParentUnit IS NULL OR ParentUnit.ParentUnit.FID_ParentUnit <> UnitCode))) AND ((UnitLevel = 'MARKET' AND FID_Brand IS NOT NULL) OR (UnitLevel <> 'MARKET' AND FID_Brand IS NULL))
```
