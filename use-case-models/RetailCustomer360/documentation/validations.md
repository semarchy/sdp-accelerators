# Validations Documentation

Validations are logical constraints that check data quality and business rules during entity processing, with execution scopes such as PRE_CONSO and POST_CONSO.

| Entity | Name | Label | Validation Scope | Condition |
|---|---|---|---|---|
| Account | AccountNameMustExist | Account Name Must Exist | PRE_CONSO | AccountName IS NOT NULL |
| Account | AccountSinceDateMustNotBeFuture | Account Since Date Must Not Be Future | PRE_CONSO | AccountSinceDate IS NULL OR AccountSinceDate <= CURRENT_DATE() |
| Account | CreditLimitMustBeNonNegative | Credit Limit Must Be Non Negative | PRE_CONSO | CreditLimit IS NULL OR CreditLimit >= 0 |
| Account | RevenueMustBeNonNegative | Revenue Must Be Non Negative | PRE_CONSO | Revenue IS NULL OR Revenue >= 0 |
| Account | RiskScoreMustBeInRange | Risk Score Must Be In Range | PRE_CONSO | RiskScore IS NULL OR (RiskScore >= 0 AND RiskScore <= 100) |
| Campaign | ActualSpendMustBeNonNegative | Actual Spend Must Be Non Negative | PRE_CONSO | ActualSpend IS NULL OR ActualSpend >= 0 |
| Campaign | BudgetMustBeNonNegative | Budget Must Be Non Negative | PRE_CONSO | Budget IS NULL OR Budget >= 0 |
| Campaign | ClicksMustNotExceedImpressions | Clicks Must Not Exceed Impressions | PRE_CONSO | Clicks IS NULL OR Impressions IS NULL OR Clicks <= Impressions |
| Campaign | ConversionsMustNotExceedClicks | Conversions Must Not Exceed Clicks | PRE_CONSO | Conversions IS NULL OR Clicks IS NULL OR Conversions <= Clicks |
| Campaign | EndDateMustNotBeBeforeStartDate | End Date Must Not Be Before Start Date | PRE_CONSO | StartDate IS NULL OR EndDate IS NULL OR EndDate >= StartDate |
| ContactPointAddress | AddressMustHaveCoreLocation | Address Must Have Core Location | PRE_CONSO | AddressLine1 IS NOT NULL OR City IS NOT NULL OR PostalCode IS NOT NULL |
| ContactPointAddress | CustomerMustExist | Customer Must Exist | POST_CONSO | FID_Customer IS NOT NULL |
| ContactPointAddress | LatitudeMustBeInRange | Latitude Must Be In Range | PRE_CONSO | Latitude IS NULL OR (Latitude >= -90 AND Latitude <= 90) |
| ContactPointAddress | LongitudeMustBeInRange | Longitude Must Be In Range | PRE_CONSO | Longitude IS NULL OR (Longitude >= -180 AND Longitude <= 180) |
| ContactPointAddress | PostalCodeRequiresCountry | Postal Code Requires Country | PRE_CONSO | PostalCode IS NULL OR FID_Country IS NOT NULL |
| ContactPointEmail | CustomerMustExist | Customer Must Exist | POST_CONSO | FID_Customer IS NOT NULL |
| LoyaltyProgram | EconomicsMustBeNonNegative | Economics Must Be Non Negative | PRE_CONSO | (EnrollmentFee IS NULL OR EnrollmentFee >= 0) AND (PointAccrualRate IS NULL OR PointAccrualRate >= 0) AND (PointRedemptionRate IS NULL OR PointRedemptionRate >= 0) AND (MinimumRedeemPoints IS NULL OR MinimumRedeemPoints >= 0) AND (PointsExpiryMonths IS NULL OR PointsExpiryMonths >= 0) |
| LoyaltyProgram | EndDateMustNotBeBeforeStartDate | End Date Must Not Be Before Start Date | PRE_CONSO | StartDate IS NULL OR EndDate IS NULL OR EndDate >= StartDate |
| LoyaltyProgramMember | PointsBalancesMustBeConsistent | Points Balances Must Be Consistent | PRE_CONSO | (AvailablePointsBalance IS NULL OR AvailablePointsBalance >= 0) AND (LifetimePointsEarned IS NULL OR LifetimePointsEarned >= 0) AND (LifetimePointsRedeemed IS NULL OR LifetimePointsRedeemed >= 0) AND (LifetimePointsEarned IS NULL OR LifetimePointsRedeemed IS NULL OR LifetimePointsRedeemed <= LifetimePointsEarned) |
| MobileAppEngagement | SessionOrDeviceMustExist | Session Or Device Must Exist | PRE_CONSO | AppSessionId IS NOT NULL OR DeviceId IS NOT NULL |
| PartyIdentification | ExpiryDateMustNotBeBeforeIssueDate | Expiry Date Must Not Be Before Issue Date | PRE_CONSO | IssueDate IS NULL OR ExpiryDate IS NULL OR ExpiryDate >= IssueDate |
| PartyIdentification | IdentificationNumberOrMaskedRequired | Identification Number Or Masked Value Required | PRE_CONSO | IdentificationNumber IS NOT NULL OR MaskedIdentificationNumber IS NOT NULL |
| Product | DiscontinueDateMustNotBeBeforeLaunchDate | Discontinue Date Must Not Be Before Launch Date | PRE_CONSO | LaunchDate IS NULL OR DiscontinueDate IS NULL OR DiscontinueDate >= LaunchDate |
| Product | PricesMustBeValid | Prices Must Be Valid | PRE_CONSO | (Price IS NULL OR Price >= 0) AND (ListPrice IS NULL OR ListPrice >= 0) AND (CostPrice IS NULL OR CostPrice >= 0) AND (Price IS NULL OR ListPrice IS NULL OR ListPrice >= Price) |
| SalesOrder | CancelledOrReturnedMustNotBePaid | Cancelled Or Returned Must Not Be Paid | PRE_CONSO | OrderStatus NOT IN ('Cancelled', 'Returned') OR PaymentStatus <> 'Paid' |
| SalesOrder | TotalAmountComponentsMustBeConsistent | Total Amount Components Must Be Consistent | PRE_CONSO | (SubtotalAmount IS NULL OR SubtotalAmount >= 0) AND (DiscountAmount IS NULL OR DiscountAmount >= 0) AND (TaxAmount IS NULL OR TaxAmount >= 0) AND (ShippingAmount IS NULL OR ShippingAmount >= 0) AND (TotalAmount IS NULL OR TotalAmount >= 0) AND (SubtotalAmount IS NULL OR DiscountAmount IS NULL OR DiscountAmount <= SubtotalAmount) |
| SalesOrderItem | MustHaveProduct | Must Have Product | PRE_CONSO | FID_Product IS NOT NULL |
| SalesOrderItem | ReturnedItemsMustNotBeOpen | Returned Items Must Not Be Open | PRE_CONSO | ReturnStatus NOT IN ('Returned', 'Refunded') OR FulfillmentStatus <> 'Pending' |
| SalesOrderItem | TotalPriceMustBeConsistentWithComponents | Total Price Must Be Consistent With Components | PRE_CONSO | (Quantity IS NULL OR Quantity >= 0) AND (UnitPrice IS NULL OR UnitPrice >= 0) AND (ListPrice IS NULL OR ListPrice >= 0) AND (DiscountAmount IS NULL OR DiscountAmount >= 0) AND (TaxAmount IS NULL OR TaxAmount >= 0) AND (TotalPrice IS NULL OR TotalPrice >= 0) AND (Quantity IS NULL OR UnitPrice IS NULL OR DiscountAmount IS NULL OR DiscountAmount <= (Quantity * UnitPrice)) |
| WebEngagement | EventTimestampShouldExistForTrackedEvents | Event Timestamp Should Exist For Tracked Events | PRE_CONSO | EventType IS NULL OR EventTimestamp IS NOT NULL |
| WebEngagement | PageUrlRequiredForPageAndProductViews | Page URL Required For Page And Product Views | PRE_CONSO | EventType NOT IN ('Page View', 'Product View') OR PageUrl IS NOT NULL |

## Validation Scope Summary

- POST_CONSO: 2 validation(s)
- PRE_CONSO: 29 validation(s)
