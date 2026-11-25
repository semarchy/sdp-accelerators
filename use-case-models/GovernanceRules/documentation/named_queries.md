# Named queries

The GovernanceRules data product has five named queries. They are the contract between the governance rules and the people or AI agents who design other data products: instead of reading raw entities, a client asks one question ("which rules apply to an email address in the Customer domain?") and gets back a ready-to-use answer.

The queries are available through the REST API and through the data product **MCP server**, which exposes them to AI agents (Claude Code, VS Code, other MCP clients). Each query description ends with an `AI agent instructions:` paragraph: the MCP server passes it to the agent, which uses it to choose the query and read the result. See [Use named queries](https://docs.semarchy.com/saas/guides/design/certification/certif-execution/named-queries) and [Use data product MCP servers](https://docs.semarchy.com/saas/guides/use/mcp) in the Semarchy documentation.

| Named query | Question it answers | Parameters | Default limit |
|---|---|---|---|
| [RuleChecklist](#rulechecklist) | Which in-force rules apply to this whole design change? (compact) | `domain`, `classifications`, `attributeTypes` (all optional) | 200 |
| [ApplicableRules](#applicablerules) | Which in-force rules apply to this attribute type, with full text and citations? | `domain`, `classification`, `attributeType` (all optional) | 200 |
| [AttributeTypeCatalog](#attributetypecatalog) | Which attribute types exist, and how is each one classified? | none | 500 |
| [RuleDetail](#ruledetail) | What does this rule say exactly? | `code` (mandatory) | 1 |
| [RulesByCategory](#rulesbycategory) | Which in-force rules belong to this category? | `category` (mandatory) | 200 |

The recommended sequence for a design change is: **AttributeTypeCatalog** (classify the attributes) → **RuleChecklist** (one call for the whole change) → **RuleDetail** (only for the rules you need to explain or quote).

## How filtering works

### What "in force" means

A rule is in force when its status is `APPROVED`, its effective date is reached, and its retirement date is empty or not reached yet. RuleChecklist, ApplicableRules and RulesByCategory test this condition in their own filter. RuleDetail does not: it returns the rule whatever its status, within what the caller's role can see.

On top of that, the **GovernanceAgent** and **GovernanceReader** roles have row filters with the same condition on rules, scopes and citations. A client connected with one of these roles never sees a draft, in-review or retired rule, whatever query it runs. These roles also only see policies with status `APPROVED`; for them, the policy code and name of a rule may come back empty when its policy is not approved, so keep the policies of in-force rules approved.

All parameters are **codes**: `CUSTOMER` (DataDomain.Code), `PERSONAL` (DataClassification.Code), `EMAIL` (BusinessAttributeType.Code), `PRIVACY` (RuleCategory code), `PRIV-003` (rule code). Labels do not match.

### Scope matching: "empty dimension = any, omitted parameter = not asked"

A rule has one or more scope rows. Each row combines a data domain, a data classification and an attribute type, and each of the three is optional. A rule is returned when **at least one** of its scope rows matches the parameters.

For each dimension of a scope row:

| Scope row value | Parameter given | Parameter omitted |
|---|---|---|
| Empty (any) | Matches | Matches |
| A code | Matches only if the codes are equal | **Does not match** |

The first rule is the familiar one: an empty dimension in a scope row means "any value". The second rule is less obvious: when you omit a parameter, you are saying "I am not asking about this dimension", so only scope rows that are not restricted on it match. A call with only `domain=CUSTOMER` returns the rules that apply to the whole Customer domain, but not the rules restricted to a classification or an attribute type.

This is what keeps industry-specific rules out of unrelated designs. For example, rules scoped to a pharma attribute type such as `NDC` only come back when the caller passes `NDC`; a domain-only call on `PRODUCT` does not return them. It also means a caller should pass every dimension it knows: always pass the data domain, and pass the classifications and attribute types of the attributes it touches.

The scope rows returned with each rule are **all** the rule's scope rows (within what the role can see), not only the ones that matched. Use them to explain why a rule applies.

---

## RuleChecklist

**Purpose.** A compact checklist of the in-force rules that apply to a whole design change, in one call. It was added because calling ApplicableRules once per attribute type produced large, repetitive answers. Each rule comes back once, even if several attributes trigger it.

**Parameters.**

| Name | Binding | Type | Mandatory | Content |
|---|---|---|---|---|
| `domain` | `:DOMAIN` | STRING | No | One data domain code, for example `CUSTOMER`. |
| `classifications` | `:CLASSIFICATIONS` | STRING | No | Comma-separated data classification codes, no spaces, for example `PERSONAL,CONFIDENTIAL`. |
| `attributeTypes` | `:ATTRIBUTE_TYPES` | STRING | No | Comma-separated attribute type codes, no spaces, for example `EMAIL,PHONE_NUMBER,PERSON_NAME`. |

**Filter.** In-force condition, and at least one scope row where the domain is empty or equal to `domain`, the classification is empty or in the `classifications` list, and the attribute type is empty or in the `attributeTypes` list. List membership is tested as text (`',' || list || ','` contains `',' || code || ','`), which is why the lists must not contain spaces.

**Returned properties.** Sorted by `Code`.

| Object | Property | Source |
|---|---|---|
| Rule | Code | Code |
| Rule | Title | Title |
| Rule | RequirementLevel | RequirementLevel (MUST, SHOULD, MAY) |
| Rule | Category | Category |
| Rule | ImplementationPattern | ImplementationPattern |
| Rule | ImplementationGuidance | ImplementationGuidance |
| Rule | PolicyCode | Policy.Code |
| Rule | Scopes | List of Scope objects, sorted by ID |
| Scope | DataDomainCode | Data domain code (empty = any) |
| Scope | DataClassificationCode | Data classification code (empty = any) |
| Scope | AttributeTypeCode | Attribute type code (empty = any) |

Statements, examples and citations are left out to keep the answer small. Call RuleDetail for them.

**AI agent instructions (from the SEML).**

> Use this query first when you design or review a change. Classify each attribute you add or change with AttributeTypeCatalog, then call RuleChecklist once with the data domain code, the distinct default classifications of these attributes and all their attribute type codes, each list separated by commas with no spaces. Implement every MUST rule with its ImplementationPattern and ImplementationGuidance, apply SHOULD rules unless you state why not, and cite each applied rule code in the description of the object that implements it. Call RuleDetail for the statement and the citations of a rule you need to explain. Rules: META-002, AI-002.

---

## ApplicableRules

**Purpose.** The detailed variant of RuleChecklist for one attribute type: the in-force rules that apply to one design context (a domain, a classification and an attribute type), with their full text, citations and scope rows. Call RuleChecklist first for the whole change, and ApplicableRules when you need the statements and citations for one attribute type.

**Parameters.**

| Name | Binding | Type | Mandatory | Content |
|---|---|---|---|---|
| `domain` | `:DOMAIN` | STRING | No | One data domain code, for example `CUSTOMER`. |
| `classification` | `:CLASSIFICATION` | STRING | No | One data classification code, for example `PERSONAL`. |
| `attributeType` | `:ATTRIBUTE_TYPE` | STRING | No | One attribute type code, for example `EMAIL`. |

**Filter.** In-force condition, and at least one scope row where each dimension is empty or equal to the parameter (see [scope matching](#scope-matching-empty-dimension--any-omitted-parameter--not-asked)).

**Returned properties.** Sorted by `Code`.

| Object | Property | Source |
|---|---|---|
| Rule | Code, Title, Statement | Rule attributes |
| Rule | RequirementLevel, Category, ImplementationPattern | Rule attributes (codes) |
| Rule | ImplementationGuidance, Example, EffectiveDate | Rule attributes |
| Rule | PolicyCode, PolicyName | Policy.Code, Policy.Name |
| Rule | OwnerCode, OwnerName | OwnerBody.Code, OwnerBody.Name |
| Rule | Citations | List of Citation objects, sorted by regulation code |
| Rule | Scopes | List of Scope objects, sorted by ID |
| Citation | RegulationCode, RegulationName, RegulationType | Regulation.Code, Regulation.Name, Regulation.Type |
| Citation | Clause, Note | Article or clause, and how it supports the rule |
| Citation | URL | Regulation.URL |
| Scope | DataDomainCode, DataClassificationCode, AttributeTypeCode | Codes of the scope row (empty = any) |

**AI agent instructions (from the SEML).**

> This is the detailed variant of RuleChecklist for one attribute type: call RuleChecklist first for the whole change, and call this query when you need the full statements and citations of the rules for one attribute type. Call AttributeTypeCatalog first to find the attribute type code, then call this query with the data domain (always pass it), the classification (the attribute type's default classification when the design does not say otherwise) and the attribute type. Apply every MUST rule, apply SHOULD rules unless you state why not, consider MAY rules. Implement each rule with its ImplementationPattern and ImplementationGuidance, and cite its Code (for example PRIV-003) in the description of the object that implements it. An empty result means no rule applies beyond the general ones: call it again with only the domain to get the domain-wide rules.

---

## AttributeTypeCatalog

**Purpose.** The full list of business attribute types, so a client can map each attribute of its design to an attribute type code and its default classification before asking for rules. It also returns the format pattern and the reference standard, which a designer reuses in validations and reference entities.

**Parameters.** None.

**Filter.** None: every attribute type the role can see. Sorted by `Code`.

**Returned properties.**

| Property | Source |
|---|---|
| Code, Name, Description | Attribute type |
| FormatPattern | Regular expression a valid value matches |
| Example | Example of a valid value |
| DefaultClassificationCode, DefaultClassificationName | DefaultClassification.Code, DefaultClassification.Name |
| SensitivityRank | DefaultClassification.SensitivityRank (1 public to 5 special category) |
| ReferenceStandardCode, ReferenceStandardName | ReferenceStandard.Code, ReferenceStandard.Name |

**AI agent instructions (from the SEML).**

> Call it first when you design or change a data product: match each attribute you add or change to an attribute type code and take its default classification, then call RuleChecklist once with the data domain and these codes (or ApplicableRules for one attribute type, with full statements and citations). Use FormatPattern for validations and ReferenceStandard for reference entities. When no attribute type fits, say so and query RuleChecklist with the domain and classification only.

---

## RuleDetail

**Purpose.** One rule by its code, with everything about it: text, rationale, lifecycle, approval, policy, owner, citations and scope rows.

**Parameters.**

| Name | Binding | Type | Mandatory | Content |
|---|---|---|---|---|
| `code` | `:CODE` | STRING | Yes | Rule code, for example `PRIV-003`. |

**Filter.** `Code = :CODE`. There is no in-force condition in the query itself: a governance owner or steward sees the rule whatever its status. For the GovernanceAgent and GovernanceReader roles, the row filter hides any rule that is not in force, so an empty answer means "unknown code or not in force".

**Returned properties.**

| Object | Property | Source |
|---|---|---|
| Rule | Code, Title, Statement, Rationale | Rule attributes |
| Rule | RequirementLevel, Category, ImplementationPattern | Rule attributes (codes) |
| Rule | ImplementationGuidance, Example | Rule attributes |
| Rule | LifecycleStatus, InForce | Rule attributes |
| Rule | EffectiveDate, RetirementDate, ApprovedOn, ApprovedBy | Rule attributes |
| Rule | PolicyCode, PolicyName, OwnerCode, OwnerName | Policy and OwnerBody |
| Rule | Citations, Scopes | Same Citation and Scope objects as ApplicableRules |

**AI agent instructions (from the SEML).**

> Use it to read a rule cited in a design or returned by RuleChecklist or ApplicableRules. Only in-force rules are visible to the agent role: an empty result means the code does not exist or the rule is not in force; do not cite it.

---

## RulesByCategory

**Purpose.** Browse a whole topic, for example every privacy rule, when the question is not tied to particular attributes.

**Parameters.**

| Name | Binding | Type | Mandatory | Content |
|---|---|---|---|---|
| `category` | `:CATEGORY` | STRING | Yes | A RuleCategory code: `DATA_QUALITY`, `PRIVACY`, `SECURITY_ACCESS`, `RETENTION`, `REFERENCE_DATA`, `IDENTITY_MATCHING`, `METADATA_DOCUMENTATION`, `AI_USAGE`, `STEWARDSHIP` or `MODELING_CONVENTIONS`. |

**Filter.** In-force condition and `Category = :CATEGORY`. Scope rows are not used for filtering, so the result includes rules of every domain, industry rules included. Sorted by `Code`.

**Returned properties.** The same Rule, Citation and Scope properties as ApplicableRules.

**AI agent instructions (from the SEML).**

> Use it to browse a whole topic (for example every PRIVACY rule) when a design question is not tied to one attribute; it ignores scopes, so it also returns rules of other domains and industries. To find what applies to a design change, use RuleChecklist instead (or ApplicableRules for one attribute type). Pass the category code, not its label.

---

## Data product instructions

The description of the GovernanceRule entity (in `GovernanceRule.Entity.seml`) carries the instructions that apply across queries; the data product description stays a short business summary, because it is also the text of the Data products catalog card, which hides descriptions longer than about 1,000 characters. In short:

1. Call **AttributeTypeCatalog** to classify each attribute you touch.
2. Call **RuleChecklist** once for the whole change, with the data domain, the classifications and the attribute type codes as comma-separated lists.
3. Use **RuleDetail** for one rule and **RulesByCategory** to browse a category.
4. Filter on codes, not labels.
5. Apply every MUST rule, apply SHOULD rules unless you state why not, and cite each applied rule code (for example `PRIV-003`) in the description of the object that implements it.
6. Never apply or cite a rule that is not in force.
7. Always pass the data domain to RuleChecklist and ApplicableRules: an omitted parameter only matches rules that are not restricted on that dimension, so industry-specific rules only come back when the design names their domains or attribute types.

For a ready-made procedure that runs these steps from Claude Code, see the `governance-check` skill in [resources/ai-agents/governance-check/SKILL.md](../resources/ai-agents/governance-check/SKILL.md) and the guide [design_with_ai_agents.md](./design_with_ai_agents.md).
