# Merchant Model — User Guide

## Overview

The Merchant Party Data Model provides a single, authoritative view of merchants while remaining flexible for multiple business roles, legal structures, and lifecycle states. It separates identity from business role to enable accurate master data management, reduce duplication, and scale over time — aligning with enterprise MDM best practices for banking, payments, marketplaces, and B2B platforms.

## Core design principle — A Merchant is not an identity; a Party is

- Party: the real-world actor (person or organization), stable over time and independently identifiable.
- Merchant: a business role describing how a Party participates commercially. Merchant has its own lifecycle, status, and role-specific attributes and can be added, changed, or terminated without changing Party identity.

This separation models real-world behavior rather than application UI artifacts.

## High-level entity roles

- Party (Core identity)  
  Unified identity layer, common naming/status/lifecycle, entry point for matching and survivorship. A Party resolves to either an Individual or a Legal Entity.

- Individual  
  Natural person attributes (name, DOB, gender). Used for sole proprietors, representatives, or individuals acting as merchants.

- Legal Entity  
  Organization-level attributes: registered business details, regulatory/tax IDs, incorporation info.

- Merchant  
  The commercial role for a Party: onboarding/activation details, merchant codes, hierarchies, industry classification, parent–child relationships. A Party may have zero, one, or many Merchant roles over time.

- Product  
  Offerings owned by a Merchant. Products cannot exist independently of a Merchant and enable merchant-level product management and reporting.


- Enrichers and validations have dedicated docs for clarity:
  - `documentation/enrichers.md` — Enricher descriptions, examples, and guidelines.
  - `documentation/validations.md` — Validation rules, plugin notes, and best practices.
- Industry, SubIndustry — industry taxonomy and mappings.
- ContactRole — lookup entity for contact roles.

## Entity details (high level)

- Merchant
  - Type: `FUZZY_MATCHED`
  - Keys: `MerchantID` (LongInteger)
  - Notes: matcher uses `TaxID` for exact matching; golden ID generated via sequence.

- PartyAddress
  - Type: `BASIC`
  - Keys: `AddressID` (LongInteger)
  - Notes: contains `Enriched*` fields and geolocation (`EnrichedLatitude`, `EnrichedLongitude`).

- PartyContact
  - Type: `FUZZY_MATCHED`
  - Keys: `PartyContactID` (LongInteger)
  - Notes: stores email and phone attributes; consider plugin validation for `Email`.

- Product / ProductCategory
  - Product has `ProductID`, `ProductName`, `Description`.
  - ProductCategory contains hierarchical categories and an active flag.


## Enrichers and validations

Enrichers and validations have dedicated docs for clarity; see:

- `documentation/enrichers.md` — Enricher descriptions, examples, and guidelines.
- `documentation/validations.md` — Validation rules, plugin notes, and best practices.

## References (relationships)

- References model foreign-key links between entities. Examples:

 - `PartyAddress.Reference.seml` — links `PartyAddress` → `Party` (addresses tied to parties).
 - `PartyHasContact.Reference.seml` — links `PartyContact` → `Party`.
 - `ProductsBelongToMerchant.Reference.seml` — links `Product` → `Merchant` (product ownership).

All references are in `src/Merchant/references`.

## Publishers and Survivorship

- Publishers are used for ranking in survivorship rules; check `model_priv_grants` and `publishers` folders for definitions.
- Survivorship strategy is often `PREFERRED_PUBLISHER`; inspect `survivorship_rules` for attribute-level functions.

## Jobs and Data Loads

- Model jobs (`*.ModelJob.seml`) live at `src/Merchant` root. Examples: `LoadCountry.ModelJob.seml`, `LoadContactRoles.ModelJob.seml`.
- Always review source mappings and connector configs before executing a job.

## Naming and conventions

- Physical names are defined in `physicalName` in attribute definitions. Use them for database mappings.
- Use `Enriched*` prefixes for enricher outputs and store source values separately when possible.
- LOVs: check `src/Merchant/list_of_values` for controlled vocabularies used as data types.

## Developer workflow

1. Edit SEML files in `src/Merchant` locally.
2. Validate changes (Semarchy tools or platform checks).
3. Commit on a feature branch and open a PR to `MerchantMaster` with description of changes and test results.

## Appendix — useful references

- Model structure: `documentation/model-structure.md`
- Enrichers: `src/Merchant/entities/*/enrichers/*`
- Validations: `src/Merchant/entities/*/validations/*`
- References: `src/Merchant/references/*.Reference.seml`
- Jobs: `src/Merchant/*.ModelJob.seml`

---
