## SAP Product / Material 360 Model Structure

This page summarizes the SAP Product / Material 360 model entities, references, and attributes. It was generated from the compiled Semarchy model artifacts in `src/sappm360`.

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|---|---|---|---|---|---|
| Product | Product Golden Record | Trusted product golden record consolidating SAP and non-SAP product information. | Material, PlantProduct, ProductClassification, ProductCrossReference, ProductRelationship, ProductRelationship, ProductSpecification, ProductVariant, RegulatoryAttribute, SupplierProduct | Brand, LifecycleStatus, ProductHierarchy, ProductStatus, ProductType | 15 |
| Material | SAP Material | SAP material definition harmonized across ECC, S/4HANA, plants, and business units. | PlantProduct, ProductCrossReference | IndustrySector, MaterialGroup, MaterialType, ProcurementType, Product, UnitOfMeasure, ValuationClass | 13 |
| ProductHierarchy | Product Hierarchy | Enterprise product hierarchy used for category, family, and product line governance. | Product, ProductHierarchy | ProductHierarchy | 7 |
| Brand | Brand | Brand owned, manufactured, or distributed by the enterprise. | Product | (none) | 5 |
| ProductType | Product Type | Product Type reference data used by the SAP Product / Material 360 model. | Product | (none) | 5 |
| ProductStatus | Product Status | Product Status reference data used by the SAP Product / Material 360 model. | Product | (none) | 5 |
| LifecycleStatus | Lifecycle Status | Lifecycle Status reference data used by the SAP Product / Material 360 model. | Product | (none) | 5 |
| MaterialType | Material Type | Material Type reference data used by the SAP Product / Material 360 model. | Material | (none) | 5 |
| MaterialGroup | Material Group | Material Group reference data used by the SAP Product / Material 360 model. | Material | (none) | 5 |
| IndustrySector | Industry Sector | Industry Sector reference data used by the SAP Product / Material 360 model. | Material | (none) | 5 |
| ProcurementType | Procurement Type | Procurement Type reference data used by the SAP Product / Material 360 model. | Material | (none) | 5 |
| ValuationClass | Valuation Class | Valuation Class reference data used by the SAP Product / Material 360 model. | Material | (none) | 5 |
| UnitOfMeasure | Unit of Measure | Standard unit of measure and conversion definition used by SAP materials. | Material, ProductSpecification | (none) | 7 |
| Plant | Plant | SAP plant or manufacturing location participating in product planning. | PlantProduct, StorageLocation | (none) | 6 |
| StorageLocation | Storage Location | SAP storage location within a plant. | PlantProduct | Plant | 20 |
| PlantProduct | Plant Product | Plant-specific planning, storage, and manufacturing data for a product or material. | (none) | Material, Plant, Product, StorageLocation | 6 |
| Supplier | Supplier | Supplier organization participating in product sourcing and procurement. | SupplierProduct | (none) | 7 |
| SupplierProduct | Supplier Product | Supplier-specific product representation and sourcing detail. | (none) | Product, Supplier | 6 |
| ProductClassification | Product Classification | Classification assignment for extensible product taxonomies and standards. | (none) | ClassificationScheme, Product | 7 |
| ClassificationScheme | Classification Scheme | Classification Scheme reference data used by the SAP Product / Material 360 model. | ProductClassification | (none) | 5 |
| ProductSpecification | Product Specification | Technical, business, packaging, or performance specification for a product. | (none) | Product, UnitOfMeasure | 7 |
| ProductVariant | Product Variant | Configurable or regional variant of a product golden record. | (none) | Product | 8 |
| RegulatoryAttribute | Regulatory Attribute | Compliance, restriction, certification, or safety attribute for a product. | (none) | ComplianceStatus, Country, Product | 7 |
| ComplianceStatus | Compliance Status | Compliance Status reference data used by the SAP Product / Material 360 model. | RegulatoryAttribute | (none) | 5 |
| Country | Country | Country reference data used by the SAP Product / Material 360 model. | RegulatoryAttribute | (none) | 5 |
| SourceSystem | Source System | SAP or downstream system participating in product data synchronization. | ProductCrossReference | (none) | 6 |
| ProductCrossReference | Product Cross Reference | Cross-system identifier mapping between product, material, and external systems. | (none) | Material, Product, SourceSystem | 6 |
| ProductRelationship | Product Relationship | Relationship between products such as substitute, successor, accessory, or bundle component. | (none) | Product, Product, RelationshipType | 6 |
| RelationshipType | Relationship Type | Relationship Type reference data used by the SAP Product / Material 360 model. | ProductRelationship | (none) | 5 |

# Detailed Model Structure

## Product

Trusted product golden record consolidating SAP and non-SAP product information.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductGoldenID | Product Golden ID | LongInteger | Yes | System generated golden identifier for the trusted product record. | No |
| ProductID | Product ID | String | Yes | Enterprise product identifier used across SAP and downstream systems. | Yes |
| ProductName | Product Name | String | Yes | Business name for the product golden record. | No |
| ProductDescription | Product Description | String | No | Business description used by stewards to understand the product. | No |
| NormalizedProductName | Normalized Product Name | String | No | Standardized product name used for matching and search. | Yes |
| ProductFamily | Product Family | String | No | Commercial or portfolio family to which the product belongs. | Yes |
| ProductLine | Product Line | String | No | Product line used for portfolio reporting and stewardship. | No |
| GTIN | GTIN | String | No | Global Trade Item Number used to identify packaged trade items. | Yes |
| ManufacturerPartNumber | Manufacturer Part Number | String | No | Manufacturer assigned part number for the product. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the product record is effective. | No |
| EffectiveTo | Effective To | Date | No | Date through which the product record remains effective. | No |
| GlobalQualityScore | Global Quality Score | Integer | No | Overall stewardship quality score for the product. | No |
| IsHazardous | Is Hazardous | Boolean | No | Indicates whether the product is treated as hazardous. | No |
| IsProcurementRelevant | Is Procurement Relevant | Boolean | No | Indicates whether the product participates in procurement processes. | No |
| IsSellable | Is Sellable | Boolean | No | Indicates whether the product can be syndicated for sales channels. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Products Brand | Brand | Brand | RESTRICT |
| References | Products Hierarchy | ProductHierarchy | Product Hierarchy | RESTRICT |
| References | Products Lifecycle Status | LifecycleStatus | Lifecycle Status | RESTRICT |
| References | Products Status | ProductStatus | Product Status | RESTRICT |
| References | Products Type | ProductType | Product Type | RESTRICT |
| Referenced by | Classification Product | ProductClassification | Product Classification | RESTRICT |
| Referenced by | Cross Reference Product | ProductCrossReference | Product Cross Reference | RESTRICT |
| Referenced by | Materials Product | Material | Material | RESTRICT |
| Referenced by | Plant Product Product | PlantProduct | Plant Product | RESTRICT |
| Referenced by | Product Specification Product | ProductSpecification | Product Specification | RESTRICT |
| Referenced by | Regulatory Product | RegulatoryAttribute | Regulatory Attribute | RESTRICT |
| Referenced by | Relationship From Product | ProductRelationship | Product Relationship | RESTRICT |
| Referenced by | Relationship To Product | ProductRelationship | Product Relationship | RESTRICT |
| Referenced by | Supplier Product Product | SupplierProduct | Supplier Product | RESTRICT |
| Referenced by | Variant Product | ProductVariant | Product Variant | RESTRICT |

**Matching Rules**
| Rule Name | Rule Label | Score | Condition |
|---|---|---|---|
| SameGTIN | Same GTIN | 100 | Record1.GTIN is not null and Record1.GTIN = Record2.GTIN |
| SameProductID | Same Product ID | 96 | Record1.ProductID is not null and Record1.ProductID = Record2.ProductID |
| SameNameAndFamily | Same Name And Family | 88 | Record1.NormalizedProductName = Record2.NormalizedProductName and COALESCE(Record1.ProductFamily,'') = COALESCE(Record2.ProductFamily,'') |

## Material

SAP material definition harmonized across ECC, S/4HANA, plants, and business units.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| MaterialGoldenID | Material Golden ID | LongInteger | Yes | System generated golden identifier for the harmonized material. | No |
| MaterialNumber | Material Number | String | Yes | SAP material number from an ECC or S/4HANA system. | Yes |
| MaterialDescription | Material Description | String | Yes | Primary material description used by SAP users. | No |
| NormalizedMaterialDesc | Normalized Material Description | String | No | Standardized material description used for duplicate detection. | Yes |
| SAPClient | SAP Client | String | No | SAP client or tenant from which the material originated. | Yes |
| SAPPlantScope | SAP Plant Scope | String | No | Plant or regional scope where the material is maintained. | No |
| MaterialStatus | Material Status | String | No | Operational status of the SAP material. | No |
| SafetyStock | Safety Stock | Integer | No | Safety stock quantity used in planning. | No |
| ReorderPoint | Reorder Point | Integer | No | Inventory level at which replenishment should be considered. | No |
| LeadTimeDays | Lead Time Days | Integer | No | Standard replenishment or procurement lead time in days. | No |
| BatchManaged | Batch Managed | Boolean | No | Indicates whether the material requires batch management. | No |
| SerialNumberProfile | Serial Number Profile | String | No | SAP serial number profile assigned to the material. | No |
| CreatedOn | Created On | Date | No | Original creation date of the material in SAP. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Materials Base UOM | UnitOfMeasure | Base UOM | RESTRICT |
| References | Materials Industry Sector | IndustrySector | Industry Sector | RESTRICT |
| References | Materials Material Group | MaterialGroup | Material Group | RESTRICT |
| References | Materials Material Type | MaterialType | Material Type | RESTRICT |
| References | Materials Procurement Type | ProcurementType | Procurement Type | RESTRICT |
| References | Materials Product | Product | Product | RESTRICT |
| References | Materials Valuation Class | ValuationClass | Valuation Class | RESTRICT |
| Referenced by | Cross Reference Material | ProductCrossReference | Product Cross Reference | RESTRICT |
| Referenced by | Plant Product Material | PlantProduct | Plant Product | RESTRICT |

**Matching Rules**
| Rule Name | Rule Label | Score | Condition |
|---|---|---|---|
| SameMaterialAndClient | Same Material And Client | 100 | Record1.MaterialNumber = Record2.MaterialNumber and COALESCE(Record1.SAPClient,'') = COALESCE(Record2.SAPClient,'') |
| SameMaterialNumber | Same Material Number | 94 | Record1.MaterialNumber = Record2.MaterialNumber |
| SameDescriptionAndProduct | Same Description And Product | 86 | Record1.NormalizedMaterialDesc = Record2.NormalizedMaterialDesc and Record1.FID_Product = Record2.FID_Product |

## ProductHierarchy

Enterprise product hierarchy used for category, family, and product line governance.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductHierarchyID | Product Hierarchy ID | String | Yes | Unique identifier for the product hierarchy node. | No |
| HierarchyCode | Hierarchy Code | String | Yes | Code that identifies the hierarchy node. | No |
| HierarchyName | Hierarchy Name | String | Yes | Business name of the hierarchy node. | No |
| HierarchyLevel | Hierarchy Level | String | No | Level such as division, category, subcategory, family, or product line. | No |
| LevelNumber | Level Number | Integer | No | Numeric level used for hierarchy ordering. | No |
| HierarchyPath | Hierarchy Path | String | No | Readable path from the top of the product hierarchy. | No |
| Active | Active | Boolean | No | Indicates whether the hierarchy node is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Hierarchy Parent | ProductHierarchy | Parent Hierarchy | RESTRICT |
| Referenced by | Hierarchy Parent | ProductHierarchy | Product Hierarchy | RESTRICT |
| Referenced by | Products Hierarchy | Product | Product | RESTRICT |

## Brand

Brand owned, manufactured, or distributed by the enterprise.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| BrandID | Brand ID | String | Yes | Unique identifier for the brand. | No |
| BrandCode | Brand Code | String | Yes | Code that identifies the brand. | No |
| BrandName | Brand Name | String | Yes | Business name of the brand. | No |
| BrandOwner | Brand Owner | String | No | Organization or business unit that owns the brand. | No |
| Active | Active | Boolean | No | Indicates whether the brand is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Products Brand | Product | Product | RESTRICT |

## ProductType

Product Type reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductTypeID | Product Type ID | String | Yes | Unique identifier for the product type. | No |
| ProductTypeCode | Product Type Code | String | Yes | Code for the product type. | No |
| ProductTypeName | Product Type Name | String | Yes | Type used to distinguish materials, finished goods, services, and kits. | No |
| Description | Description | String | No | Description for the product type. | No |
| Active | Active | Boolean | No | Indicates whether the product type is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Products Type | Product | Product | RESTRICT |

## ProductStatus

Product Status reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductStatusID | Product Status ID | String | Yes | Unique identifier for the product status. | No |
| ProductStatusCode | Product Status Code | String | Yes | Code for the product status. | No |
| ProductStatusName | Product Status Name | String | Yes | Status used to govern product lifecycle and syndication. | No |
| Description | Description | String | No | Description for the product status. | No |
| Active | Active | Boolean | No | Indicates whether the product status is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Products Status | Product | Product | RESTRICT |

## LifecycleStatus

Lifecycle Status reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LifecycleStatusID | Lifecycle Status ID | String | Yes | Unique identifier for the lifecycle status. | No |
| LifecycleStatusCode | Lifecycle Status Code | String | Yes | Code for the lifecycle status. | No |
| LifecycleStatusName | Lifecycle Status Name | String | Yes | Lifecycle phase such as active, design, phase out, or retired. | No |
| Description | Description | String | No | Description for the lifecycle status. | No |
| Active | Active | Boolean | No | Indicates whether the lifecycle status is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Products Lifecycle Status | Product | Product | RESTRICT |

## MaterialType

Material Type reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| MaterialTypeID | Material Type ID | String | Yes | Unique identifier for the material type. | No |
| MaterialTypeCode | Material Type Code | String | Yes | Code for the material type. | No |
| MaterialTypeName | Material Type Name | String | Yes | SAP material type used for accounting and logistics behavior. | No |
| Description | Description | String | No | Description for the material type. | No |
| Active | Active | Boolean | No | Indicates whether the material type is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Materials Material Type | Material | Material | RESTRICT |

## MaterialGroup

Material Group reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| MaterialGroupID | Material Group ID | String | Yes | Unique identifier for the material group. | No |
| MaterialGroupCode | Material Group Code | String | Yes | Code for the material group. | No |
| MaterialGroupName | Material Group Name | String | Yes | Material group used for procurement and reporting. | No |
| Description | Description | String | No | Description for the material group. | No |
| Active | Active | Boolean | No | Indicates whether the material group is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Materials Material Group | Material | Material | RESTRICT |

## IndustrySector

Industry Sector reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| IndustrySectorID | Industry Sector ID | String | Yes | Unique identifier for the industry sector. | No |
| IndustrySectorCode | Industry Sector Code | String | Yes | Code for the industry sector. | No |
| IndustrySectorName | Industry Sector Name | String | Yes | SAP industry sector used to classify materials. | No |
| Description | Description | String | No | Description for the industry sector. | No |
| Active | Active | Boolean | No | Indicates whether the industry sector is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Materials Industry Sector | Material | Material | RESTRICT |

## ProcurementType

Procurement Type reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProcurementTypeID | Procurement Type ID | String | Yes | Unique identifier for the procurement type. | No |
| ProcurementTypeCode | Procurement Type Code | String | Yes | Code for the procurement type. | No |
| ProcurementTypeName | Procurement Type Name | String | Yes | Procurement type used by planning and purchasing. | No |
| Description | Description | String | No | Description for the procurement type. | No |
| Active | Active | Boolean | No | Indicates whether the procurement type is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Materials Procurement Type | Material | Material | RESTRICT |

## ValuationClass

Valuation Class reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ValuationClassID | Valuation Class ID | String | Yes | Unique identifier for the valuation class. | No |
| ValuationClassCode | Valuation Class Code | String | Yes | Code for the valuation class. | No |
| ValuationClassName | Valuation Class Name | String | Yes | SAP valuation class used for account determination. | No |
| Description | Description | String | No | Description for the valuation class. | No |
| Active | Active | Boolean | No | Indicates whether the valuation class is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Materials Valuation Class | Material | Material | RESTRICT |

## UnitOfMeasure

Standard unit of measure and conversion definition used by SAP materials.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| UnitOfMeasureID | Unit of Measure ID | String | Yes | Unique identifier for the unit of measure. | No |
| UOMCode | UOM Code | String | Yes | Standard unit of measure code. | No |
| UOMName | UOM Name | String | Yes | Business name of the unit of measure. | No |
| ISOCode | ISO Code | String | No | ISO unit code used for integration. | No |
| Dimension | Dimension | String | No | Measurement dimension such as mass, volume, or count. | No |
| ConversionNumerator | Conversion Numerator | Integer | No | Numerator used for alternate unit conversion. | No |
| ConversionDenominator | Conversion Denominator | Integer | No | Denominator used for alternate unit conversion. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Materials Base UOM | Material | Material | RESTRICT |
| Referenced by | Product Specification UOM | ProductSpecification | Product Specification | RESTRICT |

## Plant

SAP plant or manufacturing location participating in product planning.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PlantID | Plant ID | String | Yes | Unique identifier for a plant. | No |
| PlantCode | Plant Code | String | Yes | SAP plant code. | No |
| PlantName | Plant Name | String | Yes | Business name of the plant. | No |
| Region | Region | String | No | Region where the plant operates. | No |
| CountryName | Country Name | String | No | Country where the plant is located. | No |
| Active | Active | Boolean | No | Indicates whether the plant is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Plant Product Plant | PlantProduct | Plant Product | RESTRICT |
| Referenced by | Storage Location Plant | StorageLocation | Storage Location | RESTRICT |

## StorageLocation

SAP storage location within a plant.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| StorageLocationID | Storage Location ID | String | Yes | Unique identifier for a storage location. | No |
| StorageLocationCode | Storage Location Code | String | Yes | SAP storage location code. | No |
| StorageLocationName | Storage Location Name | String | Yes | Business name of the storage location. | No |
| Active | Active | Boolean | No | Indicates whether the storage location is active. | No |
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

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Storage Location Plant | Plant | Plant | RESTRICT |
| Referenced by | Plant Product Storage Location | PlantProduct | Plant Product | RESTRICT |

## PlantProduct

Plant-specific planning, storage, and manufacturing data for a product or material.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PlantProductID | Plant Product ID | String | Yes | Unique identifier for plant-specific product data. | No |
| MRPType | MRP Type | String | No | SAP MRP type used for plant planning. | No |
| SafetyStock | Safety Stock | Integer | No | Plant-specific safety stock. | No |
| ReorderPoint | Reorder Point | Integer | No | Plant-specific reorder point. | No |
| LotSize | Lot Size | String | No | Lot sizing procedure or value. | No |
| ManufacturingStatus | Manufacturing Status | String | No | Manufacturing readiness or usage status for the plant. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Plant Product Material | Material | Material | RESTRICT |
| References | Plant Product Plant | Plant | Plant | RESTRICT |
| References | Plant Product Product | Product | Product | RESTRICT |
| References | Plant Product Storage Location | StorageLocation | Storage Location | RESTRICT |

## Supplier

Supplier organization participating in product sourcing and procurement.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SupplierID | Supplier ID | String | Yes | Unique identifier for the supplier. | No |
| SupplierCode | Supplier Code | String | Yes | Code that identifies the supplier. | No |
| SupplierName | Supplier Name | String | Yes | Business name of the supplier. | No |
| SupplierType | Supplier Type | String | No | Type or role of the supplier. | No |
| CountryName | Country Name | String | No | Country where the supplier is primarily located. | No |
| PreferredSupplier | Preferred Supplier | Boolean | No | Indicates whether the supplier is preferred. | No |
| Active | Active | Boolean | No | Indicates whether the supplier is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Supplier Product Supplier | SupplierProduct | Supplier Product | RESTRICT |

## SupplierProduct

Supplier-specific product representation and sourcing detail.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SupplierProductID | Supplier Product ID | String | Yes | Unique identifier for a supplier-specific product representation. | No |
| SupplierProductNumber | Supplier Product Number | String | Yes | Supplier assigned product or catalog number. | No |
| SupplierDescription | Supplier Description | String | No | Supplier-provided product description. | No |
| LeadTimeDays | Lead Time Days | Integer | No | Supplier lead time in days. | No |
| MinimumOrderQuantity | Minimum Order Quantity | Integer | No | Minimum quantity that can be ordered from the supplier. | No |
| PreferredSupplierIndicator | Preferred Supplier Indicator | Boolean | No | Indicates whether this supplier product is preferred. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Supplier Product Product | Product | Product | RESTRICT |
| References | Supplier Product Supplier | Supplier | Supplier | RESTRICT |

## ProductClassification

Classification assignment for extensible product taxonomies and standards.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductClassificationID | Product Classification ID | String | Yes | Unique identifier for a product classification assignment. | No |
| ClassificationCode | Classification Code | String | Yes | Classification code from a taxonomy such as UNSPSC or eClass. | No |
| ClassificationName | Classification Name | String | Yes | Name or label for the classification code. | No |
| ClassificationLevel | Classification Level | String | No | Level within the classification scheme. | No |
| AssignedValue | Assigned Value | String | No | Assigned value or qualifier for the product classification. | No |
| ValidFrom | Valid From | Date | No | Date from which the classification is valid. | No |
| ValidTo | Valid To | Date | No | Date through which the classification remains valid. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Classification Product | Product | Product | RESTRICT |
| References | Classification Scheme | ClassificationScheme | Classification Scheme | RESTRICT |

## ClassificationScheme

Classification Scheme reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ClassificationSchemeID | Classification Scheme ID | String | Yes | Unique identifier for the classification scheme. | No |
| ClassificationSchemeCode | Classification Scheme Code | String | Yes | Code for the classification scheme. | No |
| ClassificationSchemeName | Classification Scheme Name | String | Yes | Classification framework such as UNSPSC, eClass, or custom taxonomy. | No |
| Description | Description | String | No | Description for the classification scheme. | No |
| Active | Active | Boolean | No | Indicates whether the classification scheme is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Classification Scheme | ProductClassification | Product Classification | RESTRICT |

## ProductSpecification

Technical, business, packaging, or performance specification for a product.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductSpecificationID | Product Specification ID | String | Yes | Unique identifier for a product specification. | No |
| SpecificationName | Specification Name | String | Yes | Name of the product specification. | No |
| SpecificationType | Specification Type | String | No | Type such as dimensions, packaging, technical, or performance. | No |
| SpecificationValue | Specification Value | String | No | Value captured for the specification. | No |
| MinimumValue | Minimum Value | String | No | Minimum acceptable value for a ranged specification. | No |
| MaximumValue | Maximum Value | String | No | Maximum acceptable value for a ranged specification. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the specification is effective. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Product Specification Product | Product | Product | RESTRICT |
| References | Product Specification UOM | UnitOfMeasure | Unit of Measure | RESTRICT |

## ProductVariant

Configurable or regional variant of a product golden record.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductVariantID | Product Variant ID | String | Yes | Unique identifier for a product variant. | No |
| VariantCode | Variant Code | String | Yes | Code that identifies the product variant. | No |
| VariantName | Variant Name | String | Yes | Business name for the product variant. | No |
| Size | Size | String | No | Size option for configurable products. | No |
| Color | Color | String | No | Color option for configurable products. | No |
| PackagingType | Packaging Type | String | No | Packaging option for the product variant. | No |
| Region | Region | String | No | Region where the variant is offered or controlled. | No |
| Active | Active | Boolean | No | Indicates whether the variant is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Variant Product | Product | Product | RESTRICT |

## RegulatoryAttribute

Compliance, restriction, certification, or safety attribute for a product.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RegulatoryAttributeID | Regulatory Attribute ID | String | Yes | Unique identifier for a regulatory attribute. | No |
| RegulationCode | Regulation Code | String | Yes | Code that identifies the regulation or control. | No |
| RegulationName | Regulation Name | String | Yes | Name of the regulation, certification, or restriction. | No |
| ComplianceIndicator | Compliance Indicator | Boolean | No | Indicates whether the product is compliant. | No |
| CertificateNumber | Certificate Number | String | No | Certificate or declaration number for the control. | No |
| ExpirationDate | Expiration Date | Date | No | Date when the certification or restriction expires. | No |
| SafetyDataSheetUrl | Safety Data Sheet URL | String | No | URL for the safety data sheet or compliance document. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Regulatory Compliance Status | ComplianceStatus | Compliance Status | RESTRICT |
| References | Regulatory Country | Country | Country | RESTRICT |
| References | Regulatory Product | Product | Product | RESTRICT |

## ComplianceStatus

Compliance Status reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ComplianceStatusID | Compliance Status ID | String | Yes | Unique identifier for the compliance status. | No |
| ComplianceStatusCode | Compliance Status Code | String | Yes | Code for the compliance status. | No |
| ComplianceStatusName | Compliance Status Name | String | Yes | Compliance state used for regulatory product governance. | No |
| Description | Description | String | No | Description for the compliance status. | No |
| Active | Active | Boolean | No | Indicates whether the compliance status is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Regulatory Compliance Status | RegulatoryAttribute | Regulatory Attribute | RESTRICT |

## Country

Country reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CountryID | Country ID | String | Yes | Unique identifier for the country. | No |
| CountryCode | Country Code | String | Yes | Code for the country. | No |
| CountryName | Country Name | String | Yes | Country used for regulatory and regional restrictions. | No |
| Description | Description | String | No | Description for the country. | No |
| Active | Active | Boolean | No | Indicates whether the country is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Regulatory Country | RegulatoryAttribute | Regulatory Attribute | RESTRICT |

## SourceSystem

SAP or downstream system participating in product data synchronization.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SourceSystemID | Source System ID | String | Yes | Unique identifier for the source or target system. | No |
| SystemCode | System Code | String | Yes | Code that identifies the SAP or downstream system. | No |
| SystemName | System Name | String | Yes | Business name of the system. | No |
| SystemType | System Type | String | No | Type such as S/4HANA, ECC, MDG, PLM, PIM, or eCommerce. | No |
| Landscape | Landscape | String | No | Landscape, region, or business unit where the system operates. | No |
| Active | Active | Boolean | No | Indicates whether the system is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Cross Reference Source System | ProductCrossReference | Product Cross Reference | RESTRICT |

## ProductCrossReference

Cross-system identifier mapping between product, material, and external systems.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductCrossReferenceID | Product Cross Reference ID | String | Yes | Unique identifier for a system cross reference. | No |
| ExternalProductID | External Product ID | String | Yes | Product identifier used by an external system. | No |
| ExternalMaterialNumber | External Material Number | String | No | Material identifier used by an external system. | No |
| CrossReferenceType | Cross Reference Type | String | No | Type of mapping such as SAP ECC, S/4HANA, PLM, PIM, or legacy. | No |
| SourceLastUpdated | Source Last Updated | Timestamp | No | Timestamp when the source mapping was last updated. | No |
| Active | Active | Boolean | No | Indicates whether the cross reference is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Cross Reference Material | Material | Material | RESTRICT |
| References | Cross Reference Product | Product | Product | RESTRICT |
| References | Cross Reference Source System | SourceSystem | Source System | RESTRICT |

## ProductRelationship

Relationship between products such as substitute, successor, accessory, or bundle component.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductRelationshipID | Product Relationship ID | String | Yes | Unique identifier for a relationship between products. | No |
| RelationshipCode | Relationship Code | String | Yes | Code that identifies the product relationship. | No |
| Quantity | Quantity | Integer | No | Quantity used when the relationship represents a component or bundle. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the relationship is effective. | No |
| EffectiveTo | Effective To | Date | No | Date through which the relationship remains effective. | No |
| Active | Active | Boolean | No | Indicates whether the relationship is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| References | Relationship From Product | Product | From Product | RESTRICT |
| References | Relationship To Product | Product | To Product | RESTRICT |
| References | Relationship Type | RelationshipType | Relationship Type | RESTRICT |

## RelationshipType

Relationship Type reference data used by the SAP Product / Material 360 model.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| RelationshipTypeID | Relationship Type ID | String | Yes | Unique identifier for the relationship type. | No |
| RelationshipTypeCode | Relationship Type Code | String | Yes | Code for the relationship type. | No |
| RelationshipTypeName | Relationship Type Name | String | Yes | Type of product relationship such as substitute, successor, bundle, or accessory. | No |
| Description | Description | String | No | Description for the relationship type. | No |
| Active | Active | Boolean | No | Indicates whether the relationship type is active. | No |

**Relationships**
| Direction | Reference | Related Entity | Role Label | Delete Propagation |
|---|---|---|---|---|
| Referenced by | Relationship Type | ProductRelationship | Product Relationship | RESTRICT |
