(c) Semarchy 2026

# Governance Rules

Governance Rules is a Semarchy Data Platform data product that turns your data governance standards into managed, approved and queryable rules. The governance office writes each rule as a short MUST / SHOULD / MAY statement with its rationale, implementation guidance, the regulations it cites (GDPR, ISO 3166-1, ISO 8000, DAMA-DMBOK and others) and the exact scope where it applies: a combination of data domain, data classification and attribute type. Rules go through a review and approval workflow, and only rules in force are visible to data product designers and to the AI agents that help them, which read them through the data product MCP server and cite the rule codes in their designs. The accelerator comes with a coverage dashboard, a brand kit, demo data with a generic corpus and a pharma extension, and a Claude Code skill that checks a design against the rules.

Read the [user guide](./documentation/user_guide.md) to get started.

| Folder | Content |
|---|---|
| [src/GovernanceRules](./src/GovernanceRules) | Data product source (SEML) |
| [documentation](./documentation) | User guide, model structure, validations, enrichers, named queries |
| [resources/platform-administration](./resources/platform-administration/README.md) | Roles, API key and MCP OAuth client examples |
| [resources/image-libraries/GovernanceRules](./resources/image-libraries/GovernanceRules) | Image library (brand kit "Quiet Harbor") |
| [resources/dashboards](./resources/dashboards/README.md) | Governance coverage dashboard (Dashboard Builder) |
| [resources/demo-data](./resources/demo-data/README.md) | Demo data as CSV files and REST API payload |
| [resources/ai-agents/governance-check](./resources/ai-agents/governance-check/SKILL.md) | Claude Code skill to check a design against the rules |
