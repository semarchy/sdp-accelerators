# Private Equity Accelerator - User Guide

The Private Equity model is an MDM accelerator for governing fund, portfolio, legal entity, relationship, role, location, document, and account data used by private-equity teams. The model creates golden legal entity records, links them to private-equity structures, applies data quality and enrichment rules, supports duplicate review, and provides governed workflow for both legal entity changes and portfolio assignment changes.

The delivered application is `Private Equity`. It is organized around legal entity stewardship, fund and portfolio navigation, reference data management, relationship join tables, workflow tasks, data quality worklists, and embedded documentation.

Current validated demo anchors:

| Area | Record |
| --- | --- |
| Fund | `Asia Growth Fund` |
| Current / alternate portfolios | `Asia Growth Fund Software Development`, `Asia Growth Fund Healthcare` |
| Investment vehicle | `Apex Data Services LLC` |
| Fund manager / relationship context | `Northstar Capital GP I, LP` |
| Portfolio workflow | `Portfolio Change Approval` |

Related pages:
- [model structure](./model_structure.md)
- [enrichers](./enrichers.md)
- [validations](./validations.md)

## Personas and goals

### Portfolio Data Steward
Focus: review portfolio context and request governed changes to portfolio assignments.

Typical tasks:
- Start from `Funds` and navigate through `Asia Growth Fund` to the relevant portfolio.
- Review the investment vehicle in the Legal Entity 360 view.
- Confirm source consolidation in `MASTER DATA`.
- Start `Request Portfolio Change` from the selected portfolio assignment.
- Propose the target portfolio and send the request for approval.

Key activities and screens:
- `Funds`, Legal Entity 360, `Portfolio Assignments`
- `Portfolio Change` form
- Workflow role `DataSteward`

### Portfolio Approver
Focus: review and approve governed portfolio assignment changes.

Typical tasks:
- Open the routed approval task from `Team To Do`.
- Start the task using `Action > Start`.
- Compare `Current Assignment` and `Proposed Assignment`.
- Approve, send back, or reject the proposed move.
- Let publication run in the background and validate the result from the fund hierarchy.

Key activities and screens:
- `Team To Do`
- `Approve Portfolio Change`
- Workflow role `BusinessUser`

### Legal Team
Focus: initiate new legal entity records, maintain core legal identity and location information, and submit records into the governance workflow.

Typical tasks:
- Create new legal entity records or start edits on active legal entities.
- Maintain legal name, entity type, status, structure, address, country, state, and geography classification.
- Attach supporting comments and documents when starting workflow actions.
- Submit records to Accounting and Tax for parallel completion.

Key activities and screens:
- `Legal Entities`, `My Tasks`, `Import LEs`
- Workflow stepper `Workflowstep1Legal`
- Legal entity forms and location tabs

### Accounting Team
Focus: enrich the legal entity with accounting and investment classification data.

Typical tasks:
- Complete accounting-owned classifications such as category, subcategory, strategy, currency, and fiscal-year information.
- Review legal team information as read-only context while editing accounting-owned fields.
- Submit the accounting branch of the workflow so the record can move toward final approval.

Key activities and screens:
- `My Tasks`, `Legal Entities`
- Workflow stepper `Workflowstep2Accounting`
- Reference data for currencies, categories, subcategories, strategies, and entity structures

### Tax Team
Focus: maintain tax identifiers, tax software flags, tax-year indicators, names, and tax documents.

Typical tasks:
- Complete US FEIN and tax processing attributes.
- Maintain alternate legal entity names and tax form documents.
- Validate US FEIN format and tax document relationships before approval.
- Submit the tax branch of the workflow in parallel with Accounting.

Key activities and screens:
- `My Tasks`, `Legal Entities`, `Documents`, `Names`
- Workflow stepper `Workflowstep3Tax`
- Reference data for forms, name types, fiscal-year values, and yes/no tax flags

### Relationship and Investment Steward
Focus: maintain the relationship context around legal entities.

Typical tasks:
- Manage parent-child relationships between legal entities.
- Maintain complex relationship types such as GP, LP, stockholder, or member relationships through the relationship join tables.
- Group legal entities for investment purposes and maintain group hierarchy, inception, start, end, strategy, investment structure, and currency information.
- Link funds and portfolios to legal entities with the correct entity role.

Key activities and screens:
- `Relationships`, `Parent Children`, `LE Relationships`, `Group Hierarchies`, `Group Legal Entities`
- `LE Groups`, `Funds`, `Portfolio Legal Entities`, `Fund LEs`

### Data Steward and MDM Administrator
Focus: monitor data quality, duplicate suggestions, source survivorship, integration loads, and reference data completeness.

Typical tasks:
- Review legal entity errors and duplicate suggestions.
- Maintain reference data used by authoring and validation.
- Run or monitor the `ALL_LE` and `INTEGRATE_ALL` model jobs for integration loads and workflow publication.
- Review publisher survivorship behavior across Salesforce, Investran, EntityHub, GENEVA, and TAX sources.

Key activities and screens:
- `LE Errors`, `xDM Database`, `Reference Data`, `Data Stewardship`
- Duplicate manager `ManageDuplicatesOnLegalEntity`
- Model jobs `ALL_LE` and `INTEGRATE_ALL`

## Model at a glance

Core domains:
- Legal Entity Core: mastered legal entities, offices, contacts, alternate names, tax documents, and tax forms.
- Relationships and Hierarchies: parent-child legal entity hierarchy, complex legal entity relationships, legal entity groups, group hierarchy, and group membership.
- Funds, Portfolios, and Accounts: funds, portfolios, fund/legal entity roles, portfolio/legal entity roles, bank/custodian accounts, account types, and banks.
- Reference Data and Classification: entity type, status, structure, category, subcategory, strategy, industry, geography, region, country, state, and currency reference data.

Primary navigation groups in the `Private Equity` application:
- `Legal Entities`: LE Groups, Legal Entities, Funds, and Bank / Custodian Accounts.
- `Reference Data`: Industry RDM and Corporate RDM reference data.
- `Data Stewardship`: import actions and legal entity error worklists.
- `Relationships`: join tables for portfolio legal entities, parent children, group hierarchies, LE relationships, fund LEs, documents, group legal entities, and names.
- `Documentation`: the embedded demo guide PDF.

For a detailed list of entities and attributes, see [model structure](./model_structure.md).

## Common journey by persona

### Govern a portfolio assignment change
1. Open the `Private Equity` application.
2. Open `Funds`, expand `Asia Growth Fund`, and open the current portfolio containing `Apex Data Services LLC`.
3. Open Apex in the Legal Entity 360 view and review the business-facing profile.
4. Open `MASTER DATA` to confirm the source records consolidate into one golden Apex record.
5. Review `LOCATION`, `OFFICES`, and `PARENTS` as supporting operational and relationship context.
6. Open `Portfolio Assignments`, select the assignment row, and choose `Request Portfolio Change`.
7. Enter a short business comment for the request.
8. In the `Portfolio Change` form, review `Current Assignment`, choose the `New Portfolio`, and send for approval.
9. As the approver persona, expand `Team To Do`, select the Apex task, and choose `Action > Start`.
10. Review the proposed change, approve it, and run the publication step in the background.
11. Validate the result from the fund hierarchy. If Apex moved from Software Development to Healthcare, `Asia Growth Fund Healthcare` should show `Apex Data Services LLC`.

For repeat demos, reverse the direction if Apex is already in Healthcare: move it back to Software Development using the same workflow.

### Create a new legal entity
1. Open the `Private Equity` application.
2. Start the `Legal Entity Workflow` from an empty selection using the create action available to the Legal role.
3. Enter core legal entity data in the Legal step, including name, type, status, location, and legal classification fields.
4. Let real-time enrichers normalize the name, geocode the address, populate entity type, and default currency where configured.
5. Submit the draft. Non-critical records move into the parallel Accounting and Tax branch; critical records route directly to approval.
6. Accounting and Tax complete their respective tasks in parallel.
7. The approver reviews all submitted data, can ask for a fix, cancel, or submit the record to the golden data set.

### Edit an existing legal entity
1. Open an active golden legal entity record.
2. Start the edit workflow from selection.
3. Update the allowed fields in the authoring step.
4. Send the proposed edits for approval.
5. The approver reviews the suggested state against the existing state, then approves or cancels the changes.

### Review the legal entity 360 view
1. Open `Legal Entities` and search for the entity.
2. Review the mastered legal identity, location, status, category, entity type, and tax fields.
3. Traverse related offices and contacts to understand operational points of presence.
4. Review alternate names and tax documents for the entity.
5. Use parent-child and LE relationship screens to understand ownership, GP/LP, member, stockholder, or other relationship context.

### Govern groups, funds, portfolios, and roles
1. Use `LE Groups` to manage investment-oriented groupings of legal entities.
2. Use `Group Legal Entities` to add participating legal entities to groups.
3. Use `Group Hierarchies` to connect parent and child groups with currency context.
4. Use `Funds`, `Portfolio Legal Entities`, and `Fund LEs` to describe where a legal entity participates in fund-level and portfolio-level structures.
5. Use `Entity Roles` to maintain the allowed role values for these relationships.

## Data quality and enrichment

The model includes:
- Fuzzy matching on legal entities using exact FEIN, exact normalized name plus geocoded address, and exact name rules.
- Duplicate review through `ManageDuplicatesOnLegalEntity`.
- Address geocoding for legal entities and offices through the Google Maps plugin.
- Name normalization for legal entities and offices.
- Phone and email cleansing for contacts and offices.
- Tax and format validations for US FEIN, SSN, account number, routing number, and leading special characters in legal entity names.
- Post-consolidation unique keys for legal entity US FEIN, normalized name, and chain ID, plus unique keys for fund, portfolio, and contact identifiers.
- Survivorship rules that prioritize source publishers for chain ID, tax attributes, default attributes, and most-frequent classification values.

Details:
- Enrichers: [enrichers](./enrichers.md)
- Validations: [validations](./validations.md)

## Workflow details

### Portfolio Change Approval

The validated portfolio-forward workflow is `PortfolioChangeApproval`, labelled `Portfolio Change Approval`.

Path:
- `Start Portfolio Change` starts from a selected golden `PortfolioLegalEntity` record and requires the `DataSteward` role.
- `Request Portfolio Change` uses the `ApprovePortfolioChange` stepper and `Portfolio Change` form.
- The requester reviews `Current Assignment`, proposes `New Portfolio`, and chooses `Send For Approval`.
- `Approve Portfolio Change` is assigned to the `BusinessUser` role.
- The approver reviews the same current/proposed assignment layout and chooses `Approve`, `Send Back`, or `Reject`.
- `Apply Portfolio Change` publishes through `INTEGRATE_ALL`.

The publication step can take around two minutes in the demo environment. Use `Run in the background` and validate the final state from the fund hierarchy.

### Legal Entity Workflow

The delivered workflow is `CreateOrEditLegalEntity`.

Create path:
- `Start Create` opens the new record workflow and supports comments, attachments, priority, due dates, and descriptions.
- `New Legal Entity` is assigned to the workflow initiator and requires the `Legal` role.
- `Submit Draft` submits the legal draft.
- `Critical Creation` routes critical records directly to approval and non-critical records to the parallel branch.
- `Parallel Actions` creates Accounting and Tax tasks at the same time.
- `Pending Validation` submits the draft as `semadmin` after both branches complete.
- `Approve` lets the approver submit, cancel, or ask for a fix.
- `Active` submits the record into the active golden state.

Edit path:
- `Start Edit` is available from golden data when `FDN_Status='Active'`.
- `Edit Legal Entity` lets the initiator propose edits.
- `Approve Edits` lets an approver compare and approve the suggested changes.

## Demo data and import note

The active demo import payload is `resources/demo-data/curl-import/PrivateEquity_AllPhases_Load.json`. Current local command notes remain in `resources/demo-data/curl-import/RM_commands PE.md`.

Generated phased payloads and legacy SQL files have been moved to `Archive/` and should not be treated as the active import path.

The model includes integration model jobs `ALL_LE` and `INTEGRATE_ALL`, which process reference data, legal entities, documents, relationships, funds, portfolios, groups, offices, contacts, portfolio assignments, and accounts. The `Portfolio Change Approval` workflow uses `INTEGRATE_ALL` for publication.

The delivered use-case PDF is archived as source material. The current demo guide is the refreshed detailed demo script and recording talk track under `Archive/accelerator-work/`.

## Tips for success

- Start with the workflow when demonstrating governed creation and editing; it shows the split between Legal, Accounting, Tax, and approval responsibilities.
- Start with the fund hierarchy when demonstrating the current portfolio-forward demo; use the portfolio-change workflow as the governance proof point.
- Use the legal entity 360 view to connect identity, address, offices, contacts, names, documents, and relationships.
- Resolve duplicate suggestions before relying on the golden record for downstream reporting.
- Keep reference data current because entity type, status, structure, country, state, category, subcategory, strategy, currency, and geography all drive validation and authoring behavior.
- Use the relationship join tables to explain private-equity-specific structures that do not fit simple parent-child hierarchy.
