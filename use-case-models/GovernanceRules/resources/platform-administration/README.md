(c) Semarchy 2026

# Platform administration for GovernanceRules

Platform objects that the GovernanceRules data product expects on the target tenant. Create them before the first deployment (roles) or before loading data and connecting AI agents (API key, MCP OAuth client). You need a platform administrator to do it.

| File | What it creates | How |
|---|---|---|
| `roles/GovernanceOwner.json` | Role of the governance office lead who approves, rejects and retires rules | `sem dm admin roles set GovernanceOwner -i roles/GovernanceOwner.json`, or Platform administration › Roles |
| `roles/GovernanceSteward.json` | Role of the rule authors; also the role that loads data through the REST API (integration role) | same command with its file |
| `roles/GovernanceReader.json` | Read-only role of data product designers (in-force rules only) | same command with its file |
| `roles/GovernanceAgent.json` | Read-only role of AI agents reading the rules through MCP (in-force rules only) | same command with its file |
| `semDMApiKey_config.json` | Example API key for the demo data load (`semarchyConnect` + `GovernanceSteward`) | Platform administration › API keys; set the expiry date. The key value is shown once: keep it in a secret store, never in Git. |
| `mcp-oauth-client.json` | Public OAuth client for Claude Code on the designer's computer (fixed callback port) | Platform administration › MCP authorization › Add OAuth client, or `sem sdp admin mcp clients set claude-code-local -i mcp-oauth-client.json` with a recent Platform CLI |

The roles carry no platform privileges (all `DENIED`): what each role can do on the data comes from the privilege grants of the data product (`src/GovernanceRules/privilege_grants`). Role names are case-sensitive and must match exactly.

Assign the roles to users with `sem dm admin users assign <user> <Role>` or through your identity provider's role mapping. For AI agents, use a dedicated user that holds only `GovernanceAgent`: the agent then sees only approved, in-force rules. See [design_with_ai_agents.md](../../documentation/design_with_ai_agents.md).

The OAuth client is public (no secret). If port 38127 is already used on designers' computers, choose another fixed port and register both redirect URIs with that port. VS Code's built-in MCP client uses other redirect URIs (`http://127.0.0.1:33418/` and `https://vscode.dev/redirect`).
