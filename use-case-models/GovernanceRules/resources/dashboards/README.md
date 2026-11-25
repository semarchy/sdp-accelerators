(c) Semarchy 2026

# Governance coverage dashboard

`GovernanceRulesAnalytics` is a Dashboard Builder application for the governance office (GovernanceOwner, GovernanceSteward). It answers three questions: how many rules are in force, in review or in draft; how rules spread across categories and requirement levels; and which data domain and category pairs have no rule yet. The GovernanceRules application shows it as a tile in Quick access.

## Import the packaged application

1. Rename `GovernanceRulesAnalytics.rename_to_zip` to `GovernanceRulesAnalytics.zip`.
2. On the Semarchy Data Platform home page, go to **Tools › Dashboard Builder**.
3. Select **Import Application** and drop `GovernanceRulesAnalytics.zip`.
4. Open **Datasources**, select the `GovernanceRules` datasource and set it to the datasource of the data location where the data product is deployed (the archive ships with the placeholder `datasource-TO-SET`).
5. Save, then open the dashboard from the GovernanceRules application.

Import the dashboard application **before** deploying the data product, or redeploy afterwards: the application tile links to it by name.

## Change the dashboard

The source of the application is the YAML in `GovernanceRulesAnalytics/` (data source, queries, charts, dashboard). Edit it, set `platformDataSourceName` in `data-sources/GovernanceRules.yaml`, then rebuild the archive, for example with the Semarchy SDP plugin for Claude Code:

```
node <plugin>/tools/sdp-bridge.mjs dashboards check resources/dashboards/GovernanceRulesAnalytics --data-product-folder src/GovernanceRules
node <plugin>/tools/sdp-bridge.mjs dashboards pack  resources/dashboards/GovernanceRulesAnalytics --data-product-folder src/GovernanceRules
sem dm dashboards applications import GovernanceRulesAnalytics -i resources/dashboards/GovernanceRulesAnalytics.zip
```

Rename the new archive to `.rename_to_zip` before committing it: the library's `.gitignore` excludes `*.zip`.
