# Corporate Finance Accelerator - Enrichers

This page summarizes the enrichers defined in the Corporate Finance Accelerator. Use it to understand what is automated, which attributes are enriched, and which plugins or expressions are required.

Notes:
- Labels reflect the model configuration.
- Java plugin enrichers typically require the relevant plugin to be available in the runtime environment.
- SemQL enrichers execute in the model pipeline and do not require external services.

Related pages:
- [model structure](./model_structure.md)
- [user guide](./user_guide.md)

This table summarizes the enrichers defined in the Corporate Finance model, including their entity, name, type, label, description, enriched attribute, and expression or plugin.

| Entity name | Enricher name | Enricher type | Enricher label | Enricher description | Enriched attribute | Enricher expression / Plugin |
|---|---|---|---|---|---|---|
| Account | NormalizeAccount | SemQLEnricher | Normalize Account |  | `NormalizedAccountCode`, `NormalizedAccountName` | `RTRIM(LTRIM(UPPER(AccountCode)))`; `RTRIM(LTRIM(UPPER(AccountName)))` |
| Address | NormalizeAddress | SemQLEnricher | Normalize Address |  | `NormalizedCity`, `NormalizedRegion`, `NormalizedPostalCode` | `RTRIM(LTRIM(UPPER(City)))`; `RTRIM(LTRIM(UPPER(Region)))`; `RTRIM(LTRIM(UPPER(PostalCode)))` |
| BankAccount | NormalizeBankAccount | SemQLEnricher | Normalize Bank Account |  | `NormalizedIBAN`, `NormalizedSWIFT` | `RTRIM(LTRIM(UPPER(IBAN)))`; `RTRIM(LTRIM(UPPER(SWIFT)))` |
| ChartOfAccounts | NormalizeChartOfAccounts | SemQLEnricher | Normalize Chart Of Accounts |  | `NormalizedName` | `RTRIM(LTRIM(UPPER(Name)))` |
| Counterparty | NormalizeCounterparty | SemQLEnricher | Normalize Counterparty |  | `NormalizedLegalName`, `NormalizedTaxID` | `RTRIM(LTRIM(UPPER(LegalName)))`; `RTRIM(LTRIM(UPPER(TaxID)))` |
| Counterparty | PhonetizeCounterparty | JavaPluginEnricher | Phonetize Counterparty Legal Name |  | `PhonetizedLegalName` | `plugin: com.semarchy.engine.plugins.convergence.text` |
| CounterpartyGroup | NormalizeCounterpartyGroup | SemQLEnricher | Normalize Counterparty Group |  | `NormalizedGroupName`, `NormalizedDUNSNumber` | `RTRIM(LTRIM(UPPER(GroupName)))`; `RTRIM(LTRIM(UPPER(DUNSNumber)))` |
| CounterpartyGroup | PhonetizeCounterpartyGroup | JavaPluginEnricher | Phonetize Counterparty Group Name |  | `PhonetizedGroupName` | `plugin: com.semarchy.engine.plugins.convergence.text` |
| Country | NormalizeCountry | SemQLEnricher | Normalize Country |  | `NormalizedCountryCode`, `NormalizedCountryName`, `NormalizedISOAlpha2`, `NormalizedISOAlpha3` | `RTRIM(LTRIM(UPPER(CountryCode)))`; `RTRIM(LTRIM(UPPER(CountryName)))`; `RTRIM(LTRIM(UPPER(ISOAlpha2)))`; `RTRIM(LTRIM(UPPER(ISOAlpha3)))` |
| Currency | NormalizeCurrency | SemQLEnricher | Normalize Currency |  | `NormalizedCurrencyCode`, `NormalizedCurrencyName` | `RTRIM(LTRIM(UPPER(CurrencyCode)))`; `RTRIM(LTRIM(UPPER(CurrencyName)))` |
| Customer | NormalizeCustomer | SemQLEnricher | Normalize Customer Payment Terms |  | `NormalizedPaymentTerms` | `RTRIM(LTRIM(UPPER(PaymentTerms)))` |
| MappingRule | NormalizeMappingRule | SemQLEnricher | Normalize Mapping Rule |  | `NormalizedRuleName`, `NormalizedRuleType` | `RTRIM(LTRIM(UPPER(RuleName)))`; `RTRIM(LTRIM(UPPER(RuleType)))` |
| MappingSet | NormalizeMappingSet | SemQLEnricher | Normalize Mapping Set |  | `NormalizedMappingSetName` | `RTRIM(LTRIM(UPPER(MappingSetName)))` |
| OrgHierarchy | NormalizeOrgHierarchy | SemQLEnricher | Normalize Org Hierarchy |  | `NormalizedName`, `NormalizedHierarchyType` | `RTRIM(LTRIM(UPPER(Name)))`; `RTRIM(LTRIM(UPPER(HierarchyType)))` |
| OrgUnit | NormalizeOrgUnit | SemQLEnricher | Normalize Org Unit |  | `NormalizedOrgUnitBusinessCode`, `NormalizedOrgUnitName` | `RTRIM(LTRIM(UPPER(OrgUnitBusinessCode)))`; `RTRIM(LTRIM(UPPER(OrgUnitName)))` |
| OrgUnit | PhonetizeOrgUnit | JavaPluginEnricher | Phonetize Org Unit Name |  | `PhonetizedOrgUnitName` | `plugin: com.semarchy.engine.plugins.convergence.text` |
| OrgUnitCoAAssignment | NormalizeOrgUnitCoAAssignment | SemQLEnricher | Normalize Org Unit CoA Assignment |  | `NormalizedUsageScope` | `RTRIM(LTRIM(UPPER(UsageScope)))` |
| OrgUnitMappingCoverage | NormalizeOrgUnitMappingCoverage | SemQLEnricher | Normalize Org Unit Mapping Coverage |  | `NormalizedCoverageScope` | `RTRIM(LTRIM(UPPER(CoverageScope)))` |
| Region | NormalizeRegion | SemQLEnricher | Normalize Region |  | `NormalizedRegionName`, `NormalizedISOCode` | `RTRIM(LTRIM(UPPER(RegionName)))`; `RTRIM(LTRIM(UPPER(ISOCode)))` |
| RiskComplianceProfile | NormalizeRiskComplianceProfile | SemQLEnricher | Normalize Risk Compliance Profile |  | `NormalizedRiskCategory` | `RTRIM(LTRIM(UPPER(RiskCategory)))` |
| Supplier | NormalizeSupplier | SemQLEnricher | Normalize Supplier Payment Terms |  | `NormalizedPaymentTerms` | `RTRIM(LTRIM(UPPER(PaymentTerms)))` |

You can extend these enrichers to apply your specific transformation and standardization rules. For a full list of entities and attributes, refer to the [model structure page](./model_structure.md).
