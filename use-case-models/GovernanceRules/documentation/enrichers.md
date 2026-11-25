# Enrichers

This page lists the enrichers of the GovernanceRules data product. All four are SemQL enrichers on the **GovernanceRule** entity.

Only one enricher runs during certification: `ComputeInForce`, in the pre-consolidation scope. The three others have the execution scope `NONE`: they never run in a certification job. They are triggered by the rule steppers (on form open, and on data change where noted) to set the lifecycle status and the approval details while a user creates, submits or approves a rule.

To learn more, see [Set enrichment rules](https://docs.semarchy.com/saas/guides/design/certification/enrichment/enrichment-rules) and [Create a stepper](https://docs.semarchy.com/saas/guides/design/app-design/build/app-components/display-components/stepper) in the Semarchy documentation.

| Entity name | Enricher name | Enricher type | Enricher label | Enricher description | Enriched attribute | Enricher expression |
|---|---|---|---|---|---|---|
| GovernanceRule | ComputeInForce | SemQL (scope PRE_CONSO) | Compute In force | Sets InForce to true when the rule is APPROVED, its effective date is reached and its retirement date, if any, is not reached; false otherwise. Computed at certification. | InForce | `SEM_CAST_BOOLEAN(CASE WHEN LifecycleStatus = 'APPROVED' AND EffectiveDate <= CURRENT_DATE() AND (RetirementDate IS NULL OR RetirementDate > CURRENT_DATE()) THEN 'true' ELSE 'false' END)` |
| GovernanceRule | SetDraftStatus | SemQL (scope NONE, stepper only) | Set draft status | Stepper only: a new rule starts as DRAFT. Runs only when the status is empty (condition `LifecycleStatus IS NULL`). | LifecycleStatus | `'DRAFT'` |
| GovernanceRule | RequestReview | SemQL (scope NONE, stepper only) | Request review | Stepper only (Rule review workflow, steward task): sets the requested outcome. With a retirement date and a retirement reason the status becomes RETIREMENT_REQUESTED, otherwise IN_REVIEW (approval of a new or changed rule). | LifecycleStatus | `CASE WHEN RetirementDate IS NOT NULL AND RetirementReason IS NOT NULL THEN 'RETIREMENT_REQUESTED' ELSE 'IN_REVIEW' END` |
| GovernanceRule | ApproveRule | SemQL (scope NONE, stepper only) | Approve rule | Stepper only (Rule review workflow, approval task of the governance owner): prepares the approval when the form opens. A retirement request becomes RETIRED, any other request APPROVED; sets Approved on and Approved by, and the effective date to today when empty. The values are only kept when the owner chooses Approve: the Reject transition reverts the data of the approval task. | LifecycleStatus | `CASE WHEN LifecycleStatus IN ('RETIREMENT_REQUESTED', 'RETIRED') THEN 'RETIRED' ELSE 'APPROVED' END` |
| GovernanceRule | ApproveRule | | | | ApprovedOn | `CURRENT_DATE()` |
| GovernanceRule | ApproveRule | | | | ApprovedBy | `:V_USERNAME` |
| GovernanceRule | ApproveRule | | | | EffectiveDate | `COALESCE(EffectiveDate, CURRENT_DATE())` |

## Where the stepper enrichers run

| Stepper | Used by | Enricher | Triggered |
|---|---|---|---|
| NewGovernanceRule (label "New rule") | **New rule** and **Edit** actions on a governance rule | SetDraftStatus | On form open and on data change, Definition step |
| ReviewGovernanceRule (label "Request rule review") | Rule review workflow, task "Prepare the review request" (steward) | RequestReview | On form open and on data change, Definition step |
| ApproveGovernanceRule (label "Approve rule") | Rule review workflow, task "Approve the governance rule" (owner) | ApproveRule | On form open and on step enter (step trigger), Definition step (read-only) |

## Notes

- `InForce` is a stored flag, computed when the rule is certified. A rule whose effective date or retirement date passes later keeps its old flag until it is certified again. The row filters, the business views and the named queries do not rely on the flag: they test the status and the dates directly, so they are always current. Use `InForce` for display and for quick filters only.
- `ApproveRule` runs when the owner opens the approval form, so the form already shows the outcome (APPROVED or RETIRED) and the approval details before the owner decides, and the **Approve** transition can check them (for example that an approved rule has a scope). These values only reach the golden record when the owner approves: the **Reject** transition reverts the data of the approval task (`REVERT_DATA`), so the steward gets the rule back as it was submitted. The expression is idempotent: running it twice on a retirement request still gives RETIRED.
- Semarchy has no enricher on a workflow transition, and a step-exit trigger runs before the owner picks Approve or Reject. Running the enricher on form open and reverting on reject is therefore the way to set the approval values only on approval.
