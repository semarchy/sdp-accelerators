# Restaurant Master: demo data

Sample data for the `RestaurantMaster` data product: 2,066 records for 22 entities, about 60 restaurants of three
brands in the US and Canada. All of it is fictional: brands, companies, people, addresses and phone numbers (all
`555` numbers) are made up.

| Folder / file | Purpose |
|---|---|
| `ImportData/01_*.csv` … `22_*.csv` | One file per entity, for the application's import actions. The number is the load order (parents before children). |
| `API Import-curl/RestaurantMaster.json` | The same 2,066 records as one REST load payload (`CREATE_LOAD_AND_SUBMIT`). |
| `API Import-curl/HowTo_CallInitDataLoadCurl.md` | The cURL command that posts it. |

## Two ways to load it

**One call (recommended):** post `RestaurantMaster.json` as described in
[HowTo_CallInitDataLoadCurl.md](API%20Import-curl/HowTo_CallInitDataLoadCurl.md). Everything is loaded and certified
in one batch.

**File by file:** in the application, *Administration > Data import*, import the CSV files in number order and wait
for each import to finish before the next one. Each import is its own load, so the order keeps parents ahead of their
children.

Load the data once, into an empty data location. Loading it again creates a second history version of every record
even though nothing changed.

## What the data contains

| # | Entity | Type | Records | Loaded as (publisher) |
|---|---|---|---|---|
| 01-10 | Reference data (countries, states, brands, statuses, reasons, identifier types, source systems, service, building and location types) | Basic | 79 | hub |
| 11 | OrganizationUnit | Basic | 78 | hub |
| 12 | Franchisee | Basic | 10 | hub |
| 13 | LegalEntity | ID-matched | 30 | ERP 18, Real Estate 12 |
| 14 | Restaurant | ID-matched | 220 | Real Estate 61, ERP 51, hub 57, POS Fuego 25, POS Kettle & Crust 20, POS Bluebird 6 |
| 15 | RestaurantIdentifier | Basic | 140 | hub |
| 16 | RestaurantContactPoint | Basic | 123 | hub |
| 17 | RestaurantStatusHistory | Basic | 174 | hub |
| 18 | RestaurantHours | Basic | 659 | hub |
| 19 | RestaurantService | Basic | 320 | hub |
| 20 | RestaurantLocalizedName | Basic | 10 | hub |
| 21 | RestaurantOrgAssignment | Basic | 169 | hub |
| 22 | RestaurantOperator | Basic | 54 | hub |
| | **Total** | | **2,066** | |

## Column conventions

- Column names are the attribute names of the data product. A reference to another entity is `FID_<role>`, holding
  the referenced record's key.
- **ID-matched entities** (Restaurant, LegalEntity) carry a `PublisherID` on every record: one file holds the records
  of all the systems. Their key column is `Gold_RestaurantID` / `Gold_LegalEntityKey` in the CSV and
  `RestaurantID` / `LegalEntityKey` in the JSON. Records with the same key are consolidated into one golden record.
- Child keys follow the convention `<RestaurantID>-<suffix>` (for example `R0000001-ST-20090210`).
- Values computed by enrichers (public channel status, time zone defaults, check keys, the *known to* flags) are not
  supplied.
- Dates are `yyyy-MM-dd`; an empty cell is a null. The CSV files are UTF-8 (with BOM) because of the French names.

## What to show

| Showcase | Where | What you see |
|---|---|---|
| **Consolidation** | Restaurants, *Contributing sources* tab | 220 restaurant records from 6 systems become **61** golden restaurants. A typical open Fuego restaurant has 4 sources: Real Estate, ERP, its POS and the hub |
| **Consolidation** | Legal entities | 30 records (ERP 18, Real Estate 12) become **18** golden legal entities |
| **Survivorship** | R0000001, R0000026, R0000046 | ERP spells the street differently (`1200 W MADISON STREET`); Real Estate's spelling wins |
| **Survivorship** | Any restaurant | Name, brand and status come from the hub, even though Real Estate sends none of them |
| **Survivorship** | Legal entities | Real Estate sends the tenant name in capitals; ERP's spelling wins |
| **Provenance** | *Data coverage* section | Known to Real Estate / ERP / POS, per restaurant |
| **360° view** | R0000040 (Quebec City) | French and English names, lobby and delivery hours, delivery-app merchant IDs, Finance / Operations / Marketing placement |
| **Late-night hours** | Fuego freestanding restaurants | Drive-thru open until 02:00 on Friday and Saturday (closes the next day) |
| **Planned change** | R0000044, R0000056 | Temporarily closed; a future-dated *Open* row in the status history and a planned reopen date |
| **Operator transfer** | R0000005 | Company-operated from 2014, sold to a franchisee on 2024-04-01. *Current operator* shows the franchisee |
| **Realignment** | R0000006 | Operations district changed on 2025-01-01 (two rows, start date only) |
| **Relocation** | R0000024 → R0000058 | 24 is *Relocated*; 58 is the new restaurant, linked through *Relocated from* |
| **POS ID reuse** | R0000023, R0000058 | POS ID `F-0023`: valid for 23 until 2023-05-31, reused by 58 from 2025-07-15 |
| **Multi-brand franchisee** | Franchisees → Lakeshore Restaurant Group | Two legal entities (taco and pizza) and their restaurants |
| **Organization tree** | Organization | Regions → areas → districts; brand-specific Marketing markets |

## Deliberate defects

The data contains defects on purpose, so the stewardship screens have something to show.

**Records in error** (*Data stewardship > Records in error*)

| Entity | Expected | Records | Rule |
|---|---|---|---|
| Restaurant | **5** | `R00072` | ID format (Real Estate keyed 5 digits) |
| | | R0000021 | Open with an opening date in 2027 |
| | | R0000057 | Temporarily closed without a closure date |
| | | R0000041, R0000042 | Same brand at the same address: a mistyped ID |
| Legal entity | **1** | `US-12345678` | Key format (8 digits) |
| Opening hours | **1** | `R0000003-H-LOBBY-SUN` | Regular hours without a day |
| Operator | **1** | `R0000009-OP-…` | Franchised without an agreement number |

**Worklists** (*Data stewardship > Worklists*)

| Worklist | Expected | Restaurants |
|---|---|---|
| Awaiting onboarding | **4** | R0000049, R0000050, R0000051 (pipeline sites not completed in the hub), `R00072` |
| Listed but incomplete | **1** | R0000007 (no main phone) |
| Address to check | **1** | R0000025 (US restaurant keyed with Ontario) |
| Open but unknown to ERP or POS | **2** | R0000017 (no POS record), R0000020 (no ERP record) |
| Missing operator or status history | **3** | R0000053 (approved, no operator yet), R0000060 (open, no operator), R0000009 (its only operator row was rejected) |
| Franchisee companies without a group | **1** | `US-741000999` Seaside Fuego Operations LLC |

## Expected results

Golden record counts after the load: Restaurant 61, LegalEntity 18, Franchisee 10, OrganizationUnit 78; for each
restaurant detail, the records loaded minus the rejected ones (opening hours 658, operators 53, the full file count
for the others). The load can end in `WARNING`: that is expected, because checks after consolidation flag records.
