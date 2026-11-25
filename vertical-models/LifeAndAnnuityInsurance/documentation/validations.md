# Validations Documentation

This table summarizes the validations defined in the model, including their entity, name, label, description, and condition.

| Entity | Name | Label | Description | Condition |
|-------------|----------------------|----------------------|-----------------------------------------------|------------------------------------------------|
| AnnuityContract | AnnuityPayoutDateCheck | Annuity Payout Date Check | Checks annuity payout date check for Annuity Contract. | PayoutStartDate IS NULL OR IssueDate IS NULL OR IssueDate <= PayoutStartDate |
| BeneficiaryDesignation | BeneficiaryDesignationPercentageCheck | Beneficiary Designation Percentage Check | Checks beneficiary designation percentage check for Beneficiary Designation. | PercentageShare IS NULL OR (PercentageShare >= 0 AND PercentageShare <= 100) |
| Claim | ClaimAmountCheck | Claim Amount Check | Checks claim amount check for Claim. | ClaimAmount IS NULL OR ClaimAmount >= 0 |
| Claim | ClaimReportedDateCheck | Claim Reported Date Check | Checks claim reported date check for Claim. | ReportedDate IS NULL OR LossDate IS NULL OR LossDate <= ReportedDate |
| ClaimBenefitPayment | ClaimBenefitPaymentAmountCheck | Claim Benefit Payment Amount Check | Checks claim benefit payment amount check for Claim Benefit Payment. | PaymentAmount IS NULL OR PaymentAmount >= 0 |
| Coverage | CoverageAmountCheck | Coverage Amount Check | Checks coverage amount check for Coverage. | FaceAmount IS NULL OR FaceAmount >= 0 |
| Coverage | CoverageDateRangeCheck | Coverage Date Range Check | Checks coverage date range check for Coverage. | TerminationDate IS NULL OR EffectiveDate IS NULL OR EffectiveDate <= TerminationDate |
| InvestmentAllocation | InvestmentAllocationDateRangeCheck | Investment Allocation Date Range Check | Checks investment allocation date range check for Investment Allocation. | AllocationEndDate IS NULL OR AllocationEffectiveDate IS NULL OR AllocationEffectiveDate <= AllocationEndDate |
| InvestmentAllocation | InvestmentAllocationPercentageCheck | Investment Allocation Percentage Check | Checks investment allocation percentage check for Investment Allocation. | AllocationPercentage IS NULL OR (AllocationPercentage >= 0 AND AllocationPercentage <= 100) |
| Party | PartyDateRangeCheck | Party Date Range Check | Checks party date range check for Party. | PartyEndDate IS NULL OR PartyStartDate IS NULL OR PartyStartDate <= PartyEndDate |
| Policy | PolicyAmountCheck | Policy Amount Check | Checks policy amount check for Policy. | FaceAmount IS NULL OR FaceAmount >= 0 |
| Policy | PolicyDateRangeCheck | Policy Date Range Check | Checks policy date range check for Policy. | MaturityDate IS NULL OR EffectiveDate IS NULL OR EffectiveDate <= MaturityDate |
| PolicyLoan | PolicyLoanBalanceCheck | Policy Loan Balance Check | Checks policy loan balance check for Policy Loan. | OutstandingBalance IS NULL OR OutstandingBalance >= 0 |
| PolicyPartyRole | BeneficiaryPercentageCheck | Beneficiary Percentage Check | Checks beneficiary percentage check for Policy Party Role. | BeneficiaryPercentage IS NULL OR (BeneficiaryPercentage >= 0 AND BeneficiaryPercentage <= 100) |
| PolicyPartyRole | PolicyPartyRoleDateRangeCheck | Policy Party Role Date Range Check | Checks policy party role date range check for Policy Party Role. | RoleEndDate IS NULL OR RoleEffectiveDate IS NULL OR RoleEffectiveDate <= RoleEndDate |
| PremiumTransaction | PremiumTransactionAmountCheck | Premium Transaction Amount Check | Checks premium transaction amount check for Premium Transaction. | PaymentAmount IS NULL OR PaymentAmount >= 0 |
| Rider | RiderDateRangeCheck | Rider Date Range Check | Checks rider date range check for Rider. | TerminationDate IS NULL OR EffectiveDate IS NULL OR EffectiveDate <= TerminationDate |
| UnderwritingCase | UnderwritingDecisionDateCheck | Underwriting Decision Date Check | Checks underwriting decision date check for Underwriting Case. | DecisionDate IS NULL OR ApplicationDate IS NULL OR ApplicationDate <= DecisionDate |
| UnderwritingRequirement | UnderwritingRequirementDateCheck | Underwriting Requirement Date Check | Checks underwriting requirement date check for Underwriting Requirement. | ReceivedDate IS NULL OR OrderedDate IS NULL OR OrderedDate <= ReceivedDate |

