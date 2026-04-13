## Sales360 Model Structure

Below is a summary table of all entities in the model, including their label, documentation, references, and attribute count.

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |
|-------------|-------------|---------------------|-----------------------|--------------------|---------------------|
| Account | Account | Represents an individual account, which is an organization (such as customers, competitors, and partners). | AccountContactRelation, Contact, Leads, Opportunity, Account | AccountType, SicCode, LeadSource, Ownership, CleanStatus, Industry, NAICCode, Account | 59 |
| AccountContactRelation | Account Contact Relation | Represents a relationship between a contact and one or more accounts. | (none) | Role, Account, Contact | 6 |
| AccountType | Account Type | Type of account, for example, Customer, Competitor, or Partner | Account | (none) | 3 |
| Campaign | Campaign | Represents and tracks a marketing campaign, such as a direct mail promotion, webinar, or trade show | CampaignMember, Opportunity, Campaign | CampaignType, CampaignStatus, Campaign | 19 |
| CampaignMember | Campaign Member | Represents the association between a campaign and either a lead or a contact. | (none) | LeadSource, CampaignMemberStatus, Campaign, Contact, Leads | 8 |
| CampaignMemberStatus | Campaign Member Status | All the statuses of the contact or lead added to a campaign | CampaignMember | (none) | 3 |
| CampaignStatus | Campaign Status | Status of the campaign, for example, Planned, In Progress | Campaign | (none) | 3 |
| CampaignType | Campaign Type | Type of campaign, for example, Direct Mail or Referral Program | Campaign | (none) | 3 |
| CleanStatus | Clean Status | Record's clean status as compared with Data.com | Account, Contact, Leads | (none) | 3 |
| Contact | Contact | Represents a contact, which is a person associated with an account. | AccountContactRelation, CampaignMember, Leads, OpportunityContactRole, Contact | Salutation, LeadSource, CleanStatus, Account, Contact | 33 |
| ForecastCategory | Forecast Category | All the forecast categories based on the Stage an Opportunity is in | Opportunity | (none) | 3 |
| Industry | Industry | List of all Industries | Account, Leads | (none) | 3 |
| Leads | Leads | Represents a prospect or lead. | CampaignMember | LeadSource, Salutation, LeadStatus, Industry, Opportunity, CleanStatus, Contact, Account | 31 |
| LeadSource | Lead Source | The source of the account record | Account, CampaignMember, Contact, Leads, Opportunity | (none) | 3 |
| LeadStatus | Lead Status | Status code for converted lead | Leads | (none) | 3 |
| NAICCode | NAIC Code | The six-digit North American Industry Classification System (NAICS) code is the standard used by business and government to classify business establishments into industries | Account | (none) | 3 |
| Nickname | Nickname | List of all the Nicnames | (none) | (none) | 3 |
| Opportunity | Opportunity | Represents an opportunity, which is a sale or pending deal. | Leads, OpportunityContactRole | OpportunityType, StageName, LeadSource, ForecastCategory, Campaign, Account | 27 |
| OpportunityContactRole | Opportunity Contact Role | Represents the role that a Contact plays on an Opportunity. | (none) | Role, Opportunity, Contact | 3 |
| OpportunityType | Opportunity Type | Type of opportunity. For example, Existing Business or New Business | Opportunity | (none) | 3 |
| Ownership | Ownership | Ownership type for the account, for example Private, Public, or Subsidiary | Account | (none) | 3 |
| Role | Role | A contact's participating role in the account or opportunity | AccountContactRelation, OpportunityContactRole | (none) | 3 |
| Salutation | Salutation | Honorific added to the name for use in letters, etc. | Contact, Leads | (none) | 3 |
| SicCode | Sic Code | Standard Industrial Classification code of the company's main business categorization | Account | (none) | 3 |
| StageName | Stage Name | List of all the Stages in an Opportunity | Opportunity | (none) | 3 |

# Detailed Model Structure

Below are markdown tables for each entity in the model. Each table lists the attributes and their metadata.

## Account

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AccountID | Account ID | LongInteger | Yes | Golden ID | No |
| ValidEmailDomain | Valid Email Domain | String | No | Domain part of email address | No |
| CleansedPersonEmail | Cleansed Email | String | No | Cleansed email address | No |
| IsPersonAccount | Is Person Account | Boolean | No | Indicates if account is a person account | No |
| BusinessShippingAddressSame | Business Shipping Address Same | Boolean | No | Flag used to indicate that the Business and Shipping addresses are the same | No |
| DAndBCompanyid | D And B Companyid | String | No | Dun & Bradstreet company record ID | No |
| PersonEmailBouncedDate | Person Email Bounced Date | Timestamp | No | Date when person's email bounced | No |
| NormalizedWebsite | Normalized Website | String | No | The enriched website of this account | No |
| YearStarted | Year Started | ShortInteger | No | The date when an org was legally established. Available on business accounts, not person accounts | No |
| NickName | Nick Name | String | No | Alternate name for person account | No |
| NumberOfEmployees | Number Of Employees | Integer | No | Number of employees working at the company represented by this account | No |
| PersonTitle | Person Title | String | No | Job title of the person account | No |
| NormalizedLastName | Normalized Last Name | String | No | Enriched Last name Enriched Last name | No |
| PhoneticAccountName | Phonetic Account Name | String | No | Phonetic representation of account name | No |
| Website | Website | String | No | The website of this account | No |
| MergedInCRM | Merged In CRM | Boolean | No | Indicates if account has been merged in CRM | No |
| PersonDepartment | Person Department | String | No | Department of the person account Department of the person account | No |
| PhoneticFirstName | Phonetic First Name | String | No | Phonetic representation of first name | No |
| Active | Active | ActiveLOV | No | Indicates if account is active or inactive Indicates if account is active or inactive | No |
| JigsawCompanyId | Jigsaw Company Id | String | No | Data.com Company ID | No |
| AccountSite | Account Site | String | No | Name of the account's location | No |
| NormalizedFirstName | Normalized First Name | String | No | Enriched First name | No |
| CustomerPriority | Customer Priority | String | No | Priority level of the account as a customer Priority level of the account as a customer | No |
| Rating | Rating | RatingLOV | No | Prospect rating of the account | No |
| NumberOfLocations | Number Of Locations | Integer | No | Number of locations associated with the account | No |
| RecordTypeId | Record Type Id | String | No | Record Type ID | No |
| PersonLastCURequestDate | Person Last CU Request Date | Timestamp | No | Last date this person account was requested | No |
| Jigsaw | Jigsaw | String | No | Data.com Jigsaw ID | No |
| NormalizedAccountName | Normalized Account Name | String | No | Enriched Account name | No |
| LocalizedAccountName | Localized Account Name | String | No | Localized Account name | No |
| DunsNumber | Duns Number | String | No | The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit number assigned to every business location in the Dun & Bradstreet database that has a unique, separate, and distinct operation. D-U-N-S numbers are used by industries and organizations around the world as a global standard for business identification and tracking | No |
| Description | Description | String | No | Description of the account | No |
| AnnualRevenue | Annual Revenue | Integer | No | Estimated annual revenue of the account | No |
| AccountName | Account Name | String | Yes | Name of the account. If a Person this value is the concatenation of the FirstName, MiddleName, LastName, and Suffix of the associated person contact. | No |
| LastName | Last Name | String | No | Last name of the person for a person account. Required if the record type is a person account record type | No |
| PersonContactId | Person Contact Id | String | No | Contact ID of the person account | No |
| PersonEmail | Person Email | String | No | Email address of the person account | No |
| FirstName | First Name | String | No | First name of the person for a person account. | No |
| UpsellOpportunity | Upsell Opportunity | UpsellOppLOV | No | Indicates if account is an upsell opportunity | No |
| TradeStyle | Trade Style | String | No | A name, different from its legal name, that an org may use for conducting business | No |
| PersonEmailBouncedReason | Person Email Bounced Reason | String | No | Reason why person's email bounced | No |
| Fax | Fax | String | No | Fax number of the account | No |
| PhoneticLastName | Phonetic Last Name | String | No | Phonetic representation of last name | No |
| PersonLastCUUpdateDate | Person Last CU Update Date | Timestamp | No | Last date a person account was updated | No |
| TickerSymbol | Ticker Symbol | String | No | The stock market symbol for this account. This field is available on business accounts, not person accounts. | No |
| Salutation | Salutation | String | No | Honorific for the person account | No |
| PersonIndividualId | Person Individual Id | String | No | Data privacy record ID of the person account | No |
| PersonBirthDate | Person Birth Date | Date | No | Birth date of the person account | No |
| AccountNumber | Account Number | String | No | Account number assigned to this account | No |
| PhotoUrl | Photo Url | String | No | URL of the photo for the account | No |
| PersonAssistantName | Person Assistant Name | String | No | Name of the assistant for the person account | No |
| Phone | Phone | StandardizedPhoneType | No | Phone number of this account | No |
| PersonMailingAddress | Person Mailing Address | StandardizedAddressType | No | Mailing address of the person account | No |
| PersonAssitantPhone | Person Assitant Phone | StandardizedPhoneType | No | Phone number of the assistant for the person account | No |
| ShippingAddress | Shipping Address | StandardizedAddressType | No | Shiiping address for this account | No |
| PersonMobilePhone | Person Mobile Phone | StandardizedPhoneType | No | Mobile phone number of the person account | No |
| BillingAddress | Billing Address | StandardizedAddressType | No | Billing address for this account | No |
| PersonHomePhone | Person Home Phone | StandardizedPhoneType | No | Home phone number of the person account | No |
| PersonOtherAddress | Person Other Address | StandardizedAddressType | No | Other address of the person account | No |
| PersonOtherPhone | Person Other Phone | StandardizedPhoneType | No | Other phone number of the person account | No |

---

## OpportunityType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| OpportunityTypeID | Opportunity Type ID | String | Yes | Unique identifier for the opportunity type | No |
| OpportunityValue | Opportunity Value | String | No | Value associated with the opportunity type | No |
| OpportunityType | Opportunity Type | String | No | Name of the opportunity type | No |

---

## Ownership

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| OwnershipID | Ownership ID | String | Yes | Unique identifier for the Ownership entity | No |
| OwnershipValue | Ownership Value | String | No | Value representing the ownership type, such as Private or Public | No |
| OwnershipType | Ownership Type | String | No | Type of ownership, for example Private, Public, or Subsidiary | No |

---

## Role

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| RoleID | Role ID | String | Yes | Unique identifier for the Role entity | No |
| RoleCode | Role Code | String | No | Role codes for the role a contact is playing an inccount or opportunity like Evaluator, Decision Maker, etc. | No |
| RoleName | Role Name | String | No | Role names for the role a contact is playing an inccount or opportunity like Evaluator, Decision Maker, etc. | No |

---

## Salutation

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SalutationID | Salutation ID | String | Yes | Unique identifier for the salutation. | No |
| SalutationType | Salutation Type | String | No | Type of salutation (e.g., Mr., Ms., Dr.). | No |
| SalutationValue | Salutation Value | String | No | The actual salutation value. | No |

---

## SicCode

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| SicCodeID | Sic Code ID | String | Yes | Unique identifier for the Sic Code | No |
| SicCode | Sic Code | String | No | The actual Sic Code value | No |
| SicDesc | Sic Desc | String | No | Description of the Sic Code | No |

---

## StageName

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| StageNameID | Stage Name ID | String | Yes | Unique identifier for the Stage Name | No |
| StageName | Stage Name | String | No | Name of the Stage | No |
| StageDescription | Stage Description | String | No | Description of the Stage | No |

---

## AccountContactRelation

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AccountContactRelationID | Account Contact Relation ID | LongInteger | Yes | Unique identifier for an account contact relation | No |
| MultipleRoles | Multiple Roles | String | No | Populated if a contact is playing multiple roles in an account | No |
| EndDate | End Date | Date | No | The date a relationship between a contact and account ended | No |
| StartDate | Start Date | Date | No | The date a relationship between a contact and account began | No |
| IsDirect | Is Direct | Boolean | No | Indicates whether the account associated with the contact is the contact's primary account | No |
| IsActive | Is Active | Boolean | No | Indicates whether relationship is active | No |

---

## AccountType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| AccountTypeID | Account Type ID | String | Yes | Unique identifier for the Account Type | No |
| AccountTypeCode | Account Type Code | String | No | Code representing the Account Type | No |
| AccountTypeName | Account Type Name | String | No | Name of the Account Type | No |

---

## Campaign

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CampaignID | Campaign ID | String | Yes | Unique identifier for the campaign | No |
| NumberOfOpportunities | Number Of Opportunities | Integer | No | Number of opportunities associated with the campaign | No |
| EndDate | End Date | Date | No | Ending date for the campaign | No |
| NumberOfLeads | Number Of Leads | Integer | No | Number of leads associated with the campaign | No |
| CampaignMemberRecordTypeId | Campaign Member Record Type Id | String | No | The record type ID for CampaignMember records associated with the campaign | No |
| IsActive | Is Active | Boolean | No | Indicates whether this campaign is active | No |
| NumberSent | Number Sent | Integer | No | Number of individuals targeted by the campaign | No |
| BudgetedCost | Budgeted Cost | Integer | No | Amount of money budgeted for the campaign | No |
| Description | Description | String | No | Description of the campaign | No |
| StartDate | Start Date | Date | No | Starting date for the campaign | No |
| AmountAllOpportunities | Amount All Opportunities | Integer | No | Amount of money in all opportunities associated with the campaign, including closed/won opportunities | No |
| NumberOfResponses | Number Of Responses | Integer | No | Number of contacts and unconverted leads with a Member Status equivalent to "Responded" for the campaign | No |
| ExpectedRevenue | Expected Revenue | Integer | No | Amount of money you expect to generate from the campaign | No |
| NumberOfWonOpportunities | Number Of Won Opportunities | Integer | No | Number of closed or won opportunities associated with the campaign | No |
| ExpectedResponse | Expected Response | Integer | No | Percentage of responses you expect to receive for the campaign | No |
| ActualCost | Actual Cost | Integer | No | Amount of money spent to run the campaign | No |
| Name | Name | String | Yes | Name of the campaign | No |
| AmountWonOpportunities | Amount Won Opportunities | Integer | No | Amount of money in closed or won opportunities associated with the campaign | No |
| NumberOfContacts | Number Of Contacts | Integer | No | Number of contacts associated with the campaign | No |
| NumberOfConvertedLeads | Number Of Converted Leads | Integer | No | Number of leads that were converted to an account and contact due to the marketing efforts in the campaign | No |

---

## CampaignMember

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CampaignMemberID | Campaign Member ID | LongInteger | Yes | Unique identifier for the Campaign Member | No |
| HasOptedOutOfEmail | Has Opted Out Of Email | Boolean | No | Indicates whether the contact or lead would prefer not to receive email | No |
| DoNotCall | Do Not Call | Boolean | No | Indicates whether the contact or lead has requested not to be called | No |
| Type | Type | CampaignMemberType | No | Indicates whether the campaign member is a lead or a contact | No |
| FirstRespondedDate | First Responded Date | Date | No | Indicates the date on which the campaign member was first given a responded status | No |
| CompanyOrAccount | Company Or Account | String | No | The company or account associated with the campaign member | No |
| HasResponded | Has Responded | Boolean | No | Indicates whether the campaign member has responded to the campaign | No |
| HasOptedOutOfFax | Has Opted Out Of Fax | Boolean | No | Indicates that the contact or lead doesn't wish to receive faxes | No |

---

## CampaignMemberStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CampaignMemberStatusID | Campaign Member Status ID | String | Yes | Unique identifier for Campaign Member Status | No |
| CampaignMemberStatusCode | Campaign Member Status Code | String | No | Code representing the Campaign Member Status | No |
| CampaignMemberStatusValue | Campaign Member Status Value | String | No | Value or description of the Campaign Member Status | No |

---

## CampaignStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CampaignStatusID | Campaign Status ID | String | Yes | Unique identifier for the campaign status | No |
| CampaignStatus | Campaign Status | String | No | Name of the campaign status | No |
| CampaignStatusName | Campaign Status Name | String | No | Descriptive name of the campaign status | No |

---

## CampaignType

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CampaignTypeID | Campaign Type ID | String | Yes | Unique identifier for the Campaign Type | No |
| CampaignType | Campaign Type | String | No | Name of the Campaign Type | No |
| CampaignTypeValue | Campaign Type Value | String | No | Value associated with the Campaign Type | No |

---

## CleanStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| CleanStatusID | Clean Status ID | String | Yes | Unique identifier for the Clean Status record | No |
| CleanStatusCode | Clean Status Code | String | No | Code representing the clean status | No |
| CleanStatusValue | Clean Status Value | String | No | Value indicating the clean status | No |

---

## ForecastCategory

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ForecastCategoryID | Forecast Category ID | String | Yes | Unique identifier for the Forecast Category | No |
| ForecastCategory | Forecast Category | String | No | Name of the Forecast Category | No |
| ForecastCategoryName | Forecast Category Name | String | No | Descriptive name of the Forecast Category | No |

---

## Contact

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ContactID | Contact ID | LongInteger | Yes | Unique identifier for the contact | No |
| Description | Description | String | No | A description of the contact | No |
| IndividualId | Individual Id | String | No | ID of the data privacy record associated with this contact | No |
| LastCUUpdateDate | Last CU Update Date | Timestamp | No | The date and time of the last change made to the contact | No |
| Jigsaw | Jigsaw | String | No | References the company's ID in Data.com | No |
| Fax | Fax | String | No | Fax number of the contact | No |
| EmailBouncedDate | Email Bounced Date | Timestamp | No | If bounce management is activated and an email sent to the contact bounces, the date and time of the bounce | No |
| LastName | Last Name | String | Yes | Last name of the contact | No |
| Nickname | Nickname | String | No | Nickname based on first name | No |
| CleansedEmail | Cleansed Email | String | No | The contact's enriched email address | No |
| FirstName | First Name | String | No | The contact's first name | No |
| MergedInCRM | Merged In CRM | Boolean | No | Indicates whether the contact has been merged in the source CRM system | No |
| IsEmailBounced | Is Email Bounced | ByteInteger | No | If bounce management is activated and an email is sent to a contact, indicates whether the email bounced | No |
| FullName | Full Name | String | No | Concatenation of FirstName, MiddleName, LastName, and Suffix | No |
| Title | Title | String | No | Title of the contact | No |
| Department | Department | String | No | The contact's department | No |
| NormalizedLastName | Normalized Last Name | String | No | Enriched last name | No |
| PhotoUrl | Photo Url | String | No | URL of the contact's photo | No |
| IsPersonAccount | Is Person Account | Boolean | No | Indicates whether the contact is associated with a person account | No |
| EmailBouncedReason | Email Bounced Reason | String | No | If bounce management is activated and an email sent to the contact bounces, the reason for the bounce | No |
| BirthDate | Birth Date | Date | No | The contact's birthdate | No |
| SourceEmail | Source Email | String | No | The contact's email address as received from the source | No |
| AssistantName | Assistant Name | String | No | The assistant's name | No |
| LastCURequestDate | Last CU Request Date | Timestamp | No | The date and time of the last change request made to the contact | No |
| JigsawContactId | Jigsaw Contact Id | String | No | References the contact's ID in Data.com | No |
| NormalizedFirstName | Normalized First Name | String | No | Enriched first name | No |
| MobilePhone | Mobile Phone | StandardizedPhoneType | No | The contact's mobile phone number | No |
| AssistantPhone | Assistant Phone | StandardizedPhoneType | No | The assistant's phone number | No |
| Phone | Phone | StandardizedPhoneType | No | Phone number for the contact | No |
| MailingAddress | Mailing Address | StandardizedAddressType | No | The compound form of the mailing address | No |
| HomePhone | Home Phone | StandardizedPhoneType | No | The contact's home phone number | No |
| OtherPhone | Other Phone | StandardizedPhoneType | No | The contact's other phone number | No |
| OtherAddress | Other Address | StandardizedAddressType | No | The compound form of the other address | No |

---

## Industry

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| IndustryID | Industry ID | String | Yes | Unique identifier for the Industry | No |
| IndustryLabel | Industry Label | String | No | Label for the Industry | No |
| IndustryName | Industry Name | String | No | Name of the Industry | No |

---

## Leads

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| LeadID | Lead ID | LongInteger | Yes | Unique identifier for the lead | No |
| PhoneticCompany | Phonetic Company | String | No | Phonetic representation of the lead's company name | No |
| Fax | Fax | String | No | The lead's fax number | No |
| CleansedEmail | Cleansed Email | String | No | The lead's enriched email address | No |
| Name | Name | String | No | Concatenation of FirstName, MiddleName, LastName, and Suffix | No |
| Title | Title | String | No | Title for the lead | No |
| DAndBCompanyId | D And B Company Id | String | No | Dun & Bradstreet (D&B) D-U-N-S® Number for the lead's company | No |
| Jigsaw | Jigsaw | String | No | References the ID of a contact in Data.com | No |
| NumberOfEmployees | Number Of Employees | Integer | No | Number of employees in the lead's company | No |
| Description | Description | String | No | The lead's description | No |
| IsUnreadByOwner | Is Unread By Owner | Boolean | No | Indicates whether the lead has been read by the owner | No |
| Company | Company | String | Yes | The lead's company | No |
| Email | Email | String | No | The lead's email address from source | No |
| IsConverted | Is Converted | Boolean | No | Indicates whether the lead has been converted | No |
| EmailBouncedReason | Email Bounced Reason | String | No | If bounce management is activated and an email sent to the lead bounced, the reason for the bounce | No |
| ConvertedDate | Converted Date | Date | No | Date on which this lead was converted | No |
| Website | Website | String | No | Website for the lead | No |
| CompanyDunsNumber | Company Duns Number | String | No | The Data Universal Numbering System (D-U-N-S) number | No |
| NormalizedCompany | Normalized Company | String | No | Enriched Company name for the lead | No |
| LastName | Last Name | String | Yes | Last name of the lead | No |
| IndividualId | Individual Id | String | No | ID of the data privacy record associated with this lead | No |
| PhotoUrl | Photo URL | String | No | URL of the lead's photo | No |
| EmailBouncedDate | Email Bounced Date | Timestamp | No | If bounce management is activated and an email sent to the lead bounced, the date and time of the bounce | No |
| FirstName | First Name | String | No | The lead's first name | No |
| StandardizedWebsite | Standardized Website | String | No | Enriched Website for the lead | No |
| Jigsawcontactid | Jigsawcontactid | String | No | References the contact ID of a contact in Data.com | No |
| Rating | Rating | RatingLOV | No | Rating of the lead | No |
| NormalizedLastName | Normalized Last Name | String | No | The lead's enriched last name | No |
| AnnualRevenue | Annual Revenue | Integer | No | Annual revenue for the lead's company | No |
| NormalizedFirstName | Normalized First Name | String | No | The lead's enriched first name | No |
| MobilePhone | Mobile Phone | StandardizedPhoneType | No | The lead's mobile phone number | No |
| Phone | Phone | StandardizedPhoneType | No | The lead's phone number | No |
| Address | Address | StandardizedAddressType | No | Complex attribute for the entire address of the lead | No |

---

## LeadSource

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| LeadSourceID | Lead Source ID | String | Yes | Unique identifier for the Lead Source | No |
| LeadSourceType | Lead Source Type | String | No | Type of the Lead Source | No |
| LeadSourceValue | Lead Source Value | String | No | Value of the Lead Source | No |

---

## LeadStatus

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| LeadStatusID | Lead Status ID | String | Yes | Unique identifier for the Lead Status | No |
| LeadStatusType | Lead Status Type | String | No | Type of the Lead Status | No |
| LeadStatusValue | Lead Status Value | String | No | Value representing the Lead Status | No |

---

## NAICCode

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| NAICCodeID | NAIC Code ID | String | Yes | Unique identifier for the NAIC Code | No |
| NAICCode | NAIC Code | String | No | The six-digit NAIC code | No |
| NAICTitle | NAIC Title | String | No | The title associated with the NAIC code | No |

---

## Nickname

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| GivenName | Given Name | String | Yes | Given name of the person | No |
| AllNicknames | All Nicknames | String | No | All nicknames associated with the given name | No |
| TopNicknames | Top Nicknames | String | No | Top nicknames associated with the given name | No |

---

## Opportunity

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| OpportunityID | Opportunity ID | LongInteger | Yes | Unique identifier for the opportunity | No |
| LastStageChangeDate | Last Stage Change Date | Timestamp | No | The date of the last change made to the Stage field on this opportunity record | No |
| ContactId | Contact Id | String | No | ID of the contact associated with this opportunity, set as the primary contact | No |
| IsWon | Is Won | Boolean | No | Based on the Stage indicates if the opportunity has been won | No |
| Amount | Amount | Integer | No | Estimated total sale amount | No |
| FiscalQuarter | Fiscal Quarter | Integer | No | Represents the fiscal quarter | No |
| CloseDate | Close Date | Date | Yes | Date when the opportunity is expected to close | No |
| FiscalYear | Fiscal Year | Integer | No | Represents the fiscal year | No |
| HasOpportunityLineItem | Has Opportunity Line Item | Boolean | No | Indicates whether the opportunity has associated line items | No |
| HasOverdueTask | Has Overdue Task | Boolean | No | Indicates whether an opportunity has an overdue task | No |
| Fiscal | Fiscal | String | No | The name of the fiscal quarter or period in which the opportunity CloseDate falls | No |
| IsPrivate | Is Private | Boolean | No | Indicates whether the opportunity is private | No |
| PushCount | Push Count | Integer | No | The number of times an opportunity's close date has been pushed out by one calendar month | No |
| TotalOpportunityQuantity | Total Opportunity Quantity | Integer | No | Number of items included in this opportunity | No |
| ExpectedRevenue | Expected Revenue | Integer | No | The product of the opportunity Amount field and the Probability | No |
| IsClosed | Is Closed | Boolean | No | Based on the Stage indicates if the opportunity has been closed | No |
| Territory2Id | Territory2 Id | String | No | ID of the Territory2 associated with this opportunity | No |
| IsPriorityRecord | Is Priority Record | Boolean | No | Shows whether the user has marked the opportunity as important | No |
| Pricebook2Id | Pricebook2 Id | String | No | ID of the Pricebook2 associated with this opportunity | No |
| LastActivityDate | Last Activity Date | Date | No | The most recent date and time when an activity related to the opportunity was marked complete | No |
| Description | Description | String | No | Text description of the opportunity | No |
| HasOpenActivity | Has Open Activity | Boolean | No | Indicates whether an opportunity has an open event or task | No |
| Name | Name | String | Yes | A name for this opportunity | No |
| LastActivityInDays | Last Activity In Days | Integer | No | The number of days since the last activity on the opportunity | No |
| IsExcludedFromTerritory2Filter | Is Excluded From Territory2 Filter | Boolean | No | Indicates whether the opportunity is excluded from Territory2 filtering | No |
| NextStep | Next Step | String | No | Description of next task in closing opportunity | No |
| Probability | Probability | ByteInteger | No | Percentage of estimated confidence in closing the opportunity | No |

---

## OpportunityContactRole

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |
|---------------|----------------|-----------|------------|-------------|------------------|
| ID | ID | LongInteger | Yes | Unique identifier for the OpportunityContactRole record | No |
| IsPrimary | Is Primary | Boolean | No | Indicates whether the associated Contact plays the primary role on the Opportunity | No |
| MultipleRoles | Multiple Roles | String | No | Populated if the contact plays multiple roles in an opportunity | No |

---
