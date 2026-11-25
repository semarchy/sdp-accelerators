# Enrichers

Enrichers fill in or standardize values automatically during certification. *Before consolidation* enrichers run on each record sent by a source system; *after consolidation* enrichers run on the golden record.

| Entity | Enricher | Runs | What it does |
|---|---|---|---|
| Restaurant | Derive public listing, time zone and check keys | After consolidation | Sets what public channels must show from the lifecycle status, defaults the time zone from the state, and builds the keys that flag duplicate sites and addresses. |
| Restaurant | Normalize main phone | Before consolidation | Writes North American phone numbers as +1 followed by 10 digits. |
| Restaurant | Record which systems publish the restaurant | Before consolidation | Marks each source record with the system it comes from; consolidation keeps Yes as soon as one record of that system exists. |
| Restaurant | Standardize address | Before consolidation | Removes stray spaces in the address and formats Canadian postal codes as A1A 1A1. |
| RestaurantHours | Build the hours slot key | Before consolidation | Builds the key that keeps one row per channel, day or date and start date. |
| RestaurantContactPoint | Normalize phone numbers | Before consolidation | Writes phone and fax numbers as +1 followed by 10 digits. |
| RestaurantLocalizedName | Build the natural key | Before consolidation | Builds the key that allows only one row per restaurant and language. |
| RestaurantStatusHistory | Build the natural key | Before consolidation | Builds the key that allows only one row per restaurant and start date. |
| RestaurantOperator | Build the natural key | Before consolidation | Builds the key that allows only one row per restaurant and start date. |
| RestaurantOrgAssignment | Build the natural key | Before consolidation | Builds the key that allows only one row per restaurant, hierarchy and start date. |
| RestaurantIdentifier | Build the natural key | Before consolidation | Builds the key that allows only one row per system, identifier type, value and start date. |

## Restaurant (`Restaurant`)

### Derive public listing, time zone and check keys (`DeriveListingAndKeys`)

Sets what public channels must show from the lifecycle status, defaults the time zone from the state, and builds the keys that flag duplicate sites and addresses. Runs **after consolidation**.

| Attribute set | SemQL expression |
|---|---|
| PublicChannelStatus | `COALESCE(LifecycleStatus.PublicChannelStatus, 'NOT_LISTED')` |
| TimeZone | `COALESCE(TimeZone, StateProvince.DefaultTimeZone)` |
| DuplicateCheckKey | `CASE WHEN FID_Brand IS NULL OR AddressLine1 IS NULL OR PostalCode IS NULL THEN 'ID\|' \|\| RestaurantID ELSE FID_Brand \|\| '\|' \|\| UPPER(REGEXP_REPLACE(AddressLine1, '[^A-Za-z0-9]', '', 'g')) \|\| '\|' \|\| UPPER(REPLACE(PostalCode, ' ', '')) END` |
| SiteCheckKey | `COALESCE(SiteID, 'ID\|' \|\| RestaurantID)` |

### Normalize main phone (`NormalizeMainPhone`)

Writes North American phone numbers as +1 followed by 10 digits. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| MainPhone | `CASE WHEN LENGTH(REGEXP_REPLACE(MainPhone, '[^0-9]', '', 'g')) = 10 THEN '+1' \|\| REGEXP_REPLACE(MainPhone, '[^0-9]', '', 'g') WHEN LENGTH(REGEXP_REPLACE(MainPhone, '[^0-9]', '', 'g')) = 11 AND SUBSTR(REGEXP_REPLACE(MainPhone, '[^0-9]', '', 'g'), 1, 1) = '1' THEN '+' \|\| REGEXP_REPLACE(MainPhone, '[^0-9]', '', 'g') ELSE MainPhone END` |

### Record which systems publish the restaurant (`StampProvenance`)

Marks each source record with the system it comes from; consolidation keeps Yes as soon as one record of that system exists. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| InRealEstate | `CASE WHEN PublisherID = 'RE' THEN 'Y' ELSE 'N' END` |
| InERP | `CASE WHEN PublisherID = 'ERP' THEN 'Y' ELSE 'N' END` |
| InPOS | `CASE WHEN PublisherID IN ('POSF', 'POSK', 'POSB') THEN 'Y' ELSE 'N' END` |

### Standardize address (`StandardizeAddress`)

Removes stray spaces in the address and formats Canadian postal codes as A1A 1A1. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| AddressLine1 | `REGEXP_REPLACE(BTRIM(AddressLine1), ' +', ' ', 'g')` |
| AddressLine2 | `REGEXP_REPLACE(BTRIM(AddressLine2), ' +', ' ', 'g')` |
| City | `REGEXP_REPLACE(BTRIM(City), ' +', ' ', 'g')` |
| PostalCode | `CASE WHEN FID_Country = 'CA' THEN REGEXP_REPLACE(UPPER(REPLACE(PostalCode, ' ', '')), '^([A-Z][0-9][A-Z])([0-9][A-Z][0-9])$', '\1 \2') ELSE BTRIM(PostalCode) END` |

## Opening hours (`RestaurantHours`)

### Build the hours slot key (`BuildSlotKey`)

Builds the key that keeps one row per channel, day or date and start date. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| HoursSlotKey | `FID_Restaurant \|\| '\|' \|\| ServiceChannel \|\| '\|' \|\| HoursType \|\| '\|' \|\| COALESCE(DayOfWeek, TO_CHAR(SpecialDate, 'YYYY-MM-DD'), '-') \|\| '\|' \|\| TO_CHAR(EffectiveFrom, 'YYYY-MM-DD')` |

## Contact point (`RestaurantContactPoint`)

### Normalize phone numbers (`NormalizePhone`)

Writes phone and fax numbers as +1 followed by 10 digits. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| ContactValue | `CASE WHEN ContactPointType IN ('PHONE', 'FAX') THEN CASE WHEN LENGTH(REGEXP_REPLACE(ContactValue, '[^0-9]', '', 'g')) = 10 THEN '+1' \|\| REGEXP_REPLACE(ContactValue, '[^0-9]', '', 'g') WHEN LENGTH(REGEXP_REPLACE(ContactValue, '[^0-9]', '', 'g')) = 11 AND SUBSTR(REGEXP_REPLACE(ContactValue, '[^0-9]', '', 'g'), 1, 1) = '1' THEN '+' \|\| REGEXP_REPLACE(ContactValue, '[^0-9]', '', 'g') ELSE ContactValue END ELSE BTRIM(ContactValue) END` |

## Localized name (`RestaurantLocalizedName`)

### Build the natural key (`BuildNaturalKey`)

Builds the key that allows only one row per restaurant and language. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| NaturalKey | `FID_Restaurant \|\| '\|' \|\| Language` |

## Status history (`RestaurantStatusHistory`)

### Build the natural key (`BuildNaturalKey`)

Builds the key that allows only one row per restaurant and start date. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| NaturalKey | `FID_Restaurant \|\| '\|' \|\| TO_CHAR(StartDate, 'YYYY-MM-DD')` |

## Operator (`RestaurantOperator`)

### Build the natural key (`BuildNaturalKey`)

Builds the key that allows only one row per restaurant and start date. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| NaturalKey | `FID_Restaurant \|\| '\|' \|\| TO_CHAR(EffectiveFrom, 'YYYY-MM-DD')` |

## Organization assignment (`RestaurantOrgAssignment`)

### Build the natural key (`BuildNaturalKey`)

Builds the key that allows only one row per restaurant, hierarchy and start date. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| NaturalKey | `FID_Restaurant \|\| '\|' \|\| HierarchyType \|\| '\|' \|\| TO_CHAR(EffectiveFrom, 'YYYY-MM-DD')` |

## Restaurant identifier (`RestaurantIdentifier`)

### Build the natural key (`BuildNaturalKey`)

Builds the key that allows only one row per system, identifier type, value and start date. Runs **before consolidation**.

| Attribute set | SemQL expression |
|---|---|
| NaturalKey | `FID_SourceSystem \|\| '\|' \|\| FID_IdentifierType \|\| '\|' \|\| IdentifierValue \|\| '\|' \|\| TO_CHAR(ValidFrom, 'YYYY-MM-DD')` |
