# SAP Product / Material 360

This Master Data Management model provides a trusted product and material hub for SAP-centric landscapes. It consolidates product master data, SAP material definitions, plant extensions, suppliers, classifications, regulatory attributes, and cross-system identifiers into a governed Semarchy xDM model.

The model is designed for organizations that need a reliable Product / Material 360 view across SAP S/4HANA, SAP ECC, SAP MDG, PLM, PIM, supplier, and operational systems. It supports authoring, import, duplicate management, data quality controls, model documentation, and guided workflow-based stewardship for selected authoring scenarios.

- **Trusted product and material records:** Product and Material are fuzzy matched golden entities with generated golden identifiers and source-aware survivorship.
- **SAP operational context:** Plant, storage location, procurement, valuation, material type, and plant product entities support SAP manufacturing and planning processes.
- **Governance and compliance:** Classification, specification, variant, supplier, regulatory, and lifecycle entities provide stewardship coverage beyond core material master fields.
- **Integration-ready data loads:** CSV import files and a full JSON API payload are included under `resources/demo-data`.
- **Workflow-based authoring:** Product introduction and plant extension readiness workflows are available through the Product and Plant Product action sets.

## Prerequisites

To deploy and operate this model, configure the following components in the target Semarchy environment:

- Publishers for SAP and non-SAP sources: SAP MDG, SAP S/4HANA, SAP ECC, PLM, PIM, and Data Entry.
- Roles or role mappings for `semarchyAdmin`, `productSteward`, and any local users who will run workflow authoring tasks.
- The `sap-product-material-360` image library from `resources/image-libraries/sap-product-material-360`.
- Import access to load sample CSV files or the API payload in `resources/demo-data`.
- The latest `sem-design` CLI for build validation and package generation.

## Model Structure

The model contains product, material, hierarchy, classification, plant, supplier, regulatory, relationship, and reference-data entities. The full generated entity and attribute reference is available in [model_structure.md](./model_structure.md).

The source model includes two documentation diagrams:

- [Core Product Material](../src/sappm360/model_diagrams/CoreProductMaterial.ModelDiagram.seml) for product, material, hierarchy, classification, specification, variant, and relationship structures.
- [Governance Reference](../src/sappm360/model_diagrams/GovernanceReference.ModelDiagram.seml) for plant, supplier, regulatory, cross-reference, source-system, and reference-data structures.

### Product

Trusted product golden record consolidating SAP and non-SAP product information.

Product is the commercial golden record for product identity, lifecycle, product family, brand, hierarchy, GTIN, manufacturer part number, quality score, and sellable/procurement/hazardous indicators.

**Matching Rules:**
1. **Same GTIN** (Score: 100) - `Record1.GTIN is not null and Record1.GTIN = Record2.GTIN`
2. **Same Product ID** (Score: 96) - `Record1.ProductID is not null and Record1.ProductID = Record2.ProductID`
3. **Same Name And Family** (Score: 88) - `Record1.NormalizedProductName = Record2.NormalizedProductName and COALESCE(Record1.ProductFamily,'') = COALESCE(Record2.ProductFamily,'')`

### Material

SAP material definition harmonized across ECC, S/4HANA, plants, and business units.

Material captures the SAP material number, material description, SAP client, plant scope, planning quantities, batch/serial controls, base UOM, industry sector, material group, material type, procurement type, product association, and valuation class.

**Matching Rules:**
1. **Same Material And Client** (Score: 100) - `Record1.MaterialNumber = Record2.MaterialNumber and COALESCE(Record1.SAPClient,'') = COALESCE(Record2.SAPClient,'')`
2. **Same Material Number** (Score: 94) - `Record1.MaterialNumber = Record2.MaterialNumber`
3. **Same Description And Product** (Score: 86) - `Record1.NormalizedMaterialDesc = Record2.NormalizedMaterialDesc and Record1.FID_Product = Record2.FID_Product`

### Product Hierarchy and Classification

ProductHierarchy supports parent-child hierarchy paths, levels, and active hierarchy nodes. ProductClassification assigns products to external or internal classification schemes, with valid-from and valid-to dates for controlled classification maintenance.

### Specifications, Variants, and Relationships

ProductSpecification records measurable attributes and UOM-bound specifications. ProductVariant captures size, color, packaging, and regional variants. ProductRelationship models product-to-product relationships such as bundles, substitutes, accessories, and component relationships.

### Plant and Supply Chain

Plant, StorageLocation, and PlantProduct define where products and materials are planned, stored, manufactured, or procured. StorageLocation includes input address fields, Google Maps geocoded address outputs, and a map in the browsing form. Supplier and SupplierProduct capture supplier-specific product numbers, lead times, minimum order quantities, and preferred-supplier indicators.

### Storage Location Geocoding

StorageLocation stores geocoding inputs and outputs as individual attributes, not as a complex type. Source imports should provide the source-owned address fields: `InpAddressLine`, `InpCity`, `InpState`, `InpPostalCode`, and `InpCountry`, along with standard fields such as `StorageLocationID`, `StorageLocationCode`, `StorageLocationName`, `Active`, and `FID_Plant`.

The Google Maps Java plugin enricher `GeocodedStorageLocationAddress` populates the `Geo*` output fields, including `GeoStreetNumber`, `GeoStreetName`, `GeoLocality`, `GeoState`, `GeoPostalCode`, `GeoCountry`, `GeoCountryShort`, `GeoLatitude`, `GeoLongitude`, `GeoStatus`, and `GeoQuality`. These enriched fields are intentionally excluded from the Storage Location CSV and API payload because they are not source-provided values.

The Storage Location browsing form organizes Identity, Input Address, and Geocoded Address sections into three vertical columns. The Google Map section remains a single full-width map block.

### Regulatory and Cross-System Traceability

RegulatoryAttribute records country and compliance status details, certificates, expiration dates, and safety data sheet URLs. ProductCrossReference links products and materials to external product IDs and source systems for lineage and interoperability.

### Reference Data

Reference entities are modeled as governed Basic entities rather than simple LOVs so that stewardship, imports, and workflow patterns can be extended consistently.

- **Brand** - Brand owned, manufactured, or distributed by the enterprise.
- **Product Type** - Product Type reference data used by the SAP Product / Material 360 model.
- **Product Status** - Product Status reference data used by the SAP Product / Material 360 model.
- **Lifecycle Status** - Lifecycle Status reference data used by the SAP Product / Material 360 model.
- **Material Type** - Material Type reference data used by the SAP Product / Material 360 model.
- **Material Group** - Material Group reference data used by the SAP Product / Material 360 model.
- **Industry Sector** - Industry Sector reference data used by the SAP Product / Material 360 model.
- **Procurement Type** - Procurement Type reference data used by the SAP Product / Material 360 model.
- **Valuation Class** - Valuation Class reference data used by the SAP Product / Material 360 model.
- **Unit of Measure** - Standard unit of measure and conversion definition used by SAP materials.
- **Classification Scheme** - Classification Scheme reference data used by the SAP Product / Material 360 model.
- **Source System** - SAP or downstream system participating in product data synchronization.
- **Relationship Type** - Relationship Type reference data used by the SAP Product / Material 360 model.

## Model Components

### Application

The main application is [ProductMaterial360Hub](../src/sappm360/applications/ProductMaterial360Hub.Application.seml). It organizes business views into product governance, material management, supply chain, compliance and quality, integration, import, worklist, configuration, and administration folders.

### Publishers

| Publisher | Code | Label | Active |
|---|---|---|---|
| DataEntry | DE | Data Entry | Yes |
| PIM | PIM | PIM | Yes |
| PLM | PLM | PLM | Yes |
| S4HANA | S4HANA | SAP S/4HANA | Yes |
| SAPECC | SAPECC | SAP ECC | Yes |
| SAPMDG | SAPMDG | SAP MDG | Yes |

### Enrichers

The model uses SemQL enrichers to normalize product and material names for matching and duplicate detection, plus a Google Maps Java plugin enricher to geocode Storage Location addresses. For the complete generated list, see [enrichers.md](./enrichers.md).

### Validations

The model includes date and planning validations for products, classifications, specifications, regulatory attributes, relationships, and materials. For the complete generated list, see [validations.md](./validations.md).

### Workflows

Workflow launch actions are available directly from the Product and Plant Product action sets. Each workflow can start from scratch or from a selected golden record.

| Workflow | Label | Root Entity | Authoring Steps | Submit Job | Admin Role |
|---|---|---|---|---|---|
| NewProductIntroduction | New Product / Material Introduction | Product | Capture Product Request -> Data Quality Review -> Compliance Review -> Final Approval | INTEGRATE_ALL | semarchyAdmin |
| PlantExtensionReadiness | Plant Extension / Manufacturing Readiness | PlantProduct | Capture Plant Extension -> Plant Planning Review -> Procurement and Costing Review -> Data Steward Approval | INTEGRATE_ALL | semarchyAdmin |

### Model Jobs

| Model Job | Label | Description |
|---|---|---|
| INTEGRATE_ALL | INTEGRATE_ALL | (none) |
| ProductMaterial360 | ProductMaterial360 | (none) |
| Reference | Reference | (none) |

### Demo Data and API Imports

Sample data is provided in two formats:

- CSV files under [ImportDataSAPPM360](../resources/demo-data/ImportDataSAPPM360). The numbered filenames indicate the recommended loading order.
- A single JSON API payload under [API Import-curl](../resources/demo-data/API%20Import-curl/SAPProductMaterial360.json), with a curl usage note in the same folder.
- Storage Location sample data includes only source-loadable address input fields and excludes Google Maps `Geo*` output fields. The `Geo*` values are populated by the `GeocodedStorageLocationAddress` enricher during integration.

## Work for Developers

- Build the model with `sem-design dm model build --root-folder /shared-resources/workspace/SAPProductMaterial360/src/sappm360`.
- Keep `src/sappm360/model.json` synchronized with the latest generated `out/model.json` after successful builds.
- When adding new entities, update the model diagrams, action-set placement, image library assets, sample CSV/API payloads, and this documentation folder together.
- Keep fuzzy-entity import payloads source-aware: use `PublisherID` and `SourceID` for fuzzy entity identification, and do not provide generated golden IDs as input data.
