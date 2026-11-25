## Life and Annuity Model Structure

Below is a summary table of all entities in the model, including their label, documentation, references, and attribute count.

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|-------------|-------------|---------------------|-----------------------|--------------------|---------------------|
| AnnuityContract | Annuity Contract | Represents annuity-specific contract details, including accumulation values, surrender values, qualification, and payout timing. | (none) | AnnuityPayoutOption, Policy, TaxQualification | 15 |
| AnnuityPayoutOption | Annuity Payout Option | Defines annuity payout options such as life only, joint life, period certain, systematic withdrawal, or lump sum. | AnnuityContract | (none) | 8 |
| BeneficiaryDesignation | Beneficiary Designation | Represents beneficiary designation details for a policy or annuity contract, including percentage share, class, and revocability. | (none) | Party, Policy | 11 |
| BenefitType | Benefit Type | Defines payable benefit categories such as death benefit, annuity income, living benefit, surrender, loan, or maturity benefit. | Claim, ClaimBenefitPayment, Coverage | (none) | 7 |
| CashValueSnapshot | Cash Value Snapshot | Represents point-in-time policy value measures for life insurance and annuity contracts. | (none) | Policy | 11 |
| Claim | Claim | Represents a Life & Annuity claim event and adjudication status for death, living benefit, surrender, maturity, or annuity income claims. | ClaimBenefitPayment | BenefitType, Party, Policy | 13 |
| ClaimBenefitPayment | Claim Benefit Payment | Represents payments made for Life & Annuity claims and benefit disbursements. | (none) | BenefitType, Claim, Party, PaymentStatus | 10 |
| Coverage | Coverage | Represents base coverage or coverage segments for a Life & Annuity policy, including amount, status, and benefit option details. | Rider | BenefitType, CoverageStatus, Policy, RiskClass | 14 |
| CoverageStatus | Coverage Status | Defines coverage status values for base coverage, supplemental benefits, and riders. | Coverage | (none) | 6 |
| DistributionChannel | Distribution Channel | Defines channels through which Life & Annuity products are sold or serviced. | Policy | (none) | 6 |
| EmploymentStatus | Employment Status | Defines employment statuses used for individual profile, underwriting, suitability, and financial review context. | Individual | (none) | 6 |
| Fund | Fund | Defines funds and investment options available for variable life, variable annuity, and allocation-based products. | InvestmentAllocation | (none) | 9 |
| Individual | Individual | Represents an individual person profile maintained by the insurance company, including identity, contact, address, profile, and employment details. | Party | EmploymentStatus, IndividualStatus, MaritalStatus | 19 |
| IndividualStatus | Individual Status | Defines lifecycle statuses for individual person profiles maintained by the carrier. | Individual | (none) | 6 |
| InsurancePlan | Insurance Plan | Represents a sellable plan configuration under a Life & Annuity product, including issue rules, amounts, and lifecycle dates. | Policy, SurrenderChargeSchedule | InsuranceProduct, PlanStatus, TaxQualification | 12 |
| InsuranceProduct | Insurance Product | Represents a Life & Annuity product offered by the carrier, including commercial identity, availability, and product governance attributes. | InsurancePlan | LineOfBusiness, ProductStatus, ProductType | 11 |
| InvestmentAllocation | Investment Allocation | Represents a policy or annuity allocation to a fund or investment option. | (none) | Fund, Policy | 9 |
| LineOfBusiness | Line Of Business | Organizes Life & Annuity offerings into enterprise lines of business for product governance, reporting, and navigation. | InsuranceProduct | (none) | 8 |
| MaritalStatus | Marital Status | Defines marital statuses used for individual profile, beneficiary, underwriting, and suitability context. | Individual | (none) | 6 |
| Party | Party | Represents an umbrella party wrapper that can point to an individual, group, or organization and participate in policy, claim, and annuity relationships. | BeneficiaryDesignation, Claim, ClaimBenefitPayment, PolicyPartyRole, UnderwritingCase | Individual, PartyStatus | 10 |
| PartyRoleType | Party Role Type | Defines roles a party may play, including policy owner, insured, annuitant, beneficiary, payer, trustee, producer, assignee, and claimant. | PolicyPartyRole | (none) | 7 |
| PartyStatus | Party Status | Defines lifecycle statuses for party wrapper records, such as active, inactive, merged, or pending verification. | Party | (none) | 6 |
| PaymentPlan | Payment Plan | Defines billing modes and premium payment plans for policies and annuity contracts. | Policy, PremiumTransaction | (none) | 7 |
| PaymentStatus | Payment Status | Defines payment statuses used for premiums, disbursements, and claim benefit payments. | ClaimBenefitPayment, Policy, PremiumTransaction | (none) | 6 |
| PlanStatus | Plan Status | Defines plan lifecycle statuses used to manage availability for issue, conversion, or renewal. | InsurancePlan | (none) | 6 |
| Policy | Policy | Represents a Life & Annuity policy or contract lifecycle record, including policy identity, dates, premium measures, values, and coverage amounts. | AnnuityContract, BeneficiaryDesignation, CashValueSnapshot, Claim, Coverage, InvestmentAllocation, PolicyLoan, PolicyPartyRole, PremiumTransaction, Rider, UnderwritingCase | DistributionChannel, InsurancePlan, PaymentPlan, PaymentStatus, PolicyStatus, TaxQualification | 19 |
| PolicyLoan | Policy Loan | Represents policy loan details for cash-value life insurance and loan-eligible contracts. | (none) | Policy | 11 |
| PolicyPartyRole | Policy Party Role | Associates a party to a policy in a specific role, enabling the same party to be an owner, insured, annuitant, beneficiary, payer, trustee, producer, assignee, or claimant. | (none) | Party, PartyRoleType, Policy | 12 |
| PolicyStatus | Policy Status | Defines policy lifecycle statuses such as pending, active, lapsed, surrendered, matured, or terminated. | Policy | (none) | 6 |
| PremiumTransaction | Premium Transaction | Represents premium, payment, fee, reversal, or posting transactions associated with a policy. | (none) | PaymentPlan, PaymentStatus, Policy | 13 |
| ProductStatus | Product Status | Defines product lifecycle statuses used to govern product availability and retirement. | InsuranceProduct | (none) | 6 |
| ProductType | Product Type | Classifies Life & Annuity products by standard product families such as term life, whole life, indexed annuity, or variable annuity. | InsuranceProduct | (none) | 8 |
| RegulatoryTest | Regulatory Test | Defines regulatory and compliance tests relevant to Life & Annuity products, such as MEC, suitability, replacement, or best-interest checks. | (none) | (none) | 9 |
| RequirementType | Requirement Type | Defines underwriting requirement types such as application form, medical exam, labs, APS, financial evidence, or replacement review. | UnderwritingRequirement | (none) | 7 |
| Rider | Rider | Represents a rider or supplemental benefit attached to a policy or coverage. | (none) | Coverage, Policy, RiderType | 12 |
| RiderType | Rider Type | Defines optional rider and supplemental benefit types available on Life & Annuity products. | Rider | (none) | 8 |
| RiskClass | Risk Class | Defines underwriting risk classes used in life insurance issue and rating decisions. | Coverage, UnderwritingCase | (none) | 7 |
| SurrenderChargeSchedule | Surrender Charge Schedule | Defines surrender charge schedule rows for plans, contracts, or riders, including percentages and effective periods. | (none) | InsurancePlan | 10 |
| TaxQualification | Tax Qualification | Defines tax qualification treatment such as non-qualified, traditional IRA, Roth IRA, 401(k), 403(b), or pension rollover. | AnnuityContract, InsurancePlan, Policy | (none) | 6 |
| UnderwritingCase | Underwriting Case | Represents the underwriting review for a proposed insured, policy, or coverage decision. | UnderwritingRequirement | Party, Policy, RiskClass, UnderwritingDecisionStatus | 12 |
| UnderwritingDecisionStatus | Underwriting Decision Status | Defines underwriting decision statuses such as pending, approved, rated, postponed, declined, or withdrawn. | UnderwritingCase | (none) | 6 |
| UnderwritingRequirement | Underwriting Requirement | Represents an underwriting requirement ordered, received, waived, or evaluated during underwriting. | (none) | RequirementType, UnderwritingCase | 10 |

# Detailed Model Structure

Below are markdown tables for each entity in the model. Each table lists the attributes and their metadata.

## AnnuityContract

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AnnuityContractID | Annuity Contract ID | String | Yes | Unique identifier for the annuity contract details. | No |
| ContractNumber | Contract Number | String | No | Annuity contract number. | No |
| ContractType | Contract Type | String | No | Type of annuity contract. | No |
| IssueDate | Issue Date | Date | No | Date the annuity contract was issued. | No |
| AnnuitizationDate | Annuitization Date | Date | No | Date the contract annuitized, if applicable. | No |
| PayoutStartDate | Payout Start Date | Date | No | Date payout payments begin. | No |
| AccumulationValue | Accumulation Value | Decimal | No | Current accumulation value of the contract. | No |
| SurrenderValue | Surrender Value | Decimal | No | Current surrender value after charges and adjustments. | No |
| GuaranteedMinimumValue | Guaranteed Minimum Value | Decimal | No | Guaranteed minimum value associated with the contract. | No |
| IncomeBaseValue | Income Base Value | Decimal | No | Income base value used for guaranteed income riders. | No |
| RMDRequiredIndicator | RMDRequired Indicator | Boolean | No | Indicates whether required minimum distributions apply. | No |
| QualifiedIndicator | Qualified Indicator | Boolean | No | Indicates whether the contract is tax qualified. | No |
| FreeWithdrawalPercentage | Free Withdrawal Percentage | Decimal | No | Free withdrawal percentage allowed without surrender charge. | No |
| MaturityDate | Maturity Date | Date | No | Scheduled maturity date of the contract. | No |
| Notes | Notes | LongText | No | Additional annuity contract notes. | No |

---

## AnnuityPayoutOption

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AnnuityPayoutOptionID | Annuity Payout Option ID | String | Yes | Unique identifier for the annuity payout option. | No |
| PayoutOptionCode | Payout Option Code | String | No | Annuity payout option code. | No |
| PayoutOptionName | Payout Option Name | String | No | Business name of the payout option. | No |
| PayoutCategory | Payout Category | String | No | Payout category such as life contingent or term certain. | No |
| Description | Description | LongText | No | Description of payout option mechanics. | No |
| LifeContingentIndicator | Life Contingent Indicator | Boolean | No | Indicates whether the option depends on a life-contingent annuitization basis. | No |
| PeriodCertainMonths | Period Certain Months | Decimal | No | Default period certain duration in months, when applicable. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the payout option is active. | No |

---

## BeneficiaryDesignation

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BeneficiaryDesignationID | Beneficiary Designation ID | String | Yes | Unique identifier for the beneficiary designation. | No |
| DesignationDate | Designation Date | Date | No | Date the beneficiary designation was made. | No |
| DesignationType | Designation Type | String | No | Designation type such as primary, contingent, or tertiary. | No |
| BeneficiaryClass | Beneficiary Class | String | No | Class or grouping of the beneficiary designation. | No |
| PercentageShare | Percentage Share | Decimal | No | Percentage share assigned to the beneficiary. | No |
| PerStirpesIndicator | Per Stirpes Indicator | Boolean | No | Indicates whether per stirpes distribution applies. | No |
| RevocableIndicator | Revocable Indicator | Boolean | No | Indicates whether the designation is revocable. | No |
| ContingencyLevel | Contingency Level | Decimal | No | Numeric contingency priority level. | No |
| TrustIndicator | Trust Indicator | Boolean | No | Indicates whether the beneficiary is a trust. | No |
| MinorIndicator | Minor Indicator | Boolean | No | Indicates whether the beneficiary is a minor. | No |
| Notes | Notes | LongText | No | Additional beneficiary designation notes. | No |

---

## BenefitType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BenefitTypeID | Benefit Type ID | String | Yes | Unique identifier for the benefit type. | No |
| BenefitCode | Benefit Code | String | No | Benefit type code. | No |
| BenefitName | Benefit Name | String | No | Business name of the benefit type. | No |
| BenefitCategory | Benefit Category | String | No | Operational category for the benefit. | No |
| Description | Description | LongText | No | Description of benefit type handling. | No |
| TaxableIndicator | Taxable Indicator | Boolean | No | Indicates whether payments of this benefit are generally taxable. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the benefit type is active. | No |

---

## CashValueSnapshot

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CashValueSnapshotID | Cash Value Snapshot ID | String | Yes | Unique identifier for the cash value snapshot. | No |
| ValuationDate | Valuation Date | Date | No | Date for which policy values are measured. | No |
| AccountValue | Account Value | Decimal | No | Account value at valuation date. | No |
| CashSurrenderValue | Cash Surrender Value | Decimal | No | Cash surrender value at valuation date. | No |
| LoanBalance | Loan Balance | Decimal | No | Loan balance at valuation date. | No |
| NetCashValue | Net Cash Value | Decimal | No | Net cash value after loans and charges. | No |
| CostBasis | Cost Basis | Decimal | No | Policy cost basis at valuation date. | No |
| DividendValue | Dividend Value | Decimal | No | Dividend value or accumulation at valuation date. | No |
| InterestCreditedAmount | Interest Credited Amount | Decimal | No | Interest credited for the valuation period. | No |
| MarketValueAdjustmentAmount | Market Value Adjustment Amount | Decimal | No | Market value adjustment amount, if applicable. | No |
| Notes | Notes | LongText | No | Additional valuation notes. | No |

---

## Claim

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ClaimID | Claim ID | String | Yes | Unique identifier for the claim. | No |
| ClaimNumber | Claim Number | String | No | Carrier claim number. | No |
| ClaimType | Claim Type | String | No | Type of claim or benefit request. | No |
| ClaimStatus | Claim Status | String | No | Current claim status. | No |
| LossDate | Loss Date | Date | No | Date of death, disability, maturity, or other claim event. | No |
| ReportedDate | Reported Date | Date | No | Date the claim was reported. | No |
| ApprovedDate | Approved Date | Date | No | Date the claim was approved. | No |
| ClosedDate | Closed Date | Date | No | Date the claim was closed. | No |
| ClaimAmount | Claim Amount | Decimal | No | Claimed amount. | No |
| ApprovedAmount | Approved Amount | Decimal | No | Approved amount payable for the claim. | No |
| DenialReason | Denial Reason | String | No | Reason for denial when claim is denied. | No |
| ContestabilityReviewIndicator | Contestability Review Indicator | Boolean | No | Indicates whether contestability review is required. | No |
| Notes | Notes | LongText | No | Additional claim notes. | No |

---

## ClaimBenefitPayment

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ClaimBenefitPaymentID | Claim Benefit Payment ID | String | Yes | Unique identifier for the claim benefit payment. | No |
| PaymentNumber | Payment Number | String | No | Payment number assigned by claims or disbursement processing. | No |
| PaymentDate | Payment Date | Date | No | Date the benefit payment was issued. | No |
| PaymentAmount | Payment Amount | Decimal | No | Total payment amount. | No |
| TaxableAmount | Taxable Amount | Decimal | No | Taxable portion of the payment. | No |
| WithholdingAmount | Withholding Amount | Decimal | No | Tax withholding amount. | No |
| PaymentMethod | Payment Method | String | No | Payment method such as check, EFT, wire, or annuity income. | No |
| CheckNumber | Check Number | String | No | Check number when payment is issued by check. | No |
| EFTTraceNumber | EFTTrace Number | String | No | EFT trace number when payment is electronic. | No |
| Notes | Notes | LongText | No | Additional benefit payment notes. | No |

---

## Coverage

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CoverageID | Coverage ID | String | Yes | Unique identifier for the coverage. | No |
| CoverageNumber | Coverage Number | String | No | Carrier or administration coverage number. | No |
| CoverageName | Coverage Name | String | No | Business name of the coverage. | No |
| CoverageType | Coverage Type | String | No | Coverage type such as base, term, permanent, supplemental, or annuity benefit. | No |
| EffectiveDate | Effective Date | Date | No | Date the coverage became effective. | No |
| TerminationDate | Termination Date | Date | No | Date the coverage terminated, if applicable. | No |
| FaceAmount | Face Amount | Decimal | No | Face amount or benefit amount for the coverage. | No |
| DeathBenefitOption | Death Benefit Option | String | No | Death benefit option such as level, increasing, or return of premium. | No |
| IssueAge | Issue Age | Decimal | No | Issue age associated with the coverage. | No |
| PremiumBasis | Premium Basis | String | No | Premium basis for the coverage. | No |
| ConversionExpiryDate | Conversion Expiry Date | Date | No | Conversion privilege expiration date, if applicable. | No |
| EvidenceOfInsurabilityIndicator | Evidence Of Insurability Indicator | Boolean | No | Indicates whether evidence of insurability is required. | No |
| ReinsuranceIndicator | Reinsurance Indicator | Boolean | No | Indicates whether coverage is reinsured. | No |
| Description | Description | LongText | No | Description of coverage terms and servicing context. | No |

---

## CoverageStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CoverageStatusID | Coverage Status ID | String | Yes | Unique identifier for the coverage status. | No |
| StatusCode | Status Code | String | No | Coverage status code. | No |
| StatusName | Status Name | String | No | Coverage status name. | No |
| StatusCategory | Status Category | String | No | Lifecycle category for the coverage status. | No |
| Description | Description | LongText | No | Business meaning and service implications of the coverage status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the coverage status is active. | No |

---

## DistributionChannel

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| DistributionChannelID | Distribution Channel ID | String | Yes | Unique identifier for the distribution channel. | No |
| ChannelCode | Channel Code | String | No | Distribution channel code. | No |
| ChannelName | Channel Name | String | No | Business name of the distribution channel. | No |
| ChannelType | Channel Type | String | No | Type of channel, such as agency, bank, broker dealer, or direct. | No |
| Description | Description | LongText | No | Description of channel usage and governance. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the distribution channel is active. | No |

---

## EmploymentStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| EmploymentStatusID | Employment Status ID | String | Yes | Unique identifier for the employment status. | No |
| StatusCode | Status Code | String | No | Employment status code. | No |
| StatusName | Status Name | String | No | Employment status name. | No |
| StatusCategory | Status Category | String | No | Employment category. | No |
| Description | Description | LongText | No | Business meaning of the employment status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the employment status is active. | No |

---

## Fund

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| FundID | Fund ID | String | Yes | Unique identifier for the fund. | No |
| FundCode | Fund Code | String | No | Fund or investment option code. | No |
| FundName | Fund Name | String | No | Business name of the fund or investment option. | No |
| FundFamily | Fund Family | String | No | Fund family or manager. | No |
| AssetClass | Asset Class | String | No | Primary asset class or allocation category. | No |
| RiskLevel | Risk Level | String | No | Relative risk level for the fund. | No |
| ExpenseRatio | Expense Ratio | Decimal | No | Expense ratio associated with the fund. | No |
| InceptionDate | Inception Date | Date | No | Fund inception date. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the fund is active. | No |

---

## Individual

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| IndividualID | Individual ID | LongInteger | Yes | System-generated golden identifier for the mastered individual profile. | No |
| IndividualNumber | Individual Number | String | No | Enterprise individual number assigned by the carrier or party master. | No |
| FirstName | First Name | String | No | First name of the individual. | Yes |
| MiddleName | Middle Name | String | No | Middle name or initial of the individual. | No |
| LastName | Last Name | String | No | Last name of the individual. | Yes |
| FullName | Full Name | String | No | Full display name of the individual. | No |
| DateOfBirth | Date Of Birth | Date | No | Birth date for the individual. | Yes |
| Gender | Gender | LifeAndAnnuityInsurance.list_of_values.Gender | No | Recorded gender value where permitted and relevant. | No |
| TaxIdentifierLast4 | Tax Identifier Last4 | String | No | Last four characters of the individual tax identifier. | Yes |
| EmailAddress | Email Address | String | No | Primary email address for the individual. | Yes |
| PhoneNumber | Phone Number | String | No | Primary phone number for the individual. | Yes |
| AddressLine1 | Address Line1 | String | No | Primary mailing or residential address line. | No |
| City | City | String | No | City for the primary address. | No |
| StateProvince | State Province | String | No | State or province for the primary address. | No |
| PostalCode | Postal Code | String | No | Postal code for the primary address. | Yes |
| CountryCode | Country Code | String | No | Country code for the primary address. | No |
| OccupationTitle | Occupation Title | String | No | Occupation or job title recorded for underwriting, suitability, or servicing. | No |
| EmployerName | Employer Name | String | No | Current or most recently recorded employer name. | No |
| AnnualIncome | Annual Income | Decimal | No | Annual income amount recorded for underwriting, suitability, or financial review. | No |

---

## IndividualStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| IndividualStatusID | Individual Status ID | String | Yes | Unique identifier for the individual status. | No |
| StatusCode | Status Code | String | No | Individual status code. | No |
| StatusName | Status Name | String | No | Individual status name. | No |
| StatusCategory | Status Category | String | No | Lifecycle category for the individual status. | No |
| Description | Description | LongText | No | Business meaning and servicing implication of the individual status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the individual status is active. | No |

---

## InsurancePlan

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| InsurancePlanID | Insurance Plan ID | String | Yes | Unique identifier for the insurance plan. | No |
| PlanCode | Plan Code | String | No | Enterprise plan code. | No |
| PlanName | Plan Name | String | No | Commercial or operational name of the plan. | No |
| PlanVersion | Plan Version | String | No | Version or release identifier of the plan configuration. | No |
| PlanDescription | Plan Description | LongText | No | Detailed explanation of plan features and eligibility. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the plan is effective. | No |
| EffectiveTo | Effective To | Date | No | Date until which the plan remains effective. | No |
| IssueAgeMin | Issue Age Min | Decimal | No | Minimum issue age for the plan. | No |
| IssueAgeMax | Issue Age Max | Decimal | No | Maximum issue age for the plan. | No |
| MinimumFaceAmount | Minimum Face Amount | Decimal | No | Minimum face amount or contract amount allowed for the plan. | No |
| MinimumPremium | Minimum Premium | Decimal | No | Minimum premium allowed for the plan. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the plan is active. | No |

---

## InsuranceProduct

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| InsuranceProductID | Insurance Product ID | String | Yes | Unique identifier for the insurance product. | No |
| ProductCode | Product Code | String | No | Enterprise product code. | No |
| ProductName | Product Name | String | No | Commercial or marketing name of the product. | No |
| ProductDescription | Product Description | LongText | No | Detailed explanation of product features and target market. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the product configuration is effective. | No |
| EffectiveTo | Effective To | Date | No | Date until which the product configuration remains effective. | No |
| MarketSegment | Market Segment | String | No | Target market segment for the product. | No |
| CarrierCode | Carrier Code | String | No | Carrier or issuing company code. | No |
| IssueAgeMin | Issue Age Min | Decimal | No | Minimum issue age for the product. | No |
| IssueAgeMax | Issue Age Max | Decimal | No | Maximum issue age for the product. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the product is active. | No |

---

## InvestmentAllocation

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| InvestmentAllocationID | Investment Allocation ID | String | Yes | Unique identifier for the investment allocation. | No |
| AllocationEffectiveDate | Allocation Effective Date | Date | No | Date from which the allocation is effective. | No |
| AllocationEndDate | Allocation End Date | Date | No | Date on which the allocation ended, if applicable. | No |
| AllocationPercentage | Allocation Percentage | Decimal | No | Percentage allocated to the investment option. | No |
| AccountValue | Account Value | Decimal | No | Current account value assigned to the allocation. | No |
| TransferRestrictionIndicator | Transfer Restriction Indicator | Boolean | No | Indicates whether transfers are restricted for this allocation. | No |
| ModelPortfolioName | Model Portfolio Name | String | No | Model portfolio name when allocation is part of a model portfolio. | No |
| RebalanceIndicator | Rebalance Indicator | Boolean | No | Indicates whether automatic rebalancing is enabled. | No |
| Notes | Notes | LongText | No | Additional allocation notes. | No |

---

## LineOfBusiness

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| LineOfBusinessID | Line Of Business ID | String | Yes | Unique identifier for the line of business. | No |
| LOBCode | LOBCode | String | No | Enterprise line-of-business code. | No |
| LOBName | LOBName | String | No | Business name of the line of business. | No |
| MarketSegment | Market Segment | String | No | Market segment served by the line of business. | No |
| Description | Description | LongText | No | Business description and governance purpose of the line of business. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the line of business is effective. | No |
| EffectiveTo | Effective To | Date | No | Date until which the line of business remains effective. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the line of business is active. | No |

---

## MaritalStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| MaritalStatusID | Marital Status ID | String | Yes | Unique identifier for the marital status. | No |
| StatusCode | Status Code | String | No | Marital status code. | No |
| StatusName | Status Name | String | No | Marital status name. | No |
| StatusCategory | Status Category | String | No | Marital status category. | No |
| Description | Description | LongText | No | Business meaning of the marital status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the marital status is active. | No |

---

## Party

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PartyID | Party ID | LongInteger | Yes | System-generated golden identifier for the mastered party wrapper. | No |
| PartyNumber | Party Number | String | No | Enterprise party number. | No |
| PartyType | Party Type | LifeAndAnnuityInsurance.list_of_values.PartyType | No | Classifies the party as individual, group, or organization. | No |
| Individual | Individual ID | ForeignAttribute (Reference) | No | The identifier of the Individual associated with the Party. | Yes |
| PartyStartDate | Party Start Date | Date | No | Date from which the party wrapper is active for relationship management. | No |
| PartyEndDate | Party End Date | Date | No | Date on which the party wrapper ends or becomes inactive. | No |
| SourceSystem | Source System | String | No | System that originated or most recently asserted the party wrapper. | No |
| SourceRecordID | Source Record ID | String | No | Source-system record identifier for traceability. | No |
| VerificationDate | Verification Date | Date | No | Date on which the party wrapper was verified. | No |
| VerifiedIndicator | Verified Indicator | Boolean | No | Indicates whether the party wrapper has been verified. | No |
| Notes | Notes | LongText | No | Additional party wrapper notes. | No |

---

## PartyRoleType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PartyRoleTypeID | Party Role Type ID | String | Yes | Unique identifier for the party role type. | No |
| RoleCode | Role Code | String | No | Party role type code. | No |
| RoleName | Role Name | String | No | Business name of the party role. | No |
| RoleCategory | Role Category | String | No | Role category for party participation and servicing. | No |
| Description | Description | LongText | No | Business definition of the role and when it applies. | No |
| RequiresInsurableInterest | Requires Insurable Interest | Boolean | No | Indicates whether the role normally requires insurable interest evidence. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the party role type is active. | No |

---

## PartyStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PartyStatusID | Party Status ID | String | Yes | Unique identifier for the party status. | No |
| StatusCode | Status Code | String | No | Party status code. | No |
| StatusName | Status Name | String | No | Party status name. | No |
| StatusCategory | Status Category | String | No | Lifecycle category for the party status. | No |
| Description | Description | LongText | No | Business meaning and servicing implication of the party status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the party status is active. | No |

---

## PaymentPlan

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PaymentPlanID | Payment Plan ID | String | Yes | Unique identifier for the payment plan. | No |
| PlanCode | Plan Code | String | No | Payment plan code. | No |
| PlanName | Plan Name | String | No | Business name of the payment plan. | No |
| BillingFrequency | Billing Frequency | String | No | Billing frequency such as monthly, quarterly, semiannual, or annual. | No |
| PaymentMode | Payment Mode | String | No | Payment mode supported by the plan. | No |
| Description | Description | LongText | No | Business description of the payment plan. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the payment plan is active. | No |

---

## PaymentStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PaymentStatusID | Payment Status ID | String | Yes | Unique identifier for the payment status. | No |
| StatusCode | Status Code | String | No | Payment status code. | No |
| StatusName | Status Name | String | No | Payment status name. | No |
| StatusCategory | Status Category | String | No | Operational category for the payment status. | No |
| Description | Description | LongText | No | Business meaning and downstream implications of the payment status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the payment status is active. | No |

---

## PlanStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PlanStatusID | Plan Status ID | String | Yes | Unique identifier for the plan status. | No |
| StatusCode | Status Code | String | No | Plan status code. | No |
| StatusName | Status Name | String | No | Plan status name. | No |
| StatusCategory | Status Category | String | No | Lifecycle category for the plan status. | No |
| Description | Description | LongText | No | Business meaning and use of the plan status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the plan status is active. | No |

---

## Policy

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PolicyID | Policy ID | String | Yes | Unique identifier for the consolidated policy. | No |
| PolicyNumber | Policy Number | String | No | Carrier-issued policy or contract number. | No |
| PolicyVersion | Policy Version | String | No | Version or iteration of the policy. | No |
| IssueDate | Issue Date | Date | No | Date the policy was issued. | No |
| EffectiveDate | Effective Date | Date | No | Date the policy became effective. | No |
| MaturityDate | Maturity Date | Date | No | Scheduled maturity date of the policy or contract. | No |
| SurrenderDate | Surrender Date | Date | No | Date the policy was surrendered, if applicable. | No |
| TerminationDate | Termination Date | Date | No | Date the policy terminated, if applicable. | No |
| JurisdictionState | Jurisdiction State | String | No | State or jurisdiction governing the contract. | No |
| CurrencyCode | Currency Code | String | No | Currency in which policy values are denominated. | No |
| FaceAmount | Face Amount | Decimal | No | Face amount for the policy or base life coverage. | No |
| ModalPremium | Modal Premium | Decimal | No | Premium due per billing mode. | No |
| AnnualPremium | Annual Premium | Decimal | No | Annualized policy premium. | No |
| CashValue | Cash Value | Decimal | No | Current policy cash value when applicable. | No |
| DeathBenefitAmount | Death Benefit Amount | Decimal | No | Current death benefit amount. | No |
| FreeLookEndDate | Free Look End Date | Date | No | End date of the free-look period. | No |
| GracePeriodEndDate | Grace Period End Date | Date | No | Date on which the premium grace period ends. | No |
| LapseIndicator | Lapse Indicator | Boolean | No | Indicates whether the policy is lapsed. | No |
| AutoPayIndicator | Auto Pay Indicator | Boolean | No | Indicates whether automatic payment is enabled. | No |

---

## PolicyLoan

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PolicyLoanID | Policy Loan ID | String | Yes | Unique identifier for the policy loan. | No |
| LoanNumber | Loan Number | String | No | Policy loan number. | No |
| LoanDate | Loan Date | Date | No | Date the loan was opened. | No |
| LoanStatus | Loan Status | String | No | Current status of the loan. | No |
| LoanPrincipalAmount | Loan Principal Amount | Decimal | No | Original or current principal amount of the loan. | No |
| LoanInterestRate | Loan Interest Rate | Decimal | No | Loan interest rate. | No |
| OutstandingBalance | Outstanding Balance | Decimal | No | Current outstanding loan balance. | No |
| InterestAccruedAmount | Interest Accrued Amount | Decimal | No | Accrued interest amount on the loan. | No |
| RepaymentDueDate | Repayment Due Date | Date | No | Next repayment due date, if applicable. | No |
| CollateralValue | Collateral Value | Decimal | No | Policy value used to collateralize the loan. | No |
| Notes | Notes | LongText | No | Additional policy loan notes. | No |

---

## PolicyPartyRole

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PolicyPartyRoleID | Policy Party Role ID | String | Yes | Unique identifier for the policy party role. | No |
| RoleEffectiveDate | Role Effective Date | Date | No | Date from which the party role is effective. | No |
| RoleEndDate | Role End Date | Date | No | Date on which the party role ended, if applicable. | No |
| RoleStatus | Role Status | String | No | Current status of the policy party role. | No |
| OwnershipPercentage | Ownership Percentage | Decimal | No | Ownership percentage held by the party, if applicable. | No |
| BeneficiaryPercentage | Beneficiary Percentage | Decimal | No | Beneficiary allocation percentage, if applicable. | No |
| RevocableIndicator | Revocable Indicator | Boolean | No | Indicates whether the role or designation is revocable. | No |
| PrimaryIndicator | Primary Indicator | Boolean | No | Indicates whether this is the primary party for the role. | No |
| RelationshipToInsured | Relationship To Insured | String | No | Relationship of the party to the insured or annuitant. | No |
| InsurableInterestDescription | Insurable Interest Description | LongText | No | Description of insurable interest evidence, when applicable. | No |
| SignatureRequiredIndicator | Signature Required Indicator | Boolean | No | Indicates whether the role requires a party signature. | No |
| Notes | Notes | LongText | No | Additional notes about the policy party role. | No |

---

## PolicyStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PolicyStatusID | Policy Status ID | String | Yes | Unique identifier for the policy status. | No |
| StatusCode | Status Code | String | No | Policy status code. | No |
| StatusName | Status Name | String | No | Policy status name. | No |
| StatusCategory | Status Category | String | No | Lifecycle category for the policy status. | No |
| Description | Description | LongText | No | Business meaning and service implications of the policy status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the policy status is active. | No |

---

## PremiumTransaction

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PremiumTransactionID | Premium Transaction ID | String | Yes | Unique identifier for the premium transaction. | No |
| TransactionNumber | Transaction Number | String | No | Transaction number assigned by the payment or administration system. | No |
| TransactionDate | Transaction Date | Date | No | Date the transaction occurred. | No |
| EffectiveDate | Effective Date | Date | No | Accounting or policy effective date of the transaction. | No |
| TransactionType | Transaction Type | String | No | Transaction type such as premium, fee, reversal, or refund. | No |
| PaymentAmount | Payment Amount | Decimal | No | Amount received or disbursed as payment. | No |
| PremiumAmount | Premium Amount | Decimal | No | Premium amount represented by the transaction. | No |
| FeeAmount | Fee Amount | Decimal | No | Fee amount associated with the transaction. | No |
| CurrencyCode | Currency Code | String | No | Currency code for transaction amounts. | No |
| PostedDate | Posted Date | Date | No | Date the transaction posted. | No |
| ReversalIndicator | Reversal Indicator | Boolean | No | Indicates whether the transaction reverses a prior transaction. | No |
| SourceSystem | Source System | String | No | System that originated the transaction. | No |
| Notes | Notes | LongText | No | Additional transaction notes. | No |

---

## ProductStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ProductStatusID | Product Status ID | String | Yes | Unique identifier for the product status. | No |
| StatusCode | Status Code | String | No | Product status code. | No |
| StatusName | Status Name | String | No | Product status name. | No |
| StatusCategory | Status Category | String | No | Lifecycle category for the product status. | No |
| Description | Description | LongText | No | Business meaning and use of the product status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the product status is active. | No |

---

## ProductType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ProductTypeID | Product Type ID | String | Yes | Unique identifier for the product type. | No |
| ProductTypeCode | Product Type Code | String | No | Enterprise product type code. | No |
| ProductTypeName | Product Type Name | String | No | Business name of the product type. | No |
| ProductFamily | Product Family | String | No | Life, annuity, or related product family. | No |
| Description | Description | LongText | No | Description of product type characteristics. | No |
| LifeOrAnnuityIndicator | Life Or Annuity Indicator | String | No | Indicates whether this type primarily supports life insurance, annuity, or both. | No |
| TaxTreatment | Tax Treatment | String | No | Default tax treatment commonly associated with the product type. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the product type is active. | No |

---

## RegulatoryTest

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RegulatoryTestID | Regulatory Test ID | String | Yes | Unique identifier for the regulatory test. | No |
| TestCode | Test Code | String | No | Regulatory test code. | No |
| TestName | Test Name | String | No | Business name of the regulatory test. | No |
| RegulationName | Regulation Name | String | No | Regulation, rule, or framework associated with the test. | No |
| Jurisdiction | Jurisdiction | String | No | Jurisdiction where the test applies. | No |
| Frequency | Frequency | String | No | Frequency or timing of the test. | No |
| Description | Description | LongText | No | Description of the regulatory test. | No |
| Severity | Severity | String | No | Severity or risk level of failing the test. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the regulatory test is active. | No |

---

## RequirementType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RequirementTypeID | Requirement Type ID | String | Yes | Unique identifier for the requirement type. | No |
| RequirementCode | Requirement Code | String | No | Underwriting requirement code. | No |
| RequirementName | Requirement Name | String | No | Business name of the underwriting requirement. | No |
| RequirementCategory | Requirement Category | String | No | Category of requirement. | No |
| Description | Description | LongText | No | Description of the requirement and its purpose. | No |
| DefaultValidityDays | Default Validity Days | Decimal | No | Default number of days the requirement remains valid. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the requirement type is active. | No |

---

## Rider

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RiderID | Rider ID | String | Yes | Unique identifier for the rider. | No |
| RiderNumber | Rider Number | String | No | Carrier or administration rider number. | No |
| RiderName | Rider Name | String | No | Business name of the rider. | No |
| RiderStatus | Rider Status | String | No | Current status of the rider. | No |
| EffectiveDate | Effective Date | Date | No | Date the rider became effective. | No |
| TerminationDate | Termination Date | Date | No | Date the rider terminated, if applicable. | No |
| BenefitAmount | Benefit Amount | Decimal | No | Benefit amount provided by the rider. | No |
| RiderPremium | Rider Premium | Decimal | No | Premium charged for the rider. | No |
| WaiverIndicator | Waiver Indicator | Boolean | No | Indicates whether the rider includes premium waiver functionality. | No |
| Description | Description | LongText | No | Description of rider terms. | No |
| WaitingPeriodDays | Waiting Period Days | Decimal | No | Waiting period in days before rider benefits apply. | No |
| EliminationPeriodDays | Elimination Period Days | Decimal | No | Elimination period in days before rider benefits become payable. | No |

---

## RiderType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RiderTypeID | Rider Type ID | String | Yes | Unique identifier for the rider type. | No |
| RiderCode | Rider Code | String | No | Rider type code. | No |
| RiderName | Rider Name | String | No | Business name of the rider type. | No |
| RiderCategory | Rider Category | String | No | Rider category such as waiver, accidental death, living benefit, or income rider. | No |
| Description | Description | LongText | No | Description of the rider type. | No |
| AvailableForLife | Available For Life | Boolean | No | Indicates whether the rider is available for life insurance products. | No |
| AvailableForAnnuity | Available For Annuity | Boolean | No | Indicates whether the rider is available for annuity products. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the rider type is active. | No |

---

## RiskClass

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RiskClassID | Risk Class ID | String | Yes | Unique identifier for the risk class. | No |
| RiskClassCode | Risk Class Code | String | No | Underwriting risk class code. | No |
| RiskClassName | Risk Class Name | String | No | Business name of the risk class. | No |
| TobaccoBasis | Tobacco Basis | String | No | Tobacco or nicotine classification basis. | No |
| UnderwritingBasis | Underwriting Basis | String | No | Basis used to assign the class, such as medical, simplified, or guaranteed issue. | No |
| Description | Description | LongText | No | Description of risk class usage. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the risk class is active. | No |

---

## SurrenderChargeSchedule

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SurrenderChargeScheduleID | Surrender Charge Schedule ID | String | Yes | Unique identifier for the surrender charge schedule. | No |
| ScheduleCode | Schedule Code | String | No | Surrender charge schedule code. | No |
| ScheduleName | Schedule Name | String | No | Business name of the surrender charge schedule. | No |
| YearNumber | Year Number | Decimal | No | Policy or contract year to which this schedule row applies. | No |
| ChargePercentage | Charge Percentage | Decimal | No | Surrender charge percentage for the year. | No |
| ChargeAmount | Charge Amount | Decimal | No | Fixed surrender charge amount, if applicable. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the schedule row is effective. | No |
| EffectiveTo | Effective To | Date | No | Date until which the schedule row remains effective. | No |
| Description | Description | LongText | No | Description of the surrender charge rule. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the schedule row is active. | No |

---

## TaxQualification

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| TaxQualificationID | Tax Qualification ID | String | Yes | Unique identifier for the tax qualification. | No |
| QualificationCode | Qualification Code | String | No | Tax qualification code. | No |
| QualificationName | Qualification Name | String | No | Business name of the tax qualification. | No |
| QualificationCategory | Qualification Category | String | No | Tax treatment category. | No |
| Description | Description | LongText | No | Description of qualification rules and servicing implications. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the tax qualification is active. | No |

---

## UnderwritingCase

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| UnderwritingCaseID | Underwriting Case ID | String | Yes | Unique identifier for the underwriting case. | No |
| CaseNumber | Case Number | String | No | Underwriting case number. | No |
| ApplicationDate | Application Date | Date | No | Date the application entered underwriting. | No |
| DecisionDate | Decision Date | Date | No | Date the underwriting decision was made. | No |
| DecisionReason | Decision Reason | String | No | Reason or explanation for the underwriting decision. | No |
| APSReceivedDate | APSReceived Date | Date | No | Date attending physician statement evidence was received. | No |
| MedicalExamDate | Medical Exam Date | Date | No | Date of medical exam, if required. | No |
| MIBCheckIndicator | MIBCheck Indicator | Boolean | No | Indicates whether an MIB check was completed. | No |
| PrescriptionCheckIndicator | Prescription Check Indicator | Boolean | No | Indicates whether prescription history was checked. | No |
| FinancialUnderwritingIndicator | Financial Underwriting Indicator | Boolean | No | Indicates whether financial underwriting review was required. | No |
| ReplacementReviewIndicator | Replacement Review Indicator | Boolean | No | Indicates whether replacement review was required. | No |
| Notes | Notes | LongText | No | Additional underwriting case notes. | No |

---

## UnderwritingDecisionStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| UnderwritingDecisionStatusID | Underwriting Decision Status ID | String | Yes | Unique identifier for the underwriting decision status. | No |
| StatusCode | Status Code | String | No | Underwriting decision status code. | No |
| StatusName | Status Name | String | No | Underwriting decision status name. | No |
| StatusCategory | Status Category | String | No | Decision category for underwriting workflow. | No |
| Description | Description | LongText | No | Business meaning of the underwriting decision status. | No |
| ActiveIndicator | Active Indicator | Boolean | No | Indicates whether the underwriting decision status is active. | No |

---

## UnderwritingRequirement

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| UnderwritingRequirementID | Underwriting Requirement ID | String | Yes | Unique identifier for the underwriting requirement. | No |
| RequirementStatus | Requirement Status | String | No | Current status of the requirement. | No |
| OrderedDate | Ordered Date | Date | No | Date the requirement was ordered. | No |
| ReceivedDate | Received Date | Date | No | Date the requirement was received. | No |
| ExpirationDate | Expiration Date | Date | No | Date the requirement result expires. | No |
| RequirementResult | Requirement Result | String | No | Recorded result or finding for the requirement. | No |
| VendorName | Vendor Name | String | No | Vendor used to fulfill the requirement. | No |
| FollowUpDate | Follow Up Date | Date | No | Date for next follow-up on the requirement. | No |
| WaivedIndicator | Waived Indicator | Boolean | No | Indicates whether the requirement was waived. | No |
| Notes | Notes | LongText | No | Additional notes about the requirement. | No |

---


