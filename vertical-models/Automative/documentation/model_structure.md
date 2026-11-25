# Manufacturing and Automotive Accelerator - Model Structure

This page documents the Manufacturing model entities and their attributes. The summary table gives a quick overview, and the detailed sections list attribute metadata as configured in the accelerator.

Notes:
- Entity names, labels, descriptions, and documentation are taken from the model configuration.
- The model supports two delivered applications: `Manufacturing` and `Automotive`.
- `Used in matching` is inferred from SemQL matcher expressions in each entity file.

Related pages:
- [user guide](./user_guide.md)
- [enrichers](./enrichers.md)
- [validations](./validations.md)

## Model Diagrams

- [Manufacturing Sub-model](../src/Manufacturing/model_diagrams/Manufacturing.ModelDiagram.seml)
- [Automotive Sub-model](../src/Manufacturing/model_diagrams/Automotive.ModelDiagram.seml)
- [Automotive Reference Data Sub-model](../src/Manufacturing/model_diagrams/AutommotiveReferenceData.ModelDiagram.seml)
- [Customer Sub-model](../src/Manufacturing/model_diagrams/Customer.ModelDiagram.seml)
- [Address Sub-model](../src/Manufacturing/model_diagrams/Address.ModelDiagram.seml)

Below is a summary table of all entities in the Manufacturing model, grouped by sub-model and linked to their detailed sections.

| Sub-model | Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|---|---|---|---|---|---|---|
| Address and Contact | [Address](#address) | Address | Mastered physical address records with source input fields, geocoded components, and household grouping support. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Customer, ManufacturerAddress, ManufacturingPlantAddress, ProductDealer, SupplierAddress, SupplierManufacturerPlant | AddressCountry, AddressState | 13 |
| Address and Contact | [AddressCountry](#addresscountry) | Country | Countries reference table | Address, AddressState | (none) | 5 |
| Address and Contact | [AddressState](#addressstate) | State | State or province reference data used to validate and standardize address records. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Address | AddressCountry | 3 |
| Address and Contact | [AddressType](#addresstype) | Address Type | Type of Address- Bill To, Ship From, Pay To etc. | ManufacturerAddress, ManufacturingPlantAddress, SupplierAddress | (none) | 2 |
| Address and Contact | [Contact](#contact) | Contact | Contacts of various mnaufactuirng plant, suppliers etc. | (none) | Manufacturer, ManufacturingPlant, Supplier | 6 |
| Customer and Ownership | [Customer](#customer) | Customer | Retail customer master record used to consolidate ownership, household, contact, address, and service-history information. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | CustomerServiceAppointment, CustomerVehicle | Address | 30 |
| Customer and Ownership | [CustomerServiceAppointment](#customerserviceappointment) | Customer Service Appointment | Service appointment history linking customers, vehicles, dealers, and services performed after purchase. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Customer, ProductDealerService, ProductVehicle | 2 |
| Customer and Ownership | [CustomerVehicle](#customervehicle) | Customer Vehicle | Ownership and sales relationship between a customer and a vehicle, including purchase and sale dates. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Customer, ProductVehicle | 3 |
| Customer and Ownership | [Nickname](#nickname) | Nickname | Reference data mapping given names to common nicknames for customer matching and household analysis. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | (none) | 3 |
| Item Hub and BOM | [Item](#item) | Item | Product, part, raw material, semi-finished good, or finished assembly managed across sourcing and manufacturing processes. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ItemBillOfMaterial, ItemProductTrim, ItemSpecificAttribute, ItemUnavailability, Item_ItemImageJoin, SupplierManufacturerPlant | ItemCondition, ItemFamily, ItemSubFamily, ItemType | 7 |
| Item Hub and BOM | [ItemAttribute](#itemattribute) | Item Attribute | Defines configurable item attributes used to capture product characteristics and completeness requirements. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ItemAttributeSubFamily, ItemAttributeValue, ItemSpecificAttribute | (none) | 4 |
| Item Hub and BOM | [ItemAttributeSubFamily](#itemattributesubfamily) | Item Attribute Sub Family | Associates item attributes with item subfamilies so relevant attributes can be applied by product category. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | ItemAttribute, ItemSubFamily | 1 |
| Item Hub and BOM | [ItemAttributeValue](#itemattributevalue) | Item Attribute Value | Allowed value for a constrained item attribute used during item classification and specification. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ItemSpecificAttribute | ItemAttribute | 2 |
| Item Hub and BOM | [ItemBillOfMaterial](#itembillofmaterial) | Item Bill Of Material | Bill of material relationship that links parent items to child components with effective dates and relationship type. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Item | 5 |
| Item Hub and BOM | [ItemCondition](#itemcondition) | Item Condition | An Item is New or Remanufactured | Item | (none) | 2 |
| Item Hub and BOM | [ItemFamily](#itemfamily) | Item Family | High-level item family classification used to organize products, parts, and materials. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Item, ItemSubFamily | (none) | 1 |
| Item Hub and BOM | [ItemImage](#itemimage) | Item Image | Image metadata used to associate visual references with product and item records. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Item_ItemImageJoin | (none) | 3 |
| Item Hub and BOM | [ItemProductTrim](#itemproducttrim) | Item Product Trim | Associates an item with the vehicle trims that use it, supporting product impact and recall analysis. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Item, ProductTrim | 3 |
| Item Hub and BOM | [ItemSpecificAttribute](#itemspecificattribute) | Item Specific Attribute | Captures the actual attribute values assigned to an item, including constrained and unconstrained values. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Item, ItemAttribute, ItemAttributeValue | 2 |
| Item Hub and BOM | [ItemSubFamily](#itemsubfamily) | Item Sub Family | Lower-level item classification within an item family, used to refine product and part grouping. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Item, ItemAttributeSubFamily, ItemSubFamily | ItemFamily, ItemSubFamily | 2 |
| Item Hub and BOM | [ItemType](#itemtype) | Item Type | To define if an item is Raw Material, Finished or Semi-Finished item Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Item | (none) | 2 |
| Item Hub and BOM | [ItemUnavailability](#itemunavailability) | Item Unavailability | Records item unavailability periods and substitute items used for replacement or recall scenarios. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Item | 3 |
| Item Hub and BOM | [Item_ItemImageJoin](#item-itemimagejoin) | Item Image Join | Associates item records with one or more item images for product visualization and stewardship. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Item, ItemImage | 1 |
| Supplier, Manufacturer, and Plant | [Manufacturer](#manufacturer) | Manufacturer | Manufacturer master record used to manage automotive brands, ownership context, and related manufacturing plants. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Contact, ManufacturerAddress, ManufacturingPlant, SupplierManufacturerPlant | (none) | 5 |
| Supplier, Manufacturer, and Plant | [ManufacturerAddress](#manufactureraddress) | Manufacturer Address | Relationship between a manufacturer and an address with effective dates for location history. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Address, AddressType, Manufacturer | 3 |
| Supplier, Manufacturer, and Plant | [ManufacturingPlant](#manufacturingplant) | Manufacturing Plant | Contains details about Location of Manufacturing plants | Contact, ManufacturingPlantAddress, ManufacturingPlantWorkShift, SupplierManufacturerPlant | Manufacturer, ManufacturingPlantType | 7 |
| Supplier, Manufacturer, and Plant | [ManufacturingPlantAddress](#manufacturingplantaddress) | Manufacturing Plant Address | Relationship between a manufacturing plant and an address with effective dates for plant location history. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Address, AddressType, ManufacturingPlant | 3 |
| Supplier, Manufacturer, and Plant | [ManufacturingPlantType](#manufacturingplanttype) | Manufacturing Plant Type | Passenger vehicle, Assembly or Powertrain plant | ManufacturingPlant | (none) | 2 |
| Supplier, Manufacturer, and Plant | [ManufacturingPlantWorkShift](#manufacturingplantworkshift) | Manufacturing Plant Work Shift | Defines work-shift windows and operating patterns for manufacturing plants. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | ManufacturingPlant | 4 |
| Supplier, Manufacturer, and Plant | [PaymentTerm](#paymentterm) | Payment Term | Reference data defining supplier payment terms used in procurement and supplier management. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Supplier | (none) | 2 |
| Supplier, Manufacturer, and Plant | [Supplier](#supplier) | Supplier | Supplier master record used to manage procurement relationships, supplier hierarchy, addresses, and supplied items. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | Contact, Supplier, SupplierAddress, SupplierManufacturerPlant | PaymentTerm, Supplier | 8 |
| Supplier, Manufacturer, and Plant | [SupplierAddress](#supplieraddress) | Supplier Address | Relationship between a supplier and an address with effective dates for shipping, billing, or headquarters usage. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Address, AddressType, Supplier | 3 |
| Supplier, Manufacturer, and Plant | [SupplierManufacturerPlant](#suppliermanufacturerplant) | Supplier Manufacturer Plant | Associates suppliers with manufacturers, plants, supplied items, and addresses used in manufacturing operations. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | Address, Item, Manufacturer, ManufacturingPlant, Supplier | 1 |
| Automotive Catalog and Vehicles | [ProductMake](#productmake) | Make | Automotive make reference data representing vehicle brands in the make-model-trim hierarchy. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductDealerMake, ProductModel, ProductVehicle | (none) | 3 |
| Automotive Catalog and Vehicles | [ProductModel](#productmodel) | Model | Automotive model reference data associated with a make and model year. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductTrim, ProductVehicle | ProductMake, ProductModelYear | 2 |
| Automotive Catalog and Vehicles | [ProductModelYear](#productmodelyear) | Model Year | Automotive model-year reference data used in product and vehicle classification. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductModel, ProductVehicle | (none) | 2 |
| Automotive Catalog and Vehicles | [ProductTrim](#producttrim) | Trim | Vehicle trim level in the ACES-style make-model-trim hierarchy, including pricing, performance, and features. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ItemProductTrim, ProductTrimOptionOrFeature, ProductVehicle | ProductBodySize, ProductBodyStyle, ProductCylinders, ProductDriveTrain, ProductEngineAspiration, ProductModel, ProductTransmission | 9 |
| Automotive Catalog and Vehicles | [ProductVehicle](#productvehicle) | Vehicle | Individual vehicle master record identified by VIN and linked to make, model, trim, dealer, and ownership history. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | CustomerServiceAppointment, CustomerVehicle, ProductVehicleOptionOrFeature | ProductDealer, ProductMake, ProductModel, ProductModelYear, ProductTrim | 2 |
| Dealer and Service | [ProductDealer](#productdealer) | Dealer | Dealer master record used to manage retail locations, contact channels, services, makes sold, and vehicles sold. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductDealerMake, ProductDealerService, ProductVehicle | Address | 12 |
| Dealer and Service | [ProductDealerMake](#productdealermake) | Product Dealer Make | Associates a dealer with the vehicle makes it sells during a defined effective period. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | ProductDealer, ProductMake | 3 |
| Dealer and Service | [ProductDealerService](#productdealerservice) | Dealer Service | Associates a dealer with services offered to customers and vehicles. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | CustomerServiceAppointment | ProductDealer, ProductService | 1 |
| Dealer and Service | [ProductService](#productservice) | Service | Automotive service reference data used for dealer service offerings and customer appointment history. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductDealerService | ProductServiceType | 2 |
| Dealer and Service | [ProductServiceType](#productservicetype) | Product Service Type | Reference data classifying automotive services by type. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductService | (none) | 1 |
| Automotive Reference and Options | [ProductBodySize](#productbodysize) | Body Size | Automotive reference data describing vehicle body size classifications. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductTrim | (none) | 2 |
| Automotive Reference and Options | [ProductBodyStyle](#productbodystyle) | Body Style | Automotive reference data describing vehicle body style classifications. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductTrim | (none) | 2 |
| Automotive Reference and Options | [ProductCylinders](#productcylinders) | Cylinders | Automotive reference data describing engine cylinder configurations. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductTrim | (none) | 2 |
| Automotive Reference and Options | [ProductDriveTrain](#productdrivetrain) | Drive Train | Automotive reference data describing drivetrain configurations. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductTrim | (none) | 2 |
| Automotive Reference and Options | [ProductEngineAspiration](#productengineaspiration) | Engine Aspiration | Automotive reference data describing engine aspiration configurations. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductTrim | (none) | 2 |
| Automotive Reference and Options | [ProductOptionCategory](#productoptioncategory) | Product Option Category | Reference data grouping automotive options and features by business category. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductOptionOrFeature | (none) | 1 |
| Automotive Reference and Options | [ProductOptionOrFeature](#productoptionorfeature) | Option Or Feature | Configurable vehicle option or feature that can be attached to trims and sold vehicles. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductOptionOrFeatureRelationship, ProductOptionOrFeatureValue, ProductTrimOptionOrFeature | ProductOptionCategory, ProductOrOptionGroup | 6 |
| Automotive Reference and Options | [ProductOptionOrFeatureRelationship](#productoptionorfeaturerelationship) | Product Option Or Feature Relationship | Relationship between parent and child options or features used to model dependencies and exclusions. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | ProductOptionOrFeature, ProductOptionOrFeatureRelationshipType | 1 |
| Automotive Reference and Options | [ProductOptionOrFeatureRelationshipType](#productoptionorfeaturerelationshiptype) | Product Option Or Feature Relationship Type | Reference data classifying option and feature relationships such as dependency, exclusion, or grouping. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductOptionOrFeatureRelationship | (none) | 1 |
| Automotive Reference and Options | [ProductOptionOrFeatureValue](#productoptionorfeaturevalue) | Product Option Or Feature Value | Allowed value for an automotive option or feature, including cost and visual information. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductVehicleOptionOrFeature | ProductOptionOrFeature | 4 |
| Automotive Reference and Options | [ProductOrOptionGroup](#productoroptiongroup) | Product Or Option Group | Reference data grouping product options and features for navigation, configuration, or reporting. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductOptionOrFeature | (none) | 1 |
| Automotive Reference and Options | [ProductTransmission](#producttransmission) | Transmission | Automotive reference data describing transmission configurations. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductTrim | (none) | 2 |
| Automotive Reference and Options | [ProductTrimOptionOrFeature](#producttrimoptionorfeature) | Trim Option Or Feature | Associates a trim with an option or feature and indicates standard or additional-cost availability. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | ProductVehicleOptionOrFeature | ProductOptionOrFeature, ProductTrim | 3 |
| Automotive Reference and Options | [ProductVehicleOptionOrFeature](#productvehicleoptionorfeature) | Vehicle Option Or Feature | Associates a sold vehicle with selected option or feature values. Use this entity to understand and govern this business object in the Manufacturing and Automotive accelerator applications. | (none) | ProductOptionOrFeatureValue, ProductTrimOptionOrFeature, ProductVehicle | 2 |

---

# Detailed Model Structure

Below are markdown tables for each entity in the model. Each table lists the attributes and their metadata.

## Address and Contact

### Address

Mastered physical address records with source input fields, geocoded components, and household grouping support.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AddressID | Address ID | LongInteger | Yes | Surrogate identifier for the Address record. | No |
| GeocodedCountry | Geocoded Country | String | No | Country returned by geocoding for the Address record. | Yes |
| Household | Household | Boolean | No | Indicates whether this address represents a household grouping location for related customers. | No |
| GeocodedPostalCode | Geocoded Postal Code | String | No | Postal code returned by geocoding for the address. | No |
| GeocodedState | Geocoded State | String | No | State returned by geocoding for the Address record. | Yes |
| GeocodedStreetName | Geocoded Street Name | String | No | Street name returned by geocoding for the Address record. | Yes |
| GeocodedStreetNumber | Geocoded Street Number | String | No | Street number returned by geocoding for the Address record. | Yes |
| InputCity | Input City | String | No | Original city value provided by the source system before enrichment. | No |
| GeocodedLongitude | Geocoded Longitude | Decimal | No | Longitude returned by geocoding for the Address record. | No |
| GeocodedLocality | Geocoded Locality | String | No | Locality returned by geocoding for the Address record. | No |
| InputZipCode | Input Zip Code | String | No | Original postal or ZIP code value provided by the source system before enrichment. | No |
| InputAddressLine | Input Address Line | String | No | Original address line value provided by the source system before enrichment. | No |
| GeocodedLattitude | Geocoded Lattitude | Decimal | No | Latitude coordinate returned by geocoding for the address. | No |

---

### AddressCountry

Country reference data used to standardize addresses, plants, suppliers, dealers, and customer locations.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CountryID | Country ID | String | Yes | Surrogate identifier for the Country record. | No |
| Alpha2Code | ISO 3166-1 2-Letter Code | String | No | This two-letter code (alpha-2) is recommended as the general-purpose code. | No |
| FlagURL | Flag URL | String | No | URL or asset reference for the country flag displayed in the application. | No |
| CountryName | Country Name | String | Yes | Name of the Country | No |
| Alpha3Cde | ISO 3166-1 3-Letter Code | String | No | This three-letter code (alpha-3) is more closely related to the country name than the two-letter code. The two-letter code is preferred in most situations. | No |

---

### AddressState

State or province reference data used to validate and standardize address records.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| StateID | State ID | String | Yes | Surrogate identifier for the State record. | No |
| Name | Name | String | No | Display name of the state or province. | No |
| Code | Code | String | No | State or province code used for address standardization. | No |

---

### AddressType

Classifies the business purpose of an address, such as headquarters, billing, shipping, or plant location.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AddressType | Address Type | String | Yes | Classification value used to categorize the Address Type record. | No |
| Description | Description | String | No | Business description for the Address Type record. | No |

---

### Contact

Contact person records associated with suppliers, manufacturers, manufacturing plants, and operational relationships.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ContactID | Contact ID | LongInteger | Yes | Surrogate identifier for the Contact record. | No |
| Picture | Picture | String | No | Image or asset used to visually represent the Contact record. | No |
| Email | Email | String | No | Email value used to contact or identify the Contact record. | Yes |
| Name | Name | String | Yes | Name of the Contact Person | Yes |
| Designation | Designation | String | No | Designation of the Contact | No |
| Number | Number | String | Yes | Contact Number of the person | Yes |

---

## Customer and Ownership

### Customer

Retail customer master record used to consolidate ownership, household, contact, address, and service-history information.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CustomerID | Customer ID | LongInteger | Yes | Surrogate identifier for the Customer record. | No |
| PhoneticLastName | Phonetic Last Name | String | No | Phonetic representation of the customer last name used for fuzzy matching. | Yes |
| GeocodedLatitude | Geocoded Latitude | Decimal | No | Latitude returned by geocoding for the Customer record. | No |
| GeocodedStreetName | Geocoded Street Name | String | No | Street name returned by geocoding for the Customer record. | Yes |
| NormalizedFirstName | Normalized First Name | String | No | Standardized first name value used for matching, validation, or stewardship. | Yes |
| InputZipCode | Input Zip Code | String | No | Original customer postal or ZIP code value provided by the source system before enrichment. | No |
| MemberID | Member ID | String | No | Customer membership or loyalty identifier used as a matching and relationship key. | Yes |
| GeocodedStreetNumber | Geocoded Street Number | String | No | Street number returned by geocoding for the Customer record. | Yes |
| LastName | Last Name | String | Yes | Customer family name as captured from the source or identity record. | Yes |
| HouseholdID | Household ID (String) | String | No | String household identifier derived from address enrichment and used for household grouping. | No |
| DateOfBirth | Date Of Birth | Date | No | Customer date of birth used for age validation and identity matching. | Yes |
| InputCity | Input City | String | No | Original city value provided by the source system before enrichment. | No |
| InputCountry | Input Country | String | No | Original country value provided by the source system before enrichment. | No |
| PhoneticFirstName | Phonetic First Name | String | No | Phonetic representation of the customer first name used for fuzzy matching. | Yes |
| ValidEmailDomain | Valid Email Domain | String | No | Email value used to contact or identify the Customer record. | No |
| InputState | Input State | String | No | Original state value provided by the source system before enrichment. | No |
| GeocodedCountry | Geocoded Country | String | No | Country returned by geocoding for the Customer record. | Yes |
| GeocodedLocality | Geocoded Locality | String | No | Locality returned by geocoding for the Customer record. | Yes |
| InputAddressLine | Input Address Line | String | No | Original address line value provided by the source system before enrichment. | No |
| PhoneGeocodingData | Phone Geocoding Data | String | No | Geographic metadata returned by phone standardization. | No |
| SourceEmail | Source Email | String | No | Email value used to contact or identify the Customer record. | No |
| GeocodedLongitude | Geocoded Longitude | Decimal | No | Longitude returned by geocoding for the Customer record. | No |
| StandardizedPhone | Standardized Phone | String | No | Phone number standardized by the phone enrichment plugin. | Yes |
| SourcePhone | Source Phone | String | No | Original phone number provided by the source system. | No |
| Nickname | Nickname | String | No | Common nickname associated with the customer given name for matching. | Yes |
| GeocodedPostalCode | Geocoded Postal Code | String | No | Postal code returned by geocoding for the customer address. | Yes |
| NormalizedLastName | Normalized Last Name | String | No | Standardized last name value used for matching, validation, or stewardship. | Yes |
| GeocodedState | Geocoded State | String | No | State returned by geocoding for the Customer record. | Yes |
| FirstName | First Name | String | No | Customer given name as captured from the source or identity record. | Yes |
| CleansedEmail | MD Personator | Manufacturing.complex_types.MelissaDataPersonatorType | No | Melissa Personator enrichment output containing validated identity, address, phone, and demographic details. | Yes |

---

### CustomerVehicle

Ownership and sales relationship between a customer and a vehicle, including purchase and sale dates.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CustomerVehicleID | Customer Vehicle ID | LongInteger | Yes | Surrogate identifier for the Customer Vehicle record. | No |
| PurchaseDate | Purchase Date | Date | No | Date when the customer purchased or took ownership of the vehicle. | No |
| SaleDate | Sale Date | Date | No | Date when the customer sold or no longer owned the vehicle. | No |

---

### CustomerServiceAppointment

Service appointment history linking customers, vehicles, dealers, and services performed after purchase.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ServiceAppointmentID | Service Appointment ID | LongInteger | Yes | Surrogate identifier for the Customer Service Appointment record. | No |
| ServiceAppointmentDate | Service Appointment Date | Date | Yes | Date when the vehicle service appointment occurred or is scheduled. | No |

---

### Nickname

Reference data mapping given names to common nicknames for customer matching and household analysis.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| GivenName | Given Name | String | Yes | Formal given name associated with one or more nicknames. | No |
| AllNicknames | All Nicknames | String | Yes | List of known nicknames associated with the given name. | No |
| TopNickname | Top Nickname | String | Yes | Most common nickname associated with the given name. | No |

---

## Item Hub and BOM

### Item

Product, part, raw material, semi-finished good, or finished assembly managed across sourcing and manufacturing processes.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemID | Item ID | LongInteger | Yes | Surrogate identifier for the Item record. | No |
| SKU | SKU | String | Yes | Stock keeping unit used to uniquely identify the item within manufacturing and sourcing processes. | No |
| OtherName | Other Name | String | No | Alternate item name used by source systems, suppliers, or business users. | No |
| LeadTime | Lead Time(Days) | Integer | No | Expected number of days required to source or procure the item. | No |
| NormalizedSKU | Normalized SKU | String | No | Normalized SKU after removing dashes from SKU | No |
| Name | Name | String | Yes | Display name of the item, part, material, or assembly. | No |
| Description | Description | String | No | Description about the item | No |

---

### Item_ItemImageJoin

Associates item records with one or more item images for product visualization and stewardship.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Item_ItemImageJoinID | Item Image Join ID | LongInteger | Yes | Surrogate identifier for the Item Image Join record. | No |

---

### ItemAttribute

Defines configurable item attributes used to capture product characteristics and completeness requirements.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Surrogate identifier for the Item Attribute record. | No |
| Mandatory | Mandatory | Boolean | No | Indicates whether the Item Attribute attribute or value is required. | No |
| Constrained | Constrained | Boolean | No | Indicates whether values are limited to predefined reference values for the Item Attribute record. | No |
| Attribute | Attribute | String | Yes | Attribute name used to capture an item characteristic. | No |

---

### ItemAttributeSubFamily

Associates item attributes with item subfamilies so relevant attributes can be applied by product category.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemAttributeSubFamilyID | Item Attribute Sub Family ID | LongInteger | Yes | Surrogate identifier for the Item Attribute Sub Family record. | No |

---

### ItemAttributeValue

Allowed value for a constrained item attribute used during item classification and specification.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemAttributeValueID | Item Attribute Value ID | LongInteger | Yes | Surrogate identifier for the Item Attribute Value record. | No |
| Value | Value | String | Yes | Business value captured for the Item Attribute Value record. | No |

---

### ItemBillOfMaterial

Bill of material relationship that links parent items to child components with effective dates and relationship type.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemBillOfMaterialID | Item Bill Of Material ID | LongInteger | Yes | Surrogate identifier for the Item Bill Of Material record. | No |
| EffectiveEndDate | Effective End Date | Date | No | Date when the Item Bill Of Material relationship or classification stops being effective. | No |
| RelationshipType | Relationship Type | Manufacturing.list_of_values.ItemBOM_RelationshipType | Yes | Classification of the bill of material relationship between parent and child items. | No |
| EffectiveStartDate | Effective Start Date | Date | No | Date when the Item Bill Of Material relationship or classification becomes effective. | No |
| Name | Name | String | No | Display name for the bill of material relationship or parent assembly. | No |

---

### ItemCondition

Reference data describing whether an item is new, remanufactured, refurbished, or otherwise classified by condition.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemCondition | Item Condition | String | Yes | Classification value used to categorize the Item Condition record. | No |
| Description | Description | String | No | Business description for the Item Condition record. | No |

---

### ItemFamily

High-level item family classification used to organize products, parts, and materials.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemFamily | Item Family | String | Yes | Classification value used to categorize the Item Family record. | No |

---

### ItemImage

Image metadata used to associate visual references with product and item records.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemImageID | Item Image ID | LongInteger | Yes | Surrogate identifier for the Item Image record. | No |
| URL | URL | String | Yes | Image URL | No |
| Label | Label | String | No | Display label for the item image. | No |

---

### ItemProductTrim

Associates an item with the vehicle trims that use it, supporting product impact and recall analysis.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemProductTrimID | Item Product Trim ID | LongInteger | Yes | Surrogate identifier for the Item Product Trim record. | No |
| StartDate | Start Date | Date | No | Date when the Item Product Trim relationship or classification becomes effective. | No |
| EndDate | End Date | Date | No | Date when the Item Product Trim relationship or classification stops being effective. | No |

---

### ItemSpecificAttribute

Captures the actual attribute values assigned to an item, including constrained and unconstrained values.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemSpecificAttributeID | Item Specific Attribute ID | LongInteger | Yes | Surrogate identifier for the Item Specific Attribute record. | No |
| UnconstrainedValue | Unconstrained Value | String | No | Free-form attribute value captured when the item attribute is not constrained to a reference value. | No |

---

### ItemSubFamily

Lower-level item classification within an item family, used to refine product and part grouping.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemSubFamilyID | Item Sub Family ID | LongInteger | Yes | Surrogate identifier for the Item Sub Family record. | No |
| SubFamily | Sub Family | String | Yes | Classification value used to categorize the Item Sub Family record. | No |

---

### ItemType

To define if an item is Raw Material, Finished or Semi-Finished item

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemType | Item Type | String | Yes | Classification value used to categorize the Item Type record. | No |
| Description | Description | String | No | Business description for the Item Type record. | No |

---

### ItemUnavailability

Records item unavailability periods and substitute items used for replacement or recall scenarios.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ItemUnavailabilityID | Item Unavailability ID | LongInteger | Yes | Surrogate identifier for the Item Unavailability record. | No |
| EndDate | End Date | Date | No | Date when the Item Unavailability relationship or classification stops being effective. | No |
| StartDate | Start Date | Date | Yes | Date when the Item Unavailability relationship or classification becomes effective. | No |

---

## Supplier, Manufacturer, and Plant

### Manufacturer

Manufacturer master record used to manage automotive brands, ownership context, and related manufacturing plants.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ManufacturerID | Manufacturer ID | LongInteger | Yes | Surrogate identifier for the Manufacturer record. | No |
| Revenue | Revenue | String | No | Reported revenue for the Manufacturer record. | No |
| Webiste | Website | String | No | Website URL for the Manufacturer record. | No |
| Code | Code | String | No | Manufacturer code used by ERP or operational source systems. | Yes |
| Name | Name | String | Yes | Display name of the manufacturer. | No |

---

### ManufacturerAddress

Relationship between a manufacturer and an address with effective dates for location history.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ManufacturerAddressID | Manufacturer Address ID | LongInteger | Yes | Surrogate identifier for the Manufacturer Address record. | No |
| EndDate | End Date | Date | No | Date when the Manufacturer Address relationship or classification stops being effective. | No |
| StartDate | Start Date | Date | No | Date when the Manufacturer Address relationship or classification becomes effective. | No |

---

### ManufacturingPlant

Manufacturing facility master record used to track ownership, operating dates, output type, and supplied or produced items.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ManufacturingPlantID | Manufacturing Plant ID | LongInteger | Yes | Surrogate identifier for the Manufacturing Plant record. | No |
| OutputProduct | Output Product | Manufacturing.list_of_values.MFGPlant_OutputProductType | No | Type of product output produced by the manufacturing plant. | No |
| IsActive | Is Active | Boolean | No | Indicates whether the plant is currently active and producing output. | No |
| OperationStartDate | Start Date | Date | No | Date when the Manufacturing Plant relationship or classification becomes effective. | No |
| PlantOwnership | Plant Ownership | Manufacturing.list_of_values.MGFPlant_PlantType | No | Ownership model for the plant, such as owned, joint venture, or subcontracted. | No |
| OperationEndDate | End Date | Date | No | Date when the Manufacturing Plant relationship or classification stops being effective. | No |
| PlantName | Plant Name | String | Yes | Name of the Manufacturing Plant | No |

---

### ManufacturingPlantAddress

Relationship between a manufacturing plant and an address with effective dates for plant location history.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ManufacturingPlantAddressID | Manufacturing Plant Address ID | LongInteger | Yes | Surrogate identifier for the Manufacturing Plant Address record. | No |
| StartDate | Start Date | Date | No | Date when the Manufacturing Plant Address relationship or classification becomes effective. | No |
| EndDate | End Date | Date | No | Date when the Manufacturing Plant Address relationship or classification stops being effective. | No |

---

### ManufacturingPlantType

Reference data classifying plant types such as assembly, passenger vehicle, powertrain, or subcontracted facilities.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PlantType | Plant Type | String | Yes | Classification value used to categorize the Manufacturing Plant Type record. | No |
| Description | Description | String | No | Business description for the Manufacturing Plant Type record. | No |

---

### ManufacturingPlantWorkShift

Defines work-shift windows and operating patterns for manufacturing plants.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Surrogate identifier for the Manufacturing Plant Work Shift record. | No |
| StartTime | Start Time | String | No | Start time of the plant work shift in 24-hour format. | No |
| Is24_7 | 24*7 | Boolean | No | Indicates if the plant operates 24*7 (true/false) | No |
| EndTime | End Time | String | No | End time of the plant work shift in 24-hour format. | No |

---

### PaymentTerm

Reference data defining supplier payment terms used in procurement and supplier management.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PaymentTerm | Payment Term | String | Yes | Classification value used to categorize the Payment Term record. | No |
| Description | Description | String | No | Business description for the Payment Term record. | No |

---

### Supplier

Supplier master record used to manage procurement relationships, supplier hierarchy, addresses, and supplied items.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SupplierID | Supplier ID | LongInteger | Yes | Surrogate identifier for the Supplier record. | No |
| Website | Website | String | No | Website URL for the Supplier record. | Yes |
| Description | Description | String | No | Business description for the Supplier record. | No |
| EmployeeRange | Employee Range | String | No | Employee-count range used to classify supplier size. | No |
| Name | Name | String | Yes | Name of the supplier | Yes |
| ARIBACode | ARIBA Code | String | No | ARIBA Code of the supplier in the internal system | Yes |
| Revenue | Revenue | LongInteger | No | Reported revenue for the supplier. | No |
| FoundedYear | Founded Year | Integer | No | Calendar year when the supplier was founded. | No |

---

### SupplierAddress

Relationship between a supplier and an address with effective dates for shipping, billing, or headquarters usage.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SupplierAddressID | Supplier Address ID | LongInteger | Yes | Surrogate identifier for the Supplier Address record. | No |
| EndDate | End Date | Date | No | Date when the Supplier Address relationship or classification stops being effective. | No |
| StartDate | Start Date | Date | No | Date when the Supplier Address relationship or classification becomes effective. | No |

---

### SupplierManufacturerPlant

Associates suppliers with manufacturers, plants, supplied items, and addresses used in manufacturing operations.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | Yes | Surrogate identifier for the Supplier Manufacturer Plant record. | No |

---

## Automotive Catalog and Vehicles

### ProductMake

Automotive make reference data representing vehicle brands in the make-model-trim hierarchy.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| MakeID | Make ID | LongInteger | Yes | Surrogate identifier for the Make record. | No |
| Icon | Icon | Binary | No | Image or asset used to visually represent the Make record. | No |
| Name | Name | String | Yes | Vehicle brand name used in the make-model-trim hierarchy. | No |

---

### ProductModel

Automotive model reference data associated with a make and model year.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ModelID | Model ID | LongInteger | Yes | Surrogate identifier for the Model record. | No |
| Model | Model | String | Yes | Vehicle model name associated with a make and model year. | No |

---

### ProductModelYear

Automotive model-year reference data used in product and vehicle classification.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ModelYearID | Model Year ID | Integer | Yes | Surrogate identifier for the Model Year record. | No |
| Description | Description | String | No | Business description for the Model Year record. | No |

---

### ProductTrim

Vehicle trim level in the ACES-style make-model-trim hierarchy, including pricing, performance, and features.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| TrimID | Trim ID | LongInteger | Yes | Surrogate identifier for the Trim record. | No |
| Image | Image | Binary | No | Image or asset used to visually represent the Trim record. | No |
| Horsepower | Horsepower | String | No | Performance specification captured for the Trim record. | No |
| MSRP | MSRP | Decimal | No | Manufacturer suggested retail price for the vehicle trim. | No |
| Description | Description | String | No | Business description for the Trim record. | No |
| Trim | Trim | String | Yes | Trim name within the make-model-trim hierarchy. | No |
| Torque | Torque | String | No | Performance specification captured for the Trim record. | No |
| InvoicePrice | Invoice Price | Decimal | No | Dealer invoice price for the vehicle trim. | No |
| HighwayFuleEconomy | Highway Fule Economy | String | No | Highway fuel economy value for the vehicle trim. | No |

---

### ProductVehicle

Individual vehicle master record identified by VIN and linked to make, model, trim, dealer, and ownership history.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| VehicleID | Vehicle ID | LongInteger | Yes | Surrogate identifier for the Vehicle record. | No |
| VIN | VIN | String | Yes | Vehicle identification number used as the primary business key for matching vehicles. | Yes |

---

## Dealer and Service

### ProductDealer

Dealer master record used to manage retail locations, contact channels, services, makes sold, and vehicles sold.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| DealerID | Dealer ID | LongInteger | Yes | Surrogate identifier for the Dealer record. | No |
| SIC2 | SIC2 | String | No | Secondary Standard Industrial Classification code for the dealer. | No |
| URL | URL | String | No | Website URL for the Dealer record. | No |
| SIC1 | SIC1 | String | No | Primary Standard Industrial Classification code for the dealer. | No |
| Name | Name | String | Yes | Display name of the dealer location or organization. | No |
| SalesPhone | Sales Phone | String | No | Phone number used for dealer sales inquiries. | No |
| NAICS1 | NAICS1 | String | No | Primary NAICS industry code for the dealer. | No |
| StoreNumber | Store Number | Integer | No | Store number assigned to the dealer location. | No |
| ServicePhone | Service Phone | String | No | Phone number used for dealer service inquiries. | No |
| Fax | Fax | String | No | Fax number used by the dealer. | No |
| GeneralPhoneNumber | General Phone Number | String | No | General phone number used to contact the dealer. | No |
| NAICS2 | NAICS2 | String | No | Secondary NAICS industry code for the dealer. | No |

---

### ProductDealerMake

Associates a dealer with the vehicle makes it sells during a defined effective period.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| DealerMakeID | Dealer Make ID | LongInteger | Yes | Surrogate identifier for the Product Dealer Make record. | No |
| StartDate | Start Date | Date | No | Date when the Product Dealer Make relationship or classification becomes effective. | No |
| EndDate | End Date | Date | No | Date when the Product Dealer Make relationship or classification stops being effective. | No |

---

### ProductDealerService

Associates a dealer with services offered to customers and vehicles.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| DealerServiceID | Dealer Service ID | LongInteger | Yes | Surrogate identifier for the Dealer Service record. | No |

---

### ProductService

Automotive service reference data used for dealer service offerings and customer appointment history.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ServiceID | Service ID | LongInteger | Yes | Surrogate identifier for the Service record. | No |
| Name | Name | String | Yes | Name of the automotive service offered or performed. | No |

---

### ProductServiceType

Reference data classifying automotive services by type.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ServiceType | Service Type | String | Yes | Classification value used to categorize the Product Service Type record. | No |

---

## Automotive Reference and Options

### ProductBodySize

Automotive reference data describing vehicle body size classifications.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| BodySizeID | Body Size ID | LongInteger | Yes | Surrogate identifier for the Body Size record. | No |
| BodySize | Body Size | String | Yes | Body size classification used to describe vehicle dimensions. | No |

---

### ProductBodyStyle

Automotive reference data describing vehicle body style classifications.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| BodyStyleID | Body Style ID | LongInteger | Yes | Surrogate identifier for the Body Style record. | No |
| BodyStyle | Body Style | String | Yes | Body style classification used to describe vehicle form factor. | No |

---

### ProductCylinders

Automotive reference data describing engine cylinder configurations.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CylindersID | Cylinders ID | LongInteger | Yes | Surrogate identifier for the Cylinders record. | No |
| Cylinders | Cylinders | String | Yes | Engine cylinder configuration used in vehicle specifications. | No |

---

### ProductDriveTrain

Automotive reference data describing drivetrain configurations.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| DriveTrainID | Drive Train ID | LongInteger | Yes | Surrogate identifier for the Drive Train record. | No |
| DriveTrain | Drive Train | String | Yes | Drivetrain configuration used in vehicle specifications. | No |

---

### ProductEngineAspiration

Automotive reference data describing engine aspiration configurations.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| EngineAspirationID | Engine Aspiration ID | LongInteger | Yes | Surrogate identifier for the Engine Aspiration record. | No |
| EngineAspiration | Engine Aspiration | String | Yes | Engine aspiration configuration used in vehicle specifications. | No |

---

### ProductOptionCategory

Reference data grouping automotive options and features by business category.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductOptionCategory | Product Option Category | String | Yes | Category used to group automotive options and features. | No |

---

### ProductOptionOrFeature

Configurable vehicle option or feature that can be attached to trims and sold vehicles.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OptionOrFeatureID | Option Or Feature ID | LongInteger | Yes | Surrogate identifier for the Option Or Feature record. | No |
| AdditionalCost | Additional Cost | Decimal | No | Additional cost associated with the Option Or Feature option or feature. | No |
| Image | Image | Binary | No | Image or asset used to visually represent the Option Or Feature record. | No |
| Description | Description | String | No | Business description for the Option Or Feature record. | No |
| Name | Name | String | Yes | Display name of the vehicle option or feature. | No |
| Contrained | Contrained | Boolean | Yes | Indicates whether values are limited to predefined reference values for the Option Or Feature record. | No |

---

### ProductOptionOrFeatureRelationship

Relationship between parent and child options or features used to model dependencies and exclusions.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductOptionOrFeatureRelationshipID | Product Option Or Feature Relationship ID | LongInteger | Yes | Surrogate identifier for the Product Option Or Feature Relationship record. | No |

---

### ProductOptionOrFeatureRelationshipType

Reference data classifying option and feature relationships such as dependency, exclusion, or grouping.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductOptionOrFeatureRelationshipType | Product Option Or Feature Relationship Type | String | Yes | Classification value used to categorize the Product Option Or Feature Relationship Type record. | No |

---

### ProductOptionOrFeatureValue

Allowed value for an automotive option or feature, including cost and visual information.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductOptionOrFeatureValueID | Product Option Or Feature Value ID | LongInteger | Yes | Surrogate identifier for the Product Option Or Feature Value record. | No |
| OptionOrFeatureValue | Option Or Feature Value | String | Yes | Business value captured for the Product Option Or Feature Value record. | No |
| Image | Image | Binary | No | Image or asset used to visually represent the Product Option Or Feature Value record. | No |
| AdditionalCost | Additional Cost | Decimal | No | Additional cost associated with the Product Option Or Feature Value option or feature. | No |

---

### ProductOrOptionGroup

Reference data grouping product options and features for navigation, configuration, or reporting.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductOrOptionGroup | Product Or Option Group | String | Yes | Group used to organize automotive products, options, or features. | No |

---

### ProductTransmission

Automotive reference data describing transmission configurations.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| TransmissionID | Transmission ID | LongInteger | Yes | Surrogate identifier for the Transmission record. | No |
| Transmission | Transmission | String | Yes | Transmission configuration used in vehicle specifications. | No |

---

### ProductTrimOptionOrFeature

Associates a trim with an option or feature and indicates standard or additional-cost availability.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| TrimOptionOrFeatureID | Trim Option Or Feature ID | LongInteger | Yes | Surrogate identifier for the Trim Option Or Feature record. | No |
| AdditionalCost | Additional Cost | Decimal | No | Additional cost associated with the Trim Option Or Feature option or feature. | No |
| Standard | Standard | Boolean | No | Indicates whether the option or feature is standard for the Trim Option Or Feature record. | No |

---

### ProductVehicleOptionOrFeature

Associates a sold vehicle with selected option or feature values.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| VehicleOptionOrFeatureID | Vehicle Option Or Feature ID | LongInteger | Yes | Surrogate identifier for the Vehicle Option Or Feature record. | No |
| OptionOrFeatureUnconstrainedValue | Option Or Feature Unconstrained Value | String | No | Indicates whether values are limited to predefined reference values for the Vehicle Option Or Feature record. | No |

---
