# Validations

This page lists the data quality checks of the GovernanceRules data product. The model keeps data quality deliberately light: mandatory fields, list-of-values checks, two business rules on the governance rule, and reference checks. All checks run in the **pre-consolidation** scope (`PRE_CONSO`), on the source records, during certification. A record that fails a check goes to the error tables and does not become a golden record; stewards find it in **Stewardship › Data in error**.

To learn more, see [Set validation rules](https://docs.semarchy.com/saas/guides/design/certification/validation/validation-rules) and [Determine validation scope](https://docs.semarchy.com/saas/guides/design/certification/certif-execution/validation-scope) in the Semarchy documentation.

## SemQL validations

| Entity | Name | Label | Description | Condition | Scope |
|---|---|---|---|---|---|
| GovernanceRule | ApprovedRuleHasScope | Approved rule has a scope | An approved rule has at least one scope row. A rule with no scope row is never returned by ApplicableRules, so it would be invisible to design agents. | `LifecycleStatus <> 'APPROVED' OR any Scopes have (1 = 1)` | PRE_CONSO |
| GovernanceRule | RetirementAfterEffective | Retirement date after effective date | The retirement date of a rule, when set, is after its effective date. | `RetirementDate IS NULL OR EffectiveDate IS NULL OR RetirementDate > EffectiveDate` | PRE_CONSO |

Messages shown to users:

- **ApprovedRuleHasScope**: "An approved rule needs at least one scope (data domain, classification or attribute type; leave all three empty to apply everywhere)."
- **RetirementAfterEffective**: "The retirement date must be after the effective date."

`RetirementAfterEffective` is also checked interactively: in the Definition step of the three rule steppers (New rule, Request rule review, Approve rule) when data changes and when the user leaves the step, and as a blocking check on the **Submit for approval** and **Approve** transitions of the Rule review workflow.

`ApprovedRuleHasScope` is a blocking check on the **Approve** transition of the Rule review workflow: when the approval form opens, the rule is already prepared with status `APPROVED`, so the owner cannot approve a rule that has no scope row. It is also checked at certification, for rules loaded or saved with status `APPROVED` outside the workflow: such a rule without a scope row fails certification and lands in **Data in error**.

## Mandatory attributes

| Entity | Mandatory attributes | Scope |
|---|---|---|
| GovernanceRule | Code, Title, Statement, RequirementLevel, Category, LifecycleStatus | PRE_CONSO |
| GovernancePolicy | Code, Name | PRE_CONSO |
| GovernanceBody | Code, Name | PRE_CONSO |
| Regulation | Code, Name | PRE_CONSO |
| DataDomain | Code, Name | PRE_CONSO |
| DataClassification | Code, Name | PRE_CONSO |
| BusinessAttributeType | Code, Name | PRE_CONSO |

The Rule review workflow also blocks the **Submit for approval** and **Approve** transitions when Title, Statement, RequirementLevel or Category is empty.

## List of values checks

Each attribute typed with a list of values only accepts the codes of that list (see [model_structure.md](./model_structure.md#lists-of-values)).

| Entity | Attribute | List of values | Scope |
|---|---|---|---|
| GovernanceRule | RequirementLevel | RequirementLevel | PRE_CONSO |
| GovernanceRule | Category | RuleCategory | PRE_CONSO |
| GovernanceRule | ImplementationPattern | ImplementationPattern | PRE_CONSO |
| GovernanceRule | LifecycleStatus | LifecycleStatus | PRE_CONSO |
| GovernancePolicy | LifecycleStatus | LifecycleStatus | PRE_CONSO |
| GovernanceBody | Type | GovernanceBodyType | PRE_CONSO |
| Regulation | Type | RegulationType | PRE_CONSO |

## Reference checks

Every reference is checked in the `PRE_CONSO` scope: a referenced code must exist. Three references are mandatory.

| Entity | Reference | Message when missing |
|---|---|---|
| RuleScope | Rule (RuleScopeHasRule) | A RuleScope needs a rule. |
| RuleCitation | Rule (RuleCitationHasRule) | A RuleCitation needs a rule. |
| RuleCitation | Regulation (RuleCitationHasRegulation) | A RuleCitation needs a regulation. |
