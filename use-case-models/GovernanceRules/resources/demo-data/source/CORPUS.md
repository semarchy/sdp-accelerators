# GovernanceRules seed corpus

Review of the starting corpus of the GovernanceRules data product (publisher SEED), generated from the JSON files of this folder.
Codes, attribute names and lists of values follow `DESIGN.md`. Nothing has been loaded to a tenant.

Scope rows read as *domain + classification + attribute type*; a missing dimension means "any", and `any` alone means the rule applies to every design. A rule applies when any of its rows matches.
Rule codes `xx-1nn` form the **pharma extension** (policy POL-GXP): every one of their scope rows names a pharma domain (MEDICINAL_PRODUCT, HCP, CLINICAL_SITE) or a pharma attribute type (NDC, NPI, HCP_LICENSE_NUMBER, MPID, PHPID, TRANSFER_OF_VALUE), so they never reach a non-pharma design.

## Counts

| File | Rows |
|---|---|
| GovernanceRule.json | 71 |
| RuleScope.json | 133 |
| RuleCitation.json | 146 |
| GovernancePolicy.json | 6 |
| GovernanceBody.json | 5 |
| Regulation.json | 26 |
| DataDomain.json | 11 |
| DataClassification.json | 6 |
| BusinessAttributeType.json | 27 |

Rules: 56 generic + 15 pharma extension. By status: APPROVED 65, DRAFT 2, IN_REVIEW 2, RETIRED 2. By level: MAY 1, MUST 53, SHOULD 17.

| Category | Generic | Pharma | MUST | SHOULD | MAY |
|---|---|---|---|---|---|
| Data quality (DQ-) | 8 | 4 | 9 | 3 | 0 |
| Privacy (PRIV-) | 8 | 2 | 9 | 1 | 0 |
| Security and access (SEC-) | 5 | 3 | 7 | 1 | 0 |
| Retention (RET-) | 5 | 2 | 6 | 0 | 1 |
| Reference data (REF-) | 6 | 2 | 7 | 1 | 0 |
| Identity and matching (MDM-) | 5 | 1 | 3 | 3 | 0 |
| Metadata and documentation (META-) | 5 | 0 | 3 | 2 | 0 |
| AI usage (AI-) | 5 | 0 | 4 | 1 | 0 |
| Stewardship (STW-) | 4 | 1 | 3 | 2 | 0 |
| Modeling conventions (MOD-) | 5 | 0 | 2 | 3 | 0 |

## Demo step 1.1 - rules supporting the cross-domain rule and attribute

The design agent changing the Customer and Product models should find and cite these rules:

| Need in the demo | Rules |
|---|---|
| Country codes validated against a managed ISO 3166-1 alpha-2 reference | REF-001 (+ MOD-004 to bind the attribute to COUNTRY_CODE) |
| Product descriptions in each market's official languages (Canada: English and French) | DQ-006, REF-003 |
| Every new attribute documented for people and AI agents, citing rule codes | META-001, META-002 |
| Personal data attributes hidden from roles without a need to know | PRIV-002 (+ PRIV-001 classification, AI-004 for agent roles) |
| Derived rule: an active B2B account must have a billing organisation in an approved country | DQ-002 (status requires mandatory relationships) + MDM-003 (explicit BillingOrganization reference) + REF-001 (managed Country reference) + REF-004 (country approval flag in the Country reference) |
| Draft and retired rules never reach the agent | PRIV-008, MOD-005 (DRAFT), MDM-005, AI-005 (IN_REVIEW), DQ-007, RET-005 (RETIRED) |

## Rules by category

### Data quality (DQ-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| DQ-001 | MUST | APPROVED | Completeness rules enforced at certification | VALIDATION | any | ISO-8000 ISO 8000-8; DAMA-DMBOK DMBOK2, Ch. 13 Data Quality |
| DQ-002 | MUST | APPROVED | Active records require their mandatory relationships | VALIDATION | CUSTOMER; SUPPLIER; PRODUCT | ISO-8000 ISO 8000-8; BCBS-239 Principle 3 - Accuracy and integrity; BCBS-239 Principle 4 - Completeness |
| DQ-003 | MUST | APPROVED | Typed attributes conform to their format | VALIDATION | any | ISO-8000 ISO 8000-110 |
| DQ-004 | MUST | APPROVED | Check digits of standard identifiers are verified | VALIDATION | GTIN; IBAN; LEI | GS1-GTIN GS1 General Specifications - GTIN check digit calculation; ISO-13616 ISO 13616-1 - IBAN check digits; ISO-17442 ISO 17442-1 - LEI check digits |
| DQ-005 | SHOULD | APPROVED | Phone numbers normalised to E.164 | ENRICHER | PHONE_NUMBER | ITU-T-E164 E.164 number structure |
| DQ-006 | MUST | APPROVED | Product descriptions in the official languages of each market | VALIDATION | PRODUCT; PRODUCT_DESCRIPTION | CA-CPLA Consumer Packaging and Labelling Regulations, C.R.C., c. 417, s. 6; QC-CFL s. 51; QC-CFL s. 52; ISO-639 Two-letter language identifiers (ISO 639 Set 1) |
| DQ-007 | SHOULD | RETIRED | Phone numbers stored in national format | VALIDATION | PHONE_NUMBER | ITU-T-E164 E.164 number structure |
| DQ-008 | MUST | APPROVED | Dates and timestamps exchanged in ISO 8601 | VALIDATION | DATE; TIMESTAMP; DATE_OF_BIRTH | ISO-8601 ISO 8601-1:2019, extended format |

### Privacy (PRIV-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| PRIV-001 | MUST | APPROVED | Every attribute is classified | DESCRIPTION_AI_INSTRUCTION | any | GDPR Art. 4(1); GDPR Art. 30; ISO-IEC-27001 Annex A 5.12 |
| PRIV-002 | MUST | APPROVED | Personal data hidden from roles without a need to know | PRIVILEGE_ROW_FILTER | PERSONAL; SENSITIVE_PERSONAL; PHI | GDPR Art. 25(2); GDPR Art. 32(1)(b) and 32(4); ISO-IEC-27001 Annex A 8.3; CCPA-CPRA Cal. Civ. Code 1798.100 |
| PRIV-003 | MUST | APPROVED | Personal attributes have a documented purpose | DESCRIPTION_AI_INSTRUCTION | PERSONAL; SENSITIVE_PERSONAL | GDPR Art. 5(1)(b); GDPR Art. 5(1)(c); CCPA-CPRA Cal. Civ. Code 1798.100 |
| PRIV-004 | MUST | APPROVED | Sensitive personal data require DPO approval | WORKFLOW | SENSITIVE_PERSONAL | GDPR Art. 9; GDPR Art. 35; CCPA-CPRA Cal. Civ. Code 1798.121 |
| PRIV-005 | MUST | APPROVED | Data subject requests are executable on golden records | WORKFLOW | CUSTOMER + PERSONAL; EMPLOYEE + PERSONAL | GDPR Art. 15; GDPR Art. 16; GDPR Art. 17; CCPA-CPRA Cal. Civ. Code 1798.105, 1798.106, 1798.110 |
| PRIV-006 | MUST | APPROVED | Consents and opt-outs are recorded with evidence | VALIDATION | CUSTOMER + PERSONAL | GDPR Art. 7(1); CCPA-CPRA Cal. Civ. Code 1798.120 |
| PRIV-007 | MUST | APPROVED | No real personal data in non-production data locations | ENRICHER | PERSONAL; SENSITIVE_PERSONAL | GDPR Art. 25(1); GDPR Art. 32(1)(a); ISO-IEC-27001 Annex A 8.11; ISO-IEC-27001 Annex A 8.33 |
| PRIV-008 | SHOULD | DRAFT | Hosting region of personal data documented | DESCRIPTION_AI_INSTRUCTION | PERSONAL | GDPR Art. 44-49 (Chapter V) |

### Security and access (SEC-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| SEC-001 | MUST | APPROVED | Least privilege for every role | PRIVILEGE_ROW_FILTER | any | ISO-IEC-27001 Annex A 5.15; ISO-IEC-27001 Annex A 5.18; GDPR Art. 32(1) |
| SEC-002 | MUST | APPROVED | Dedicated technical roles for integrations and AI agents | PRIVILEGE_ROW_FILTER | any | ISO-IEC-27001 Annex A 5.16; ISO-IEC-27001 Annex A 8.2; ISO-IEC-27001 Annex A 8.3 |
| SEC-003 | SHOULD | APPROVED | Row filters for country or business-unit segregation | PRIVILEGE_ROW_FILTER | CUSTOMER; EMPLOYEE; FINANCE | ISO-IEC-27001 Annex A 8.3; GDPR Art. 25(2) |
| SEC-004 | MUST | APPROVED | Segregation of duties in approval workflows | WORKFLOW | any | ISO-IEC-27001 Annex A 5.3 |
| SEC-005 | MUST | APPROVED | Bank account and government identifiers masked by default | PRIVILEGE_ROW_FILTER | IBAN; NATIONAL_ID | ISO-IEC-27001 Annex A 8.11; GDPR Art. 32(1) |

### Retention (RET-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| RET-001 | MUST | APPROVED | Retention period defined for personal data | RETENTION_POLICY | PERSONAL; SENSITIVE_PERSONAL | GDPR Art. 5(1)(e); CCPA-CPRA Cal. Civ. Code 1798.100; ISO-IEC-27001 Annex A 8.10 |
| RET-002 | MUST | APPROVED | Reporting master data historized | RETENTION_POLICY | FINANCE; CUSTOMER; SUPPLIER | BCBS-239 Principle 3 - Accuracy and integrity; ISO-IEC-27001 Annex A 5.33 |
| RET-003 | MUST | APPROVED | Source, staging and error records follow golden retention | RETENTION_POLICY | PERSONAL; SENSITIVE_PERSONAL | GDPR Art. 5(1)(e); GDPR Art. 17 |
| RET-004 | MUST | APPROVED | Erasure covers history | WORKFLOW | PERSONAL | GDPR Art. 17(1) and 17(3)(b); ISO-IEC-27001 Annex A 8.10 |
| RET-005 | MAY | RETIRED | Archive golden records after ten years | RETENTION_POLICY | any | DAMA-DMBOK DMBOK2, Ch. 9 Document and Content Management |

### Reference data (REF-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| REF-001 | MUST | APPROVED | Country codes validated against the managed ISO 3166-1 reference | REFERENCE_ENTITY | COUNTRY_CODE; LOCATION; REFERENCE | ISO-3166-1 Alpha-2 code elements; DAMA-DMBOK DMBOK2, Ch. 10 Reference and Master Data |
| REF-002 | MUST | APPROVED | Currencies as ISO 4217 codes | REFERENCE_ENTITY | CURRENCY_CODE; MONETARY_AMOUNT | ISO-4217 Alphabetic code and minor unit |
| REF-003 | MUST | APPROVED | Languages as ISO 639 codes | REFERENCE_ENTITY | LANGUAGE_CODE; PRODUCT_DESCRIPTION | ISO-639 Two-letter language identifiers (ISO 639 Set 1, formerly ISO 639-1) |
| REF-004 | MUST | APPROVED | Country eligibility governed in the Country reference | REFERENCE_ENTITY | COUNTRY_CODE; REFERENCE; CUSTOMER; SUPPLIER | ISO-3166-1 Alpha-2 code elements; DAMA-DMBOK DMBOK2, Ch. 10 Reference and Master Data |
| REF-005 | SHOULD | APPROVED | Reference entities rather than lists of values for shared code sets | REFERENCE_ENTITY | REFERENCE; any | DAMA-DMBOK DMBOK2, Ch. 10 Reference and Master Data; ISO-IEC-11179 ISO/IEC 11179-3 |
| REF-006 | MUST | APPROVED | Changes to shared reference data are approved and historized | WORKFLOW | REFERENCE | DAMA-DMBOK DMBOK2, Ch. 10 Reference and Master Data; ISO-IEC-27001 Annex A 8.32 |

### Identity and matching (MDM-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| MDM-001 | MUST | APPROVED | Golden records keep their source cross-references | MATCHING_SURVIVORSHIP | CUSTOMER; SUPPLIER; PRODUCT; EMPLOYEE; SOURCE_ID | BCBS-239 Principle 2 - Data architecture and IT infrastructure; DAMA-DMBOK DMBOK2, Ch. 10 Reference and Master Data |
| MDM-002 | SHOULD | APPROVED | Organisations matched on registered identifiers first | MATCHING_SURVIVORSHIP | CUSTOMER + LEI; SUPPLIER + LEI; CUSTOMER + VAT_NUMBER; SUPPLIER + VAT_NUMBER; FINANCE + LEI | ISO-17442 ISO 17442-1; ISO-8000 ISO 8000-115 |
| MDM-003 | MUST | APPROVED | B2B accounts reference their organisation and billing organisation | VALIDATION | CUSTOMER | BCBS-239 Principle 2 - Data architecture and IT infrastructure; DAMA-DMBOK DMBOK2, Ch. 10 Reference and Master Data |
| MDM-004 | SHOULD | APPROVED | Survivorship rules documented per attribute | MATCHING_SURVIVORSHIP | CUSTOMER; SUPPLIER; PRODUCT; EMPLOYEE | GDPR Art. 5(1)(d); DAMA-DMBOK DMBOK2, Ch. 10 Reference and Master Data |
| MDM-005 | SHOULD | IN_REVIEW | Person merges below the confidence threshold are reviewed | MATCHING_SURVIVORSHIP | CUSTOMER + PERSONAL; EMPLOYEE + PERSONAL | GDPR Art. 5(1)(d); GDPR Art. 5(1)(f) |

### Metadata and documentation (META-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| META-001 | MUST | APPROVED | Every new object documented for people and AI agents | DESCRIPTION_AI_INSTRUCTION | any | ISO-IEC-11179 ISO/IEC 11179-4; DAMA-DMBOK DMBOK2, Ch. 12 Metadata Management |
| META-002 | MUST | APPROVED | Implemented rule codes cited in the design | DESCRIPTION_AI_INSTRUCTION | any | GDPR Art. 5(2); DAMA-DMBOK DMBOK2, Ch. 3 Data Governance |
| META-003 | SHOULD | APPROVED | Definitions follow the business glossary | DESCRIPTION_AI_INSTRUCTION | any | ISO-IEC-11179 ISO/IEC 11179-4 |
| META-004 | SHOULD | APPROVED | Source and transformation of loaded attributes documented | DESCRIPTION_AI_INSTRUCTION | any | BCBS-239 Principle 2 - Data architecture and IT infrastructure; DAMA-DMBOK DMBOK2, Ch. 12 Metadata Management |
| META-005 | MUST | APPROVED | Business owner and steward named for each entity | DESCRIPTION_AI_INSTRUCTION | any | DAMA-DMBOK DMBOK2, Ch. 3 Data Governance; ISO-IEC-27001 Annex A 5.9 |

### AI usage (AI-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| AI-001 | MUST | APPROVED | AI agents use governed interfaces only | PRIVILEGE_ROW_FILTER | any | ISO-IEC-27001 Annex A 5.15; ISO-IEC-27001 Annex A 8.2 |
| AI-002 | MUST | APPROVED | AI agents read only approved, in-force content | PRIVILEGE_ROW_FILTER | any | EU-AI-ACT Art. 10(2)-(3); DAMA-DMBOK DMBOK2, Ch. 3 Data Governance |
| AI-003 | MUST | APPROVED | Human approval of AI-proposed changes | WORKFLOW | any | EU-AI-ACT Art. 14 |
| AI-004 | MUST | APPROVED | No personal data exposed to AI agents without approval | PRIVILEGE_ROW_FILTER | PERSONAL; SENSITIVE_PERSONAL; PHI | GDPR Art. 5(1)(b); GDPR Art. 25; GDPR Art. 35 |
| AI-005 | SHOULD | IN_REVIEW | Quality of master data used to train or evaluate AI documented | DESCRIPTION_AI_INSTRUCTION | any | EU-AI-ACT Art. 10(2)-(3) |

### Stewardship (STW-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| STW-001 | MUST | APPROVED | Data quality errors routed to a steward | WORKFLOW | any | ISO-8000 ISO 8000-61; DAMA-DMBOK DMBOK2, Ch. 16 Data Management Organization and Role Expectations |
| STW-002 | MUST | APPROVED | High-impact changes approved through a workflow | WORKFLOW | CUSTOMER; SUPPLIER; FINANCE | ISO-IEC-27001 Annex A 8.32; DAMA-DMBOK DMBOK2, Ch. 10 Reference and Master Data |
| STW-003 | SHOULD | APPROVED | Duplicate suggestions resolved within ten business days | WORKFLOW | CUSTOMER; SUPPLIER; PRODUCT | ISO-8000 ISO 8000-61 |
| STW-004 | SHOULD | APPROVED | Data quality reviewed monthly | WORKFLOW | any | ISO-8000 ISO 8000-61; DAMA-DMBOK DMBOK2, Ch. 13 Data Quality |

### Modeling conventions (MOD-)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| MOD-001 | MUST | APPROVED | Entity and attribute naming | NAMING_CONVENTION | any | ISO-IEC-11179 ISO/IEC 11179-5; DAMA-DMBOK DMBOK2, Ch. 5 Data Modeling and Design |
| MOD-002 | MUST | APPROVED | Codes and references named by their business role | NAMING_CONVENTION | any | ISO-IEC-11179 ISO/IEC 11179-5; DAMA-DMBOK DMBOK2, Ch. 5 Data Modeling and Design |
| MOD-003 | SHOULD | APPROVED | Boolean attributes named as predicates | NAMING_CONVENTION | any | ISO-IEC-11179 ISO/IEC 11179-5 |
| MOD-004 | SHOULD | APPROVED | New attributes bound to a business attribute type | NAMING_CONVENTION | any | ISO-IEC-11179 ISO/IEC 11179-3; DAMA-DMBOK DMBOK2, Ch. 5 Data Modeling and Design |
| MOD-005 | SHOULD | DRAFT | Status attributes with a documented lifecycle | REFERENCE_ENTITY | any | DAMA-DMBOK DMBOK2, Ch. 5 Data Modeling and Design |

## Pharma extension (POL-GXP)

| Code | Level | Status | Title | Pattern | Scope (domain + classification + type) | Citations |
|---|---|---|---|---|---|---|
| DQ-101 | MUST | APPROVED | National Drug Codes valid and listed | VALIDATION | MEDICINAL_PRODUCT + NDC; NDC | FDA-NDC 21 CFR 207.33 |
| DQ-102 | MUST | APPROVED | National Provider Identifiers verified | VALIDATION | HCP + NPI; NPI | HIPAA-NPI 45 CFR 162.406 |
| DQ-103 | MUST | APPROVED | Covered recipient data complete for Open Payments | VALIDATION | HCP + TRANSFER_OF_VALUE; HCP + HCP_LICENSE_NUMBER | SUNSHINE-ACT 42 U.S.C. 1320a-7h(a); SUNSHINE-ACT 42 CFR 403.904 |
| DQ-104 | SHOULD | APPROVED | Built-in checks on manual entry of critical GxP data | VALIDATION | MEDICINAL_PRODUCT; CLINICAL_SITE | EU-GMP-ANNEX-11 Section 6 - Accuracy checks; EU-GMP-ANNEX-11 Section 5 - Data |
| PRIV-101 | MUST | APPROVED | No protected health information in HCP and site master data | PRIVILEGE_ROW_FILTER | HCP + PHI; CLINICAL_SITE + PHI; HCP; CLINICAL_SITE | HIPAA 45 CFR 164.502(b); HIPAA 45 CFR 164.514(d); HIPAA 45 CFR 164.312(a)(1) |
| PRIV-102 | MUST | APPROVED | HCP data processed as personal data | DESCRIPTION_AI_INSTRUCTION | HCP | GDPR Art. 6(1)(f); GDPR Art. 14 |
| SEC-101 | MUST | APPROVED | Access and authority checks for GxP master data | PRIVILEGE_ROW_FILTER | MEDICINAL_PRODUCT; CLINICAL_SITE | 21-CFR-11 21 CFR 11.10(d); 21-CFR-11 21 CFR 11.10(g); EU-GMP-ANNEX-11 Section 12 - Security |
| SEC-102 | MUST | APPROVED | Audit trail with reason for change on GxP master data | WORKFLOW | MEDICINAL_PRODUCT; CLINICAL_SITE | 21-CFR-11 21 CFR 11.10(e); EU-GMP-ANNEX-11 Section 9 - Audit trails |
| SEC-103 | MUST | APPROVED | Electronic signature of GxP approvals | WORKFLOW | MEDICINAL_PRODUCT; CLINICAL_SITE | 21-CFR-11 21 CFR 11.50; 21-CFR-11 21 CFR 11.70; EU-GMP-ANNEX-11 Section 14 - Electronic signature |
| RET-101 | MUST | APPROVED | GxP master data and audit trail retained and readable | RETENTION_POLICY | MEDICINAL_PRODUCT; CLINICAL_SITE | 21-CFR-11 21 CFR 11.10(c); EU-GMP-ANNEX-11 Section 7 - Data storage; EU-GMP-ANNEX-11 Section 17 - Archiving |
| RET-102 | MUST | APPROVED | Open Payments records retained | RETENTION_POLICY | HCP + TRANSFER_OF_VALUE; TRANSFER_OF_VALUE | SUNSHINE-ACT 42 CFR Part 403, Subpart I |
| REF-101 | MUST | APPROVED | Medicinal products identified with IDMP identifiers | REFERENCE_ENTITY | MEDICINAL_PRODUCT; MPID; PHPID | ISO-11615 ISO 11615; ISO-11616 ISO 11616 |
| REF-102 | MUST | APPROVED | IDMP controlled vocabularies as managed references | REFERENCE_ENTITY | MEDICINAL_PRODUCT | ISO-11615 ISO 11615; ISO-11616 ISO 11616 |
| MDM-101 | MUST | APPROVED | HCPs matched on NPI and licence first | MATCHING_SURVIVORSHIP | HCP; NPI; HCP_LICENSE_NUMBER | HIPAA-NPI 45 CFR 162.406; SUNSHINE-ACT 42 CFR 403.904 |
| STW-101 | MUST | APPROVED | GxP data product validated and under change control | WORKFLOW | MEDICINAL_PRODUCT; CLINICAL_SITE | 21-CFR-11 21 CFR 11.10(a); EU-GMP-ANNEX-11 Section 4 - Validation; EU-GMP-ANNEX-11 Section 10 - Change and configuration management |

## Rule statements

Normative text of every rule, for review.

- **DQ-001** (MUST, APPROVED, POL-DQ, owner DQO) - Attributes required for a record to be used MUST be enforced by validations that run before the record is certified, and the validation message MUST name the missing attribute in business terms.
- **DQ-002** (MUST, APPROVED, POL-DQ, owner DQO) - A master record MUST NOT reach an active, released or approved status unless every relationship that this status requires references an existing golden record (for example the billing organisation of an active B2B account, the supplier of an active purchased item).
- **DQ-003** (MUST, APPROVED, POL-DQ, owner DQO) - Every attribute bound to a business attribute type that defines a format pattern MUST be validated against that pattern, after normalisation by enrichers and before certification.
- **DQ-004** (MUST, APPROVED, POL-DQ, owner DQO) - Identifiers that carry a check digit defined by their standard (GTIN, IBAN, LEI) MUST have the check digit verified before the record is certified.
- **DQ-005** (SHOULD, APPROVED, POL-DQ, owner DQO) - Telephone numbers SHOULD be normalised to the E.164 international format by an enricher, keeping the original value as entered only when a consuming process needs it.
- **DQ-006** (MUST, APPROVED, POL-DQ, owner DQO) - A consumer-facing product description MUST be provided in every official language required in each market where the product is sold; for Canada the description MUST exist in both English and French, and for Quebec no other language MAY be given greater prominence than French.
- **DQ-007** (SHOULD, RETIRED, POL-DQ, owner DQO) - Telephone numbers SHOULD be stored in the national format of the country of the record, without the international prefix.
- **DQ-008** (MUST, APPROVED, POL-DQ, owner DQO) - Dates and timestamps MUST be stored in date or timestamp datatypes and, when exchanged as text through APIs, files or named queries, MUST use the ISO 8601 extended format with an explicit UTC offset for timestamps.
- **PRIV-001** (MUST, APPROVED, POL-PRIV, owner DPO) - Every attribute of a data product MUST be assigned a data classification before deployment, and any attribute that relates to an identified or identifiable natural person MUST be classified PERSONAL or higher.
- **PRIV-002** (MUST, APPROVED, POL-PRIV, owner DPO) - Attributes classified PERSONAL or SENSITIVE_PERSONAL MUST NOT be readable by roles without a documented need to know; by default business, integration and AI agent roles MUST receive no privilege on these attributes, and access MUST be granted explicitly per role.
- **PRIV-003** (MUST, APPROVED, POL-PRIV, owner DPO) - A personal data attribute MUST only be added to a data product when its purpose is documented, and it MUST be limited to what is necessary for that purpose.
- **PRIV-004** (MUST, APPROVED, POL-PRIV, owner DPO) - Sensitive personal data (special categories, government identifiers, health data) MUST NOT be added to a master data product unless a data protection impact assessment has been approved by the Data Protection Office.
- **PRIV-005** (MUST, APPROVED, POL-PRIV, owner DPO) - Data products holding personal data of customers or employees MUST support access, rectification and erasure requests on the golden record and all its source records, through a traceable process.
- **PRIV-006** (MUST, APPROVED, POL-PRIV, owner DPO) - Marketing consents and opt-outs MUST be recorded per person, purpose and channel with their source, date and status, so that the consent in force can be demonstrated at any time.
- **PRIV-007** (MUST, APPROVED, POL-PRIV, owner DPO) - Personal data loaded into development, test or demo data locations MUST be synthetic or pseudonymised; production extracts of personal data MUST NOT be loaded unchanged.
- **PRIV-008** (SHOULD, DRAFT, POL-PRIV, owner DPO) - Data products holding personal data SHOULD document the region where the data are hosted and every consuming system located outside the European Economic Area, with the transfer mechanism used.
- **SEC-001** (MUST, APPROVED, POL-SEC, owner ISEC) - Every role of a data product MUST be granted only the privileges its persona needs; no business role MAY hold full update and delete privileges on all entities.
- **SEC-002** (MUST, APPROVED, POL-SEC, owner ISEC) - Integrations and AI agents MUST connect with dedicated technical roles distinct from human roles, read-only unless they publish data, and limited to the entities and attributes their use case needs.
- **SEC-003** (SHOULD, APPROVED, POL-SEC, owner ISEC) - When users only need the records of their country, region or business unit, their role SHOULD be restricted with a row filter rather than given access to all records.
- **SEC-004** (MUST, APPROVED, POL-SEC, owner ISEC) - The person who submits a change requiring approval MUST NOT be the person who approves it.
- **SEC-005** (MUST, APPROVED, POL-SEC, owner ISEC) - Bank account numbers and government identifiers MUST be hidden from every role except the roles that execute payments, payroll or regulatory reporting.
- **RET-001** (MUST, APPROVED, POL-SEC, owner DPO) - Every entity holding personal data MUST have a defined retention period and an end-of-retention action (deletion or anonymisation), documented with its legal or business basis.
- **RET-002** (MUST, APPROVED, POL-SEC, owner ISEC) - Master data used in financial or regulatory reporting MUST be historized so that any reported figure can be traced to the version of the golden record in force at the reporting date.
- **RET-003** (MUST, APPROVED, POL-SEC, owner DPO) - Source records, load history and rejected records containing personal data MUST be purged on the same schedule as the corresponding golden records.
- **RET-004** (MUST, APPROVED, POL-SEC, owner DPO) - When personal data must be erased, the erasure MUST also remove or anonymise the data in the history of the golden record, unless a legal obligation requires keeping it.
- **RET-005** (MAY, RETIRED, POL-SEC, owner ISEC) - Golden records inactive for ten years MAY be archived to the data lake and removed from the data product.
- **REF-001** (MUST, APPROVED, POL-DQ, owner DQO) - Every country attribute MUST hold an ISO 3166-1 alpha-2 code and MUST be a reference to the managed Country reference entity; free-text countries and local lists of values MUST NOT be used.
- **REF-002** (MUST, APPROVED, POL-DQ, owner DQO) - Every currency attribute MUST hold an ISO 4217 alphabetic code referencing the managed Currency reference entity, and every monetary amount MUST be stored with its currency.
- **REF-003** (MUST, APPROVED, POL-DQ, owner DQO) - Every language attribute, including the language of multilingual texts, MUST hold a two-letter ISO 639 code referencing the managed Language reference entity.
- **REF-004** (MUST, APPROVED, POL-DQ, owner DGC) - The list of countries approved for doing business MUST be maintained as governed reference data, as an approval attribute of the managed Country reference; any rule that depends on country eligibility MUST read it from there and MUST NOT hard-code country lists.
- **REF-005** (SHOULD, APPROVED, POL-DQ, owner DQO) - Code sets that carry attributes, are shared by several data products or change outside release cycles SHOULD be modelled as reference entities; lists of values MAY be used for small, stable, internal code sets.
- **REF-006** (MUST, APPROVED, POL-DQ, owner DQO) - Changes to reference data shared across data products MUST be approved by the reference data owner before they take effect and MUST be historized.
- **MDM-001** (MUST, APPROVED, POL-DQ, owner DQO) - Every golden record MUST keep the identifiers of all the source records it consolidates, so that any value can be traced to its source and returned to the source systems.
- **MDM-002** (SHOULD, APPROVED, POL-DQ, owner DQO) - Organisations SHOULD be matched first on registered identifiers (LEI, then tax registration number with its country) and only then on fuzzy name and address rules.
- **MDM-003** (MUST, APPROVED, POL-DQ, owner DQO) - Every B2B customer account MUST reference the organisation golden record of its legal entity, and its billing organisation MUST be held as an explicit reference with a business role name, not inferred from addresses.
- **MDM-004** (SHOULD, APPROVED, POL-DQ, owner DQO) - Survivorship SHOULD be defined per attribute or attribute group with a documented source ranking or recency rule, and personal contact data SHOULD survive from the most recently verified source.
- **MDM-005** (SHOULD, IN_REVIEW, POL-DQ, owner DQO) - Merges of records describing natural persons SHOULD be confirmed automatically only above a high match score; lower-score suggestions SHOULD be reviewed by a steward, and every merge MUST be reversible.
- **META-001** (MUST, APPROVED, POL-META, owner DGC) - Every entity, attribute, reference, validation and named query added to a data product MUST carry a business description written for both people and AI agents, stating meaning, format or unit, and classification; when correct use is not obvious, the description MUST include an 'AI agent instructions:' paragraph.
- **META-002** (MUST, APPROVED, POL-META, owner DGC) - Every model object that implements a governance rule MUST cite the rule code in its description.
- **META-003** (SHOULD, APPROVED, POL-META, owner DGC) - Labels and definitions SHOULD use the terms of the business glossary and SHOULD state what the object is, not how it is used or computed.
- **META-004** (SHOULD, APPROVED, POL-META, owner DGC) - Attributes fed by integrations SHOULD document their source systems and any transformation applied by enrichers.
- **META-005** (MUST, APPROVED, POL-META, owner DGC) - Every master entity MUST name its accountable business owner and its steward role in its description or in the data product documentation.
- **AI-001** (MUST, APPROVED, POL-AI, owner DGC) - AI agents MUST access master data only through governed interfaces (data product MCP server, named queries, REST API) with a dedicated role, and MUST NOT receive database credentials or human user accounts.
- **AI-002** (MUST, APPROVED, POL-AI, owner DGC) - AI agent roles MUST be restricted by row filters to approved, in-force records (golden data, approved rules, active reference values); drafts, rejected and retired records MUST NOT reach an agent.
- **AI-003** (MUST, APPROVED, POL-AI, owner DGC) - Changes to a data product model or to golden data proposed by an AI agent MUST be reviewed and approved by an accountable person before deployment or certification.
- **AI-004** (MUST, APPROVED, POL-AI, owner DPO) - Attributes classified PERSONAL or higher MUST NOT be exposed to AI agent roles unless the purpose is documented and approved by the Data Protection Office.
- **AI-005** (SHOULD, IN_REVIEW, POL-AI, owner DGC) - Master data sets used to train, validate or test AI systems SHOULD be documented with their origin, preparation steps, known gaps and data quality measures.
- **STW-001** (MUST, APPROVED, POL-META, owner DQO) - Every master entity MUST have a steward role that receives its data quality errors and duplicate suggestions as tasks.
- **STW-002** (MUST, APPROVED, POL-META, owner DQO) - Changes with high business impact (deactivation of a customer or supplier, change of legal name, bank details or tax identifiers) MUST be approved through a workflow before they take effect.
- **STW-003** (SHOULD, APPROVED, POL-META, owner DQO) - Duplicate suggestions SHOULD be confirmed or rejected by the steward within ten business days.
- **STW-004** (SHOULD, APPROVED, POL-META, owner DQO) - The data quality of each master entity SHOULD be reviewed monthly by its owner and the Data Quality Office, based on validation errors and completeness measures.
- **MOD-001** (MUST, APPROVED, POL-META, owner DGC) - Entity and attribute names MUST be English, singular, in PascalCase without abbreviations or source-system prefixes, and labels MUST use business language.
- **MOD-002** (MUST, APPROVED, POL-META, owner DGC) - Attributes holding codes MUST end with 'Code', and references MUST be named after the business role of the referenced record (e.g. BillingOrganization, ShipToLocation), never after the target entity with a number.
- **MOD-003** (SHOULD, APPROVED, POL-META, owner DGC) - Boolean attributes SHOULD be named as predicates (Is..., Has..., Can...) and SHOULD NOT allow a third, undefined state unless 'unknown' is meaningful.
- **MOD-004** (SHOULD, APPROVED, POL-META, owner DGC) - A new attribute SHOULD be bound to a business attribute type of the governance catalogue, from which it inherits its default classification, format and reference standard.
- **MOD-005** (SHOULD, DRAFT, POL-META, owner DGC) - Status attributes SHOULD use a governed list of values or reference entity whose allowed transitions are documented, and the meaning of each status SHOULD be described.
- **DQ-101** (MUST, APPROVED, POL-GXP, owner GXPQA) - Every National Drug Code MUST be stored in its hyphenated 10-digit form with a valid 4-4-2, 5-3-2 or 5-4-1 segment configuration and MUST correspond to a drug listing of the labeler.
- **DQ-102** (MUST, APPROVED, POL-GXP, owner GXPQA) - Every NPI MUST be a 10-digit number whose check digit is valid (Luhn formula with the 80840 prefix) and SHOULD be verified against the NPPES registry.
- **DQ-103** (MUST, APPROVED, POL-GXP, owner GXPQA) - A healthcare professional or teaching hospital that receives a transfer of value MUST have the identification data required for Open Payments reporting: name, business address, specialty, NPI and state licence number(s) for physicians and other covered practitioners.
- **DQ-104** (SHOULD, APPROVED, POL-GXP, owner GXPQA) - Manual entry of critical GxP master data (product strength, dose form, site status) SHOULD be protected by built-in checks for correct and secure entry.
- **PRIV-101** (MUST, APPROVED, POL-GXP, owner DPO) - Healthcare professional and clinical site master data MUST NOT store protected health information; when a use case covered by HIPAA requires it, only the minimum necessary PHI MAY be stored and it MUST be restricted to the roles that need it.
- **PRIV-102** (MUST, APPROVED, POL-GXP, owner DPO) - Data about individual healthcare professionals MUST be classified as personal data, with a documented lawful basis and information of the HCP when the data are obtained from third parties.
- **SEC-101** (MUST, APPROVED, POL-GXP, owner GXPQA) - Data products holding GxP master data MUST limit access to authorised individuals and MUST check that a user is authorised before allowing them to create, change, approve or sign a record.
- **SEC-102** (MUST, APPROVED, POL-GXP, owner GXPQA) - Creation, change and deletion of GxP master data MUST be recorded in a secure, computer-generated, time-stamped audit trail that keeps previous values, and the reason for each change MUST be documented.
- **SEC-103** (MUST, APPROVED, POL-GXP, owner GXPQA) - Approvals of GxP master data that replace a handwritten signature MUST be electronic signatures showing the signer's printed name, the date and time and the meaning of the signature, permanently linked to the record.
- **RET-101** (MUST, APPROVED, POL-GXP, owner GXPQA) - GxP master data and their audit trail MUST be retained for the retention period of the GMP or GCP records that depend on them and MUST remain accessible and readable throughout that period.
- **RET-102** (MUST, APPROVED, POL-GXP, owner GXPQA) - Transfers of value and the HCP master data used to report them MUST be retained for at least the record retention period required by the Open Payments regulations (five years from publication).
- **REF-101** (MUST, APPROVED, POL-GXP, owner GXPQA) - Medicinal products MUST carry their IDMP Medicinal Product Identifier and the Pharmaceutical Product Identifier(s) of their pharmaceutical products when assigned by the competent authority.
- **REF-102** (MUST, APPROVED, POL-GXP, owner GXPQA) - Medicinal product attributes that IDMP describes with controlled vocabularies (dose form, route of administration, units, packaging) MUST reference managed reference entities synchronised with the authority's referentials, not free text.
- **MDM-101** (MUST, APPROVED, POL-GXP, owner GXPQA) - Healthcare professionals MUST be matched first on NPI (United States) or licence number with its issuing authority, and only then on fuzzy name and address rules with steward review.
- **STW-101** (MUST, APPROVED, POL-GXP, owner GXPQA) - The configuration of a data product holding GxP master data (model, validations, enrichers, workflows, roles) MUST be validated for its intended use and every change MUST go through documented change control.

## Policies

| Code | Name | Owner | Rules |
|---|---|---|---|
| POL-DQ | Data Quality and Reference Data Policy | DQO | 19 |
| POL-PRIV | Personal Data Protection Policy | DPO | 8 |
| POL-SEC | Data Security and Records Retention Policy | ISEC | 10 |
| POL-META | Metadata, Modeling and Stewardship Policy | DGC | 14 |
| POL-AI | Responsible AI Data Usage Policy | DGC | 5 |
| POL-GXP | GxP and Health Data Extension Policy | GXPQA | 15 |

## Governance bodies

| Code | Name | Type | Contact |
|---|---|---|---|
| DGC | Data Governance Council | COUNCIL | data-governance-council@example.com |
| DPO | Data Protection Office | OFFICE | dpo@example.com |
| DQO | Data Quality Office | OFFICE | data-quality@example.com |
| ISEC | Information Security Office | OFFICE | infosec@example.com |
| GXPQA | GxP Quality Assurance | OFFICE | gxp-qa@example.com |

## Regulations and standards

| Code | Name | Type | Jurisdiction | Cited by |
|---|---|---|---|---|
| GDPR | General Data Protection Regulation (Regulation (EU) 2016/679) | REGULATION | European Union / EEA | 19 rules |
| CCPA-CPRA | California Consumer Privacy Act, as amended by the California Privacy Rights Act | REGULATION | United States - California | 6 rules |
| EU-AI-ACT | Artificial Intelligence Act (Regulation (EU) 2024/1689) | REGULATION | European Union | 3 rules |
| ISO-3166-1 | ISO 3166-1 Codes for the representation of names of countries and their subdivisions - Part 1: Country code | STANDARD | International | 2 rules |
| ISO-4217 | ISO 4217 Codes for the representation of currencies | STANDARD | International | 1 rules |
| ISO-639 | ISO 639 Codes for individual languages and language groups | STANDARD | International | 2 rules |
| ISO-8601 | ISO 8601 Date and time - Representations for information interchange | STANDARD | International | 1 rules |
| ITU-T-E164 | ITU-T Recommendation E.164 The international public telecommunication numbering plan | STANDARD | International | 2 rules |
| ISO-13616 | ISO 13616-1 Financial services - International bank account number (IBAN) | STANDARD | International | 1 rules |
| ISO-17442 | ISO 17442 Financial services - Legal entity identifier (LEI) | STANDARD | International | 2 rules |
| GS1-GTIN | GS1 Global Trade Item Number (GTIN) | STANDARD | International | 1 rules |
| ISO-8000 | ISO 8000 Data quality (series) | STANDARD | International | 7 rules |
| ISO-IEC-11179 | ISO/IEC 11179 Metadata registries (MDR) (series) | STANDARD | International | 7 rules |
| ISO-IEC-27001 | ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection - Information security management systems - Requirements | STANDARD | International | 15 rules |
| BCBS-239 | BCBS 239 Principles for effective risk data aggregation and risk reporting | FRAMEWORK | International (banking) | 5 rules |
| CA-CPLA | Consumer Packaging and Labelling Act (R.S.C. 1985, c. C-38) and Consumer Packaging and Labelling Regulations (C.R.C., c. 417) | REGULATION | Canada | 1 rules |
| QC-CFL | Charter of the French Language (CQLR c. C-11), as amended by Bill 96 (S.Q. 2022, c. 14) | REGULATION | Canada - Quebec | 1 rules |
| DAMA-DMBOK | DAMA-DMBOK: Data Management Body of Knowledge, 2nd edition | FRAMEWORK | International | 21 rules |
| 21-CFR-11 | 21 CFR Part 11 Electronic Records; Electronic Signatures | REGULATION | United States | 5 rules |
| EU-GMP-ANNEX-11 | EudraLex Volume 4, EU GMP Annex 11: Computerised Systems | REGULATION | European Union | 6 rules |
| ISO-11615 | ISO 11615 Health informatics - Identification of medicinal products (IDMP) - Data elements and structures for the unique identification and exchange of regulated medicinal product information | STANDARD | International | 2 rules |
| ISO-11616 | ISO 11616 Health informatics - Identification of medicinal products (IDMP) - Data elements and structures for the unique identification and exchange of regulated pharmaceutical product information | STANDARD | International | 2 rules |
| HIPAA | HIPAA Privacy and Security Rules (45 CFR Parts 160 and 164) | REGULATION | United States | 1 rules |
| HIPAA-NPI | HIPAA Administrative Simplification: Standard Unique Health Identifier for Health Care Providers (45 CFR Part 162, Subpart D) | REGULATION | United States | 2 rules |
| SUNSHINE-ACT | Physician Payments Sunshine Act (42 U.S.C. 1320a-7h) and Open Payments regulations (42 CFR Part 403, Subpart I) | REGULATION | United States | 3 rules |
| FDA-NDC | 21 CFR Part 207 Establishment registration and drug listing, National Drug Code | REGULATION | United States | 1 rules |

## Data domains

| Code | Name | Description |
|---|---|---|
| CUSTOMER | Customer | Individual consumers and B2B customer accounts, their contacts, addresses, consents and account hierarchy. |
| PRODUCT | Product | Products and trade items sold to customers: identification, classification, descriptions, packaging and market availability. |
| SUPPLIER | Supplier | Suppliers and vendors: legal entity, sites, bank details, qualification and status. |
| EMPLOYEE | Employee | Employees and contingent workers: identity, organisation assignment, contact data. |
| LOCATION | Location | Sites, addresses and geographic hierarchies (country, region, city). |
| FINANCE | Finance | Financial master data: legal entities of the group, cost centres, chart of accounts, bank accounts. |
| ASSET | Asset | Physical and technical assets: equipment, installed base, serial numbers. |
| REFERENCE | Reference data | Shared code lists and reference entities used across domains: countries, currencies, languages, units, statuses. |
| MEDICINAL_PRODUCT | Medicinal product | Pharma extension. Regulated medicinal and pharmaceutical products, packages, marketing authorisations, IDMP and NDC identification. |
| HCP | Healthcare professional | Pharma extension. Healthcare professionals and organisations (prescribers, teaching hospitals): identity, licences, NPI, specialties, transfers of value. |
| CLINICAL_SITE | Clinical site | Pharma extension. Clinical trial sites and investigators: site identity, address, qualification and GxP-relevant status. |

## Data classifications

| Code | Name | Rank | Description |
|---|---|---|---|
| PUBLIC | Public | 1 | Information intended for or harmless if publicly disclosed (e.g. product descriptions, country codes, LEI). |
| INTERNAL | Internal | 2 | Business information for internal use, with limited impact if disclosed (e.g. internal codes, source identifiers). |
| CONFIDENTIAL | Confidential | 3 | Commercially sensitive information restricted to roles with a business need (e.g. prices, bank account numbers of companies, contract terms). |
| PERSONAL | Personal data | 4 | Any information relating to an identified or identifiable natural person (GDPR Art. 4(1); personal information under CCPA/CPRA). |
| SENSITIVE_PERSONAL | Sensitive personal data | 5 | Special categories of personal data (GDPR Art. 9), data on criminal convictions (Art. 10), and sensitive personal information under CCPA/CPRA (e.g. government identifiers, health, precise geolocation). |
| PHI | Protected health information | 5 | Individually identifiable health information held by a HIPAA covered entity or business associate (45 CFR 160.103). Used by the pharma extension. |

## Attribute types

| Code | Name | Default classification | Reference standard | Format pattern | Example |
|---|---|---|---|---|---|
| COUNTRY_CODE | Country code | PUBLIC | ISO-3166-1 | `^[A-Z]{2}$` | CA |
| CURRENCY_CODE | Currency code | PUBLIC | ISO-4217 | `^[A-Z]{3}$` | CAD |
| LANGUAGE_CODE | Language code | PUBLIC | ISO-639 | `^[a-z]{2}$` | fr |
| DATE | Date | INTERNAL | ISO-8601 | `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[12][0-9]\|3[01])$` | 2026-12-11 |
| TIMESTAMP | Timestamp | INTERNAL | ISO-8601 | `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?(Z\|[+-][0-9]{2}:[0-9]{2})$` | 2026-12-11T14:30:00Z |
| PHONE_NUMBER | Phone number | PERSONAL | ITU-T-E164 | `^\+[1-9][0-9]{1,14}$` | +15145550123 |
| EMAIL | Email address | PERSONAL | - | `^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$` | jane.doe@example.com |
| PERSON_NAME | Person name | PERSONAL | - | - | Jane Doe |
| POSTAL_ADDRESS | Postal address | PERSONAL | - | - | 1000 Rue Sherbrooke O, Montreal QC H3A 3G4, CA |
| DATE_OF_BIRTH | Date of birth | PERSONAL | ISO-8601 | `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[12][0-9]\|3[01])$` | 1980-04-23 |
| NATIONAL_ID | Government identifier | SENSITIVE_PERSONAL | - | - | 123-45-6789 |
| HEALTH_DATA | Health data | SENSITIVE_PERSONAL | GDPR | - | Allergy: penicillin |
| IBAN | IBAN | CONFIDENTIAL | ISO-13616 | `^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$` | FR7630006000011234567890189 |
| LEI | Legal entity identifier | PUBLIC | ISO-17442 | `^[A-Z0-9]{18}[0-9]{2}$` | 5493001KJTIIGC8Y1R12 |
| VAT_NUMBER | VAT or tax registration number | INTERNAL | - | `^[A-Z0-9]{4,15}$` | FR40303265045 |
| ORGANIZATION_NAME | Organisation name | PUBLIC | - | - | Northwind Distribution Inc. |
| GTIN | GTIN | PUBLIC | GS1-GTIN | `^([0-9]{8}\|[0-9]{12,14})$` | 00012345600012 |
| PRODUCT_DESCRIPTION | Product description | PUBLIC | - | - | en: Organic oat drink 1 L / fr: Boisson d'avoine biologique 1 L |
| MONETARY_AMOUNT | Monetary amount | CONFIDENTIAL | ISO-4217 | `^-?[0-9]+(\.[0-9]{1,4})?$` | 1250.00 |
| SOURCE_ID | Source record identifier | INTERNAL | - | - | SAP-ECC:0000104521 |
| FREE_TEXT | Free-text comment | INTERNAL | - | - | Customer asked to be called after 5 pm |
| NDC | National Drug Code | PUBLIC | FDA-NDC | `^([0-9]{4}-[0-9]{4}-[0-9]{2}\|[0-9]{5}-[0-9]{3}-[0-9]{2}\|[0-9]{5}-[0-9]{4}-[0-9])$` | 50242-040-62 |
| NPI | National Provider Identifier | PERSONAL | HIPAA-NPI | `^[0-9]{10}$` | 1234567893 |
| HCP_LICENSE_NUMBER | HCP state licence number | PERSONAL | SUNSHINE-ACT | - | MD-123456 (NY) |
| MPID | Medicinal Product Identifier | PUBLIC | ISO-11615 | - | EU-100001234-PRD |
| PHPID | Pharmaceutical Product Identifier | PUBLIC | ISO-11616 | - | PHPID-L1-0042 |
| TRANSFER_OF_VALUE | Transfer of value | CONFIDENTIAL | SUNSHINE-ACT | - | Consulting fee, 1500.00 USD, 2026-03-02 |

## Files and checks

This folder (`resources/demo-data/source/`) is the editable source of the test dataset; the load files are generated from it.

- One JSON array per entity (`<Entity>.json`), keyed by the SEML attribute names; a reference holds the target code under the reference role name (`Policy`, `OwnerBody`, `DefaultClassification`, `ReferenceStandard`, `Rule`, `DataDomain`, `DataClassification`, `AttributeType`, `Regulation`). RuleScope and RuleCitation rows have no ID: it is generated by a sequence at load time. `InForce` is never in the source: the ComputeInForce enricher computes it.
- The two RETIRED rules carry a `RetirementReason` (DQ-007 superseded by DQ-005; RET-005 replaced by RET-001 and RET-003); every other rule has it empty.
- `_deliberate-failures.json` holds three extra GovernanceRule rows (DQ-BAD1, DQ-BAD2, DQ-BAD3) that are not part of the corpus and are appended after it so that the first certification shows one record in error per check. They are not counted in the tables above.
- `../tools/build_demo_data.py` writes `../data-files/NN-<Entity>.csv` and `../API Import-curl/GovernanceRules-demo-data.json` from these files.
- `../tools/validate_demo_data.py` checks the generated files against the SEML model (names, `FID_` columns, lists of values, lengths, mandatory attributes, referential integrity, code uniqueness, expected counts, in-force logic, deliberate failures, privacy) and repeats the corpus checks: code format and prefix match the category, the statement contains its requirement level keyword, every APPROVED rule has at least one scope and is in force, every rule has a citation, retirement after effective date, retired rules have a reason, format patterns compile and match their examples, pharma rules scoped only to pharma domains or attribute types.
- Citations are to real articles and clauses; where a precise clause was not certain, the citation stays at section or part level (e.g. `42 CFR Part 403, Subpart I`, `ISO 11615`).
