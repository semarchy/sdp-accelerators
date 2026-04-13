# Model Structure

| Entity Name         | Entity Label         | Entity Documentation                                                                 | Referenced by Entities                | References Entities                | Number of Attributes |
|---------------------|---------------------|--------------------------------------------------------------------------------------|---------------------------------------|------------------------------------|---------------------|
| Employee           | Employee            | This entity is used to define various employees, which can be referenced in other entities. | Contract                              | Address, Gender, Position, Study   | 22                  |
| Address            | Address             | This entity contains attributes related to physical addresses, including street, city, state, and postal code. | Employee, Company                     | Country                            | 12                  |
| Contract           | Contract            | This entity represents a contract within the organization, including details such as start and end dates, and reasons for leaving. | ContractCostCenter                    | Employee, Division, ContractType   | 6                   |
| Company            | Company             | This entity contains attributes related to companies, such as name, address, and contact information. | Domain, Address                       | Country                            | 3                   |
| Division           | Division            | This entity is used to define various divisions, which can be referenced in other entities. | Contract                              | Region                             | 2                   |
| Region             | Region              | This entity is used to define various regions, which can be referenced in other entities. | Division                              | Domain                             | 4                   |
| Domain             | Domain              | This entity is used to define various domains, which can be referenced in other entities. | Region                                | Company                            | 2                   |
| ContractCostCenter | Contract Cost Center| This entity is used to link contracts with their respective cost centers, allowing for better financial tracking and management. | (none)                       | Contract, CostCenter               | 1                   |
| ContractType       | Contract Type       | This entity is used to define various contract types, which can be referenced in the Contract entity. | Contract                              | (none)                    | 3                   |
| CostCenter         | Cost Center         | This entity is used to define various cost centers, which can be referenced in other entities. | ContractCostCenter                     | (none)                    | 2                   |
| Country            | Country             | This entity is used to define various countries, which can be referenced in other entities. | Address, Company                       | (none)                    | 9                   |
| Gender             | Gender              | This entity is used to define Gender types, which can be referenced in other entities. | Employee                               | (none)                    | 3                   |
| JobRole            | Job Role            | This entity is used to define various job roles, which can be referenced in other entities. | (none)                        | (none)                    | 2                   |
| Position           | Position            | This entity is used to define various positions, which can be referenced in other entities. | Employee                               | (none)                    | 3                   |
| Study              | Study               | This entity is used to define various studies, which can be referenced in other entities. | Employee                               | (none)                    | 2                   |

# Entity Attributes

## Employee
| Attribute name      | Attribute label      | Data type                                   | Mandatory? | Description                                      | Used in matching |
|--------------------|---------------------|----------------------------------------------|------------|--------------------------------------------------|------------------|
| ID                 | ID                  | LongInteger                                  | Yes        | MDM identifier of the employee                   | No               |
| FirstName          | First Name          | String                                       | No         | An employee given name                           | No               |
| LastName           | Last Name           | String                                       | Yes        | An employee's surname                            | No               |
| PhoneticFirstName  | Phonetic First Name | String                                       | No         | First name transformed using the phonetic metaphone algorithm | Yes              |
| PhoneticLastName   | Phonetic Last Name  | String                                       | No         | Last name transformed using the phonetic metaphone algorithm  | Yes              |
| NormalizedFirstName| Normalized First Name| String                                       | No         | Normalized first name for matching               | Yes              |
| NormalizedLastName | Normalized Last Name| String                                       | No         | Normalized last name for matching                | Yes              |
| Nickname           | Nickname            | String                                       | No         | Most common nickname for this given name–used for matching | Yes              |
| MemberID           | Member ID           | String                                       | No         | Internal or national identifier of the employee  | Yes              |
| DateOfBirth        | Date of Birth       | Date                                         | No         | Date of birth of the employee                    | Yes              |
| NormalizedStreet   | Normalized Street   | String                                       | No         | Normalized street address for matching           | Yes              |
| NormalizedCity     | Normalized City     | String                                       | No         | Normalized city name for matching                | Yes              |
| NormalizedState    | Normalized State    | String                                       | No         | Normalized state name for matching               | Yes              |
| SourceEmail        | Source Email        | String                                       | Yes        | Employee email address before cleansing          | No               |
| CleansedEmail      | Cleansed Email      | String                                       | No         | Employee email address after cleansing           | Yes              |
| ValidEmailDomain   | Valid Email Domain  | String                                       | No         | Valid email domain flag                          | No               |
| SourcePhone        | Source Phone        | String                                       | No         | Employee phone number                            | No               |
| StandardizedPhone  | Standardized Phone  | String                                       | No         | Employee phone number after standardization      | Yes              |
| PhoneGeocodingData | Phone Geocoding Data| String                                       | No         | Geocoding data for the phone number              | No               |
| EmployeeType       | Employee Type       | Organization.list_of_values.EmployeeType      | No         | Type of employee                                 | No               |
| Address            | Address             | Organization.complex_types.SourceAddressType  | No         | Employee address                                 | No               |

## Address
| Attribute name      | Attribute label      | Data type   | Mandatory? | Description                        | 
|---------------------|---------------------|------------|------------|------------------------------------|
| AddressID           | Address ID          | LongInteger| Yes        | Unique identifier for the address  |
| Number              | Number              | String     | Yes        | House or building number           | 
| EnrichedNumber      | Enriched Number     | String     | No         | Enriched house or building number  |
| Street              | Street              | String     | Yes        | Street name                        |
| EnrichedStreet      | Enriched Street     | String     | No         | Enriched street name               |
| City                | City                | String     | Yes        | City name                          |
| EnrichedCity        | Enriched City       | String     | No         | Enriched city name                 |
| State               | State               | String     | No         | State or province name             |
| ZipCode             | Zip Code            | String     | No         | Postal code                        | 
| Latitude            | Latitude            | Decimal    | No         | Geographic latitude                |
| Longitude           | Longitude           | Decimal    | No         | Geographic longitude               | 

## Contract
| Attribute name      | Attribute label      | Data type   | Mandatory? | Description                        |
|---------------------|---------------------|------------|------------|------------------------------------|
| ContractID          | Contract ID         | LongInteger| Yes        | Unique identifier for the contract |
| ContractRef         | Contract Reference  | String     | Yes        | Internal contract reference        |
| IsMain              | Is Main             | Boolean    | No         | Indicates if this is the main contract |
| StartDate           | Start Date          | Date       | Yes        | Start date of the contract         |
| EndDate             | End Date            | Date       | Yes        | End date of the contract           |
| TerminationReason       | Termination Reason      | String     | No         | Reason for terminating the contract    |

## Company
| Attribute name | Attribute label | Data type   | Mandatory? | Description                        | Documentation                  |
|---------------|----------------|------------|------------|------------------------------------|-------------------------------|
| CompanyID     | Company ID     | LongInteger| Yes        | Unique identifier for company      | Unique identifier for company  |
| Name          | Company name   | LongInteger| No         | Name of the company                | Name of the company           |
| Description   | Company description | String | No | Description of the company | Description of the company |

## Division
| Attribute name | Attribute label | Data type   | Mandatory? | Description                        | Documentation                  |
|---------------|----------------|------------|------------|------------------------------------|-------------------------------|
| DivisionID    | Division ID    | LongInteger| Yes        | Unique identifier for division     | Primary key for Division entity|
| Name          | Name           | String     | Yes        | Name of the division               | Name of the division          |

## Region
| Attribute name     | Attribute label     | Data type   | Mandatory? | Description                        | Documentation                  |
|--------------------|--------------------|------------|------------|------------------------------------|-------------------------------|
| RegionID           | Region ID          | LongInteger| Yes        | Unique identifier for region       | Primary key for Region entity  |
| RegionName         | Region Name        | String     | No         | Name of the region                 | Name of the region            |
| RegionDescription  | Region Description | String     | No         | Description of the region          | Detailed description of region |
| RegionCode         | Region Code        | String     | No         | Code for the region                | Code for the region           |

## Domain
| Attribute name | Attribute label | Data type   | Mandatory? | Description                        | Documentation                  |
|---------------|----------------|------------|------------|------------------------------------|-------------------------------|
| DomainID      | Domain ID      | LongInteger| Yes        | Unique identifier for domain       | Primary key for Domain entity  |
| Name          | Name           | String     | Yes        | Name of the domain                 | Name of the domain            |

## ContractCostCenter
| Attribute name        | Attribute label        | Data type   | Mandatory? | Description                        | Documentation                  |
|----------------------|-----------------------|------------|------------|------------------------------------|-------------------------------|
| ContractCostCenterID | Contract Cost Center ID| LongInteger| Yes        | Unique identifier                  | Primary key for ContractCostCenter |

## ContractType
| Attribute name   | Attribute label   | Data type   | Mandatory? | Description                        | Documentation                  |
|------------------|------------------|------------|------------|------------------------------------|-------------------------------|
| ContractTypeID   | Contract Type ID | LongInteger| Yes        | Unique identifier for contract type| Primary key for ContractType entity |
| Name             | Name             | String     | Yes        | Name of the contract type          | Name of the contract type      |
| Description      | Description      | String     | No         | Description of the contract type   | Additional info about contract type |

## CostCenter
| Attribute name | Attribute label | Data type   | Mandatory? | Description                        | Documentation                  |
|---------------|----------------|------------|------------|------------------------------------|-------------------------------|
| CostCenterID  | Cost Center ID | LongInteger| Yes        | Unique identifier for cost center  | Primary key for CostCenter entity |
| Name          | Name           | String     | Yes        | Name of the cost center            | Name of the cost center        |

## Country
| Attribute name   | Attribute label           | Data type | Mandatory? | Description                        | Documentation                  |
|------------------|--------------------------|-----------|------------|------------------------------------|-------------------------------|
| ID               | ID                       | String    | Yes        | Unique identifier for country      | Primary key for Country entity |
| Alpha2Code       | ISO 3166-1 2-Letter Code | String    | No         | Two-letter code for country        | ISO 3166 Country Codes         |
| Alpha3Code       | ISO 3166-1 3-Letter Code | String    | No         | Three-letter code for country      | ISO 3166 Country Codes         |
| NumericCode      | ISO 3166-1 Numeric Code  | String    | No         | Numeric code for country           | ISO 3166 Country Codes         |
| URLWikipedia     | Wikipedia URL            | String    | No         | URL to Wikipedia page              | Wikipedia URL for country      |
| LocalShortName   | Local Short Name         | String    | No         | Local short name of country        | Local short name of country    |
| EnglishShortName | English Short Name       | String    | No         | English short name of country      | English short name of country  |
| EnglishFullName  | English Full Name        | String    | No         | English full name of country       | English full name of country   |

## Gender
| Attribute name | Attribute label | Data type   | Mandatory? | Description                        | Documentation                  |
|---------------|----------------|------------|------------|------------------------------------|-------------------------------|
| GenderID      | Gender ID      | LongInteger| Yes        | Unique identifier                  | Primary key for Gender entity  |
| Label         | Label          | String     | Yes        | Label                              | Label for Gender               |
| Code          | Code           | String     | Yes        | Code                               | Code for Gender                |

## JobRole
| Attribute name | Attribute label | Data type   | Mandatory? | Description                        | Documentation                  |
|---------------|----------------|------------|------------|------------------------------------|-------------------------------|
| JobRoleID     | Job Role ID    | LongInteger| Yes        | Unique identifier for job role     | Primary key for JobRole entity |
| Label         | Label          | String     | Yes        | Label for job role                 | Label for job role             |

## Position
| Attribute name | Attribute label | Data type   | Mandatory? | Description                        | Documentation                  |
|---------------|----------------|------------|------------|------------------------------------|-------------------------------|
| PositionID    | Position ID    | LongInteger| Yes        | Unique identifier for position     | Primary key for Position entity|
| Name          | Name           | String     | Yes        | Name of the position               | Name of the position           |
| Description   | Description    | String     | No         | Description of the position        | Detailed description of position|

## Study
| Attribute name | Attribute label | Data type   | Mandatory? | Description                        | Documentation                  |
|---------------|----------------|------------|------------|------------------------------------|-------------------------------|
| StudyID       | Study ID       | LongInteger| Yes        | Unique identifier for study        | Primary key for Study entity   |
| Name          | Name           | String     | Yes        | Name of the study                  | Name of the study              |