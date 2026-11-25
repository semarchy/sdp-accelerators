# Model structure

This page lists the entities, attributes, references and lists of values of the GovernanceRules data product, as defined in the SEML files under [`src/GovernanceRules`](../src/GovernanceRules). For an explanation of how the pieces fit together, read the [user guide](./user_guide.md).

All entities are **basic** entities: records are authored or loaded once per key, so no attribute is used in matching. The "Number of attributes" column counts the entity attributes plus the reference (foreign) attributes.

## Entities

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|---|---|---|---|---|---|
| GovernanceRule | Governance rule | A standard data governance rule that every MDM project of the company must apply, written as an imperative RFC 2119 statement (MUST, SHOULD, MAY), with its category, the implementation pattern a designer uses to apply it, its scopes (data domain, data classification, attribute type) and the regulations or standards it cites. Authored by the governance stewards and approved by the governance owner through the Rule review workflow; each approved version is kept in the history. AI agent instructions: Only rules with InForce = true apply to a design. Cite the rule Code (for example PRIV-003) in the description of every object that implements the rule. RequirementLevel MUST is mandatory, SHOULD is expected unless justified, MAY is optional. Never apply or cite a rule that is not in force. When you design or change a data product, first call the AttributeTypeCatalog named query to classify each attribute you touch (attribute type code, default classification), then call RuleChecklist once for the whole change with the data domain, the classifications and the attribute type codes as comma-separated lists (ApplicableRules returns the same rules for one attribute type with their statements and citations); use RuleDetail for one rule and RulesByCategory to browse a category. Lists of values store codes (MUST, SHOULD, MAY; PRIVACY, DATA_QUALITY...): filter on the code. Always pass the data domain: an omitted parameter only matches rules that are not restricted on that dimension, so industry-specific rules (for example pharma rules scoped to MEDICINAL_PRODUCT, HCP, CLINICAL_SITE or to pharma attribute types such as NDC or NPI) only come back when your design names those domains or attribute types. | RuleCitation, RuleScope | GovernanceBody, GovernancePolicy | 18 |
| RuleScope | Rule scope | One applicability combination of a rule: a data domain, a data classification and an attribute type, each optional. An empty dimension means any. A rule applies when any of its scope rows matches. AI agent instructions: A scope row with no domain, no classification and no attribute type makes the rule apply everywhere. | - | BusinessAttributeType, DataClassification, DataDomain, GovernanceRule | 5 |
| RuleCitation | Citation | A regulation or standard cited by a rule, with the article or clause that anchors it. | - | GovernanceRule, Regulation | 5 |
| GovernancePolicy | Policy | A governance policy that groups related rules (for example the privacy policy), owned by a governance body. | GovernanceRule | GovernanceBody | 6 |
| GovernanceBody | Governance body | A body that owns rules and policies: a council, an office or a role (for example DPO, the Data Governance Council). | GovernancePolicy, GovernanceRule | - | 5 |
| Regulation | Regulation or standard | A regulation, standard or framework that rules cite (for example GDPR, ISO 3166-1, DAMA-DMBOK). | BusinessAttributeType, RuleCitation | - | 7 |
| DataDomain | Data domain | A business data domain that a data product covers (for example CUSTOMER, PRODUCT, HCP). Used to scope rules. | RuleScope | - | 3 |
| DataClassification | Data classification | A data sensitivity classification (for example PUBLIC, PERSONAL, SPECIAL_CATEGORY). Used to scope rules and as the default classification of attribute types. | BusinessAttributeType, RuleScope | - | 4 |
| BusinessAttributeType | Attribute type | A business attribute type (for example EMAIL, PHONE, COUNTRY_CODE, NDC), with its default classification, the standard that governs its format and a format pattern. Used to scope rules. AI agent instructions: Classify each new attribute of a design against this list before asking for the applicable rules. | RuleScope | DataClassification, Regulation | 7 |

## Attributes per entity

### GovernanceRule (Governance rule)

Key: `Code`, entered by the author. Table `GOV_RULE`, golden history kept (each certified version), deletion disabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String (40) | Yes | Natural key of the rule; its prefix follows the category: DQ-, PRIV-, SEC-, RET-, REF-, MDM-, META-, AI-, STW-, MOD-, entered by the author and never changed (for example PRIV-003). | No |
| Title | Title | String (200) | Yes | Short title of the rule. | No |
| Statement | Statement | String (4000) | Yes | Normative text of the rule, an imperative sentence in RFC 2119 style (MUST, SHOULD, MAY). | No |
| Rationale | Rationale | String (4000) | No | Why the rule exists: the risk it addresses or the regulation it serves. | No |
| RequirementLevel | Requirement level | List of values `RequirementLevel` | Yes | Strength of the rule, code MUST (Must), SHOULD (Should) or MAY (May), as in RFC 2119. | No |
| Category | Category | List of values `RuleCategory` | Yes | Category of the rule, code DATA_QUALITY, PRIVACY, SECURITY_ACCESS, RETENTION, REFERENCE_DATA, IDENTITY_MATCHING, METADATA_DOCUMENTATION, AI_USAGE, STEWARDSHIP or MODELING_CONVENTIONS. | No |
| ImplementationPattern | Implementation pattern | List of values `ImplementationPattern` | No | How a designer implements the rule in a data product, code VALIDATION, ENRICHER, PRIVILEGE_ROW_FILTER, MATCHING_SURVIVORSHIP, WORKFLOW, RETENTION_POLICY, DESCRIPTION_AI_INSTRUCTION, NAMING_CONVENTION or REFERENCE_ENTITY. | No |
| ImplementationGuidance | Implementation guidance | String (4000) | No | Concrete guidance for the designer: what to build in the data product to comply with the rule. | No |
| Example | Example | String (4000) | No | An example of a compliant implementation or value. | No |
| LifecycleStatus | Status | List of values `LifecycleStatus` | Yes | Lifecycle status, code DRAFT (Draft), IN_REVIEW (In review), APPROVED (Approved), RETIREMENT_REQUESTED (Retirement requested) or RETIRED (Retired). Changed by the Rule review workflow. | No |
| EffectiveDate | Effective date | Date | No | Date from which the rule applies. | No |
| RetirementDate | Retirement date | Date | No | Date from which the rule no longer applies; empty while the rule is not retired. | No |
| RetirementReason | Retirement reason | String (1000) | No | Why the rule is retired, entered when the retirement is requested. | No |
| ApprovedOn | Approved on | Date | No | Date of the last approval by the governance owner. | No |
| ApprovedBy | Approved by | String (128) | No | User who gave the last approval. | No |
| InForce | In force | Boolean | No | Computed: true when the status is APPROVED, the effective date is reached and the retirement date, if any, is not reached. Computed when the rule is certified. | No |
| OwnerBody | Owner | Reference to GovernanceBody | No | The governance body that owns the rule. | No |
| Policy | Policy | Reference to GovernancePolicy | No | The policy a rule belongs to. | No |

### RuleScope (Rule scope)

Key: `ID`, generated from a sequence. Table `GOV_RULE_SCOPE`, no history, deletion enabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | No | Generated identifier of the scope row. | No |
| AttributeType | Attribute type | Reference to BusinessAttributeType | No | Attribute type of the scope row; empty means any attribute type. | No |
| DataClassification | Classification | Reference to DataClassification | No | Data classification of the scope row; empty means any classification. | No |
| DataDomain | Domain | Reference to DataDomain | No | Data domain of the scope row; empty means any domain. | No |
| Rule | Rule | Reference to GovernanceRule | Yes | The rule that the scope row applies to. Scope rows belong to their rule and are deleted with it. | No |

### RuleCitation (Citation)

Key: `ID`, generated from a sequence. Table `GOV_RULE_CITATION`, no history, deletion enabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ID | ID | LongInteger | No | Generated identifier of the citation. | No |
| Clause | Article or clause | String (200) | No | Article or clause cited, for example Art. 5(1)(e). | No |
| Note | Note | String (2000) | No | How the cited text supports the rule. | No |
| Regulation | Regulation | Reference to Regulation | Yes | The regulation or standard cited. | No |
| Rule | Rule | Reference to GovernanceRule | Yes | The rule that cites the regulation. Citations belong to their rule and are deleted with it. | No |

### GovernancePolicy (Policy)

Key: `Code`, entered by the author. Table `GOV_POLICY`, no history, deletion enabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String (40) | Yes | Natural key of the policy, entered by the author and never changed (for example POL-PRIV). | No |
| Name | Name | String (200) | Yes | Name of the policy. | No |
| Description | Description | String (4000) | No | What the policy covers. | No |
| Purpose | Purpose | String (4000) | No | The objective of the policy. | No |
| LifecycleStatus | Status | List of values `LifecycleStatus` | No | Lifecycle status, code DRAFT (Draft), IN_REVIEW (In review), APPROVED (Approved), RETIREMENT_REQUESTED (Retirement requested) or RETIRED (Retired). | No |
| OwnerBody | Owner | Reference to GovernanceBody | No | The governance body that owns the policy. | No |

### GovernanceBody (Governance body)

Key: `Code`, entered by the author. Table `GOV_BODY`, no history, deletion enabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String (40) | Yes | Natural key of the governance body, entered by the author and never changed (for example DPO). | No |
| Name | Name | String (200) | Yes | Name of the body. | No |
| Type | Type | List of values `GovernanceBodyType` | No | Kind, code COUNCIL, OFFICE or ROLE. | No |
| ContactEmail | Contact email | String (200) | No | Email address to contact the body. | No |
| Description | Description | String (4000) | No | Mission of the body. | No |

### Regulation (Regulation or standard)

Key: `Code`, entered by the author. Table `GOV_REGULATION`, no history, deletion enabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String (40) | Yes | Natural key of the regulation or standard, entered by the author and never changed (for example GDPR or ISO-3166-1). | No |
| Name | Name | String (200) | Yes | Official name. | No |
| Type | Type | List of values `RegulationType` | No | Kind, code REGULATION, STANDARD, FRAMEWORK or INTERNAL. | No |
| Issuer | Issuer | String (200) | No | Body that issues the regulation or standard (for example European Union, ISO). | No |
| Jurisdiction | Jurisdiction | String (100) | No | Where it applies (for example EU, US, Canada, Global). | No |
| URL | URL | String (500) | No | Link to the official text. | No |
| Description | Description | String (4000) | No | What the regulation or standard covers. | No |

### DataDomain (Data domain)

Key: `Code`, entered by the author. Table `GOV_DATA_DOMAIN`, no history, deletion enabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String (40) | Yes | Natural key of the data domain, entered by the author and never changed (for example CUSTOMER). | No |
| Name | Name | String (200) | Yes | Name of the domain. | No |
| Description | Description | String (4000) | No | What the domain covers. | No |

### DataClassification (Data classification)

Key: `Code`, entered by the author. Table `GOV_DATA_CLASS`, no history, deletion enabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String (40) | Yes | Natural key of the classification, entered by the author and never changed (for example PERSONAL). | No |
| Name | Name | String (200) | Yes | Name of the classification. | No |
| Description | Description | String (4000) | No | What data falls under the classification. | No |
| SensitivityRank | Sensitivity rank | Integer | No | Sensitivity from 1 (public) to 5 (special category). | No |

### BusinessAttributeType (Attribute type)

Key: `Code`, entered by the author. Table `GOV_ATTR_TYPE`, no history, deletion enabled.

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| Code | Code | String (40) | Yes | Natural key of the attribute type, entered by the author and never changed (for example EMAIL). | No |
| Name | Name | String (200) | Yes | Name of the attribute type. | No |
| Description | Description | String (4000) | No | What values of this type hold. | No |
| FormatPattern | Format pattern | String (500) | No | Regular expression that a valid value matches. | No |
| Example | Example | String (500) | No | An example of a valid value. | No |
| DefaultClassification | Default classification | Reference to DataClassification | No | The classification that an attribute of this type gets by default. | No |
| ReferenceStandard | Reference standard | Reference to Regulation | No | The standard that governs the format of values of this type (for example ISO 3166-1 for COUNTRY_CODE). | No |

## References

| Reference | Label | From entity (attribute) | To entity | Role on the referenced side | Mandatory? | On delete of the referenced record | Description |
|---|---|---|---|---|---|---|---|
| BusinessAttributeTypeHasDefaultClassification | Default classification of the attribute type | BusinessAttributeType (DefaultClassification) | DataClassification | AttributeTypes | No | Restrict: deletion refused while referenced | The classification that an attribute of this type gets by default. |
| BusinessAttributeTypeHasReferenceStandard | Reference standard of the attribute type | BusinessAttributeType (ReferenceStandard) | Regulation | AttributeTypes | No | Restrict: deletion refused while referenced | The standard that governs the format of values of this type (for example ISO 3166-1 for COUNTRY_CODE). |
| GovernancePolicyHasOwnerBody | Owner of the policy | GovernancePolicy (OwnerBody) | GovernanceBody | OwnedPolicies | No | Restrict: deletion refused while referenced | The governance body that owns the policy. |
| GovernanceRuleHasOwnerBody | Owner of the rule | GovernanceRule (OwnerBody) | GovernanceBody | OwnedRules | No | Restrict: deletion refused while referenced | The governance body that owns the rule. |
| GovernanceRuleHasPolicy | Policy of the rule | GovernanceRule (Policy) | GovernancePolicy | Rules | No | Restrict: deletion refused while referenced | The policy a rule belongs to. |
| RuleCitationHasRegulation | Regulation of the citation | RuleCitation (Regulation) | Regulation | Citations | Yes | Restrict: deletion refused while referenced | The regulation or standard cited. |
| RuleCitationHasRule | Rule of the citation | RuleCitation (Rule) | GovernanceRule | Citations | Yes | Cascade: child rows are deleted with it | The rule that cites the regulation. Citations belong to their rule and are deleted with it. |
| RuleScopeHasAttributeType | Attribute type of the scope | RuleScope (AttributeType) | BusinessAttributeType | RuleScopes | No | Restrict: deletion refused while referenced | Attribute type of the scope row; empty means any attribute type. |
| RuleScopeHasDataClassification | Classification of the scope | RuleScope (DataClassification) | DataClassification | RuleScopes | No | Restrict: deletion refused while referenced | Data classification of the scope row; empty means any classification. |
| RuleScopeHasDataDomain | Domain of the scope | RuleScope (DataDomain) | DataDomain | RuleScopes | No | Restrict: deletion refused while referenced | Data domain of the scope row; empty means any domain. |
| RuleScopeHasRule | Rule of the scope | RuleScope (Rule) | GovernanceRule | Scopes | Yes | Cascade: child rows are deleted with it | The rule that the scope row applies to. Scope rows belong to their rule and are deleted with it. |

## Lists of values

Lists of values store the **code**; the label is what users see in the application. Named queries and the MCP server return codes, so filter on the code.

### GovernanceBodyType (Governance body type)

Kind of governance body that owns rules and policies. Used by: GovernanceBody.Type.

| Code | Label | Description |
|---|---|---|
| `COUNCIL` | Council | A committee of several members that decides collectively, for example the Data Governance Council. |
| `OFFICE` | Office | A permanent organisational unit, for example the Chief Data Officer office. |
| `ROLE` | Role | A single accountable function held by one person, for example the Data Protection Officer. |

### ImplementationPattern (Implementation pattern)

How a data product designer implements a governance rule in a Semarchy data product. Used by: GovernanceRule.ImplementationPattern.

| Code | Label | Description |
|---|---|---|
| `VALIDATION` | Validation | Implement the rule as a validation (SemQL, plugin, mandatory, list of values or unique key). |
| `ENRICHER` | Enricher | Implement the rule as an enricher that computes, normalizes or standardizes values. |
| `PRIVILEGE_ROW_FILTER` | Privilege or row filter | Implement the rule with privilege grants: entity and attribute access, row filters. |
| `MATCHING_SURVIVORSHIP` | Matching and survivorship | Implement the rule in match rules, merge thresholds or survivorship rules. |
| `WORKFLOW` | Workflow | Implement the rule as a workflow, for example an approval before a change is certified. |
| `RETENTION_POLICY` | Retention policy | Implement the rule with a data retention policy or historization settings. |
| `DESCRIPTION_AI_INSTRUCTION` | Description and AI instruction | Implement the rule in the descriptions of the model, including the AI agent instructions. |
| `NAMING_CONVENTION` | Naming convention | Implement the rule by following a naming convention for objects, attributes or codes. |
| `REFERENCE_ENTITY` | Reference entity | Implement the rule with a managed reference entity or a list of values instead of free text. |

### LifecycleStatus (Status)

Lifecycle status of a governance rule or a policy. Only APPROVED rules can be in force. Used by: GovernanceRule.LifecycleStatus, GovernancePolicy.LifecycleStatus.

| Code | Label | Description |
|---|---|---|
| `DRAFT` | Draft | Being written by a steward; not applied. |
| `IN_REVIEW` | In review | New or changed rule submitted for approval in the Rule review workflow; waiting for the governance owner. |
| `APPROVED` | Approved | Approved by the governance owner; in force from its effective date until its retirement date. |
| `RETIREMENT_REQUESTED` | Retirement requested | Retirement requested in the Rule review workflow, with a retirement date and a reason; waiting for the governance owner. |
| `RETIRED` | Retired | No longer applied; kept for history. |

### RegulationType (Regulation type)

Kind of source that a governance rule cites. Used by: Regulation.Type.

| Code | Label | Description |
|---|---|---|
| `REGULATION` | Regulation | A law or binding regulation, for example GDPR or HIPAA. |
| `STANDARD` | Standard | A published standard, for example ISO 3166-1 or ISO 8000. |
| `FRAMEWORK` | Framework | A body of good practice that is not binding, for example DAMA-DMBOK. |
| `INTERNAL` | Internal | An internal policy or standard of the company. |

### RequirementLevel (Requirement level)

Strength of a governance rule, as defined by RFC 2119. Used by: GovernanceRule.RequirementLevel.

| Code | Label | Description |
|---|---|---|
| `MUST` | Must | Mandatory: every design in scope applies the rule. |
| `SHOULD` | Should | Expected: apply the rule unless there is a valid reason, and state that reason. |
| `MAY` | May | Optional: apply the rule when it helps. |

### RuleCategory (Rule category)

Topic of a governance rule. The rule code prefix follows the category. Used by: GovernanceRule.Category.

| Code | Label | Description |
|---|---|---|
| `DATA_QUALITY` | Data quality | Completeness, validity and consistency of data (code prefix DQ-). |
| `PRIVACY` | Privacy | Protection of personal data and data subject rights (code prefix PRIV-). |
| `SECURITY_ACCESS` | Security and access | Access control, need to know and protection of sensitive data (code prefix SEC-). |
| `RETENTION` | Retention | How long data and its history are kept, and how they are purged (code prefix RET-). |
| `REFERENCE_DATA` | Reference data | Use of managed reference data and code standards (code prefix REF-). |
| `IDENTITY_MATCHING` | Identity and matching | Identification, matching and merging of master records (code prefix MDM-). |
| `METADATA_DOCUMENTATION` | Metadata and documentation | Documentation of models and data for people and AI agents (code prefix META-). |
| `AI_USAGE` | AI usage | Use of data by AI agents and AI features (code prefix AI-). |
| `STEWARDSHIP` | Stewardship | Ownership, review and approval of data changes (code prefix STW-). |
| `MODELING_CONVENTIONS` | Modeling conventions | Naming and modeling conventions of data products (code prefix MOD-). |
