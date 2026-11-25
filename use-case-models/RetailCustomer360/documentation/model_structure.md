# Retail Customer 360 Model Structure

This document provides an overview of the entities, attributes, relationships, and matching usage in the Retail Customer 360 data model.

## Summary

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|---|---|---|---|---|---:|
| Account | Account | Represents a business account, organization, corporate customer, or retail partner account. | Account, AccountContact, AccountCustomerRelationship, Opportunity, PartyIdentification | Account, Currency | 31 |
| AccountContact | Account Contact | A person acting within a business account, with a defined role in that account. | Case | Account, Customer | 20 |
| AccountCustomerRelationship | Account Customer Relationship | Represents the relationship between a customer and an account, without embedding reference attributes. |  | Account, Customer | 19 |
| Brand | Brand | Commercial brand under which products are marketed. | LoyaltyProgram, Product |  | 16 |
| Campaign | Campaign | Marketing campaigns representing promotional activities and initiatives. | EmailEngagement, Lead, MobileAppEngagement, Promotion, SMSEngagement, WebEngagement | Currency | 29 |
| Case | Case | Customer service issue tracked from first contact through to resolution. |  | AccountContact, Customer, Product, SalesOrder | 24 |
| CommunicationSubscription | Communication Subscription | Named communication stream a customer has subscribed to or unsubscribed from. |  | CommunicationSubscriptionChannelType, Customer | 14 |
| CommunicationSubscriptionChannelType | Subscription Channel Type | Reference list of channels on which communication subscriptions can be offered. | CommunicationSubscription |  | 9 |
| Consent | Consent | Consent data for Customer 360. |  | Customer, DataUsePurpose | 17 |
| ConsentAction | Consent Action | Specific processing action a customer can consent to or refuse. | ContactPointConsent |  | 8 |
| ContactPointAddress | Contact Point Address | Stores customer address contact points for location-based matching and outreach. |  | Country, Customer | 18 |
| ContactPointApp | App Contact Point | Installed application instance through which a customer can receive push communication. |  | Customer, Device, SoftwareApplication | 19 |
| ContactPointConsent | Contact Point Consent | Consent preference recorded for a customer on one specific contact point and channel. |  | ConsentAction, Customer, DataUseLegalBasis, DataUsePurpose | 13 |
| ContactPointEmail | Contact Point Email | Stores customer email contact points with primary and verification indicators. |  | Customer | 14 |
| ContactPointPhone | Contact Point Phone | Stores customer phone contact points with primary, mobile, and verification indicators. |  | Customer | 16 |
| ContactPointSocial | Social Contact Point | Social media identity through which a customer can be reached or observed. |  | Customer | 16 |
| Country | Country | Reference data entity containing ISO country codes and metadata for address validation, localization, and location-based customer analysis. | ContactPointAddress, Currency, Customer, Lead, PartyIdentification, SalesStore |  | 12 |
| Currency | Currency | Reference data entity containing ISO currency metadata used by financial attributes across Customer 360 entities. | Account, Campaign, LoyaltyProgram, Opportunity, Product, Promotion, SalesOrder, SalesOrderItem, SalesStore | Country | 14 |
| Customer | Customer | Represents a uniquely identified  customer or person, including core identity, demographic, lifecycle, and audit information used for customer 360 matching and unification. | AccountContact, AccountCustomerRelationship, Case, CommunicationSubscription, Consent, ContactPointAddress, ContactPointApp, ContactPointConsent, ContactPointEmail, ContactPointPhone, ContactPointSocial, Device, EmailEngagement, Lead, LoyaltyProgramMember, MobileAppEngagement, Opportunity, PartyIdentification, SalesOrder, ShoppingCartEngagement, SMSEngagement, Voucher, WebEngagement, WebSearchEngagement | Country | 27 |
| DataUseLegalBasis | Data Use Legal Basis | Legal ground relied upon to process customer personal data in a given jurisdiction. | ContactPointConsent |  | 9 |
| DataUsePurpose | Data Use Purpose | Business purpose for which customer personal data may be processed. | Consent, ContactPointConsent |  | 9 |
| Device | Device | Electronic device from which a customer interacts with the brand. | ContactPointApp, WebEngagement | Customer | 14 |
| EmailEngagement | Email Engagement | Engagement with marketing or transactional emails. |  | Campaign, Customer | 15 |
| Lead | Lead | A person or company that has shown interest in the brand and is not yet a converted customer. |  | Campaign, Country, Customer | 25 |
| LoyaltyLedger | Loyalty Ledger | Individual movement of loyalty points into or out of a member's balance. |  | LoyaltyProgramMember, SalesOrder | 13 |
| LoyaltyProgram | Loyalty Program | Loyalty program definition and configuration. | LoyaltyProgramMember, LoyaltyTier | Brand, Currency | 20 |
| LoyaltyProgramMember | Loyalty Program Member | Represents a customer's membership in a loyalty program. | LoyaltyLedger | Customer, LoyaltyProgram, LoyaltyTier | 18 |
| LoyaltyTier | Loyalty Tier | Benefit level within a loyalty program that members qualify for and can be promoted through. | LoyaltyProgramMember | LoyaltyProgram | 13 |
| MobileAppEngagement | Mobile App Engagement | Customer activity in the mobile app. |  | Campaign, Customer, SoftwareApplication | 18 |
| Opportunity | Opportunity | In-progress sales deal tracked to a win or loss outcome. | OpportunityProduct | Account, Currency, Customer | 21 |
| OpportunityProduct | Opportunity Product | Product line quoted on a sales opportunity. |  | Opportunity, Product | 10 |
| OrderDeliveryMethod | Delivery Method | Way in which an order is delivered to or collected by the customer. | SalesOrder |  | 11 |
| PartyIdentification | Party Identification | Stores party identification documents with verification and status tracking. |  | Account, Country, Customer | 18 |
| Product | Product | Product master data with brand, category, and standard pricing. | Case, OpportunityProduct, SalesOrderItem | Brand, Currency, ProductCatalog, UnitOfMeasure | 22 |
| ProductCatalog | Product Catalog | Curated set of products offered to a market or channel for a period of time. | Product, ProductCatalogCategory |  | 11 |
| ProductCatalogCategory | Catalog Category | Merchandising grouping used to navigate a product catalog. | ProductCatalogCategory | ProductCatalog, ProductCatalogCategory | 9 |
| Promotion | Promotion | Time-bound marketing offer that changes price, points or delivery for qualifying customers. | Voucher | Campaign, Currency | 16 |
| SalesOrder | Sales Order | Sales order data for Customer 360. | Case, LoyaltyLedger, SalesOrderItem, ShoppingCartEngagement | Currency, Customer, OrderDeliveryMethod, SalesStore | 24 |
| SalesOrderItem | Sales Order Item | Sales order line item data for Customer 360. |  | Currency, Product, SalesOrder | 20 |
| SalesStore | Sales Store | Physical or virtual selling location where orders are placed and fulfilled. | SalesOrder | Country, Currency | 18 |
| ShoppingCartEngagement | Shopping Cart Engagement | Shopping cart session showing what a customer assembled and whether it converted. |  | Customer, SalesOrder | 15 |
| SMSEngagement | SMS Engagement | Interaction between a customer and an SMS message sent by the brand. |  | Campaign, Customer | 13 |
| SoftwareApplication | Software Application | Branded application through which customers engage, such as a mobile or web app. | ContactPointApp, MobileAppEngagement |  | 11 |
| UnitOfMeasure | Unit Of Measure | Standard unit in which product quantities are expressed and converted. | Product |  | 9 |
| Voucher | Voucher | Individually issued instrument a customer can redeem for a discount or benefit. |  | Customer, Promotion | 16 |
| WebEngagement | Web Engagement | Customer activity and interactions on the website. |  | Campaign, Customer, Device | 20 |
| WebSearchEngagement | Web Search Engagement | Search a customer performed before or while browsing the brand's site. |  | Customer | 13 |

# Detailed Model Structure

## Account (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AccountId | Account Id | LongInteger | Yes | Primary identifier | No |
| AccountNumber | Account Number | String | No | Business account number | Yes |
| AccountName | Account Name | String | No | Account name | Yes |
| AccountType | Account Type | RetailCustomer360.list_of_values.AccountType | No | Corporate, Retailer, Distributor, Supplier, Partner | No |
| Industry | Industry | RetailCustomer360.list_of_values.Industry | No | Industry classification | No |
| AccountStatus | Account Status | RetailCustomer360.list_of_values.AccountStatus | No | Active, Inactive, Prospect, Closed | No |
| Revenue | Revenue | Decimal | No | Annual or reported revenue | No |
| EmployeeCount | Employee Count | Integer | No | Number of employees | No |
| Location | Location | String | No | Primary account location | Yes |
| WebsiteUrl | Website Url | String | No | Company website | No |
| TaxRegistrationNumber | Tax Registration Number | String | No | Tax or business registration number | Yes |
| LegalEntityName | Legal Entity Name | String | No | Registered legal entity name | No |
| ExternalAccountId | External Account Id | String | No | External account identifier from partner or ERP systems | No |
| DUNSNumber | DUNS Number | String | No | Global Dun & Bradstreet identifier | No |
| RegistrationCountryCode | Registration Country Code | RetailCustomer360.list_of_values.Country | No | Country where the legal entity is registered | No |
| AccountSinceDate | Account Since Date | Date | No | Relationship start date | No |
| PreferredContactChannel | Preferred Contact Channel | RetailCustomer360.list_of_values.PreferredChannel | No | Preferred communication channel | No |
| CreditLimit | Credit Limit | Decimal | No | Approved credit limit | No |
| PaymentTermDays | Payment Term (Days) | Integer | No | Standard payment term in days | No |
| RiskScore | Risk Score | Decimal | No | Risk score from 0 to 100 | No |
| IsStrategicAccount | Is Strategic Account | Boolean | No | Indicates whether this account is strategically important | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| SourceAccountKey | Source Account Key | String | No | Source account identifier | No |
| AccountNameNormalized | Account Name (Normalized) | String | No | Uppercase normalized account name used for search and matching | No |
| RevenueBand | Revenue Band | String | No | Derived revenue bucket | No |
| AccountAgeYears | Account Age (Years) | Integer | No | Years since AccountSinceDate | No |
| AccountAgeSegment | Account Age Segment | String | No | Derived age segment for account relationship | No |
| EmployeeSizeBand | Employee Size Band | String | No | Derived employee-size segment | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## AccountContact (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AccountContactId | Account Contact Id | LongInteger | Yes | Primary identifier of the account contact. | No |
| FirstName | First Name | String | No | Given name of the contact. | No |
| LastName | Last Name | String | No | Family name of the contact. | No |
| JobTitle | Job Title | String | No | Professional title held by the contact. | No |
| Department | Department | String | No | Department the contact belongs to within the account. | No |
| ContactRole | Contact Role | RetailCustomer360.list_of_values.ContactRole | No | Role the contact plays in decisions for the account. | Yes |
| EmailAddress | Email Address | String | No | Business email address of the contact. | Yes |
| PhoneNumber | Phone Number | String | No | Business phone number of the contact. | No |
| IsPrimaryContact | Is Primary Contact | Boolean | No | Whether this contact is the main point of contact for the account. | No |
| PreferredChannel | Preferred Channel | RetailCustomer360.list_of_values.PreferredChannel | No | Channel the contact prefers to be reached on. | No |
| StartDate | Start Date | Date | No | Date the contact became active on the account. | No |
| EndDate | End Date | Date | No | Date the contact ceased to be active on the account. | No |
| Status | Status | RetailCustomer360.list_of_values.AccountStatus | No | Lifecycle status of the account contact. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the contact record originates from. | No |
| SourceContactKey | Source Contact Key | String | No | Natural key of the contact in the source system. | No |
| FullName | Full Name | String | No | Derived full name of the contact. | No |
| FullNameNormalized | Full Name Normalized | String | No | Uppercased and trimmed full name used for matching. | Yes |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## AccountCustomerRelationship (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AccountCustomerRelationshipId | Account Customer Relationship Id | LongInteger | Yes | Primary identifier | No |
| RelationshipType | Relationship Type | RetailCustomer360.list_of_values.RelationshipType | No | Employee, Owner, Buyer, Decision Maker, Household Member | No |
| RelationshipRole | Relationship Role | RetailCustomer360.list_of_values.RelationshipRole | No | Primary Contact, Billing Contact, Authorized Buyer | No |
| RelationshipStatus | Relationship Status | RetailCustomer360.list_of_values.RelationshipStatus | No | Active, Inactive, Ended | No |
| StartDate | Start Date | Date | No | Relationship start date | No |
| EndDate | End Date | Date | No | Relationship end date | No |
| OwnershipPercentage | Ownership Percentage | Decimal | No | Optional ownership percentage | No |
| IsPrimaryRelationship | Is Primary Relationship | Boolean | No | Indicates primary account relationship | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| SourceRelationshipKey | Source Relationship Key | String | No | Source relationship identifier | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |
| RelationshipStrength | Relationship Strength | Decimal | No | Derived score describing how strong the account-customer link is. | No |
| AuthorityLevel | Authority Level | String | No | Level of authority the customer holds on the account. | No |
| IsBillingContact | Is Billing Contact | Boolean | No | Whether the customer receives billing for the account. | No |
| IsDecisionMaker | Is Decision Maker | Boolean | No | Whether the customer can commit the account to a purchase. | No |
| LastInteractionDate | Last Interaction Date | Timestamp | No | Date and time of the most recent interaction on this relationship. | No |
| RelationshipDurationDays | Relationship Duration Days | LongInteger | No | Derived number of days the relationship has been active. | No |

## Brand (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| BrandId | Brand Id | LongInteger | Yes | Primary identifier of the brand. | No |
| BrandCode | Brand Code | String | No | Short code identifying the brand. | No |
| BrandName | Brand Name | String | No | Commercial name of the brand. | No |
| BrandOwner | Brand Owner | String | No | Legal entity that owns the brand. | No |
| CountryOfOrigin | Country Of Origin | String | No | Country the brand originates from. | No |
| WebsiteUrl | Website Url | String | No | Public website of the brand. | No |
| LogoUrl | Logo Url | String | No | Location of the brand logo image. | No |
| LaunchYear | Launch Year | LongInteger | No | Year the brand was launched. | No |
| IsActive | Is Active | Boolean | No | Whether the brand is currently sold. | No |
| IsPrivateLabel | Is Private Label | Boolean | No | Whether the brand is a retailer own-label. | No |
| Description | Description | String | No | Positioning statement for the brand. | No |
| BrandNameNormalized | Brand Name Normalized | String | No | Uppercased and trimmed brand name used for lookups. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the brand record originates from. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## Campaign (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CampaignId | Campaign Id | LongInteger | Yes | Primary identifier | No |
| CampaignCode | Campaign Code | String | No | Business campaign code | No |
| CampaignName | Campaign Name | String | No | Campaign name | No |
| CampaignType | Campaign Type | RetailCustomer360.list_of_values.CampaignType | No | Acquisition, Retention, Winback, Loyalty, Cross-sell | No |
| Channel | Channel | RetailCustomer360.list_of_values.CampaignChannel | No | Email, SMS, Push, Web, Social, Store | No |
| StartDate | Start Date | Date | No | Campaign start date | No |
| EndDate | End Date | Date | No | Campaign end date | No |
| Status | Status | RetailCustomer360.list_of_values.CampaignStatus | No | Planned, Active, Paused, Completed, Cancelled | No |
| Objective | Objective | RetailCustomer360.list_of_values.CampaignObjective | No | Awareness, Conversion, Retention, Reactivation | No |
| TargetSegment | Target Segment | RetailCustomer360.list_of_values.TargetSegment | No | Target customer segment | No |
| Budget | Budget | Decimal | No | Campaign budget | No |
| ActualSpend | Actual Spend | Decimal | No | Actual campaign spend | No |
| PlannedAudienceSize | Planned Audience Size | Integer | No | Expected audience size targeted by the campaign | No |
| ActualReach | Actual Reach | Integer | No | Number of unique customers reached | No |
| Impressions | Impressions | LongInteger | No | Total campaign impressions | No |
| Clicks | Clicks | LongInteger | No | Total number of clicks generated | No |
| Conversions | Conversions | LongInteger | No | Total number of conversions generated | No |
| AttributedRevenue | Attributed Revenue | Decimal | No | Revenue attributed to this campaign | No |
| OwnerName | Owner Name | String | No | Campaign owner or manager | No |
| Notes | Notes | String | No | Additional campaign notes | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| SourceCampaignKey | Source Campaign Key | String | No | Source campaign identifier | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |
| EnrichmentPerformanceScore | Enrichment Performance Score | Decimal | No | Derived 0-100 score based on campaign performance indicators | No |
| EnrichmentPacingStatus | Enrichment Pacing Status | String | No | Derived pacing status based on spend progression and schedule | No |
| EnrichmentROIBand | Enrichment ROI Band | String | No | Derived ROI classification based on attributed revenue versus spend | No |
| EnrichmentHealthStatus | Enrichment Health Status | String | No | Derived campaign health indicator | No |

## Case (ID_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CaseNumber | Case Number | String | Yes | Universal identifier of the case across systems. | No |
| Subject | Subject | String | No | Short statement of what the case is about. | No |
| CaseType | Case Type | RetailCustomer360.list_of_values.CaseType | No | Nature of the issue raised. | No |
| CaseStatus | Case Status | RetailCustomer360.list_of_values.CaseStatus | No | Lifecycle status of the case. | No |
| CasePriority | Case Priority | RetailCustomer360.list_of_values.CasePriority | No | Urgency assigned to the case. | No |
| CaseOrigin | Case Origin | RetailCustomer360.list_of_values.CaseOrigin | No | Channel the case was raised through. | No |
| Description | Description | String | No | Detailed account of the customer's issue. | No |
| OpenedDate | Opened Date | Timestamp | No | Date and time the case was opened. | No |
| FirstResponseDate | First Response Date | Timestamp | No | Date and time the first agent response was sent. | No |
| DueDate | Due Date | Timestamp | No | Date and time the case must be resolved by. | No |
| ClosedDate | Closed Date | Timestamp | No | Date and time the case was closed. | No |
| Resolution | Resolution | String | No | Explanation of how the case was resolved. | No |
| SatisfactionScore | Satisfaction Score | Decimal | No | Score the customer gave for handling of the case. | No |
| EscalationCount | Escalation Count | LongInteger | No | Number of times the case was escalated. | No |
| OwnerName | Owner Name | String | No | Agent accountable for resolving the case. | No |
| IsEscalated | Is Escalated | Boolean | No | Whether the case is currently escalated. | No |
| IsClosed | Is Closed | Boolean | No | Whether the case has been closed. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the case originates from. | No |
| SourceCaseKey | Source Case Key | String | No | Natural key of the case in the source system. | No |
| ResolutionHours | Resolution Hours | Decimal | No | Derived number of hours between opening and closing. | No |
| CaseAgeDays | Case Age Days | LongInteger | No | Derived number of days the case has been open. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## CommunicationSubscription (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SubscriptionId | Subscription Id | LongInteger | Yes | Primary identifier of the subscription. | No |
| SubscriptionName | Subscription Name | String | No | Business name of the communication stream. | No |
| SubscriptionStatus | Subscription Status | RetailCustomer360.list_of_values.SubscriptionStatus | No | Current state of the subscription. | No |
| EngagementChannelType | Engagement Channel | RetailCustomer360.list_of_values.EngagementChannelType | No | Channel the subscription is delivered on. | No |
| Frequency | Frequency | String | No | How often the customer chose to receive the communication. | No |
| SubscribedDate | Subscribed Date | Timestamp | No | Date and time the customer subscribed. | No |
| UnsubscribedDate | Unsubscribed Date | Timestamp | No | Date and time the customer unsubscribed. | No |
| UnsubscribeReason | Unsubscribe Reason | String | No | Reason captured when the customer unsubscribed. | No |
| PreferredSendTime | Preferred Send Time | String | No | Time of day the customer prefers to receive the communication. | No |
| IsTransactional | Is Transactional | Boolean | No | Whether the stream is transactional and therefore exempt from marketing opt-out. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the subscription originates from. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## CommunicationSubscriptionChannelType (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ChannelTypeId | Channel Type Id | LongInteger | Yes | Primary identifier of the channel type. | No |
| ChannelCode | Channel Code | String | No | Short code identifying the channel type. | No |
| ChannelName | Channel Name | String | No | Business name of the channel type. | No |
| EngagementChannelType | Engagement Channel | RetailCustomer360.list_of_values.EngagementChannelType | No | Underlying engagement channel this type maps to. | No |
| Description | Description | String | No | Explanation of what the channel type covers. | No |
| IsActive | Is Active | Boolean | No | Whether the channel type is currently offered. | No |
| RequiresDoubleOptIn | Requires Double Opt In | Boolean | No | Whether subscriptions on this channel need confirmed opt-in. | No |
| DefaultFrequency | Default Frequency | String | No | Frequency applied when the customer expresses no preference. | No |
| DisplayOrder | Display Order | LongInteger | No | Position of the channel type in preference centre listings. | No |

## Consent (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ConsentId | Consent Id | LongInteger | Yes | Primary identifier | No |
| ConsentType | Consent Type | RetailCustomer360.list_of_values.ConsentType | No | Marketing, Profiling, Personalization, Data Sharing, Cookies | No |
| ConsentChannel | Consent Channel | RetailCustomer360.list_of_values.ConsentChannel | No | Email, SMS, Phone, Push, Web, Store | No |
| ConsentStatus | Consent Status | RetailCustomer360.list_of_values.ConsentStatus | No | Opted In, Opted Out, Withdrawn, Pending, Unknown | No |
| ConsentSource | Consent Source | RetailCustomer360.list_of_values.ConsentSource | No | Website, Mobile App, POS, Call Center, CRM | No |
| ConsentCaptureMethod | Consent Capture Method | RetailCustomer360.list_of_values.ConsentCaptureMethod | No | Checkbox, Form, Verbal, Imported, Preference Center | No |
| ConsentVersion | Consent Version | String | No | Consent policy/version accepted | No |
| EffectiveDate | Effective Date | Timestamp | No | Consent effective date/time | No |
| ExpiryDate | Expiry Date | Timestamp | No | Consent expiry date/time | No |
| WithdrawalDate | Withdrawal Date | Timestamp | No | Date/time consent was withdrawn | No |
| LegalBasis | Legal Basis | RetailCustomer360.list_of_values.LegalBasis | No | Consent, Contract, Legitimate Interest, Legal Obligation | No |
| Jurisdiction | Jurisdiction | RetailCustomer360.list_of_values.Jurisdiction | No | GDPR, CCPA, DPDP, Other | No |
| ProofText | Proof Text | String | No | Consent evidence text or statement | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## ConsentAction (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ConsentActionId | Consent Action Id | LongInteger | Yes | Primary identifier of the consent action. | No |
| ActionCode | Action Code | String | No | Short code identifying the action. | No |
| ActionName | Action Name | String | No | Business name of the action. | No |
| ActionType | Action Type | RetailCustomer360.list_of_values.ConsentActionType | No | Category of processing the action represents. | No |
| Description | Description | String | No | Explanation of what the action permits or restricts. | No |
| IsActive | Is Active | Boolean | No | Whether the action is currently offered. | No |
| IsRestrictive | Is Restrictive | Boolean | No | Whether refusing the action blocks downstream processing. | No |
| DisplayOrder | Display Order | LongInteger | No | Position of the action in preference centre listings. | No |

## ContactPointAddress (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AddressId | Address Id | LongInteger | Yes | Primary identifier for the address contact point record. | No |
| AddressLine1 | Address Line 1 | String | No | Street address line 1. | Yes |
| AddressLine2 | Address Line 2 | String | No | Street address line 2. | No |
| AddressLine3 | Address Line 3 | String | No | Optional additional address line. | No |
| City | City | String | No | City. | Yes |
| StateProvince | State Province | String | No | State or province. | Yes |
| PostalCode | Postal Code | String | No | ZIP/postal code. | Yes |
| AddressType | Address Type | RetailCustomer360.list_of_values.AddressType | No | Address type classification (Home, Work, Billing, Shipping, Store Pickup). | No |
| IsPrimary | Is Primary | Boolean | No | Indicates primary address. | No |
| IsVerified | Is Verified | Boolean | No | Indicates standardized/verified address. | No |
| VerificationDate | Verification Date | Timestamp | No | Date/time address was verified. | No |
| Latitude | Latitude | Decimal | No | Optional geocoded latitude. | No |
| Longitude | Longitude | Decimal | No | Optional geocoded longitude. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system. | No |
| SourceAddressKey | Source Address Key | String | No | Source address identifier. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## ContactPointApp (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AppContactId | App Contact Id | LongInteger | Yes | Primary identifier of the app contact point. | No |
| AppInstallId | App Install Id | String | No | Unique identifier of the application installation. | Yes |
| PushToken | Push Token | String | No | Token used to deliver push notifications to the installation. | Yes |
| PushOptInStatus | Push Opt In Status | RetailCustomer360.list_of_values.PushOptInStatus | No | Whether the customer accepted push notifications. | No |
| AppPlatform | App Platform | RetailCustomer360.list_of_values.AppPlatform | No | Platform the application instance runs on. | Yes |
| AppVersion | App Version | String | No | Version of the application installed. | No |
| InstallDate | Install Date | Timestamp | No | Date and time the application was installed. | No |
| LastOpenDate | Last Open Date | Timestamp | No | Date and time the application was last opened. | No |
| NotificationEnabled | Notification Enabled | Boolean | No | Whether notifications are enabled at operating-system level. | No |
| IsPrimary | Is Primary | Boolean | No | Whether this is the customer's main application installation. | No |
| Locale | Locale | String | No | Locale configured in the application. | No |
| TimeZone | Time Zone | String | No | Time zone reported by the installation. | No |
| Status | Status | RetailCustomer360.list_of_values.AccountStatus | No | Lifecycle status of the app contact point. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the app contact point originates from. | No |
| SourceAppKey | Source App Key | String | No | Natural key of the record in the source system. | No |
| DaysSinceLastOpen | Days Since Last Open | LongInteger | No | Derived number of days since the application was last opened. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## ContactPointConsent (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CPConsentId | Contact Point Consent Id | LongInteger | Yes | Primary identifier of the contact point consent. | No |
| EngagementChannelType | Engagement Channel | RetailCustomer360.list_of_values.EngagementChannelType | No | Channel the preference applies to. | No |
| ConsentStatus | Consent Status | RetailCustomer360.list_of_values.ConsentStatus | No | Whether the customer opted in or out for this contact point. | No |
| EffectiveDate | Effective Date | Timestamp | No | Date and time the preference took effect. | No |
| ExpiryDate | Expiry Date | Timestamp | No | Date and time the preference expires. | No |
| CaptureMethod | Capture Method | RetailCustomer360.list_of_values.ConsentCaptureMethod | No | How the preference was captured from the customer. | No |
| DoubleOptInConfirmed | Double Opt In Confirmed | Boolean | No | Whether the customer confirmed the opt-in a second time. | No |
| OptOutReason | Opt Out Reason | String | No | Reason the customer gave for opting out. | No |
| Jurisdiction | Jurisdiction | RetailCustomer360.list_of_values.Jurisdiction | No | Privacy regime governing the preference. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the preference originates from. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## ContactPointEmail (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| EmailId | Email Id | LongInteger | Yes | Primary identifier for the email contact point record. | No |
| EmailAddress | Email Address | String | No | Email address. | Yes |
| EmailType | Email Type | RetailCustomer360.list_of_values.EmailType | No | Email type classification (Personal, Work, Billing, Shipping, Other). | No |
| IsPrimary | Is Primary | Boolean | No | Indicates primary email. | No |
| IsVerified | Is Verified | Boolean | No | Indicates verified email address. | No |
| VerificationDate | Verification Date | Timestamp | No | Date/time email was verified. | No |
| ConsentStatus | Consent Status | RetailCustomer360.list_of_values.ConsentStatus | No | Consent status (Opted In, Opted Out, Pending, Unknown). | No |
| EmailDeliverabilityStatus | Email Deliverability Status | RetailCustomer360.list_of_values.EmailDeliverabilityStatus | No | Email deliverability status (Deliverable, Bounced, Invalid, Suppressed). | No |
| BounceReason | Bounce Reason | String | No | Reason for bounce, if applicable. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system. | No |
| SourceEmailKey | Source Email Key | String | No | Source email identifier. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## ContactPointPhone (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PhoneId | Phone Id | LongInteger | Yes | Primary identifier for the phone contact point record. | No |
| PhoneNumber | Phone Number | String | No | Full phone number. | Yes |
| CountryCode | Country Code | String | No | International dialing code. | No |
| NationalNumber | National Number | String | No | Local/national number. | No |
| ExtensionNumber | Extension Number | String | No | Extension, if applicable. | No |
| PhoneType | Phone Type | RetailCustomer360.list_of_values.PhoneType | No | Phone type classification (Mobile, Home, Work, Landline, Other). | No |
| IsPrimary | Is Primary | Boolean | No | Indicates primary phone. | No |
| IsVerified | Is Verified | Boolean | No | Indicates verified phone. | No |
| VerificationDate | Verification Date | Timestamp | No | Date/time phone was verified. | No |
| ConsentStatus | Consent Status | RetailCustomer360.list_of_values.ConsentStatus | No | Consent status (Opted In, Opted Out, Pending, Unknown). | No |
| DoNotCallFlag | Do Not Call Flag | Boolean | No | Indicates do-not-call preference. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system. | No |
| SourcePhoneKey | Source Phone Key | String | No | Source phone identifier. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## ContactPointSocial (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SocialId | Social Id | LongInteger | Yes | Primary identifier of the social contact point. | No |
| SocialNetwork | Social Network | RetailCustomer360.list_of_values.SocialNetwork | No | Platform the social identity belongs to. | Yes |
| SocialHandle | Social Handle | String | No | Public handle or username on the platform. | No |
| ProfileUrl | Profile Url | String | No | Direct link to the public profile. | Yes |
| FollowerCount | Follower Count | LongInteger | No | Number of followers the profile has. | No |
| EngagementScore | Engagement Score | Decimal | No | Derived measure of how actively the profile engages with the brand. | No |
| IsVerified | Is Verified | Boolean | No | Whether the platform has verified the profile. | No |
| IsPrimary | Is Primary | Boolean | No | Whether this is the customer's main social identity. | No |
| LastActivityDate | Last Activity Date | Timestamp | No | Date and time of the most recent observed activity. | No |
| Status | Status | RetailCustomer360.list_of_values.AccountStatus | No | Lifecycle status of the social contact point. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the social contact point originates from. | No |
| SourceSocialKey | Source Social Key | String | No | Natural key of the record in the source system. | No |
| HandleNormalized | Handle Normalized | String | No | Lowercased handle without leading punctuation, used for matching. | Yes |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## Country (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CountryCode | ISO Alpha 2 Code | String | Yes | ISO 3166-1 alpha-2 country code (e.g., US, GB) | No |
| Alpha3Code | ISO 3166-1 3-Letter Code | String | No | ISO 3166-1 alpha-3 country code (e.g., USA, GBR) | No |
| NumericCode | Numeric Code | String | No | ISO numeric country code | No |
| URLWikipedia | URL Wikipedia | String | No | Link to the country's Wikipedia page for reference | No |
| LocalShortName | Local Short Name | String | No | Short name of the country in the local language | No |
| EnglishShortName | English Short Name | String | No | Short name of the country in English | No |
| EnglishShortNameCAPS | English Short Name ALLCAPS | String | No | Uppercase English short name (for legacy or matching needs) | No |
| EnglishFullName | English Full Name | String | No | Full official country name in English | No |
| FlagURL | Flag URL | String | No | URL pointing to an image of the country's flag | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## Currency (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CurrencyCode | Currency Code | String | Yes | ISO 4217 currency code (e.g., USD, EUR, INR) | No |
| CurrencyName | Currency Name | String | No | Official currency name | No |
| CurrencySymbol | Currency Symbol | String | No | Common symbol used to represent the currency | No |
| MinorUnit | Minor Unit | Integer | No | Number of decimal digits for the currency minor unit | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |
| NumericCode | Numeric Code | String | No | ISO 4217 numeric code of the currency. | No |
| SymbolPosition | Symbol Position | String | No | Whether the symbol is shown before or after the amount. | No |
| DecimalPlaces | Decimal Places | LongInteger | No | Number of decimal places amounts are expressed with. | No |
| ExchangeRateToBase | Exchange Rate To Base | Decimal | No | Rate converting this currency into the reporting base currency. | No |
| ExchangeRateDate | Exchange Rate Date | Date | No | Date the exchange rate was captured. | No |
| IsBaseCurrency | Is Base Currency | Boolean | No | Whether this is the group reporting currency. | No |
| IsActive | Is Active | Boolean | No | Whether the currency is currently accepted. | No |

## Customer (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CustomerId | Customer Id | LongInteger | No | Enterprise customer identifier | No |
| FirstName | First Name | String | No | Customer first name | No |
| LastName | Last Name | String | No | Customer last name | No |
| MiddleName | Middle Name | String | No | Customer middle name | No |
| BirthDate | Birth Date | Date | No | Date of birth | Yes |
| Gender | Gender | RetailCustomer360.list_of_values.Gender | No | Gender identity | No |
| CustomerSegment | Customer Segment | RetailCustomer360.list_of_values.CustomerSegment | No | Segmentation category | No |
| Status | Status | RetailCustomer360.list_of_values.Status | No | Active, Prospect, Inactive, etc. | No |
| PreferredLanguage | Preferred Language | String | No | ISO language code | No |
| Occupation | Occupation | String | No | Occupation | No |
| AnnualIncome | Annual Income | Decimal | No | Estimated annual income | No |
| CustomerSinceDate | Customer Since Date | Date | No | First known interaction date | No |
| PreferredChannel | Preferred Channel | RetailCustomer360.list_of_values.PreferredChannel | No | Preferred engagement channel | No |
| CreatedDate | Created Date | Timestamp | No | Timestamp when the customer record was created. | No |
| SourceCustomerKey | Source Customer Key | String | No | Unique key from the source system | Yes |
| FullName | Full Name | String | No | Computed full display name (First + Middle + Last) | No |
| FullNameNormalized | Full Name (Normalized) | String | No | Uppercase, trimmed full name used for matching and search | Yes |
| Initials | Initials | String | No | Customer initials derived from first and last name | No |
| Age | Age | Integer | No | Computed age in years from BirthDate | No |
| AgeGroup | Age Group | String | No | Computed age bracket (e.g. 18-24, 25-34, 35-44...) | No |
| TenureYears | Tenure (Years) | Integer | No | Years since CustomerSinceDate | No |
| TenureSegment | Tenure Segment | String | No | Tenure bracket (New, Established, Loyal, Veteran) | No |
| CustomerType | Customer Type | String | No | Derived business classification for the party record | No |
| CustomerValueBand | Customer Value | String | No | Derived customer value band based on segment, income, and tenure | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## DataUseLegalBasis (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LegalBasisId | Legal Basis Id | LongInteger | Yes | Primary identifier of the legal basis. | No |
| LegalBasisCode | Legal Basis Code | String | No | Short code identifying the legal basis. | No |
| LegalBasisName | Legal Basis Name | String | No | Business name of the legal basis. | No |
| LegalBasisType | Legal Basis Type | RetailCustomer360.list_of_values.LegalBasis | No | Category of legal ground being relied upon. | No |
| Jurisdiction | Jurisdiction | RetailCustomer360.list_of_values.Jurisdiction | No | Privacy regime the legal basis applies under. | No |
| Description | Description | String | No | Explanation of when the legal basis may be relied upon. | No |
| IsActive | Is Active | Boolean | No | Whether the legal basis is currently in use. | No |
| EffectiveDate | Effective Date | Date | No | Date the legal basis became applicable. | No |
| ExpiryDate | Expiry Date | Date | No | Date the legal basis ceased to be applicable. | No |

## DataUsePurpose (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PurposeId | Purpose Id | LongInteger | Yes | Primary identifier of the data use purpose. | No |
| PurposeCode | Purpose Code | String | No | Short code identifying the purpose. | No |
| PurposeName | Purpose Name | String | No | Business name of the purpose. | No |
| PurposeType | Purpose Type | RetailCustomer360.list_of_values.DataUsePurposeType | No | Category the purpose belongs to. | No |
| Description | Description | String | No | Explanation of how data is used for this purpose. | No |
| IsActive | Is Active | Boolean | No | Whether the purpose is currently in use. | No |
| RetentionMonths | Retention Months | LongInteger | No | Number of months data may be retained for this purpose. | No |
| RequiresExplicitConsent | Requires Explicit Consent | Boolean | No | Whether the purpose needs affirmative customer consent. | No |
| DisplayOrder | Display Order | LongInteger | No | Position of the purpose in preference centre listings. | No |

## Device (ID_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| DeviceIdentifier | Device Identifier | String | Yes | Universal identifier of the device across systems. | No |
| DeviceType | Device Type | RetailCustomer360.list_of_values.DeviceType | No | Category of hardware the device belongs to. | No |
| OperatingSystem | Operating System | RetailCustomer360.list_of_values.OperatingSystem | No | Operating system running on the device. | No |
| OsVersion | Os Version | String | No | Version of the operating system. | No |
| Manufacturer | Manufacturer | String | No | Company that manufactured the device. | No |
| DeviceModel | Device Model | String | No | Commercial model name of the device. | No |
| WebBrowser | Web Browser | RetailCustomer360.list_of_values.WebBrowser | No | Browser most often used on the device. | No |
| ScreenResolution | Screen Resolution | String | No | Screen resolution reported by the device. | No |
| Locale | Locale | String | No | Locale configured on the device. | No |
| TimeZone | Time Zone | String | No | Time zone reported by the device. | No |
| FirstSeenDate | First Seen Date | Timestamp | No | Date and time the device was first observed. | No |
| LastSeenDate | Last Seen Date | Timestamp | No | Date and time the device was last observed. | No |
| IsActive | Is Active | Boolean | No | Whether the device is still in active use. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the device record originates from. | No |

## EmailEngagement (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| EmailEventId | Email Event Id | LongInteger | Yes | Primary identifier | No |
| EmailMessageId | Email Message Id | String | No | Email platform message identifier | No |
| EmailAddress | Email Address | String | No | Email address engaged | No |
| EventType | Event Type | RetailCustomer360.list_of_values.EmailEventType | No | Sent, Delivered, Opened, Clicked, Bounced, Unsubscribed | No |
| EventTimestamp | Event Timestamp | Timestamp | No | Event date/time | No |
| SubjectLine | Subject Line | String | No | Email subject | No |
| LinkUrl | Link URL | String | No | Clicked URL, if applicable | No |
| DeviceType | Device Type | RetailCustomer360.list_of_values.DeviceType | No | Desktop, Mobile, Tablet | No |
| EmailClient | Email Client | RetailCustomer360.list_of_values.EmailClient | No | Gmail, Outlook, Apple Mail, Yahoo, Other | No |
| BounceType | Bounce Type | RetailCustomer360.list_of_values.BounceType | No | Hard Bounce, Soft Bounce, Technical Bounce | No |
| BounceReason | Bounce Reason | String | No | Bounce reason | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## Lead (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LeadId | Lead Id | LongInteger | Yes | Primary identifier of the lead. | No |
| FirstName | First Name | String | No | Given name of the lead. | No |
| LastName | Last Name | String | No | Family name of the lead. | No |
| CompanyName | Company Name | String | No | Company the lead represents, when the lead is a business prospect. | Yes |
| EmailAddress | Email Address | String | No | Email address captured for the lead. | Yes |
| PhoneNumber | Phone Number | String | No | Phone number captured for the lead. | Yes |
| JobTitle | Job Title | String | No | Professional title declared by the lead. | No |
| LeadStatus | Lead Status | RetailCustomer360.list_of_values.LeadStatus | No | Progress of the lead through qualification. | No |
| LeadSource | Lead Source | RetailCustomer360.list_of_values.LeadSource | No | Origin that generated the lead. | No |
| LeadRating | Lead Rating | RetailCustomer360.list_of_values.LeadRating | No | Qualitative interest level assigned to the lead. | No |
| Industry | Industry | RetailCustomer360.list_of_values.Industry | No | Industry the lead operates in. | No |
| EstimatedValue | Estimated Value | Decimal | No | Estimated revenue opportunity represented by the lead. | No |
| LeadScore | Lead Score | Decimal | No | Behavioural score used to prioritise follow-up. | No |
| CapturedDate | Captured Date | Timestamp | No | Date and time the lead was first captured. | No |
| ConvertedDate | Converted Date | Timestamp | No | Date and time the lead was converted into a customer. | No |
| CampaignCode | Campaign Code | String | No | Code of the campaign that generated the lead. | No |
| ConsentGiven | Consent Given | Boolean | No | Whether the lead agreed to be contacted. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the lead record originates from. | No |
| SourceLeadKey | Source Lead Key | String | No | Natural key of the lead in the source system. | No |
| FullName | Full Name | String | No | Derived full name of the lead. | No |
| FullNameNormalized | Full Name Normalized | String | No | Uppercased and trimmed full name used for matching. | Yes |
| LeadAgeDays | Lead Age Days | LongInteger | No | Derived number of days since the lead was captured. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## LoyaltyLedger (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LedgerEntryId | Ledger Entry Id | LongInteger | Yes | Primary identifier of the ledger entry. | No |
| TransactionDate | Transaction Date | Timestamp | No | Date and time the points movement occurred. | No |
| TransactionType | Transaction Type | RetailCustomer360.list_of_values.LedgerTransactionType | No | Nature of the points movement. | No |
| PointsType | Points Type | RetailCustomer360.list_of_values.PointsType | No | Classification of the points involved. | No |
| Points | Points | LongInteger | No | Number of points added or removed. | No |
| PointsBalanceAfter | Points Balance After | LongInteger | No | Member balance immediately after the movement. | No |
| MonetaryValue | Monetary Value | Decimal | No | Cash value attributed to the points movement. | No |
| ExpirationDate | Expiration Date | Date | No | Date the accrued points expire. | No |
| ReferenceNumber | Reference Number | String | No | Order or transaction the movement relates to. | No |
| Description | Description | String | No | Explanation of why the movement occurred. | No |
| IsReversed | Is Reversed | Boolean | No | Whether the movement has been reversed. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the ledger entry originates from. | No |
| SourceLedgerKey | Source Ledger Key | String | No | Natural key of the entry in the source system. | No |

## LoyaltyProgram (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LoyaltyProgramId | Loyalty Program Id | LongInteger | Yes | Primary identifier | No |
| ProgramCode | Program Code | String | No | Business program code | No |
| ProgramName | Program Name | String | No | Loyalty program name | No |
| ProgramType | Program Type | RetailCustomer360.list_of_values.ProgramType | No | Points, Tiered, Cashback, Subscription, Hybrid | No |
| Status | Status | RetailCustomer360.list_of_values.ProgramStatus | No | Active, Inactive, Retired | No |
| StartDate | Start Date | Date | No | Program start date | No |
| EndDate | End Date | Date | No | Program end date | No |
| PointsExpiryMonths | Points Expiry Months | Integer | No | Months before points expire | No |
| Description | Description | String | No | Program description | No |
| ProgramOwner | Program Owner | String | No | Business owner accountable for program performance | No |
| EnrollmentFee | Enrollment Fee | Decimal | No | Optional one-time enrollment fee | No |
| PointAccrualRate | Point Accrual Rate | Decimal | No | Points earned per base currency unit | No |
| PointRedemptionRate | Point Redemption Rate | Decimal | No | Currency value per point redeemed | No |
| MinimumRedeemPoints | Minimum Redeem Points | Integer | No | Minimum points required for redemption | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| ProgramHealthStatus | Program Health Status | String | No | Derived lifecycle health status (Healthy, Scheduled, Expired, Inactive, Unknown) | No |
| ProgramWindowStatus | Program Window Status | String | No | Derived scheduling window status (Scheduled, Ongoing, Expired, Open) | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## LoyaltyProgramMember (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LoyaltyMemberId | Loyalty Member Id | LongInteger | Yes | Primary identifier | No |
| LoyaltyMemberNumber | Loyalty Member Number | String | No | Membership number | No |
| MembershipStatus | Membership Status | RetailCustomer360.list_of_values.MembershipStatus | No | Active, Inactive, Suspended, Closed | No |
| Tier | Tier | RetailCustomer360.list_of_values.Tier | No | Bronze, Silver, Gold, Platinum, Diamond | No |
| JoinDate | Join Date | Date | No | Membership join date | No |
| EnrollmentChannel | Enrollment Channel | RetailCustomer360.list_of_values.EnrollmentChannel | No | Store, Web, Mobile App, Call Center | No |
| AvailablePointsBalance | Available Points Balance | Decimal | No | Available points | No |
| LifetimePointsEarned | Lifetime Points Earned | Decimal | No | Total points earned | No |
| LifetimePointsRedeemed | Lifetime Points Redeemed | Decimal | No | Total points redeemed | No |
| PointsExpiryDate | Points Expiry Date | Date | No | Next points expiry date | No |
| LastActivityDate | Last Activity Date | Date | No | Last loyalty activity date | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| SourceLoyaltyMemberKey | Source Loyalty Member Key | String | No | Source member identifier | No |
| MemberHealthStatus | Member Health Status | String | No | Derived membership health indicator | No |
| ActivityRecencyBand | Activity Recency Band | String | No | Derived activity recency category | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## LoyaltyTier (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| LoyaltyTierId | Loyalty Tier Id | LongInteger | Yes | Primary identifier of the loyalty tier. | No |
| TierCode | Tier Code | String | No | Short code identifying the tier. | No |
| TierName | Tier Name | String | No | Business name of the tier. | No |
| TierLevel | Tier Level | RetailCustomer360.list_of_values.LoyaltyTierLevel | No | Standard level the tier corresponds to. | No |
| TierOrder | Tier Order | LongInteger | No | Rank of the tier within the program, lowest first. | No |
| QualifyingPoints | Qualifying Points | LongInteger | No | Points needed to reach the tier. | No |
| QualifyingSpend | Qualifying Spend | Decimal | No | Spend needed to reach the tier. | No |
| RetentionPoints | Retention Points | LongInteger | No | Points needed to stay in the tier for another period. | No |
| PointMultiplier | Point Multiplier | Decimal | No | Rate at which members in this tier earn points. | No |
| ValidityMonths | Validity Months | LongInteger | No | Number of months tier status lasts once earned. | No |
| BenefitSummary | Benefit Summary | String | No | Short summary of the benefits the tier grants. | No |
| IsActive | Is Active | Boolean | No | Whether the tier is currently offered. | No |
| Description | Description | String | No | Positioning of the tier within the program. | No |

## MobileAppEngagement (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| AppEventId | App Event Id | LongInteger | Yes | Primary identifier | No |
| AppSessionId | App Session Id | String | No | Mobile app session identifier | No |
| DeviceId | Device Id | String | No | Device identifier | No |
| EventType | Event Type | RetailCustomer360.list_of_values.MobileAppEventType | No | App Open, Product View, Search, Add to Cart, Purchase | No |
| ScreenName | Screen Name | String | No | App screen name | No |
| AppVersion | App Version | String | No | App version | No |
| OperatingSystem | Operating System | RetailCustomer360.list_of_values.OperatingSystem | No | iOS, Android | No |
| OperatingSystemVersion | Operating System Version | String | No | OS version | No |
| DeviceModel | Device Model | String | No | Device model | No |
| EventTimestamp | Event Timestamp | Timestamp | No | Event date/time | No |
| PushOptInStatus | Push Opt In Status | RetailCustomer360.list_of_values.PushOptInStatus | No | Opted In, Opted Out, Unknown | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| EngagementRecencyBand | Engagement Recency Band | String | No | Derived recency classification for the mobile event | No |
| MobilePlatformFamily | Mobile Platform Family | String | No | Derived platform family | No |
| EngagementQualityStatus | Engagement Quality Status | String | No | Derived quality and actionability status | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## Opportunity (ID_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OpportunityNumber | Opportunity Number | String | Yes | Universal identifier of the opportunity across systems. | No |
| OpportunityName | Opportunity Name | String | No | Business name of the opportunity. | No |
| OpportunityStage | Opportunity Stage | RetailCustomer360.list_of_values.OpportunityStage | No | Sales stage the opportunity has reached. | No |
| ForecastCategory | Forecast Category | RetailCustomer360.list_of_values.ForecastCategory | No | Forecast bucket the opportunity contributes to. | No |
| Amount | Amount | RetailCustomer360.complex_types.MonetaryAmount | No | Expected value of the opportunity. | No |
| Probability | Probability | Decimal | No | Estimated percentage likelihood of winning. | No |
| OpenDate | Open Date | Date | No | Date the opportunity was created. | No |
| CloseDate | Close Date | Date | No | Date the opportunity is expected to close or did close. | No |
| SalesChannel | Sales Channel | RetailCustomer360.list_of_values.SalesChannel | No | Channel the opportunity is being pursued through. | No |
| LossReason | Loss Reason | RetailCustomer360.list_of_values.LossReason | No | Reason recorded when the opportunity was lost. | No |
| NextStep | Next Step | String | No | Agreed next action to progress the opportunity. | No |
| OwnerName | Owner Name | String | No | Salesperson accountable for the opportunity. | No |
| IsClosed | Is Closed | Boolean | No | Whether the opportunity has reached a final outcome. | No |
| IsWon | Is Won | Boolean | No | Whether the closed opportunity was won. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the opportunity originates from. | No |
| SourceOpportunityKey | Source Opportunity Key | String | No | Natural key of the opportunity in the source system. | No |
| WeightedAmount | Weighted Amount | Decimal | No | Derived expected value weighted by win probability. | No |
| DaysOpen | Days Open | LongInteger | No | Derived number of days the opportunity has been open. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## OpportunityProduct (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OpportunityProductId | Opportunity Product Id | LongInteger | Yes | Primary identifier of the opportunity line. | No |
| LineNumber | Line Number | LongInteger | No | Position of the line within the opportunity. | No |
| Quantity | Quantity | Decimal | No | Quantity of the product quoted. | No |
| UnitPrice | Unit Price | Decimal | No | Price quoted per unit. | No |
| TotalPrice | Total Price | Decimal | No | Total value of the line before discount. | No |
| DiscountAmount | Discount Amount | Decimal | No | Discount applied to the line. | No |
| ExpectedDeliveryDate | Expected Delivery Date | Date | No | Date the customer expects the product. | No |
| IsPrimaryLine | Is Primary Line | Boolean | No | Whether this line drives the opportunity value. | No |
| Notes | Notes | String | No | Free-text commentary on the quoted line. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the opportunity line originates from. | No |

## OrderDeliveryMethod (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| DeliveryMethodId | Delivery Method Id | LongInteger | Yes | Primary identifier of the delivery method. | No |
| DeliveryMethodCode | Delivery Method Code | String | No | Short code identifying the delivery method. | No |
| DeliveryMethodName | Delivery Method Name | String | No | Business name of the delivery method. | No |
| DeliveryMethodType | Delivery Method Type | RetailCustomer360.list_of_values.DeliveryMethodType | No | Category of delivery the method represents. | No |
| Carrier | Carrier | String | No | Logistics provider that performs the delivery. | No |
| EstimatedDays | Estimated Days | LongInteger | No | Typical number of days from dispatch to delivery. | No |
| BaseCost | Base Cost | Decimal | No | Standard charge applied for this delivery method. | No |
| IsActive | Is Active | Boolean | No | Whether the method is currently offered. | No |
| RequiresSignature | Requires Signature | Boolean | No | Whether the customer must sign on receipt. | No |
| IsTrackable | Is Trackable | Boolean | No | Whether the shipment can be tracked end to end. | No |
| Description | Description | String | No | Explanation of how the delivery method works. | No |

## PartyIdentification (FUZZY_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PartyIdentificationId | Party Identification Id | LongInteger | Yes | Primary identifier for the party identification record. | No |
| IdentificationType | Identification Type | RetailCustomer360.list_of_values.IdentificationType | No | Identification type classification (PAN, Passport, National ID, Driver License, Loyalty Number). | Yes |
| IdentificationNumber | Identification Number | String | No | Identifier value. | Yes |
| IssuingAuthority | Issuing Authority | String | No | Authority that issued the identifier. | No |
| IssueDate | Issue Date | Date | No | Issue date. | No |
| ExpiryDate | Expiry Date | Date | No | Expiry date. | No |
| IdentificationStatus | Identification Status | RetailCustomer360.list_of_values.IdentificationStatus | No | Identification status (Active, Expired, Revoked, Suspended). | No |
| IsVerified | Is Verified | Boolean | No | Indicates verified identifier. | No |
| VerificationDate | Verification Date | Date | No | Date/time verified. | No |
| MaskedIdentificationNumber | Masked Identification Number | String | No | Masked display version. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system. | No |
| SourceIdentificationKey | Source Identification Key | String | No | Source identifier key. | No |
| IdentificationLifecycleStatus | Identification Lifecycle Status | String | No | Derived lifecycle status for the identification document. | No |
| VerificationFreshnessBand | Verification Freshness Band | String | No | Derived recency band for verification evidence. | No |
| VerificationConfidenceStatus | Verification Confidence Status | String | No | Derived confidence status based on verification evidence. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## Product (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ProductId | Product Id | LongInteger | Yes | Primary identifier | No |
| ProductCode | Product Code | String | No | Product business code | No |
| ProductName | Product Name | String | No | Product name | No |
| ProductDescription | Product Description | String | No | Product description | No |
| SKU | SKU | String | No | Stock keeping unit | No |
| Barcode | Barcode | String | No | EAN/UPC/GTIN | No |
| ProductType | Product Type | RetailCustomer360.list_of_values.ProductType | No | Physical, Digital, Service, Bundle | No |
| ProductStatus | Product Status | RetailCustomer360.list_of_values.ProductStatus | No | Active, Inactive, Discontinued | No |
| Price | Price | Decimal | No | Current selling price | No |
| ListPrice | List Price | Decimal | No | Standard list price | No |
| CostPrice | Cost Price | Decimal | No | Product cost, if maintained | No |
| LaunchDate | Launch Date | Date | No | Product launch date | No |
| DiscontinueDate | Discontinue Date | Date | No | Product discontinue date | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| SourceProductKey | Source Product Key | String | No | Source product identifier | No |
| MarginAmount | Margin Amount | Decimal | No | Derived gross margin amount (Price - CostPrice) | No |
| MarginPercent | Margin Percent | Decimal | No | Derived gross margin percentage | No |
| ProductLifecycleStatus | Product Lifecycle Status | String | No | Derived lifecycle state from launch/discontinue dates and status | No |
| PricingHealthStatus | Pricing Health Status | String | No | Derived pricing quality status | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## ProductCatalog (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CatalogId | Catalog Id | LongInteger | Yes | Primary identifier of the catalog. | No |
| CatalogCode | Catalog Code | String | No | Short code identifying the catalog. | No |
| CatalogName | Catalog Name | String | No | Business name of the catalog. | No |
| CatalogStatus | Catalog Status | RetailCustomer360.list_of_values.CatalogStatus | No | Publication state of the catalog. | No |
| Description | Description | String | No | Purpose and audience of the catalog. | No |
| EffectiveFrom | Effective From | Date | No | Date the catalog becomes available. | No |
| EffectiveTo | Effective To | Date | No | Date the catalog is withdrawn. | No |
| SalesChannel | Sales Channel | RetailCustomer360.list_of_values.SalesChannel | No | Channel the catalog is published to. | No |
| IsDefault | Is Default | Boolean | No | Whether this is the fallback catalog for its channel. | No |
| DisplayOrder | Display Order | LongInteger | No | Position of the catalog in listings. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the catalog originates from. | No |

## ProductCatalogCategory (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CatalogCategoryId | Catalog Category Id | LongInteger | Yes | Primary identifier of the catalog category. | No |
| CatalogCategoryCode | Catalog Category Code | String | No | Short code identifying the catalog category. | No |
| CatalogCategoryName | Catalog Category Name | String | No | Business name of the catalog category. | No |
| Description | Description | String | No | Explanation of what the category groups. | No |
| DisplayOrder | Display Order | LongInteger | No | Position of the category in catalog navigation. | No |
| HierarchyLevel | Hierarchy Level | LongInteger | No | Depth of the category within the catalog hierarchy. | No |
| IsActive | Is Active | Boolean | No | Whether the category is currently shown. | No |
| IsVisibleOnline | Is Visible Online | Boolean | No | Whether the category is exposed on the online storefront. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the catalog category originates from. | No |

## Promotion (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| PromotionId | Promotion Id | LongInteger | Yes | Primary identifier of the promotion. | No |
| PromotionCode | Promotion Code | String | No | Short code customers or systems use to apply the promotion. | No |
| PromotionName | Promotion Name | String | No | Business name of the promotion. | No |
| PromotionType | Promotion Type | RetailCustomer360.list_of_values.PromotionType | No | Mechanic the promotion uses. | No |
| PromotionStatus | Promotion Status | RetailCustomer360.list_of_values.PromotionStatus | No | Lifecycle status of the promotion. | No |
| StartDate | Start Date | Timestamp | No | Date and time the promotion becomes redeemable. | No |
| EndDate | End Date | Timestamp | No | Date and time the promotion stops being redeemable. | No |
| DiscountValue | Discount Value | Decimal | No | Value of the discount or multiplier applied. | No |
| MinimumSpend | Minimum Spend | Decimal | No | Spend a customer must reach to qualify. | No |
| MaxRedemptions | Max Redemptions | LongInteger | No | Maximum number of times the promotion can be redeemed. | No |
| RedemptionCount | Redemption Count | LongInteger | No | Number of redemptions recorded so far. | No |
| TargetSegment | Target Segment | RetailCustomer360.list_of_values.TargetSegment | No | Customer segment the promotion is aimed at. | No |
| TermsAndConditions | Terms And Conditions | String | No | Conditions attached to the promotion. | No |
| IsStackable | Is Stackable | Boolean | No | Whether the promotion can combine with other offers. | No |
| PromotionWindowStatus | Promotion Window Status | String | No | Derived indication of whether the promotion is upcoming, live or past. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the promotion originates from. | No |

## SalesOrder (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OrderId | Order Id | LongInteger | Yes | Primary identifier | No |
| OrderNumber | Order Number | String | No | Business order number | No |
| OrderDate | Order Date | Timestamp | No | Order placement date/time | No |
| OrderStatus | Order Status | RetailCustomer360.list_of_values.OrderStatus | No | Draft, Submitted, Confirmed, Fulfilled, Cancelled, Returned | No |
| OrderType | Order Type | RetailCustomer360.list_of_values.OrderType | No | Purchase, Return, Exchange, Subscription | No |
| SalesChannel | Sales Channel | RetailCustomer360.list_of_values.SalesChannel | No | Store, Web, Mobile App, Marketplace, Call Center | No |
| FulfillmentMethod | Fulfillment Method | RetailCustomer360.list_of_values.FulfillmentMethod | No | Delivery, Pickup, Ship to Store, Digital | No |
| PaymentMethod | Payment Method | RetailCustomer360.list_of_values.PaymentMethod | No | Card, Cash, Wallet, UPI, BNPL, Gift Card | No |
| PaymentStatus | Payment Status | RetailCustomer360.list_of_values.PaymentStatus | No | Pending, Paid, Failed, Refunded, Partially Refunded | No |
| SubtotalAmount | Subtotal Amount | Decimal | No | Order subtotal | No |
| DiscountAmount | Discount Amount | Decimal | No | Total discount | No |
| TaxAmount | Tax Amount | Decimal | No | Total tax | No |
| ShippingAmount | Shipping Amount | Decimal | No | Shipping charge | No |
| TotalAmount | Total Amount | Decimal | No | Final order value | No |
| CouponCode | Coupon Code | String | No | Applied coupon or promotion code | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| SourceOrderKey | Source Order Key | String | No | Source order identifier | No |
| NetAmount | Net Amount | Decimal | No | Derived net amount before tax and shipping | No |
| DiscountRatePercent | Discount Rate Percent | Decimal | No | Derived discount rate percent on subtotal | No |
| OrderLifecycleStatus | Order Lifecycle Status | String | No | Derived lifecycle stage from order and payment status | No |
| FinancialHealthStatus | Financial Health Status | String | No | Derived financial consistency status | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## SalesOrderItem (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| OrderItemId | Order Item Id | LongInteger | Yes | Primary identifier | No |
| LineNumber | Line Number | Integer | No | Order line number | No |
| ItemType | Item Type | RetailCustomer360.list_of_values.ItemType | No | Product, Service, Shipping, Discount, Gift Wrap | No |
| Quantity | Quantity | Integer | No | Quantity ordered | No |
| UnitPrice | Unit Price | Decimal | No | Unit selling price | No |
| ListPrice | List Price | Decimal | No | Original list price | No |
| DiscountAmount | Discount Amount | Decimal | No | Discount amount for item | No |
| TaxAmount | Tax Amount | Decimal | No | Tax amount for item | No |
| TotalPrice | Total Price | Decimal | No | Final line amount | No |
| FulfillmentStatus | Fulfillment Status | RetailCustomer360.list_of_values.FulfillmentStatus | No | Pending, Packed, Shipped, Delivered, Cancelled, Returned | No |
| ReturnStatus | Return Status | RetailCustomer360.list_of_values.ReturnStatus | No | Not Returned, Return Requested, Returned, Refunded | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| SourceOrderItemKey | Source Order Item Key | String | No | Source order item identifier | No |
| GrossAmount | Gross Amount | Decimal | No | Derived gross amount before discounts and taxes | No |
| EffectiveUnitPrice | Effective Unit Price | Decimal | No | Derived effective unit price after discount | No |
| ItemLifecycleStatus | Item Lifecycle Status | String | No | Derived lifecycle status from fulfillment and return states | No |
| ItemFinancialHealthStatus | Item Financial Health Status | String | No | Derived financial consistency status for item amounts | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## SalesStore (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| StoreId | Store Id | LongInteger | Yes | Primary identifier of the store. | No |
| StoreCode | Store Code | String | No | Short code identifying the store. | No |
| StoreName | Store Name | String | No | Business name of the store. | No |
| StoreType | Store Type | RetailCustomer360.list_of_values.StoreType | No | Retail format of the store. | No |
| StoreStatus | Store Status | RetailCustomer360.list_of_values.StoreStatus | No | Operating status of the store. | No |
| Address | Address | RetailCustomer360.complex_types.PostalAddress | No | Postal address of the store. | No |
| Coordinates | Coordinates | RetailCustomer360.complex_types.GeoCoordinates | No | Geographic position of the store. | No |
| OpeningDate | Opening Date | Date | No | Date the store opened for trading. | No |
| ClosingDate | Closing Date | Date | No | Date the store ceased trading. | No |
| SellingAreaSqm | Selling Area Sqm | Decimal | No | Selling floor area in square metres. | No |
| EmployeeCount | Employee Count | LongInteger | No | Number of staff assigned to the store. | No |
| PhoneNumber | Phone Number | String | No | Contact phone number for the store. | No |
| EmailAddress | Email Address | String | No | Contact email address for the store. | No |
| ManagerName | Manager Name | String | No | Name of the store manager. | No |
| TimeZone | Time Zone | String | No | Time zone the store operates in. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the store record originates from. | No |
| SourceStoreKey | Source Store Key | String | No | Natural key of the store in the source system. | No |
| StoreNameNormalized | Store Name Normalized | String | No | Uppercased and trimmed store name used for lookups. | No |

## ShoppingCartEngagement (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| CartId | Cart Id | LongInteger | Yes | Primary identifier of the cart session. | No |
| SessionId | Session Id | String | No | Browsing session the cart belongs to. | No |
| CartStatus | Cart Status | RetailCustomer360.list_of_values.CartStatus | No | Outcome state of the cart. | No |
| ItemCount | Item Count | LongInteger | No | Number of items placed in the cart. | No |
| CartValue | Cart Value | Decimal | No | Total value of the items in the cart. | No |
| CurrencyCode | Currency Code | String | No | Currency the cart value is expressed in. | No |
| CreatedTimestamp | Created Timestamp | Timestamp | No | Date and time the cart was created. | No |
| LastUpdatedTimestamp | Last Updated Timestamp | Timestamp | No | Date and time the cart was last modified. | No |
| AbandonedTimestamp | Abandoned Timestamp | Timestamp | No | Date and time the cart was considered abandoned. | No |
| ConvertedTimestamp | Converted Timestamp | Timestamp | No | Date and time the cart became an order. | No |
| CouponCode | Coupon Code | String | No | Coupon applied to the cart. | No |
| SalesChannel | Sales Channel | RetailCustomer360.list_of_values.SalesChannel | No | Channel the cart was assembled in. | No |
| RecoveryEmailSent | Recovery Email Sent | Boolean | No | Whether an abandonment recovery email was sent. | No |
| CartAgeHours | Cart Age Hours | Decimal | No | Derived number of hours between creation and last update. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the cart engagement originates from. | No |

## SMSEngagement (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SmsEngagementId | Sms Engagement Id | LongInteger | Yes | Primary identifier of the SMS engagement. | No |
| MessageId | Message Id | String | No | Identifier of the SMS message in the sending platform. | No |
| PhoneNumber | Phone Number | String | No | Number the message was sent to. | No |
| EventType | Event Type | RetailCustomer360.list_of_values.SMSEventType | No | Event recorded against the message. | No |
| EventTimestamp | Event Timestamp | Timestamp | No | Date and time the event occurred. | No |
| MessageBody | Message Body | String | No | Text content of the message. | No |
| ShortCode | Short Code | String | No | Short code or sender id the message was sent from. | No |
| SegmentCount | Segment Count | LongInteger | No | Number of SMS segments the message consumed. | No |
| DeliveryStatus | Delivery Status | String | No | Carrier delivery status reported for the message. | No |
| FailureReason | Failure Reason | String | No | Reason the message failed to deliver. | No |
| LinkUrl | Link Url | String | No | Tracked link included in the message. | No |
| Locale | Locale | String | No | Locale the message was composed in. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the SMS engagement originates from. | No |

## SoftwareApplication (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| ApplicationId | Application Id | LongInteger | Yes | Primary identifier of the application. | No |
| ApplicationCode | Application Code | String | No | Short code identifying the application. | No |
| ApplicationName | Application Name | String | No | Business name of the application. | No |
| AppPlatform | App Platform | RetailCustomer360.list_of_values.AppPlatform | No | Platform the application is published on. | No |
| AppVersion | App Version | String | No | Current released version of the application. | No |
| BundleIdentifier | Bundle Identifier | String | No | Store bundle or package identifier. | No |
| ReleaseDate | Release Date | Date | No | Date the current version was released. | No |
| IsActive | Is Active | Boolean | No | Whether the application is still supported. | No |
| SupportUrl | Support Url | String | No | Link to customer support for the application. | No |
| Description | Description | String | No | Purpose of the application. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the application record originates from. | No |

## UnitOfMeasure (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| UomId | Unit Of Measure Id | LongInteger | Yes | Primary identifier of the unit of measure. | No |
| UomCode | Unit Code | String | No | Short code identifying the unit. | No |
| UomName | Unit Name | String | No | Business name of the unit. | No |
| UomType | Unit Type | RetailCustomer360.list_of_values.UnitOfMeasureType | No | Dimension the unit measures. | No |
| BaseUnitCode | Base Unit Code | String | No | Code of the base unit this unit converts to. | No |
| ConversionFactor | Conversion Factor | Decimal | No | Multiplier that converts this unit into the base unit. | No |
| DecimalPrecision | Decimal Precision | LongInteger | No | Number of decimal places quantities are expressed with. | No |
| IsBaseUnit | Is Base Unit | Boolean | No | Whether this unit is the base of its dimension. | No |
| IsActive | Is Active | Boolean | No | Whether the unit is currently in use. | No |

## Voucher (ID_MATCHED)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| VoucherCode | Voucher Code | String | Yes | Universal identifier of the voucher across systems. | No |
| VoucherType | Voucher Type | RetailCustomer360.list_of_values.VoucherType | No | Kind of benefit the voucher grants. | No |
| VoucherStatus | Voucher Status | RetailCustomer360.list_of_values.VoucherStatus | No | Redemption state of the voucher. | No |
| FaceValue | Face Value | Decimal | No | Original value of the voucher when issued. | No |
| RemainingValue | Remaining Value | Decimal | No | Value still available on the voucher. | No |
| CurrencyCode | Currency Code | String | No | Currency the voucher value is expressed in. | No |
| IssuedDate | Issued Date | Timestamp | No | Date and time the voucher was issued. | No |
| ExpirationDate | Expiration Date | Timestamp | No | Date and time the voucher expires. | No |
| RedeemedDate | Redeemed Date | Timestamp | No | Date and time the voucher was redeemed. | No |
| MinimumSpend | Minimum Spend | Decimal | No | Spend required before the voucher can be used. | No |
| IsTransferable | Is Transferable | Boolean | No | Whether the voucher can be passed to another person. | No |
| IsPartialRedeemAllowed | Is Partial Redeem Allowed | Boolean | No | Whether the voucher can be redeemed across several transactions. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the voucher originates from. | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes. | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High). | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated. | No |

## WebEngagement (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| EventId | Event Id | LongInteger | Yes | Primary identifier | No |
| SessionId | Session Id | String | No | Web session identifier | No |
| EventType | Event Type | RetailCustomer360.list_of_values.WebEventType | No | Page View, Product View, Search, Add to Cart, Checkout | No |
| PageUrl | Page URL | String | No | URL visited | No |
| PageTitle | Page Title | String | No | Page title | No |
| ReferrerUrl | Referrer URL | String | No | Referrer URL | No |
| DeviceType | Device Type | RetailCustomer360.list_of_values.DeviceType | No | Desktop, Mobile, Tablet | No |
| Browser | Browser | RetailCustomer360.list_of_values.WebBrowser | No | Chrome, Safari, Edge, Firefox, Other | No |
| OperatingSystem | Operating System | RetailCustomer360.list_of_values.OperatingSystem | No | iOS, Android, Windows, macOS, Linux | No |
| EventTimestamp | Event Timestamp | Timestamp | No | Event date/time | No |
| UtmSource | UTM Source | String | No | UTM source | No |
| UtmMedium | UTM Medium | String | No | UTM medium | No |
| UtmCampaign | UTM Campaign | String | No | UTM campaign | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | Source system | No |
| EngagementRecencyBand | Engagement Recency Band | String | No | Derived recency category of the web event | No |
| TrafficAttributionStatus | Traffic Attribution Status | String | No | Derived attribution quality from UTM and referrer context | No |
| ChannelIntentSignal | Channel Intent Signal | String | No | Derived intent signal from event type | No |
| EnrichmentCompletenessScore | Enrichment Completeness Score | Decimal | No | Derived completeness score based on key business attributes | No |
| EnrichmentCompletenessBand | Enrichment Completeness Band | String | No | Derived completeness band (Low, Medium, High) | No |
| EnrichmentUpdatedOn | Enrichment Updated On | Date | No | Date when enrichment was last calculated | No |

## WebSearchEngagement (BASIC)

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---|---|---|---|---|---|
| SearchEngagementId | Search Engagement Id | LongInteger | Yes | Primary identifier of the search engagement. | No |
| SessionId | Session Id | String | No | Browsing session the search belongs to. | No |
| SearchEngine | Search Engine | RetailCustomer360.list_of_values.SearchEngine | No | Provider that served the search. | No |
| SearchTerm | Search Term | String | No | Text the customer searched for. | No |
| ResultCount | Result Count | LongInteger | No | Number of results returned for the search. | No |
| ClickedPosition | Clicked Position | LongInteger | No | Rank of the result the customer clicked. | No |
| LandingPageUrl | Landing Page Url | String | No | Page the customer arrived on after the search. | No |
| EventTimestamp | Event Timestamp | Timestamp | No | Date and time the search was performed. | No |
| WebBrowser | Web Browser | RetailCustomer360.list_of_values.WebBrowser | No | Browser used to perform the search. | No |
| DeviceType | Device Type | RetailCustomer360.list_of_values.DeviceType | No | Type of device the search came from. | No |
| CountryCode | Country Code | String | No | Country the search originated from. | No |
| IsInternalSearch | Is Internal Search | Boolean | No | Whether the search used the site's own search box. | No |
| SourceSystem | Source System | RetailCustomer360.list_of_values.SourceSystem | No | System the search engagement originates from. | No |

