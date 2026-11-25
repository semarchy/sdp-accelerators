# Model structure

The data product has **22 entities**, **31 relationships** and **16 lists of values**. Two entities are ID-matched (Restaurant and Legal Entity): several source systems send the same record with the same key, and the platform consolidates them into one golden record. All the others are basic entities.

## Entities

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|---|---|---|---|---|---|
| Restaurant | Restaurant | ID-matched entity. One physical restaurant of the group, across brands and lifecycle stages, from pipeline site to closure. Its identifier is the common restaurant ID issued by Real Estate and carried by every publishing system (Real Estate, ERP, POS), so records from those systems consolidate into one trusted record. | Restaurant, RestaurantContactPoint, RestaurantHours, RestaurantIdentifier, RestaurantLocalizedName, RestaurantOperator, RestaurantOrgAssignment, RestaurantService, RestaurantStatusHistory | Brand, BuildingType, Country, LifecycleStatus, LifecycleStatusReason, LocationType, Restaurant, StateProvince | 33 |
| RestaurantHours | Opening hours | Basic entity. Opening hours of a restaurant per service channel: regular weekly hours and special hours for one date. | - | Restaurant | 14 |
| RestaurantService | Service | Basic entity. A service or amenity a restaurant offers (drive-thru, delivery with a given partner, catering, curbside...), with its availability. | - | Restaurant, ServiceType, SourceSystem | 4 |
| RestaurantContactPoint | Contact point | Basic entity. Additional phone numbers, fax, email addresses, website and ordering or social links of a restaurant, public or internal. | - | Restaurant | 5 |
| RestaurantLocalizedName | Localized name | Basic entity. The restaurant's public name in a given language (French names for Quebec listings). | - | Restaurant | 4 |
| RestaurantStatusHistory | Status history | Basic entity. Lifecycle statuses of a restaurant over time, with reason and comment; a planned change is a row dated in the future. | - | LifecycleStatus, LifecycleStatusReason, Restaurant | 4 |
| RestaurantOperator | Operator | Basic entity. Which legal entity operates the restaurant, under which ownership type and agreement, from a start date (transfer closing date). | - | LegalEntity, Restaurant | 6 |
| RestaurantOrgAssignment | Organization assignment | Basic entity. Places a restaurant in the Finance, Operations or Marketing hierarchy at a unit, from a start date. | - | OrganizationUnit, Restaurant | 4 |
| RestaurantIdentifier | Restaurant identifier | Basic entity. The restaurant's own ID in another system: ERP Restaurant Number, POS ID, delivery merchant ID, listing ID, HR location code. | - | IdentifierType, Restaurant, SourceSystem | 5 |
| Franchisee | Franchisee | Basic entity. A franchise organization behind one or more legal entities, possibly across several brands. Copperline's own companies roll up to a 'Corporate' franchisee record. | LegalEntity | - | 5 |
| LegalEntity | Legal entity | ID-matched entity. A company that signs leases (Real Estate) and franchise agreements and is billed (ERP): a franchisee company or a Copperline company. Identified by its country and tax identifier, shared by ERP and Real Estate. | RestaurantOperator | Country, Franchisee, StateProvince | 10 |
| OrganizationUnit | Organization unit | Basic entity. A unit of the Finance, Operations or Marketing organization: region, area, district or brand-specific market, with its parent unit. | OrganizationUnit, RestaurantOrgAssignment | Brand, OrganizationUnit | 5 |
| Country | Country | Basic entity. Countries where the group operates. | LegalEntity, Restaurant, StateProvince | - | 2 |
| StateProvince | State or province | Basic entity. States and provinces of the countries where the group operates. | LegalEntity, Restaurant | Country | 3 |
| Brand | Brand | Basic entity. Restaurant brands of the group; shared with the future Menu Item and Supply Chain domains. | OrganizationUnit, Restaurant | - | 2 |
| LifecycleStatus | Lifecycle status | Basic entity. Lifecycle stages of a restaurant, from pipeline to closure. | LifecycleStatusReason, Restaurant, RestaurantStatusHistory | - | 4 |
| LifecycleStatusReason | Status reason | Basic entity. Reasons for a lifecycle status (remodel, weather, lease expiry...), each belonging to one status. | Restaurant, RestaurantStatusHistory | LifecycleStatus | 2 |
| IdentifierType | Identifier type | Basic entity. Kinds of system identifier a restaurant can have. | RestaurantIdentifier | - | 2 |
| SourceSystem | Source system | Basic entity. Systems that know a restaurant: publishers, consumers and delivery partners. | RestaurantIdentifier, RestaurantService | - | 3 |
| ServiceType | Service type | Basic entity. Catalogue of services and amenities a restaurant can offer. | RestaurantService | - | 2 |
| BuildingType | Building type | Basic entity. Restaurant formats: freestanding, inline, end-cap, food court, kiosk, ghost kitchen. | Restaurant | - | 2 |
| LocationType | Location type | Basic entity. Venue of a restaurant: street, shopping center, airport, university, travel center, military base. | Restaurant | - | 2 |

## Relationships

| Relationship | Child entity | Parent entity | Mandatory? | Child's reference field | Parent's list of children | On parent delete |
|---|---|---|---|---|---|---|
| LegalEntityHasBillingState | LegalEntity | StateProvince | No | BillingState | BilledLegalEntities | Restrict |
| LegalEntityHasCountry | LegalEntity | Country | Yes | Country | LegalEntities | Restrict |
| LegalEntityHasFranchisee | LegalEntity | Franchisee | No | Franchisee | LegalEntities | Restrict |
| LifecycleStatusReasonHasStatus | LifecycleStatusReason | LifecycleStatus | Yes | LifecycleStatus | Reasons | Restrict |
| OrganizationUnitHasBrand | OrganizationUnit | Brand | No | Brand | OrganizationUnits | Restrict |
| OrganizationUnitHasParent | OrganizationUnit | OrganizationUnit | No | ParentUnit | ChildUnits | Restrict |
| RestaurantContactPointHasRestaurant | RestaurantContactPoint | Restaurant | Yes | Restaurant | ContactPoints | Cascade |
| RestaurantHasBrand | Restaurant | Brand | No | Brand | Restaurants | Restrict |
| RestaurantHasBuildingType | Restaurant | BuildingType | No | BuildingType | Restaurants | Restrict |
| RestaurantHasCountry | Restaurant | Country | No | Country | Restaurants | Restrict |
| RestaurantHasLifecycleStatus | Restaurant | LifecycleStatus | No | LifecycleStatus | Restaurants | Restrict |
| RestaurantHasLocationType | Restaurant | LocationType | No | LocationType | Restaurants | Restrict |
| RestaurantHasStateProvince | Restaurant | StateProvince | No | StateProvince | Restaurants | Restrict |
| RestaurantHasStatusReason | Restaurant | LifecycleStatusReason | No | LifecycleStatusReason | Restaurants | Restrict |
| RestaurantHoursHasRestaurant | RestaurantHours | Restaurant | Yes | Restaurant | Hours | Cascade |
| RestaurantIdentifierHasIdentifierType | RestaurantIdentifier | IdentifierType | Yes | IdentifierType | RestaurantIdentifiers | Restrict |
| RestaurantIdentifierHasRestaurant | RestaurantIdentifier | Restaurant | Yes | Restaurant | Identifiers | Cascade |
| RestaurantIdentifierHasSourceSystem | RestaurantIdentifier | SourceSystem | Yes | SourceSystem | RestaurantIdentifiers | Restrict |
| RestaurantLocalizedNameHasRestaurant | RestaurantLocalizedName | Restaurant | Yes | Restaurant | LocalizedNames | Cascade |
| RestaurantOperatorHasLegalEntity | RestaurantOperator | LegalEntity | Yes | LegalEntity | OperatedRestaurants | Restrict |
| RestaurantOperatorHasRestaurant | RestaurantOperator | Restaurant | Yes | Restaurant | Operators | Cascade |
| RestaurantOrgAssignmentHasRestaurant | RestaurantOrgAssignment | Restaurant | Yes | Restaurant | OrgAssignments | Cascade |
| RestaurantOrgAssignmentHasUnit | RestaurantOrgAssignment | OrganizationUnit | Yes | OrganizationUnit | RestaurantAssignments | Restrict |
| RestaurantRelocatedFrom | Restaurant | Restaurant | No | RelocatedFrom | RelocationSuccessors | Restrict |
| RestaurantServiceHasDeliveryPartner | RestaurantService | SourceSystem | No | DeliveryPartner | DeliveryServices | Restrict |
| RestaurantServiceHasRestaurant | RestaurantService | Restaurant | Yes | Restaurant | Services | Cascade |
| RestaurantServiceHasServiceType | RestaurantService | ServiceType | Yes | ServiceType | RestaurantServices | Restrict |
| RestaurantStatusHistoryHasReason | RestaurantStatusHistory | LifecycleStatusReason | No | LifecycleStatusReason | StatusHistoryRows | Restrict |
| RestaurantStatusHistoryHasRestaurant | RestaurantStatusHistory | Restaurant | Yes | Restaurant | StatusHistory | Cascade |
| RestaurantStatusHistoryHasStatus | RestaurantStatusHistory | LifecycleStatus | Yes | LifecycleStatus | StatusHistoryRows | Restrict |
| StateProvinceHasCountry | StateProvince | Country | Yes | Country | StatesProvinces | Restrict |

## Attributes per entity

*Used in matching*: the two ID-matched entities consolidate on their primary key only (no fuzzy matcher). Reference fields to other entities are listed in the relationships table above, not repeated here.

### Hub

#### Restaurant (`Restaurant`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantID | Restaurant ID | String (20) | Yes (primary key) | Common restaurant ID: 'R' followed by 7 digits, issued by Real Estate when the site enters the pipeline and stored by every system. | Yes (ID match) |
| RestaurantName | Restaurant name | String (256) | No | Public name of the restaurant. | No |
| SiteID | Site ID | String (64) | No | Site identifier of the Real Estate system, assigned at lease signing; empty for early pipeline sites. Never a matching key. | No |
| StatusEffectiveDate | Status effective date | Date | No | Date the current lifecycle status took effect. | No |
| LeaseSignedDate | Lease signed date | Date | No | Date the lease was signed. | No |
| LeaseExpirationDate | Lease expiration date | Date | No | End of the current lease term. | No |
| ConstructionStartDate | Construction start date | Date | No | Start of construction works. | No |
| PlannedOpenDate | Planned open date | Date | No | Target opening date of a pipeline restaurant. | No |
| OriginalOpenDate | Original open date | Date | No | Date the restaurant first opened. | No |
| TemporaryClosureDate | Temporary closure date | Date | No | Start of the current temporary closure. | No |
| PlannedReopenDate | Planned reopen date | Date | No | Expected reopening after a temporary closure; published to maps and delivery apps. | No |
| PermanentClosureDate | Permanent closure date | Date | No | Date the restaurant closed for good. | No |
| AddressLine1 | Address line 1 | String (256) | No | Street address of the site. | No |
| AddressLine2 | Address line 2 | String (256) | No | Suite, unit or mall location. | No |
| City | City | String (128) | No | City of the site. | No |
| PostalCode | Postal code | String (10) | No | US ZIP or ZIP+4, or Canadian postal code (A1A 1A1). | No |
| County | County | String (128) | No | County of the site (US tax and licensing). | No |
| Latitude | Latitude | Decimal (9,6) | No | Latitude in decimal degrees (WGS 84). | No |
| Longitude | Longitude | Decimal (9,6) | No | Longitude in decimal degrees (WGS 84). | No |
| CoordinateSource | Coordinate source | List of values (Coordinate source) | No | How the coordinates were obtained. | No |
| TimeZone | Time zone | List of values (Time zone) | No | Time zone of the site; defaulted from the state or province when empty, set by a steward in states spanning two zones. | No |
| MainPhone | Main phone | String (20) | No | Public phone number, normalized as +1 and 10 digits. | No |
| SquareFootage | Square footage | Integer | No | Building area in square feet. | No |
| SeatingCapacity | Seating capacity | Integer | No | Number of dining-room seats. | No |
| DriveThruLaneCount | Drive-thru lanes | Integer | No | Number of drive-thru lanes; 0 when the restaurant has none. | No |
| ProjectNumber | Project number | String (64) | No | Real Estate or construction project number. | No |
| CostCenterCode | Cost center | String (64) | No | ERP cost center of the restaurant. | No |
| PublicChannelStatus | Public channel status | List of values (Public channel status) | No | What public channels must show, derived from the lifecycle status after each change. | No |
| InRealEstate | Known to Real Estate | List of values (Yes / No) | No | Yes when Real Estate has published this restaurant (computed). | No |
| InERP | Known to ERP | List of values (Yes / No) | No | Yes when ERP has published this restaurant (computed). | No |
| InPOS | Known to POS | List of values (Yes / No) | No | Yes when a POS system has published this restaurant (computed). | No |
| DuplicateCheckKey | Duplicate check key | String (400) | No | Brand, normalized street address and postal code; two restaurants with the same key are flagged as possible duplicates (typically a mistyped restaurant ID in one system). | No |
| SiteCheckKey | Site check key | String (80) | No | The Site ID, or a unique placeholder when the restaurant has none; enforces one restaurant per site. | No |

### Restaurant details (children of Restaurant)

#### Opening hours (`RestaurantHours`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantHoursID | Key | String (100) | Yes (primary key) | Key of the row, sent by the publishing system or typed by the steward: the restaurant ID, a dash, then the row's own business key in its source (for example R0000123-POS-4471). | No |
| ServiceChannel | Channel | List of values (Service channel) | Yes | Channel the hours apply to. | No |
| HoursType | Hours type | List of values (Hours type) | Yes | Regular weekly hours or special hours for one date. | No |
| DayOfWeek | Day of week | List of values (Day of week) | No | Day, for regular hours. | No |
| SpecialDate | Date | Date | No | Date, for special hours. | No |
| Occasion | Occasion | String (128) | No | Holiday or event the special hours are for. | No |
| OpenTime | Opens at | String (5) | No | Opening time, HH:MM on a 24-hour clock. | No |
| CloseTime | Closes at | String (5) | No | Closing time, HH:MM on a 24-hour clock. | No |
| ClosesNextDay | Closes next day | List of values (Yes / No) | No | Yes when the closing time falls on the following day (late-night hours). | No |
| Closed | Closed | List of values (Yes / No) | No | Yes when the channel is closed all day. | No |
| Open24Hours | Open 24 hours | List of values (Yes / No) | No | Yes when the channel is open round the clock. | No |
| EffectiveFrom | Effective from | Date | Yes | First day these hours apply. | No |
| EffectiveTo | Effective to | Date | No | Last day these hours apply; empty when open-ended. | No |
| HoursSlotKey | Slot key | String (160) | No | Channel, hours type, day or date and start date, without empty parts; enforces one row per slot. | No |

#### Service (`RestaurantService`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantServiceID | Key | String (100) | Yes (primary key) | Key of the row, sent by the publishing system or typed by the steward: the restaurant ID, a dash, then the row's own business key in its source (for example R0000123-POS-4471). | No |
| Available | Available | List of values (Yes / No) | Yes | Currently offered (No when temporarily unavailable, for example a drive-thru under repair). | No |
| EffectiveFrom | Effective from | Date | Yes | First day the service is offered. | No |
| EffectiveTo | Effective to | Date | No | Last day the service is offered; empty when open-ended. | No |

#### Contact point (`RestaurantContactPoint`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantContactPointID | Key | String (100) | Yes (primary key) | Key of the row, sent by the publishing system or typed by the steward: the restaurant ID, a dash, then the row's own business key in its source (for example R0000123-POS-4471). | No |
| ContactPointType | Type | List of values (Contact point type) | Yes | Kind of contact point. | No |
| Audience | Audience | List of values (Audience) | Yes | Public or internal. | No |
| ContactValue | Value | String (512) | Yes | Number, address or link. | No |
| Extension | Extension | String (16) | No | Phone extension. | No |

#### Localized name (`RestaurantLocalizedName`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantLocalizedNameID | Key | String (100) | Yes (primary key) | Key of the row, sent by the publishing system or typed by the steward: the restaurant ID, a dash, then the row's own business key in its source (for example R0000123-POS-4471). | No |
| Language | Language | List of values (Language) | Yes | Language of the name. | No |
| LocalizedName | Localized name | String (256) | Yes | Public name in that language. | No |
| NaturalKey | Natural key | String (300) | No | Business key of the row, built from its restaurant and its distinguishing fields; enforces uniqueness. | No |

#### Status history (`RestaurantStatusHistory`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantStatusHistoryID | Key | String (100) | Yes (primary key) | Key of the row, sent by the publishing system or typed by the steward: the restaurant ID, a dash, then the row's own business key in its source (for example R0000123-POS-4471). | No |
| StartDate | Start date | Date | Yes | Day the status starts; it ends the day the next status of the restaurant starts. | No |
| StatusComment | Comment | String (1000) | No | Why the status changed. | No |
| NaturalKey | Natural key | String (300) | No | Business key of the row, built from its restaurant and its distinguishing fields; enforces uniqueness. | No |

#### Operator (`RestaurantOperator`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantOperatorID | Key | String (100) | Yes (primary key) | Key of the row, sent by the publishing system or typed by the steward: the restaurant ID, a dash, then the row's own business key in its source (for example R0000123-POS-4471). | No |
| OwnershipType | Ownership type | List of values (Ownership type) | Yes | How the restaurant is operated. | No |
| AgreementNumber | Agreement number | String (64) | No | Franchise or license agreement; empty when company-operated. | No |
| AgreementExpirationDate | Agreement expiration date | Date | No | End of the agreement term (renewal planning). | No |
| EffectiveFrom | Effective from | Date | Yes | Day this operator takes over; it stays current until the next operator starts. | No |
| NaturalKey | Natural key | String (300) | No | Business key of the row, built from its restaurant and its distinguishing fields; enforces uniqueness. | No |

#### Organization assignment (`RestaurantOrgAssignment`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantOrgAssignmentID | Key | String (100) | Yes (primary key) | Key of the row, sent by the publishing system or typed by the steward: the restaurant ID, a dash, then the row's own business key in its source (for example R0000123-POS-4471). | No |
| HierarchyType | Hierarchy | List of values (Organization hierarchy) | Yes | Hierarchy the assignment belongs to. | No |
| EffectiveFrom | Effective from | Date | Yes | Day the assignment starts; it ends when the next assignment in the same hierarchy starts. | No |
| NaturalKey | Natural key | String (300) | No | Business key of the row, built from its restaurant and its distinguishing fields; enforces uniqueness. | No |

#### Restaurant identifier (`RestaurantIdentifier`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RestaurantIdentifierID | Key | String (100) | Yes (primary key) | Key of the row, sent by the publishing system or typed by the steward: the restaurant ID, a dash, then the row's own business key in its source (for example R0000123-POS-4471). | No |
| IdentifierValue | Identifier value | String (128) | Yes | The identifier as the system knows it. | No |
| ValidFrom | Valid from | Date | Yes | First day the identifier designates this restaurant. | No |
| ValidTo | Valid to | Date | No | Last day the identifier designates this restaurant; empty while in use. | No |
| NaturalKey | Natural key | String (300) | No | Business key of the row, built from its restaurant and its distinguishing fields; enforces uniqueness. | No |

### Operators

#### Franchisee (`Franchisee`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| FranchiseeNumber | Franchisee number | String (20) | Yes (primary key) | Number of the franchisee group. | No |
| FranchiseeName | Franchisee name | String (256) | Yes | Name of the franchisee group. | No |
| FranchiseeStatus | Status | List of values (Active status) | Yes | Whether the franchisee is active. | No |
| PrincipalName | Principal | String (256) | No | [PII] The person with operational control of the group. | No |
| PrincipalEmail | Principal email | String (256) | No | [PII] Business email of the principal. | No |

#### Legal entity (`LegalEntity`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LegalEntityKey | Legal entity key | String (12) | Yes (primary key) | Country and tax identifier: US- followed by the 9-digit EIN, or CA- followed by the 9-digit Business Number. | Yes (ID match) |
| LegalName | Legal name | String (256) | Yes | Registered name. | No |
| DoingBusinessAs | Doing business as | String (256) | No | Trade name, when different. | No |
| LegalEntityType | Type | List of values (Legal entity type) | Yes | Franchisee company or Copperline company. | No |
| BillingAccountNumber | Billing account | String (64) | No | ERP customer account used for royalty billing. | No |
| BillingAddressLine1 | Billing address line 1 | String (256) | No | Billing street address. | No |
| BillingAddressLine2 | Billing address line 2 | String (256) | No | Billing suite or unit. | No |
| BillingCity | Billing city | String (128) | No | Billing city. | No |
| BillingPostalCode | Billing postal code | String (10) | No | Billing ZIP or postal code. | No |
| LegalEntityStatus | Status | List of values (Active status) | No | Whether the company is active. | No |

### Organization

#### Organization unit (`OrganizationUnit`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| UnitCode | Unit code | String (64) | Yes (primary key) | Code of the unit. | No |
| UnitName | Unit name | String (256) | Yes | Name of the unit. | No |
| HierarchyType | Hierarchy | List of values (Organization hierarchy) | Yes | Hierarchy the unit belongs to. | No |
| UnitLevel | Level | List of values (Organization level) | Yes | Level of the unit. | No |
| ManagerName | Manager | String (256) | No | [PII] Person responsible for the unit. | No |

### Reference data

#### Country (`Country`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CountryCode | Country code | String (2) | Yes (primary key) | ISO 3166-1 alpha-2 code. | No |
| CountryName | Country name | String (256) | Yes | Name of the country. | No |

#### State or province (`StateProvince`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| StateCode | State code | String (6) | Yes (primary key) | ISO 3166-2 code (for example US-TX, CA-QC). | No |
| StateName | State name | String (256) | Yes | Name of the state or province. | No |
| DefaultTimeZone | Default time zone | List of values (Time zone) | No | Time zone of most of the state; the default for restaurants located there. | No |

#### Brand (`Brand`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| BrandCode | Brand code | String (64) | Yes (primary key) | Code of the brand. | No |
| BrandName | Brand name | String (256) | Yes | Name of the brand. | No |

#### Lifecycle status (`LifecycleStatus`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| StatusCode | Status code | String (64) | Yes (primary key) | Code of the status. | No |
| StatusName | Status name | String (256) | Yes | Name of the status. | No |
| PublicChannelStatus | Public channel status | List of values (Public channel status) | Yes | What public channels show for a restaurant in this status. | No |
| Sequence | Sequence | Integer | Yes | Order of the status in the lifecycle. | No |

#### Status reason (`LifecycleStatusReason`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ReasonCode | Reason code | String (64) | Yes (primary key) | Code of the reason, unique across statuses. | No |
| ReasonName | Reason name | String (256) | Yes | Name of the reason. | No |

#### Identifier type (`IdentifierType`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| IdentifierTypeCode | Type code | String (64) | Yes (primary key) | Code of the identifier type. | No |
| IdentifierTypeName | Type name | String (256) | Yes | Name of the identifier type. | No |

#### Source system (`SourceSystem`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SourceSystemCode | System code | String (64) | Yes (primary key) | Code of the system. | No |
| SourceSystemName | System name | String (256) | Yes | Name of the system. | No |
| SystemRole | Role | List of values (System role) | Yes | Role of the system towards the hub. | No |

#### Service type (`ServiceType`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ServiceTypeCode | Service code | String (64) | Yes (primary key) | Code of the service. | No |
| ServiceTypeName | Service name | String (256) | Yes | Name of the service. | No |

#### Building type (`BuildingType`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| BuildingTypeCode | Building type code | String (64) | Yes (primary key) | Code of the format. | No |
| BuildingTypeName | Building type name | String (256) | Yes | Name of the format. | No |

#### Location type (`LocationType`)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LocationTypeCode | Location type code | String (64) | Yes (primary key) | Code of the venue. | No |
| LocationTypeName | Location type name | String (256) | Yes | Name of the venue. | No |

## Lists of values

| List | Values (code: label) |
|---|---|
| Active status (`ActiveStatus`) | `ACTIVE`: Active, `INACTIVE`: Inactive |
| Audience (`Audience`) | `PUBLIC`: Public, `INTERNAL`: Internal |
| Contact point type (`ContactPointType`) | `PHONE`: Phone, `FAX`: Fax, `EMAIL`: Email, `WEBSITE`: Website, `ORDERING`: Online ordering, `SOCIAL`: Social media |
| Coordinate source (`CoordinateSource`) | `SURVEYED`: Surveyed, `GEOCODED`: Geocoded, `MANUAL`: Entered by hand |
| Day of week (`DayOfWeek`) | `MON`: Monday, `TUE`: Tuesday, `WED`: Wednesday, `THU`: Thursday, `FRI`: Friday, `SAT`: Saturday, `SUN`: Sunday |
| Hours type (`HoursType`) | `REGULAR`: Regular, `SPECIAL`: Special |
| Language (`Language`) | `EN`: English, `FR`: French |
| Legal entity type (`LegalEntityType`) | `FRANCHISEE`: Franchisee company, `CORPORATE`: Copperline company |
| Organization hierarchy (`OrganizationHierarchy`) | `FINANCE`: Finance, `OPERATIONS`: Operations, `MARKETING`: Marketing |
| Organization level (`OrganizationLevel`) | `REGION`: Region, `AREA`: Area, `DISTRICT`: District, `MARKET`: Market |
| Ownership type (`OwnershipType`) | `FRANCHISED`: Franchised, `COMPANY_OPERATED`: Company-operated, `JOINT_VENTURE`: Joint venture, `LICENSED`: Licensed |
| Public channel status (`PublicChannelStatus`) | `LISTED_OPEN`: Listed open, `LISTED_TEMP_CLOSED`: Listed temporarily closed, `NOT_LISTED`: Not listed |
| Service channel (`ServiceChannel`) | `LOBBY`: Lobby, `DRIVE_THRU`: Drive-thru, `DELIVERY`: Delivery, `PICKUP`: Pickup |
| System role (`SystemRole`) | `PUBLISHER`: Publisher, `CONSUMER`: Consumer, `DELIVERY_PARTNER`: Delivery partner |
| Time zone (`TimeZone`) | `America/New_York`: Eastern (New York), `America/Toronto`: Eastern (Toronto), `America/Chicago`: Central (Chicago), `America/Winnipeg`: Central (Winnipeg), `America/Denver`: Mountain (Denver), `America/Edmonton`: Mountain (Edmonton), `America/Phoenix`: Mountain, no daylight saving (Phoenix), `America/Los_Angeles`: Pacific (Los Angeles), `America/Vancouver`: Pacific (Vancouver), `America/Anchorage`: Alaska, `Pacific/Honolulu`: Hawaii, `America/Halifax`: Atlantic (Halifax), `America/St_Johns`: Newfoundland |
| Yes / No (`YesNoFlag`) | `Y`: Yes, `N`: No |
