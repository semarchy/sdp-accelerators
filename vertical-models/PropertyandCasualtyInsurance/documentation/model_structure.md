## Property and Casualty Model Structure

Below is a summary table of all entities in the model, including their label, documentation, references, and attribute count.

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|-------------|-------------|---------------------|-----------------------|--------------------|---------------------|
| AssetStatus | Asset Status | Reference record for managed asset lifecycle statuses. | InsurableAsset | (none) | 4 |
| AssetType | Asset Type | Reference record for managed asset type classifications. | InsurableAsset | (none) | 4 |
| BasementType | Basement Type | Reference record for managed basement classifications. | HomeAsset | (none) | 4 |
| BodyStyle | Body Style | Reference record for managed vehicle body style classifications. | VehicleAsset | (none) | 4 |
| ConstructionType | Construction Type | Reference record for managed home construction classifications. | HomeAsset | (none) | 4 |
| Coverage | Coverage | This entity captures coverage identifiers, descriptive metadata, default limit and deductible behavior. | LineOfCoverage | CoverageCategory, InsurancePlan | 18 |
| CoverageCategory | Coverage Category | This entity represents the different categories of coverage available | Coverage | (none) | 3 |
| CoverageStatus | Coverage Status | Represents reference lifecycle states used to manage coverage availability and servicing behavior. | LineOfCoverage | (none) | 7 |
| DistributionChannel | Distribution Channel | Represents master sales and distribution channels used across policy operations. | Policy | (none) | 4 |
| FormEndorsement | Form Endorsement | This entity captures form identifiers, type, edition date, jurisdiction, lifecycle dates, and active status for policy assembly and compliance. | (none) | InsurancePlan | 10 |
| FoundationType | Foundation Type | Reference record for managed foundation classifications. | HomeAsset | (none) | 4 |
| HomeAsset | Home Asset | Residential property asset mastered for homeowner and dwelling underwriting. | InsurableAsset | BasementType, ConstructionType, FoundationType, RoofType | 35 |
| InclusionExclusion | Inclusion Exclusion | (none) | (none) | LineOfBusiness | 8 |
| InsurableAsset | Insurable Asset | Enterprise-level insured asset record linking policy exposure to vehicle, home, owner, and risk location context. | (none) | AssetStatus, AssetType, HomeAsset, LineOfBusiness, Policy, VehicleAsset | 4 |
| InsurancePlan | Insurance Plan | This entity defines plan-level configuration used by underwriting, rating, and policy issuance. It captures plan identifiers, versioning, effective dates, operational status, and filing references to support governance and regulatory traceability. | Coverage, FormEndorsement, Rating, RegulatoryTest | InsuranceType | 9 |
| InsuranceProduct | Insurance Product | This entity serves as the foundational reference for all insurance products within the system, enabling consistent product definition, management, and integration across policy administration, rating, and reporting systems. It captures essential details such as product codes, names, descriptions, status, and effective dates to support comprehensive product lifecycle management and governance. | InsuranceType | LineOfBusiness | 7 |
| InsuranceType | Insurance Type | Represents a classification of insurance coverage types offered by the company | InsurancePlan | InsuranceProduct, RiskClass | 7 |
| LineOfBusiness | Line Of Business | (none) | InclusionExclusion, InsurableAsset, InsuranceProduct | (none) | 7 |
| LineOfCoverage | Line Of Coverage | Represents a policy-level coverage instance including limits, pricing, and lifecycle details. | (none) | Coverage, CoverageStatus, Policy | 34 |
| PaymentPlan | Payment Plan | Represents billing and premium payment plan options available for policy servicing. | Policy | (none) | 6 |
| PaymentStatus | Payment Status | Represents master payment standing states used by billing and collections. | Policy | (none) | 5 |
| Policy | Policy | (none) | InsurableAsset, LineOfCoverage | DistributionChannel, PaymentPlan, PaymentStatus, PolicyStatus | 20 |
| PolicyStatus | Policy Status | Represents reference policy lifecycle states used by policy administration. | Policy | (none) | 5 |
| Rating | Rating | This entity captures plan-level rating configuration, versioning, effective dates, method, and actuarial notes. | (none) | InsurancePlan | 8 |
| RegulatoryTest | Regulatory Test | This entity captures regulatory test identifiers, jurisdiction, severity, effective dates, and rule descriptions for plan-level compliance governance. | (none) | InsurancePlan | 8 |
| RiskClass | Risk Class | (none) | InsuranceType | (none) | 3 |
| RoofType | Roof Type | Reference record for managed roofing classifications. | HomeAsset | (none) | 4 |
| StateProvince | State or Province | Reference record for state and province jurisdictions. | VehicleAsset | (none) | 5 |
| VehicleAsset | Vehicle Asset | Vehicle asset mastered for auto underwriting, rating, and claims linkage. | InsurableAsset | BodyStyle, StateProvince, VehicleMake, VehicleModel, VehicleSafetyFeature, VehicleTrim, VehicleType | 17 |
| VehicleMake | Vehicle Make | Reference record for vehicle manufacturers. | VehicleAsset, VehicleModel | (none) | 5 |
| VehicleModel | Vehicle Model | Reference record for vehicle models. | VehicleAsset, VehicleTrim | VehicleMake | 4 |
| VehicleSafetyFeature | Vehicle Safety Feature | Reference record for vehicle safety and driver assistance features. | VehicleAsset | (none) | 4 |
| VehicleTrim | Vehicle Trim | Reference record for vehicle trim levels. | VehicleAsset | VehicleModel | 4 |
| VehicleType | Vehicle Type | Reference record for managed vehicle type classifications. | VehicleAsset | (none) | 4 |

# Detailed Model Structure

Below are markdown tables for each entity in the model. Each table lists the attributes and their metadata.

## AssetStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AssetStatusID | Asset Status ID | LongInteger | Yes | Unique identifier for an asset status. | No |
| AssetStatusCode | Asset Status Code | String | Yes | Enterprise code for the asset status. | No |
| AssetStatusName | Asset Status Name | String | Yes | Asset status display name. | No |
| Description | Description | String | No | Asset status description. | No |

---

## AssetType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AssetTypeID | Asset Type ID | LongInteger | Yes | Unique identifier for an asset type. | No |
| AssetTypeCode | Asset Type Code | String | Yes | Enterprise code for the asset type. | No |
| AssetTypeName | Asset Type Name | String | Yes | Asset type display name. | No |
| Description | Description | String | No | Asset type description. | No |

---

## BasementType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BasementTypeID | Basement Type ID | LongInteger | Yes | Unique identifier for a basement type. | No |
| BasementTypeCode | Basement Type Code | String | Yes | Enterprise code for the basement type. | No |
| BasementTypeName | Basement Type Name | String | Yes | Basement type display name. | No |
| Description | Description | String | No | Basement type description. | No |

---

## BodyStyle

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| BodyStyleID | Body Style ID | LongInteger | Yes | Unique identifier for a body style. | No |
| BodyStyleCode | Body Style Code | String | Yes | Enterprise code for the body style. | No |
| BodyStyleName | Body Style Name | String | Yes | Body style display name. | No |
| Description | Description | String | No | Body style description. | No |

---

## ConstructionType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ConstructionTypeID | Construction Type ID | LongInteger | Yes | Unique identifier for a construction type. | No |
| ConstructionTypeCode | Construction Type Code | String | Yes | Enterprise code for the construction type. | No |
| ConstructionTypeName | Construction Type Name | String | Yes | Construction type display name. | No |
| Description | Description | String | No | Construction type description. | No |

---

## Coverage

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CoverageID | Coverage ID | String | Yes |  | No |
| CoverageCode | Coverage Code | String | Yes | Enterprise-defined unique identifier representing a specific coverage component. | No |
| CoverageName | Coverage Name | String | Yes | Display name of the coverage as presented to agents and policyholders. | No |
| CoverageDescription | Coverage Description | LongText | No | Detailed explanation of the protection provided, including scope and intent. | No |
| DefaultLimitType | Default Limit Type | CoverageLimitType | No | Default limit structure associated with this coverage definition. | No |
| DefaultDeductibleType | Default Deductible Type | CoverageDeductibleType | No | Default deductible structure associated with this coverage. | No |
| MinimumLimitAmount | Minimum Limit Amount | Decimal | No | Minimum allowable coverage limit that may be selected for this coverage. | No |
| MaximumLimitAmount | Maximum Limit Amount | Decimal | No | Maximum allowable coverage limit permitted for this coverage. | No |
| DefaultLimitAmount | Default Limit Amount | Decimal | No | Default coverage limit automatically assigned during policy creation if no override is selected. | No |
| MinimumDeductibleAmount | Minimum Deductible Amount | Decimal | No | Lowest deductible amount permitted for this coverage. | No |
| MaximumDeductibleAmount | Maximum Deductible Amount | Decimal | No | Highest deductible amount permitted for this coverage. | No |
| DefaultDeductibleAmount | Default Deductible Amount | Decimal | No | Default deductible assigned to the coverage if no customer selection is made. | No |
| CoinsurancePercentage | Coinsurance Percentage | Decimal | No | Percentage of covered loss shared by the insured under policy terms. | No |
| WaitingPeriodDays | Waiting Period Days | Integer | No | Number of days that must elapse before coverage benefits become payable. | No |
| AggregateLimitIndicator | Aggregate Limit Indicator | Boolean | No | Indicates whether the coverage is subject to an aggregate limit across multiple claims. | No |
| OccurrenceLimitIndicator | Occurrence Limit Indicator | Boolean | No | Indicates whether the coverage enforces a per-occurrence claim limit. | No |
| EffectiveFrom | Effective From | Date | No | Date from which this coverage definition is valid. | No |
| EffectiveTo | Effective To | Date | No | Date until which this coverage definition remains valid. | No |

---

## CoverageCategory

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CoverageCategoryID | Coverage Category ID | LongInteger | Yes |  | No |
| CoverageCategoryName | Coverage Category Name | String | No |  | No |
| Description | Description | String | No |  | No |

---

## CoverageStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CoverageStatusCode | Coverage Status Code | String | Yes | Unique code representing a coverage lifecycle state. | No |
| CoverageStatusName | Coverage Status Name | String | Yes | Display name of the coverage status (e.g., Available, Suspended, Retired). | No |
| CoverageLifecycleStage | Coverage Lifecycle Stage | String | No | Lifecycle grouping such as Draft, Released, Suspended, or Retired. | No |
| SelectableForNewBusinessFlag | Selectable For New Business Flag | Boolean | Yes | Indicates whether this status allows the coverage to be selected on new quotes and policies. | No |
| ClaimsPayableFlag | Claims Payable Flag | Boolean | Yes | Indicates whether claims remain payable for coverages in this status. | No |
| RequiresUnderwriterReviewFlag | Requires Underwriter Review Flag | Boolean | No | Indicates whether this status requires an underwriting review before coverage can be changed or activated. | No |
| Description | Description | LongText | No | Detailed explanation of the coverage status and its operational implications. | No |

---

## DistributionChannel

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ChannelCode | Channel Code | String | Yes | Unique identifier for sales/distribution channel. | No |
| ChannelName | Channel Name | String | Yes | Display name of channel (Direct, Agency, Broker, Partner). | No |
| ChannelType | Channel Type | String | No | Higher-level grouping (Retail, Wholesale, Digital). | No |
| CommissionEligibleFlag | Commission Eligible Flag | Boolean | No | Indicates whether channel earns commission. | No |

---

## FormEndorsement

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| FormEndorsementID | Form Endorsement ID | String | Yes |  | No |
| FormCode | Form Code | String | Yes | Canonical enterprise identifier for a form or endorsement. | No |
| FormNumber | Form Number | String | No | Carrier-issued or industry-standard form number. | No |
| FormTitle | Form Title | String | Yes | Official title of the form or endorsement. | No |
| FormType | Form Type | FormEndorsementType | Yes | Classification indicating document purpose (Coverage Form, Endorsement, Notice, Other). | No |
| EditionDate | Edition Date | Date | No | Official edition or revision date of the form. | No |
| JurisdictionState | Jurisdiction State | String | No | State or jurisdiction where the form applies. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the form becomes available for use. | No |
| EffectiveTo | Effective To | Date | No | Date until which the form remains valid. | No |
| ActiveFlag | Active Flag | Boolean | No | Indicates whether the form is currently active and selectable. | No |

---

## FoundationType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| FoundationTypeID | Foundation Type ID | LongInteger | Yes | Unique identifier for a foundation type. | No |
| FoundationTypeCode | Foundation Type Code | String | Yes | Enterprise code for the foundation type. | No |
| FoundationTypeName | Foundation Type Name | String | Yes | Foundation type display name. | No |
| Description | Description | String | No | Foundation type description. | No |

---

## HomeAsset

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| HomeAssetId | Home Asset ID | LongInteger | Yes | Unique identifier representing a specific residential property asset record. | No |
| PropertyAddressLine1 | Property Address Line 1 | String | No | Primary street address for the insured residential property. | Yes |
| PropertyAddressLine2 | Property Address Line 2 | String | No | Secondary address information such as unit, suite, or apartment number. | No |
| PropertyCity | Property City | String | No | City of the insured residential property location. | Yes |
| PropertyState | Property State | String | No | State or province of the insured residential property location. | Yes |
| PropertyPostalCode | Property Postal Code | String | No | Postal or ZIP code of the insured residential property location. | Yes |
| PropertyCountry | Property Country | String | No | Country of the insured residential property location. | No |
| YearBuilt | Year Built | Integer | No | Calendar year the dwelling structure was originally constructed. | Yes |
| ConstructionQuality | Construction Quality | ConstructionQuality | No | Quality or grade of construction (e.g., Standard, Custom, Luxury). | No |
| RoofYear | Roof Year | Integer | No | Year the roof was last replaced or substantially renovated. | No |
| SquareFootage | Square Footage | Integer | No | Total finished living area of the dwelling. | Yes |
| NumberOfStories | Number Of Stories | Integer | No | Number of above-grade floors in the structure. | No |
| NumberOfUnits | Number Of Units | Integer | No | Total residential units within the structure. | No |
| GarageType | Garage Type | GarageType | No | Classification of garage structure (Attached, Detached, None). | No |
| OccupancyType | Occupancy Type | OccupancyType | Yes | Indicates how the dwelling is occupied (Owner, Tenant, Vacant, Seasonal). | No |
| PrimaryResidenceFlag | Primary Residence Flag | Boolean | No | Indicates whether the property is the insured's primary residence. | No |
| ProtectionClass | Protection Class | String | No | Fire protection class assigned to the location. | No |
| DistanceToFireStation | Distance To Fire Station | Decimal | No | Distance from property to nearest responding fire station. | No |
| SprinklerSystemFlag | Sprinkler System Flag | Boolean | No | Indicates presence of an operational fire sprinkler system. | No |
| BurglarAlarmFlag | Burglar Alarm Flag | Boolean | No | Indicates presence of monitored burglary alarm system. | No |
| SmokeDetectorFlag | Smoke Detector Flag | Boolean | No | Indicates presence of functional smoke detection systems. | No |
| SwimmingPoolFlag | Swimming Pool Flag | Boolean | No | Indicates presence of a swimming pool on premises. | No |
| TrampolineFlag | Trampoline Flag | Boolean | No | Indicates presence of a trampoline on premises. | No |
| DogBreed | Dog Breed | String | No | Declared breed of dog(s) residing at the property, if applicable. | No |
| ReplacementCost | Replacement Cost | Decimal | No | Estimated cost to rebuild the dwelling at current construction prices. | Yes |
| MarketValue | Market Value | Decimal | No | Estimated current market value of the property. | Yes |
| PersonalPropertyLimit | Personal Property Limit | Decimal | No | Coverage limit for personal property contents. | No |
| LossUseLimit | Loss Use Limit | Decimal | No | Coverage limit for additional living expenses or loss of use. | No |
| LiabilityLimit | Liability Limit | Decimal | No | Personal liability coverage limit associated with the dwelling. | No |
| DeductibleAmount | Deductible Amount | Decimal | No | Deductible applicable to property damage claims. | No |
| FloodZone | Flood Zone | String | No | FEMA-designated flood zone classification for the property. | No |
| EarthquakeZone | Earthquake Zone | String | No | Seismic hazard classification applicable to the property location. | No |
| WindHailExclusionFlag | Wind Hail Exclusion Flag | Boolean | No | Indicates whether wind or hail perils are excluded from coverage. | No |
| StartDate | Start Date | Date | No | Date the home asset becomes insured under a policy. | No |
| EndDate | End Date | Date | No | Date the home asset is removed from coverage. | No |

---

## InclusionExclusion

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| InclusionExclusionID | Inclusion Exclusion ID | LongInteger | Yes | System-generated unique identifier for the inclusion or exclusion record. | No |
| Type | Type | InclusionExclusionType | No | Indicates whether the clause expands (Inclusion) or restricts (Exclusion) coverage. | No |
| Title | Title | String | No | Short descriptive title summarizing the clause content. | No |
| Description | Description | LongText | No | Plain-language explanation summarizing the intent and effect of the clause. | No |
| RuleText | Rule Text | LongText | No | Formal legal or contractual wording of the clause. | No |
| JurisdictionState | Jurisdiction State | String | No | State or jurisdiction where the clause specifically applies. | No |
| EffectiveFrom | Effective From | Date | No | Date from which this clause becomes applicable. | No |
| EffectiveTo | Effective To | Date | No | Date until which this clause remains applicable. | No |

---

## InsurableAsset

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AssetId | Asset ID | LongInteger | Yes | System-generated unique identifier representing an insurable asset across the enterprise. | No |
| AssetDescription | Asset Description | String | No | Human-readable description summarizing the insured asset. | No |
| StartDate | Start Date | Date | No | Date the asset becomes eligible or scheduled for insurance coverage. | No |
| EndDate | End Date | Date | No | Date the asset is removed from insurance coverage. | No |

---

## InsurancePlan

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| InsurancePlanID | Insurance Plan ID | String | Yes |  | No |
| PlanCode | Plan Code | String | Yes | Unique identifier representing a configured plan within an insurance type. | No |
| PlanName | Plan Name | String | Yes | Business-facing name of the plan configuration. | No |
| Description | Description | LongText | No | Detailed description of the insurance plan, its features, and intended use cases. | No |
| PlanVersion | Plan Version | String | No | Version identifier for iterative plan updates. | No |
| EffectiveFrom | Effective From | Date | No | Date on which this plan configuration becomes effective. | No |
| EffectiveTo | Effective To | Date | No | Date on which this plan configuration expires. | No |
| PlanStatus | Plan Status | PlanStatus | Yes | Current operational status of the plan (e.g., Active, Withdrawn, Suspended). | No |
| FilingReference | Filing Reference | String | No | Regulatory filing or approval identifier tied to this plan. | No |

---

## InsuranceProduct

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| InsuranceProductID | Insurance Product ID | String | Yes | Unique identifier for the Insurance Product | No |
| ProductCode | Product Code | String | No | Enterprise-defined unique identifier for the insurance product. | No |
| ProductName | Product Name | String | No | Commercial or marketing name of the insurance product. | No |
| ProductDescription | Product Description | LongText | No | Detailed explanation of product features, target market, and coverage positioning. | No |
| ProductStatus | Product Status | InsuranceProductStaus | No | Current lifecycle state of the product (e.g., Active, Retired, Suspended). | No |
| EffectiveFrom | Effective From | Date | No | Date from which the product configuration is effective. | No |
| EffectiveTo | Effective To | Date | No | Date until which the product configuration remains valid. | No |

---

## InsuranceType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| InsuranceTypeID | Insurance Type ID | String | Yes | Unique identifier for each insurance type record, generated sequentially to ensure uniqueness and support efficient referencing across the system. | No |
| InsuranceTypeCode | Insurance Type Code | String | No | Enterprise-unique identifier representing a specific insurance type classification. | No |
| InsuranceTypeName | Insurance Type Name | String | No | Display name of the insurance type (e.g., Personal Auto, Commercial Property). | No |
| Description | Description | LongText | No | Detailed description of the insurance type, outlining its characteristics and coverage details. | No |
| AdmittedFlag | Admitted Flag | Boolean | No | Indicates whether the coverage is admitted (regulated and approved) or non-admitted. | No |
| EffectiveFrom | Effective From | Date | No | Date from which this insurance type definition becomes effective. | No |
| EffectiveTo | Effective To | Date | No | Date until which this insurance type definition remains valid. | No |

---

## LineOfBusiness

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| LineOfBusinessID | Line Of Business ID | String | Yes |  | No |
| LOBCode | LOB Code | String | No | Enterprise-unique identifier representing a specific Line of Business classification. | No |
| LOBName | LOB Name | String | No | Display name of the Line of Business (e.g., Personal Auto, Commercial Property). | No |
| LOBDescription | LOB Description | LongText | No | Detailed description of the Line of Business, including key characteristics and coverage details. | No |
| EffectiveFrom | Effective From | Date | No | Date from which this LOB configuration becomes valid. | No |
| EffectiveTo | Effective To | Date | No | Date until which this LOB configuration remains valid. | No |
| ActiveFlag | Active Flag | Boolean | No | Indicates whether this LOB is currently active for underwriting and issuance. | No |

---

## LineOfCoverage

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| LineOfCoverageId | Line Of Coverage Id | String | Yes | System-generated unique identifier representing a specific policy coverage instance. | No |
| AssetId | Asset Id | String | No | Reference to specific insured asset when coverage applies at item level. | No |
| CoverageTrigger | Coverage Trigger | CoverageTriggerType | No | Defines claim trigger mechanism such as Occurrence or Claims-Made. | No |
| ClaimsMadeRetroDate | Claims Made Retro Date | Date | No | Retroactive date applicable for claims-made coverage. | No |
| LimitAmount | Limit Amount | Decimal | No | Primary limit of liability for this coverage instance. | No |
| LimitType | Limit Type | CoverageLimitType | No | Structure of the limit (Per Occurrence, Aggregate, Combined Single Limit). | No |
| AggregateLimit | Aggregate Limit | Decimal | No | Maximum cumulative payout allowed during policy period. | No |
| SublimitAmount | Sublimit Amount | Decimal | No | Specific lower limit applied to defined peril or subcategory. | No |
| PerRiskLimit | Per Risk Limit | Decimal | No | Limit applied individually per insured asset or risk unit. | No |
| DeductibleAmount | Deductible Amount | Decimal | No | Deductible applicable to this coverage instance. | No |
| DeductibleType | Deductible Type | CoverageDeductibleType | No | Type of deductible structure (Flat, Percentage, Franchise). | No |
| Rate | Rate | Decimal | No | Applied rating factor or premium rate for the coverage. | No |
| ExposureBase | Exposure Base | Decimal | No | Exposure metric used for rating (e.g., payroll, sales, area). | No |
| ExposureUnit | Exposure Unit | String | No | Unit of measure associated with exposure base. | No |
| ManualPremium | Manual Premium | Decimal | No | Premium calculated before discretionary credits or debits. | No |
| TechnicalPremium | Technical Premium | Decimal | No | Actuarially indicated premium based on risk characteristics. | No |
| WrittenPremium | Written Premium | Decimal | No | Premium recorded at issuance for this coverage. | No |
| EarnedPremium | Earned Premium | Decimal | No | Premium portion earned over elapsed coverage period. | No |
| FullyEarnedFlag | Fully Earned Flag | Boolean | No | Indicates whether premium is fully earned at inception. | No |
| DiscountAmount | Discount Amount | Decimal | No | Total discount applied to coverage premium. | No |
| SurchargeAmount | Surcharge Amount | Decimal | No | Additional premium applied due to elevated risk factors. | No |
| ValuationMethod | Valuation Method | ValuationMethod | No | Method used to determine claim settlement value. | No |
| BlanketIndicator | Blanket Indicator | Boolean | No | Indicates coverage applies collectively across multiple assets. | No |
| PrimaryExcessIndicator | Primary Excess Indicator | String | No | Indicates whether coverage is primary, excess, or umbrella layer. | No |
| QuotaSharePercent | Quota Share Percent | Decimal | No | Percentage of risk ceded under quota share arrangement. | No |
| EndorsementIndicator | Endorsement Indicator | Boolean | No | Indicates coverage was added or modified via endorsement. | No |
| EndorsementEffectiveDate | Endorsement Effective Date | Date | No | Date endorsement-related changes become effective. | No |
| OriginalEffectiveDate | Original Effective Date | Date | No | Original inception date of this coverage instance. | No |
| UnderwriterNotes | Underwriter Notes | LongText | No | Internal notes documenting underwriting rationale or exceptions. | No |
| RiskScore | Risk Score | Decimal | No | Quantitative risk score derived from underwriting or predictive modeling. | No |
| LossHistoryIndicator | Loss History Indicator | Boolean | No | Indicates prior losses relevant to this coverage. | No |
| EffectiveFrom | Effective From | Date | Yes | Date coverage becomes effective under the policy. | No |
| EffectiveTo | Effective To | Date | No | Date coverage terminates or expires. | No |
| ActiveFlag | Active Flag | Boolean | Yes | Indicates whether the coverage instance is currently active. | No |

---

## PaymentPlan

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PlanCode | Plan Code | String | Yes | Unique identifier for a payment plan option. | No |
| PlanName | Plan Name | String | Yes | Business-friendly name of the payment plan (e.g., Monthly, Quarterly, Annual). | No |
| BillingFrequency | Billing Frequency | String | No | Frequency of payment billing cycle such as Monthly, Quarterly, or Annual. | No |
| InstallmentCount | Installment Count | Integer | No | Number of installments expected during the policy term under this plan. | No |
| AutoPaySupportedFlag | Auto Pay Supported Flag | Boolean | No | Indicates whether this payment plan supports automatic recurring payments. | No |
| GracePeriodDays | Grace Period Days | Integer | No | Number of grace days allowed after due date before delinquency actions begin. | No |

---

## PaymentStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| StatusCode | Status Code | String | Yes | Unique identifier for a payment status value. | No |
| StatusName | Status Name | String | Yes | Display name of payment status (e.g., Paid, Overdue, Delinquent). | No |
| StatusCategory | Status Category | String | No | Higher-level grouping such as Current, AtRisk, or Delinquent. | No |
| DelinquentIndicator | Delinquent Indicator | Boolean | No | Indicates whether this status represents delinquency requiring follow-up actions. | No |
| ActiveFlag | Active Flag | Boolean | No | Indicates whether the payment status code is currently active for use. | No |

---

## Policy

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PolicyID | Policy ID | String | Yes | System-generated golden identifier uniquely representing a consolidated policy record across source systems. | No |
| PolicyNumber | Policy Number | String | Yes | Carrier-issued business policy number visible to customers and agents. | No |
| PolicyVersion | Policy Version | String | No | Version or iteration of the policy when explicit versioning is supported by the carrier. | No |
| EffectiveDate | Effective Date | Date | No | Date on which policy coverage becomes effective. | No |
| ExpirationDate | Expiration Date | Date | No | Date on which policy coverage expires. | No |
| IssueDate | Issue Date | Date | No | Date the policy was formally issued or bound by the carrier. | No |
| CancelDate | Cancel Date | Date | No | Date the policy was cancelled prior to expiration, if applicable. | No |
| CancellationReason | Cancellation Reason | String | No | Reason code explaining why the policy was cancelled or non-renewed. | No |
| JurisdictionState | Jurisdiction State | String | No | State or jurisdiction governing the policy contract. | No |
| CurrencyCode | Currency Code | String | No | Currency in which premiums, limits, and claims are denominated. | No |
| WrittenPremium | Written Premium | Decimal | No | Total premium written for the policy term at issuance. | No |
| TotalPremium | Total Premium | Decimal | No | Total premium payable by the insured including fees and adjustments. | No |
| LastPremiumPaidDate | Last Premium Paid Date | Date | No | Date on which the most recent premium payment was successfully received for the policy. | No |
| LastPremiumPaidAmount | Last Premium Paid Amount | Decimal | No | Amount of the most recent successfully received premium payment. | No |
| OutstandingPremiumAmount | Outstanding Premium Amount | Decimal | No | Remaining unpaid premium balance associated with the policy. | No |
| PaymentDueDate | Payment Due Date | Date | No | Next scheduled premium payment due date for the policy billing cycle. | No |
| AutoPayIndicator | Auto Pay Indicator | Boolean | No | Indicates whether the policyholder is enrolled in automatic recurring premium payments. | No |
| GracePeriodEndDate | Grace Period End Date | Date | No | Date on which the non-payment grace period expires and policy may become subject to lapse processing. | No |
| PolicyLapseIndicator | Policy Lapse Indicator | Boolean | No | Indicates whether the policy has entered a lapsed state due to non-payment of premium obligations. | No |
| ReinstatementDate | Reinstatement Date | Date | No | Date on which a previously cancelled or lapsed policy was reinstated and returned to active coverage status. | No |

---

## PolicyStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| PolicyStatusCode | Policy Status Code | String | Yes | Unique code representing a policy lifecycle state. | No |
| PolicyStatusName | Policy Status Name | String | Yes | Display name of the policy status (e.g., Active, Cancelled). | No |
| StatusCategory | Status Category | String | No | High-level grouping (e.g., In-Force, Terminated, Pending). | No |
| IsInForceFlag | Is In Force Flag | Boolean | Yes | Indicates whether status represents active coverage. | No |
| Description | Description | LongText | No | Detailed explanation of the policy status, including implications for coverage and servicing. | No |

---

## Rating

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RatingID | Rating ID | String | Yes |  | No |
| RatingPlanCode | Rating Plan Code | String | Yes | Unique identifier representing a rating configuration or plan. | No |
| RatingPlanName | Rating Plan Name | String | Yes | Business-facing name of the rating plan. | No |
| Version | Version | String | No | Version identifier tracking changes to rating logic or rate factors. | No |
| EffectiveFrom | Effective From | Date | No | Date from which the rating plan becomes effective. | No |
| EffectiveTo | Effective To | Date | No | Date until which the rating plan remains valid. | No |
| RatingMethod | Rating Method | RatingMethod | No | Method used to compute premium (e.g., Table-driven, Formula-based, External engine). | No |
| Notes | Notes | LongText | No | Additional contextual information regarding rating assumptions or configuration. | No |

---

## RegulatoryTest

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RegulatoryTestID | Regulatory Test ID | String | Yes |  | No |
| RegulatoryTestCode | Regulatory Test Code | String | Yes | Unique identifier representing a regulatory or compliance validation rule. | No |
| Jurisdiction | Jurisdiction | String | No | Regulatory authority or jurisdiction governing the validation rule. | No |
| TestName | Test Name | String | Yes | Name of the compliance or validation test. | No |
| TestDescription | Test Description | LongText | No | Detailed explanation of the regulatory rule logic and business purpose. | No |
| Severity | Severity | RegulatoryTestSeverity | Yes | Severity level triggered upon test failure (Warning, Error, Blocking). | No |
| EffectiveFrom | Effective From | Date | No | Date from which this regulatory rule becomes enforceable. | No |
| EffectiveTo | Effective To | Date | No | Date until which this regulatory rule remains enforceable. | No |

---

## RiskClass

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RiskClassID | Risk Class ID | LongInteger | Yes | Unique identifier for the Risk Class entity. | No |
| RiskClassName | Risk Class Name | String | No | Name of the Risk Class. | No |
| RiskClassDescription | Risk Class Description | String | No | Description of the Risk Class. | No |

---

## RoofType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RoofTypeID | Roof Type ID | LongInteger | Yes | Unique identifier for a roof type. | No |
| RoofTypeCode | Roof Type Code | String | Yes | Enterprise code for the roof type. | No |
| RoofTypeName | Roof Type Name | String | Yes | Roof type display name. | No |
| Description | Description | String | No | Roof type description. | No |

---

## StateProvince

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| StateProvinceID | State Province ID | LongInteger | Yes | Unique identifier for a state or province. | No |
| StateCode | State Code | String | Yes | State or province code. | No |
| StateName | State Name | String | Yes | State or province name. | No |
| CountryCode | Country Code | String | No | Country code. | No |
| Description | Description | String | No | Description of the jurisdiction. | No |

---

## VehicleAsset

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| VehicleAssetId | Vehicle Asset ID | LongInteger | Yes | System-generated unique identifier representing a specific vehicle asset record. | No |
| VIN | VIN | String | No | Vehicle Identification Number uniquely assigned to the vehicle. | Yes |
| PlateNumber | Plate Number | String | No | Registered license plate number assigned by issuing authority. | Yes |
| Year | Year | Integer | Yes | Model year of the vehicle as defined by manufacturer. | Yes |
| FuelType | Fuel Type | FuelType | No | Primary fuel or propulsion type (Gasoline, Diesel, Hybrid, Electric). | No |
| EngineSize | Engine Size | String | No | Engine displacement or performance specification. | No |
| AntiTheftDeviceFlag | Anti Theft Device Flag | Boolean | No | Indicates presence of approved anti-theft or immobilizer system. | No |
| UsageType | Usage Type | UsageType | Yes | Declared primary usage of the vehicle (Pleasure, Commute, Business). | No |
| AnnualMileage | Annual Mileage | Integer | No | Estimated miles driven annually. | No |
| OwnershipType | Ownership Type | OwnershipType | No | Ownership classification (Owned, Leased, Financed). | No |
| OriginalPurchasePrice | Original Purchase Price | Decimal | No | Original acquisition cost of the vehicle. | No |
| CurrentMarketValue | Current Market Value | Decimal | No | Estimated current actual cash value of the vehicle. | No |
| CollisionDeductible | Collision Deductible | Decimal | No | Deductible amount applicable to collision coverage. | No |
| ComprehensiveDeductible | Comprehensive Deductible | Decimal | No | Deductible amount applicable to comprehensive coverage. | No |
| UninsuredMotoristLimit | Uninsured Motorist Limit | Decimal | No | Coverage limit for uninsured/underinsured motorist protection. | No |
| StartDate | Start Date | Date | No | Date vehicle becomes insured under the policy. | No |
| EndDate | End Date | Date | No | Date vehicle is removed from coverage. | No |

---

## VehicleMake

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| VehicleMakeID | Vehicle Make ID | LongInteger | Yes | Unique identifier for a vehicle make. | No |
| MakeCode | Make Code | String | Yes | Enterprise code for the vehicle manufacturer. | No |
| MakeName | Make Name | String | Yes | Vehicle manufacturer name. | No |
| Website | Website | String | Yes | Brand website | No |
| Description | Description | String | No | Vehicle make description. | No |

---

## VehicleModel

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| VehicleModelID | Vehicle Model ID | LongInteger | Yes | Unique identifier for a vehicle model. | No |
| ModelCode | Model Code | String | Yes | Enterprise code for the vehicle model. | No |
| ModelName | Model Name | String | Yes | Vehicle model name. | No |
| Description | Description | String | No | Vehicle model description. | No |

---

## VehicleSafetyFeature

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| VehicleSafetyFeatureID | Vehicle Safety Feature ID | LongInteger | Yes | Unique identifier for a vehicle safety feature. | No |
| FeatureCode | Feature Code | String | Yes | Enterprise code for the safety feature. | No |
| FeatureName | Feature Name | String | Yes | Safety feature name. | No |
| Description | Description | String | No | Safety feature description. | No |

---

## VehicleTrim

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| VehicleTrimID | Vehicle Trim ID | LongInteger | Yes | Unique identifier for a vehicle trim. | No |
| TrimCode | Trim Code | String | Yes | Enterprise code for the vehicle trim. | No |
| TrimName | Trim Name | String | Yes | Vehicle trim name. | No |
| Description | Description | String | No | Vehicle trim description. | No |

---

## VehicleType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| VehicleTypeID | Vehicle Type ID | LongInteger | Yes | Unique identifier for a vehicle type. | No |
| VehicleTypeCode | Vehicle Type Code | String | Yes | Enterprise code for the vehicle type. | No |
| VehicleTypeName | Vehicle Type Name | String | Yes | Vehicle type display name. | No |
| Description | Description | String | No | Vehicle type description. | No |

---


