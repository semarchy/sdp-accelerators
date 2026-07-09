# Corporate Finance Accelerator - User Guide

The Corporate Finance model is a finance master data application that consolidates counterparties, organizational structures, charts of accounts, and mapping assets into a unified, governed view. It supports stewardship workflows, duplicate review for counterparties, controlled approval for organization changes, managed local-to-group account mappings for reporting alignment, and dashboard-based monitoring of key data quality and completeness signals.

Use this guide by persona so each role can focus on the most relevant workflows and screens.

Related pages:
- [model structure](./model_structure.md)
- [enrichers](./enrichers.md)
- [validations](./validations.md)

## Personas and goals

### Data Steward
Focus: correct and enrich operational master data before it is consumed by finance and governance processes.

Typical tasks:
- Review, confirm, and resolve potential counterparty duplicates.
- Propose organizational changes to reflect acquisitions, reorganizations, or reporting-structure updates.
- Maintain counterparty and related 360 data such as addresses, contacts, bank accounts, and risk/compliance details.

Key activities and screens:
- `Counterparties: Confirm Matches`
- `Counterparties: Review Suggestions`
- `Add Org Unit`
- `Author Counterparties`, `Author Org Units`, `Author Addresses`, `Author Bank Accounts`

### Finance Controller
Focus: approve organizational changes and maintain chart-of-accounts alignment for group reporting.

Typical tasks:
- Review and approve stewarded org unit changes from `My Tasks`.
- Maintain charts of accounts, accounts, mapping sets, and account mappings.
- Review unmapped or incomplete mapping coverage and complete missing mappings.
- Validate that local statutory accounts roll correctly into group reporting structures.

Key activities and screens:
- `Add Org Unit` approval task
- `Author Account Mappings`
- `Author Mapping Sets`
- `Author Charts Of Accounts`, `Author Accounts`, `Author Mapping Rules`

### Transformation / Governance Lead
Focus: ensure traceability, data quality, and adherence to standards for the Corporate Finance Data Product.

Typical tasks:
- Review workflow history and ownership of key data changes.
- Monitor dashboards and data quality indicators.
- Identify incomplete or non-compliant records requiring remediation.
- Direct operational teams back to source records that need correction.

Key focus areas:
- Workflow administration and task traceability
- Governance dashboards
- Incomplete or exception records surfaced from stewardship and finance domains

## Model at a glance

Core sub-models:
- Organizational Structure: `OrgUnit`, `OrgHierarchy`, `OrgHierarchyNode`, and related assignment/coverage entities.
- CoA and Mappings: `ChartOfAccounts`, `Account`, `MappingSet`, `AccountMapping`, `MappingRule`, `SplitAllocation`.
- Counterparty Domain: `Counterparty`, `CounterpartyGroup`, `Customer`, `Supplier`, `BankAccount`, `RiskComplianceProfile`.
- Reference and Time: `Country`, `Currency`, `Region`, `FiscalCalendar`, `FiscalPeriod`, `TaxCode`, `CostType`, `StatusCode`.

Primary navigation groups in the application:
- `Our Organizations`
- `Charts of Accounts`
- `Counterparties`
- `Data Stewardship`

For a detailed list of entities and attributes, see [model structure](./model_structure.md).

## Dashboards and analytics

The accelerator includes dashboard elements for both monitoring and remediation.

At a high level, these dashboards help users:

- stewards can spot quality gaps before reviewing records one by one
- controllers can see which local accounts are still unmapped before completing finance mappings
- governance users can combine workflow traceability with dashboard signals to direct remediation back to the right team

Current accelerator scope:

- the delivered dashboard assets focus on the two most immediate operational needs in this accelerator: counterparty monitoring/data quality and finance mapping completeness
- broader governance or cross-domain oversight views can be added as needed for more specific customer use cases without changing the underlying model foundation

## Common journey by persona

### Data Steward
1. Open `Data Stewardship` to review duplicate suggestions and confirm potential matches.
2. Correct or enrich counterparty data where needed.
3. Create new organizational units through the governed workflow.
4. Submit changes for approval instead of publishing structural changes directly.

### Finance Controller
1. Open approval tasks from `My Tasks` or workflow notifications.
2. Review org unit and hierarchy changes submitted by stewards.
3. Open `Charts of Accounts` -> `Accounts & Mappings` to inspect mapping sets and account mappings.
4. Open a mapping set and review the embedded `UnmappedAccounts` chart to identify missing mappings.
5. Complete or adjust local-to-group mappings so reporting remains aligned.

### Transformation / Governance Lead
1. Review workflow traceability for key organizational and finance changes.
2. Use the delivered dashboards and quality views to assess data quality and completeness within the current accelerator scope.
3. Identify incomplete records and route remediation back to the operational team.

## Data quality and enrichment

The model includes:
- Fuzzy matching and stewardship review for counterparties.
- Workflow-based approval for organizational changes.
- Enrichers for normalization and phoneticization across key master-data entities.
- Validations that enforce explicit business rules plus mandatory and referential checks during authoring.
- A data quality dashboard layer, currently focused on counterparty metrics and completeness indicators.

Details:
- Enrichers: [enrichers](./enrichers.md)
- Validations: [validations](./validations.md)

## UI import note

Some UI import files include date fields and require an explicit date format during import.

For those files, use:
- `dd-MM-yyyy`

Example:
- [07-FiscalCalendar.csv](c:/Users/romdarts/git/Accelerators/AL-CorpFin/sdp-ps-accelerators/use-case-models/CorporateFinance/resources-WIP/demo-data-WIP/UI%20Import-WIP/07-FiscalCalendar.csv) uses values such as `01-01-2025` and `31-12-2025`, so the import format must be set to `dd-MM-yyyy`.

## Tips for success

- Start with the navigation group aligned to your role or domain of interest: stewardship, organizations, counterparties, or charts of accounts.
- Resolve counterparty quality issues early so downstream org and finance processes work on trusted records.
- Keep charts of accounts and mapping sets aligned to reporting needs before loading new local data.
- Use workflow traceability and dashboards together: one explains who changed data, the other shows where quality gaps still remain.
