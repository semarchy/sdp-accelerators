# Enrichers Documentation

This table summarizes the enrichers defined in the model, including their entity, name, type, label, description, enriched attribute, and expression.

| Entity name | Enricher name | Enricher type | Enricher label | Enricher description | Enriched attribute | Enricher expression |
|-------------|---------------|---------------|----------------|----------------------|--------------------|---------------------|
| Account     | AccountKey    | SemQLEnricher | Account Key    | Enriches the Account entity with a unique key based on the Routing Number and Account Number. | AccountKey         | Fund.ChainID &#124;&#124; '~' &#124;&#124; Portfolio.ChainID &#124;&#124; '~' &#124;&#124; ChainID |
| Account     | AccountName   | SemQLEnricher | Account Name   | Enriches the Account entity with a unique name based on the Legal Entity and Bank. | AccountKey         | FDN_LegalEntity &#124;&#124; '~' &#124;&#124; FDN_Bank |
| Contact     | AutopopulateFullName | SemQLEnricher | Autopopulate Full Name | Populates the FullName attribute by concatenating FirstName and LastName. | FullName           | FirstName &#124;&#124; ' ' &#124;&#124; LastName |
| Contact     | AutopopulateSitePhone | SemQLEnricher | Autopopulate Site Phone | Populates the Phone attribute with the standardized phone from the related Site. | Phone              | Site.StandardizedPhone |
| LegalEntity | AutopopulateCurrency | SemQLEnricher | Autopopulate Currency | Populates the Currency attribute based on the Country (e.g., USD for US). | FID_Currency       | case  when FID_Country = 'US' then 'USD' else null end |
| LegalEntity | NormalizeEntityName | SemQLEnricher | Normalize Entity Name | Normalizes the entity name by trimming and converting to uppercase. | NormalizedName     | RTRIM(LTRIM(UPPER(Name))) |
| LegalEntity | PopulateType   | SemQLEnricher | Autopopulate Type | Populates the Entity Type based on the Name pattern. | FID_EntityType     | case when  REGEXP_LIKE(Name, '[PSG]{3}') then 'Internal' else 'Investor' end |
| LegalEntity | ReplaceSingleQuotation | SemQLEnricher | Replace Single Quotation | Replaces specific substrings in the Name (e.g., 'KKR' with 'Kohlberg Kravis Roberts'). | NormalizedName     | REGEXP_REPLACE(Name, 'KKR', 'Kohlberg Kravis Roberts') |
| LegalEntity | SetStatusActive | SemQLEnricher | Set Status 'Active' | Sets the Status attribute to 'Active'. | FID_Status         | Case when 1=1 then 'Active' else null end |
| LegalEntity | SetStatusDraft | SemQLEnricher | Set Status Draft | Sets the Status attribute to 'Draft'. | FID_Status         | Case when 1=1 then 'Draft' else null end |
| LegalEntity | SetStatusPendingValidation | SemQLEnricher | Set Status Pending Validation | Sets the Status attribute to 'Pending Validation'. | FID_Status         | Case when 1=1 then 'Pending Validation' else null end |
| Portfolio   | PortfolioName  | SemQLEnricher | Portfolio Name  | Populates the Portfolio Name by combining Fund and Industry. | Name               | FDN_Fund &#124;&#124; ' ' &#124;&#124; FDN_Industry |
| Site        | NormalizedName | SemQLEnricher | Normalize Site Name | Normalizes the site name by trimming and converting to uppercase. | NormalizedName     | RTRIM(LTRIM(UPPER(Name))) |
