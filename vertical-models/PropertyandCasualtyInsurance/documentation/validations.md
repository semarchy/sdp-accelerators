# Validations Documentation

This table summarizes the validations defined in the model, including their entity, name, label, description, and condition.

| Entity | Name | Label | Description | Condition |
|-------------|----------------------|----------------------|-----------------------------------------------|------------------------------------------------|
| Coverage | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for a Coverage entity. | EffectiveFrom <= EffectiveTo |
| CoverageCategory | CoverageCategoryNameMandatory | Coverage Category Name Mandatory Check | Checks that CoverageCategoryName is provided for a Coverage Category entity. | COALESCE(CoverageCategoryName, '') <> '' |
| FormEndorsement | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for a Form Endorsement entity. | EffectiveFrom <= EffectiveTo |
| HomeAsset | DateRangeCheck | Date Range Check | Checks that the StartDate is less than or equal to the EndDate for a Home Asset entity. | StartDate <= EndDate |
| HomeAsset | PropertyAddressLine1Mandatory | Property Address Line 1 Mandatory Check | Checks that PropertyAddressLine1 is provided for a Home Asset entity. | COALESCE(PropertyAddressLine1, '') <> '' |
| InclusionExclusion | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for an Inclusion Exclusion entity. | EffectiveFrom <= EffectiveTo |
| InsurableAsset | DateRangeCheck | Date Range Check | Checks that the StartDate is less than or equal to the EndDate for an Insurable Asset entity. | StartDate <= EndDate |
| InsurancePlan | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for an Insurance Plan entity. | EffectiveFrom <= EffectiveTo |
| InsuranceProduct | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for an Insurance Product entity. | EffectiveFrom <= EffectiveTo |
| InsuranceProduct | ProductNameMandatory | Product Name Mandatory Check | Checks that ProductName is provided for an Insurance Product entity. | COALESCE(ProductName, '') <> '' |
| InsuranceType | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for an Insurance Type entity. | EffectiveFrom <= EffectiveTo |
| InsuranceType | InsuranceTypeNameMandatory | Insurance Type Name Mandatory Check | Checks that InsuranceTypeName is provided for an Insurance Type entity. | COALESCE(InsuranceTypeName, '') <> '' |
| LineOfBusiness | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for a Line of Business entity. | EffectiveFrom <= EffectiveTo |
| LineOfCoverage | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for a Line of Coverage entity. | EffectiveFrom <= EffectiveTo |
| Policy | DateRangeCheck | Date Range Check | Checks that the EffectiveDate is less than or equal to the ExpirationDate for a Policy entity. | EffectiveDate <= ExpirationDate |
| Policy | IssueClosedDateCheck | Issue Closed Date Check | Checks that the IssueDate is less than or equal to the policy close date (stored as CancelDate). | IssueDate <= CancelDate |
| Policy | NoCancellationReason | No Cancellation Reason | (none) | CancelDate IS NULL AND COALESCE(CancellationReason, '') = '' OR CancelDate IS NOT NULL AND COALESCE(CancellationReason, '') <> '' |
| Rating | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for a Rating entity. | EffectiveFrom <= EffectiveTo |
| RegulatoryTest | DateRangeCheck | Date Range Check | Checks that the EffectiveFrom date is less than or equal to the EffectiveTo date for a Regulatory Test entity. | EffectiveFrom <= EffectiveTo |
| RiskClass | RiskClassNameMandatory | Risk Class Name Mandatory Check | Checks that RiskClassName is provided for a Risk Class entity. | COALESCE(RiskClassName, '') <> '' |
| VehicleAsset | DateRangeCheck | Date Range Check | Checks that the StartDate is less than or equal to the EndDate for a Vehicle Asset entity. | StartDate <= EndDate |
| VehicleAsset | PlateNumberMandatory | Plate Number Mandatory Check | Checks that PlateNumber is provided for a Vehicle Asset entity. | COALESCE(PlateNumber, '') <> '' |
| VehicleAsset | VINMandatory | VIN Mandatory Check | Checks that the VIN (Vehicle Identification Number) is provided for a Vehicle Asset entity. | COALESCE(VIN, '') <> '' |

