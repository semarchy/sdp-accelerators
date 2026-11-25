# Retail Customer 360

This Master Data Management (MDM) model for the retail customer domain is designed to centralize and harmonize customer, account, contact-point, consent, loyalty, commerce, and engagement data from multiple operational systems. The model provides a trusted golden record for customer-facing and analytics use cases so teams across marketing, commerce, customer care, and data governance can work from consistent, de-duplicated, and quality-managed data.

The model covers customer and account master data, digital and physical contact points, campaign and engagement telemetry, orders and order lines, loyalty programs and balances, and privacy/compliance controls.

- **Data Consolidation:** Integrates data from CRM, E-Commerce, POS, Loyalty, API feeds, and Manual Data Entry into one governed domain model.
- **Data Quality & Enrichment:** Applies enrichers and validations to normalize identity attributes, derive quality indicators, and compute business metrics used for matching and stewardship.
- **Reference Data Management:** Maintains key lookup domains (for example Country, Currency, Delivery Method, Legal Basis, Data Use Purpose, Product Catalog) as governed entities.
- **Publisher-Aware Survivorship:** Uses publisher ranking and targeted survivorship rules to keep the most trusted values in golden records.
- **Data Stewardship:** Provides dedicated duplicate-management views and erroneous-data views to support data curation.
- **Extensibility:** Offers a complete foundation for extending entities, matching strategy, enrichers, validations, UI navigation, and analytics.

This model is a practical foundation for a retail customer 360 initiative and can serve as an MVP for workshops and iterative implementation.

## Prerequisites

To run this model successfully in SDP DM, configure the following platform components:

- Publishers used by the model: **API**, **CRM**, **ECOMMERCE**, **LOYALTY**, **MANUAL**, **POS**, and **UI**.
- A model integration job **INTEGRATE_ALL** available in the model at `/certification_jobs/INTEGRATE_ALL.CertificationJob.seml`.
- Access to API-based loading if you plan to run scripted imports (sample payload is provided in resources).

Optional but recommended:

- Dashboard runtime configured for the dashboards referenced by the application (Revenue Snapshot, Executive Overview, Customer Health, Customer Overview, Account Portfolio, Engagement Pulse, Loyalty Health, Compliance Risk).

## Model Structure

This model includes ten fuzzy-matched core entities and a broad set of supporting entities for customer profile, engagement, loyalty, commerce, and compliance.

The fuzzy-matched entities are:

- **Customer**
- **Account**
- **Lead**
- **AccountContact**
- **ContactPointAddress**
- **ContactPointEmail**
- **ContactPointPhone**
- **ContactPointApp**
- **ContactPointSocial**
- **PartyIdentification**

Model diagrams are provided under `/model_diagrams/`:

- **CustomerMaster**
- **AccountManagement**
- **ContactProfile**
- **Commerce**
- **Engagement**
- **Loyalty**
- **Governance**

You can extend the model by adding entities, attributes, business views, enrichers, and validations.

### Customer

The `Customer` entity is the central customer hub and is fuzzy matched.

Main fields contributing to matching are source customer key, normalized full name, birth date, and country.

**Matching Rules:**
1. **Source Customer Key Exact Match** (Score: 100)
2. **Name and BirthDate Match** (Score: 89)
3. **Fuzzy name with birthdate and country** (Score: 72)

### Account

The `Account` entity represents the account/commercial profile linked to customers and is fuzzy matched.

Main fields contributing to matching are account number, tax registration number, account name, and location.

**Matching Rules:**
1. **Account number exact match** (Score: 100)
2. **Tax registration exact match** (Score: 98)
3. **Account name and location exact match** (Score: 92)
4. **Account name fuzzy match with location confirmation** (Score: 72)

### Lead

The `Lead` entity captures prospective-customer records and is fuzzy matched.

Main fields contributing to matching are email address, normalized name, company context, and phone number.

**Matching Rules:**
1. **Email exact match** (Score: 100)
2. **Similar name and same company** (Score: 90)
3. **Phone exact match** (Score: 80)

### AccountContact

The `AccountContact` entity captures account-contact persons and is fuzzy matched.

**Matching Rules:**
1. **Business email exact match** (Score: 100)
2. **Similar name and same role** (Score: 85)

### ContactPointAddress

The `ContactPointAddress` entity stores customer addresses and is fuzzy matched.

**Matching Rules:**
1. **Full address exact match** (Score: 100)
2. **Same customer with fuzzy street address and same postal code** (Score: 73)

The model includes latitude/longitude attributes and range validations; geocoding can be added as a customization if needed.

### ContactPointEmail

The `ContactPointEmail` entity stores email channels and is fuzzy matched.

**Matching Rules:**
1. **Email exact match** (Score: 100)
2. **Same customer with similar email address** (Score: 70)

### ContactPointPhone

The `ContactPointPhone` entity stores phone channels and is fuzzy matched.

**Matching Rules:**
1. **Phone exact match** (Score: 100)
2. **Same customer with similar phone number** (Score: 70)

### ContactPointApp

The `ContactPointApp` entity stores app-installation channels and is fuzzy matched.

**Matching Rules:**
1. **Same application installation** (Score: 100)
2. **Same push token** (Score: 95)
3. **Same customer on same app platform** (Score: 68)

### ContactPointSocial

The `ContactPointSocial` entity stores social identities and is fuzzy matched.

**Matching Rules:**
1. **Same handle on the same network** (Score: 100)
2. **Same profile url** (Score: 95)
3. **Same customer on same social network** (Score: 65)

### PartyIdentification

The `PartyIdentification` entity stores customer identification documents and is fuzzy matched.

**Matching Rules:**
1. **Identification exact match** (Score: 100)
2. **Same customer with similar identification number** (Score: 75)

## Reference and Supporting Data

Beyond the fuzzy entities, the model includes governed supporting domains and transactional structures such as:

- **Reference domains:** Country, Currency, UnitOfMeasure, SoftwareApplication, OrderDeliveryMethod, DataUseLegalBasis, DataUsePurpose, ProductCatalog, ProductCatalogCategory, Brand, SalesStore, CommunicationSubscriptionChannelType.
- **Commerce and pipeline:** Opportunity, OpportunityProduct, Product, Promotion, SalesOrder, SalesOrderItem.
- **Loyalty:** LoyaltyProgram, LoyaltyTier, LoyaltyProgramMember, LoyaltyLedger, Voucher.
- **Engagement:** EmailEngagement, MobileAppEngagement, WebEngagement, SMSEngagement, WebSearchEngagement, ShoppingCartEngagement.
- **Governance/compliance:** Consent, ConsentAction, ContactPointConsent.

## Model Components

### Hierarchies and Relationships

The model links customers to accounts, contacts, identifications, communication endpoints, loyalty membership, opportunities, and commerce/engagement events. This structure supports both operational customer 360 use cases and analytics scenarios.

### Publishers

The model defines the following publishers for source-system integration and survivorship ranking:

- **REST API** (`API`)
- **CRM System** (`CRM`)
- **E-Commerce Platform** (`ECOMMERCE`)
- **Loyalty Platform** (`LOYALTY`)
- **Manual Data Entry** (`MANUAL`)
- **Point of Sale** (`POS`)
- **UI Publisher** (`UI`)

As part of customization, you can adjust labels/codes, add or remove publishers, and tune publisher rankings in survivorship rules.

### Enrichers

Enrichers run primarily in **PRE_CONSO** and derive standardized or analytics-ready values while preserving input attributes.

Representative enrichers include:

- **Customer Name Enricher**: computes `FullName`, `FullNameNormalized`, and `Initials`.
- **Customer Age Enricher**: computes `Age` and `AgeGroup`.
- **Customer Tenure Enricher**: computes `TenureYears` and `TenureSegment`.
- **Customer Business Profile Enricher**: computes `CustomerType` and `CustomerValueBand`.
- **Account Name Enricher**: computes `AccountNameNormalized`.
- **Lead Name Enricher**: computes `FullName`, `FullNameNormalized`, and `LeadAgeDays`.
- **ContactPointSocial Handle Enricher**: computes normalized handle from social handle input.
- **PartyIdentification Masking Enricher**: computes `MaskedIdentificationNumber` to protect sensitive ID values.
- **Campaign Performance Enricher**: computes campaign performance score, pacing status, ROI band, and health status.
- **Country Wikipedia Enricher**: computes a Wikipedia URL from the country short name.

Many entities also include completeness enrichers (`EnrichmentCompletenessScore`, `EnrichmentCompletenessBand`, `EnrichmentUpdatedOn`) to support quality monitoring.

### Survivorship

The model includes default and targeted survivorship strategies across multiple entities. Several rules explicitly rank publishers with business context, for example:

- Contact point quality/verification rules for email, phone, and address.
- Customer demographic/lifecycle consolidation with publisher preference.
- Party identification authority and source-priority rules for compliance-sensitive attributes.
- Account strategic-priority and business-profile survivorship rules.

You can review and tune survivorship behavior in each entity's `/survivorship_rules/` folder.

### Validations

The model uses logical validations (primarily **PRE_CONSO**, with some **POST_CONSO**) to preserve load flexibility while surfacing data issues for stewardship.

Representative validations include:

- **Identity and existence checks:** customer must exist for contact points; identification number or masked value required.
- **Date consistency:** campaign end date not before start date; loyalty points expiry not before join date; identification expiry not before issue date.
- **Numerical consistency:** clicks <= impressions; conversions <= clicks; non-negative balances and amounts.
- **Financial checks:** sales order and order item amount component consistency.
- **Location and channel checks:** core address elements required; latitude/longitude ranges; page URL required for page/product view events.

### Data Stewardship

The application includes dedicated stewardship-oriented navigation:

- **Duplicate Management** folder with review-suggested-match views for all fuzzy entities (customers, accounts, leads, identifications, contact points).
- **Data > Erroneous Data** folder with source-data-with-errors views (`SAWE`) across key entities for validation remediation.

This supports both duplicate resolution and data-quality correction workflows.

### Search and Analytics

The application provides:

- **Global Search** across major business views (customers, accounts, email/phone/address, campaigns, consents, loyalty, orders/items, products).
- **Analytics** actions for dashboards: Revenue Snapshot, Executive Overview, Customer Health, Customer Overview, Account Portfolio, Engagement Pulse, Loyalty Health, Compliance Risk.

## Work for Developers

This model is intended as a working accelerator and can be evolved in multiple dimensions.

Recommended areas for extension:

1. **UI and navigation:** Add custom folders, forms, steppers, and dashboards for your business personas.
2. **Matching strategy:** Tune thresholds and rule conditions in fuzzy entities to align with your data profile.
3. **Survivorship ranking:** Adjust publisher trust per attribute and per entity based on operational reality.
4. **Validation policy:** Add business-specific checks while preserving stewardship-friendly correction flows.
5. **Data governance:** Extend consent/compliance logic and audit-oriented views.
6. **Integrations:** Expand batch/API pipelines and bi-directional synchronization patterns where needed.
7. **Advanced enrichment:** Add external verification/geocoding or AI-assisted enrichment where justified.
8. **Analytics and KPIs:** Extend quality, duplication, lifecycle, engagement, and revenue indicators.

## Demo Data and Loading Assets

The accelerator includes ready-to-use import assets:

- CSV import files in `/resources/import-data/`.
- API load examples in `/resources/api-data/`, including:
  - `how-to-curl-api-load.md`
  - `retailcustomer360_api_load_payload.json`

Use these assets with the import actions in the application and run `INTEGRATE_ALL` to process matching, consolidation, enrichment, and validations.
