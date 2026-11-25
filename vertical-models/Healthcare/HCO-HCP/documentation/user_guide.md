# HCO-HCP Healthcare Demo - User Guide

The HCO-HCP model is a healthcare master data application that consolidates Health Care Organizations (HCOs), Health Care Providers (HCPs), Members, Encounters, Products, and clinical reference data into a unified, governed view. It supports stewardship workflows, matching and merging for key masters, and reference catalogs used across clinical and product domains.

Use this guide by persona so each role can focus on the most relevant workflows and screens.

## Personas and goals

### Data Steward
Focus: resolve duplicates, correct identities, and maintain golden records and reference data.

Typical tasks:
- Review and merge duplicate HCO/HCP/Member/Products records.
- Validate and complete missing demographics, identifiers, and reference values.
- Apply normalization and geocoding results.
- Maintain ICD mappings, taxonomies, and specialties as needed.

Key workflows:
- Duplicate HCOs
- Author HCOs, Author HCPs, Author Members
- Author Products, Author Administration, Author Forms, Author Strength, Author Sponsors
- Author ICD-9-CM, Author ICD-10-CM, Author ICD Mappings
- Author Taxonomy Groupings/Classifications/Specializations, Author Specialties

### Business User
Focus: analyze trusted data and extract insights.

Typical tasks:
- Explore golden records across HCO/HCP/Member/Products.
- Connect encounters to providers and organizations.
- Use reference dimensions for reporting and rollups.

Key entities:
- Encounter, HCO, HCP, Member, Products
- Taxonomy and ICD references

## Model at a glance

Core masters:
- HCO: organization and location master data.
- HCP: provider identifiers, names, licenses, and addresses.
- Member: patient demographics and payer context.
- Products: healthcare or pharma product catalog.

Reference domains:
- ICD-9-CM, ICD-10-CM, and mappings
- Taxonomy groupings, classifications, specializations
- Specialties and coverage/payer references

For a detailed list of entities and attributes, see [model structure](./model_structure.md).

## Common journey by persona

### Data Steward
1) Load data via publishers or jobs.
2) Review validation results.
3) Resolve duplicates and merge.
4) Maintain reference data as needed.
5) Confirm golden records.

### Business User
1) Explore curated masters and encounters.
2) Use taxonomy and ICD references for rollups.
3) Share insights with stewardship for data corrections.

## Data quality and enrichment

The model includes:
- Fuzzy matching for HCO, HCP, Member, and Products.
- Survivorship rules for golden record consolidation.
- Enrichers for normalization, phoneticization, geocoding, and third-party lookups.
- Validations that enforce required fields and business rules.

Details:
- Enrichers: [enrichers](./enrichers.md)
- Validations: [validations](./validations.md)

## Tips for success

- Start with the workflows mapped to your persona; they align navigation and permissions.
- Address validation failures before duplicate resolution to avoid rework.
- Keep reference data up to date to improve matching quality and analytics.
- When adding new sources, validate enrichers and external keys in lower environments first.
