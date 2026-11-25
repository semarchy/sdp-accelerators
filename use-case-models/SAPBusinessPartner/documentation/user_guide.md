# SAP Business Partner 360

This Master Data Management (MDM) model for the SAP Business Partner domain is designed to centralize and harmonize business partner, supplier, address, contact, and banking data coming from multiple SAP and non-SAP source systems. The model delivers a single, trusted golden record for every business partner and supplier, so that finance, procurement, and master-data teams across the enterprise work from consistent, accurate, and de-duplicated information.

The model is inspired by the [SAP S/4HANA Business Partner](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE) data model (the central `BUT000` business partner and its vendor/customer extensions). The number of entities has been focused on the most common business-partner and supplier scenarios and can be extended based on your specific requirements.

- **Data Consolidation:** Integrates and reconciles party data from SAP S/4HANA, SAP ECC, CRM, and manual data entry, producing one version of the truth for business partners and suppliers.
- **Data Quality & Enrichment:** Applies business rules, validations, and enrichers to improve data quality including name normalization, address geocoding, and search-key standardization.
- **Reference Data Management:** Manages code lists and reference tables (e.g., Country, Currency, Payment Terms, Business Partner Role, Industry) as governed entities to support consistent categorization and reporting.
- **Publisher Management:** Supports ranking and source-system identification across SAP S/4HANA, SAP ECC, CRM, and Data Entry systems for survivorship.
- **Data Stewardship:** Provides dedicated navigation for reviewing match suggestions and correcting source-data errors.
- **Extensibility:** Offers a flexible foundation for UI components, hierarchies, and future enhancements.

This model is a robust foundation for enterprise business-partner data management, enabling better vendor onboarding, compliance, spend consolidation, and operational efficiency.

## Prerequisites

To correctly integrate this model with SDP DM, create the following components in the platform:

- Publishers configured for your source systems: **SAP S/4HANA**, **SAP ECC**, **CRM**, and **DataEntry**.
- The **Google Maps API** row-transformer plugin configured for address geocoding (used by the `BPAddress` geocoding enricher). If you do not use address geocoding, this enricher can be disabled.
- A model job `INTEGRATE_ALL` (present under `/model_jobs/`) to integrate loaded data.

## Model Structure

This model describes the entities and relationships used to manage business-partner and supplier data in an SAP context. It contains six core (fuzzy-matched) entities - **Business Partner**, **Supplier**, **Supplier Purchasing Org**, **BP Address**, **BP Contact**, and **BP Bank** - together with transactional child entities and a broad set of reference-data entities that provide typology and hierarchical relationships.

Three model diagrams are provided for navigation and documentation:

- **BP Core** - the business partner hub and its immediate address, contact, role, industry, identification, and tax details.
- **Financial & Relationships** - banking, tax, and partner-to-partner relationships.
- **Supplier Branch** - supplier, purchasing-organization, company-code, partner-function, and text data.

You can extend the data model by adding your own entities and/or attributes to the existing ones. For the full list of tables and attributes, refer to the [model structure page](./model_structure.md).

### Business Partner

The `BusinessPartner` entity is the central hub of the model. It represents any party - an organization or a natural person - that the enterprise does business with, consolidating the SAP central business partner with CRM party records.

It is a **fuzzy-matching** entity. A normalized name is derived during enrichment to support exact-comparison matching and to improve matching performance.

Main fields contributing to the matching decision are:
- **SAP business partner number** (kept for traceability across systems)
- **Normalized Name** (derived from the full name)
- **Organization name** and **Search Term**

**Matching Rules:**
1. **Same Business Partner Number** (Score: 96) - Matches records that share the same SAP business partner number.
2. **Same Full Name** (Score: 88) - Matches records with the same normalized full name.
3. **Same Organization And Search Term** (Score: 85) - Matches records with the same organization name line 1 and search term.

Source values (e.g., `BusinessPartnerFullName`) are preserved while the enriched value (`NormalizedName`) is stored separately, so source vs. enriched data can be compared.

> To change the matching strategy, edit the [BusinessPartner.Entity.seml](../src/sapbp360/entities/BusinessPartner/BusinessPartner.Entity.seml) file, property `matcher`. See the Semarchy [SDP documentation](https://docs.semarchy.com/sdp/reference/vscode/objects/Entity#matcher) for guidance.

### Supplier

The `Supplier` entity represents a business partner in the vendor role, carrying procurement- and payment-relevant attributes. It is a **fuzzy-matched** entity linked back to its `BusinessPartner` record.

Main fields contributing to the matching decision are the VAT registration, the supplier number, and the normalized supplier name.

**Matching Rules:**
1. **Same VAT Registration** (Score: 100) - Matches suppliers sharing the same VAT registration number.
2. **Same Supplier Number** (Score: 96) - Matches suppliers with the same supplier number.
3. **Same Supplier Name** (Score: 85) - Matches suppliers with the same normalized name.

### Supplier Purchasing Org

The `SupplierPurchasingOrg` entity holds purchasing-organization-level data for a supplier (incoterms, order controls, invoicing rules, responsible sales person). It is a **fuzzy-matched** entity linked to `Supplier`.

**Matching Rule:**
1. **Same Responsible Sales Person** (Score: 80) - Matches purchasing-org records with the same normalized responsible sales person name.

### BP Address

The `BPAddress` entity stores postal addresses for a business partner. It is a **fuzzy-matched** entity that is enriched with **geocoding** through the Google Maps API, and a normalized city is derived for search and comparison.

**Matching Rules:**
1. **Same Full Address** (Score: 90) - Matches on street, house number, city, and postal code.
2. **Same City And Postal Code** (Score: 82) - Matches on city and postal code.

Input address fields (`Inp*`) feed the geocoder, and the geocoded output (`Geo*`) is stored in separate attributes so the source address remains available for review.

### BP Contact

The `BPContact` entity models the contact-person relationship linking an organization business partner (company) to a person business partner. It is a **fuzzy-matched** entity, with a normalized contact name derived for matching.

**Matching Rule:**
1. **Same Contact Name** (Score: 85) - Matches contact records with the same normalized contact name.

### BP Bank

The `BPBank` entity stores bank-account details (IBAN, SWIFT/BIC, account holder) for a business partner. It is a **fuzzy-matched** entity.

**Matching Rules:**
1. **Same IBAN** (Score: 100) - Matches bank records sharing the same IBAN.
2. **Same Bank Account** (Score: 94) - Matches bank records with the same bank key and account number.

### Reference Data

The remaining tables are reference (code-list) data for the business-partner domain. They are designed as **Basic** entities without matching, on the assumption that reference data arrives already cleansed into the MDM system. Modeling them as governed entities (rather than Lists of Values) allows a governance process - workflows, stewardship, and flexible create/update - around reference data.

Representative reference entities include Country, Currency, Language, Region, Industry, Industry Sector, Payment Terms, Incoterms Classification, Shipping Condition, Business Partner Category / Grouping / Role, BP Status, Partner Function, Relationship Category, Company Code, House Bank, Reconciliation Account, Tax Jurisdiction, Tax Number Category, and Supplier Account / Corporate Group.

The full list of reference tables with attributes is on the [model structure page](./model_structure.md).

## Model Components

### Hierarchies and Relationships

Business partners can be linked to one another through the `BPRelationship` entity (e.g., parent, headquarter, or affiliate relationships between two business partners), enabling corporate-structure modeling. Suppliers and their purchasing organizations, company codes, partner functions, and texts branch off the supplier hub.

### Publishers

The model defines four publishers for source-system integration, used for ranking in survivorship rules:

- **SAP S/4HANA** - primary SAP source for business partner and supplier master data.
- **SAP ECC** - legacy SAP source for business partner and supplier data.
- **CRM** - customer relationship system (party and contact data).
- **DataEntry** - manual data-entry interface (typically the lowest priority for survivorship).

As part of your customization you can change publisher labels and/or IDs, add or remove publishers, and adjust survivorship ranking based on your data-quality and business requirements.

### Enrichers

The model includes enrichers to standardize and enrich entity fields. All enrichers run in the **PRE_CONSO** scope, and enriched values are stored in separate attributes so the original source values remain available for review. For full details see the [enrichers documentation](./enrichers.md).

- **Business Partner** - `NormalizedName` derived from the full name for matching.
- **Supplier** - `NormalizedName` derived from the supplier name.
- **Supplier Purchasing Org** - `NormalizedRespName` derived from the responsible sales person name.
- **BP Address** - Google Maps geocoding of the address, plus `NormalizedCity` (upper-cased city).
- **BP Address Email** - `SearchEmailAddress` (upper-cased email) for search.
- **BP Contact** - `NormalizedName` derived from the contact full name.
- **BP Tax Number** - `NormalizedTaxNumber` (upper-cased, spaces removed).
- **BP Identification** - `NormalizedIdNumber` (upper-cased, spaces removed).

As part of your customization you can modify or remove existing enrichers, or create your own transformation rules based on these examples. AI-based enrichers can additionally be introduced where suggestions add value.

### Validations

The model implements logical (soft) validations in the **PRE_CONSO** scope rather than database constraints, so data can still be loaded and corrected through the stewardship UI. For full details see the [validations documentation](./validations.md).

Implemented validations include:
- **Logical mandatory checks** - e.g., Business Partner last name required for natural persons, Contact full name required, Supplier name required, Tax number required, Identification number required.
- **Date-range checks** - Valid To not before Valid From (Address Usage, Relationship, Role), Validity End not before Validity Start (Bank), and Last Modified not before Created (Business Partner).
- **Format / length checks** - Email pattern, phone length, IBAN length (15-34), SWIFT/BIC length (8 or 11).
- **Value checks** - Minimum order amount not negative, and city required when a postal code is present.

You can extend validations to apply your specific business rules.

### Data Stewardship (Manage)

The **SAP Business Partner 360** application includes a **Manage** navigation folder for data stewards, with two areas:

- **Match Suggestions** - browses each fuzzy entity filtered to records with pending duplicate-merge suggestions (`HasSuggestedMerge`), so stewards can review and confirm consolidations for Business Partners, Suppliers, Supplier Purchasing Orgs, Addresses, Contacts, and Banks.
- **Source Errors** - browses each validated entity in its source-data-with-errors view, so stewards can find and correct records that failed a validation.

## Work for Developers

This model covers the core use cases for SAP business-partner and supplier data management and illustrates application components you can extend. Functionally it can serve as a first MVP and a basis for MDM design workshops.

It enables you to:
- Load your SAP S/4HANA, SAP ECC, or CRM party data and apply data-quality rules to assess your current data state.
- Present the UI/UX to business users through the SAP Business Partner 360 Hub application and gather feedback.
- Demonstrate matching rules and the stewardship process to help define your specific consolidation approach.

Main areas for your DM developers to enhance and extend:

1. **User Interface.** The SAP Business Partner 360 Hub application provides global search across Business Partners, Suppliers, Addresses, and Contacts, domain navigation folders, and a Manage folder for stewardship. Extend it with custom views, dashboards, and steppers to match your users' preferences.

2. **Hierarchies.** Extend `BPRelationship` or add additional hierarchies (e.g., corporate-group or purchasing hierarchies) based on your organizational requirements.

3. **Matching Rules.** The Business Partner, Supplier, Supplier Purchasing Org, Address, Contact, and Bank entities each apply match rules to detect duplicates. Adjust the thresholds and conditions in each entity's `matcher` property to fit your data-quality objectives.

4. **Survivorship.** Review and tune the survivorship rules and publisher ranking so the golden record reflects the most trusted source for each attribute.

5. **Workflows.** Add data-entry steppers and approval workflows (e.g., vendor onboarding approval, blocking/unblocking, or address-change review) based on your governance requirements.

6. **Integration with External Systems.** The publisher model supports multiple SAP and non-SAP sources. Configure and extend integration patterns and consider bi-directional synchronization for critical entities.

7. **Advanced Analytics.** Leverage the consolidated data for a business-partner 360 view, supplier spend consolidation, duplicate-rate and data-quality KPIs, and compliance reporting (tax IDs, blocked flags, banking).

8. **Enrichment Extension.** Add further enrichers such as AI-based classification or additional address/phone standardization, following the existing PRE_CONSO, source-preserving pattern.

Demo data for loading and testing (including intentional duplicates and validation-failing records) is available under [`../resources/demo-data`](../resources/demo-data), with a ready-to-run API payload in the `API Import-curl` subfolder.
