# Restaurant Master: user guide

## Introduction and use case

### The business problem

A quick-service restaurant group runs hundreds or thousands of restaurants under several brands. Each restaurant
exists in many systems at once: Real Estate tracks the site and the lease, Finance (ERP) bills the company that
operates it, each brand's point-of-sale (POS) system knows it as a terminal location, and delivery apps, brand
websites and map listings show it to customers. Each system holds its own copy, with its own identifier, and the
copies drift apart: a restaurant closes but stays listed, a new operator is billed under the old company, opening
hours differ between the website and the delivery app.

**Restaurant Master** gives the group one trusted record per physical restaurant, shared by every system, and the
processes to keep it correct.

### The fictional customer

The accelerator is built for **Copperline Restaurant Group**, a fictional group used for this demo:

| Brand | Restaurants (in the scenario) | Profile |
|---|---|---|
| Fuego Street Taqueria | about 1,100 | about 60% franchised |
| Kettle & Crust | about 950 | about 85% franchised, delivery-heavy |
| Bluebird Biscuit Co. | about 450 | mostly company-owned |

About 12% of the restaurants are in Canada, some of them in Quebec with French public names. The demo dataset is a
much smaller sample of about 60 restaurants. All names, companies and addresses are made up.

### What the accelerator covers

- **The restaurant:** identity, brand, address and coordinates, time zone, lifecycle status and key dates, site and
  facility profile, cost center, and which systems know it.
- **Restaurant details:** opening hours per channel (regular and special), services and amenities, contact points,
  public names per language, status history, operators over time, organization assignments, and each system's
  identifier for the restaurant.
- **Operators:** the franchisee groups and the legal entities that operate restaurants and are billed.
- **Organization:** the Finance, Operations and Marketing hierarchies the restaurants belong to.
- **Reference data:** countries, states and provinces, brands, lifecycle statuses and reasons, identifier types,
  source systems, service types, building types and location types.

**Not covered:** POS terminal setup, tax settings, delivery radius, menu availability, employee data, royalty
calculation and billing. Geocoding is not included (coordinates come from Real Estate).

### Who uses it

| Persona | What they do in Restaurant Master |
|---|---|
| Data steward (Real Estate, Operations, Finance, Marketing) | Onboards new restaurants, maintains public data, hours, services, lifecycle and operators |
| Approver (restaurant data owner) | Approves or rejects the changes stewards submit |
| Data administrator | Maintains reference data and the organization hierarchies |
| Consumers (HR, Marketing, delivery partners, map agency) | Read and export the trusted data |

In this accelerator, three roles have full access to the data: the built-in `semarchyAdmin` role and the two demo
roles `demo` and `demosemarchy`. Any user can start and work the workflows (see [Workflows](#workflows)). See
[Work for developers](#work-for-developers) to split the roles for a real project.

### Business value

- One trusted restaurant record, so every channel shows the same name, address, status and hours.
- Consuming systems read the same certified record instead of keeping their own copy.
- Correct, current operator and franchisee relationships for billing and reporting.
- Less re-keying when a restaurant opens, closes, relocates or changes hands.
- A foundation for related domains such as menu items or supply chain.

## Prerequisites

- Visual Studio Code with the Semarchy extension (DXP 2.2.0 or later), or the Semarchy Design CLI 2.2.0 or later.
- A Semarchy Data Platform instance (SaaS or Self-Hosted) and a datasource for a new data location.
- The Semarchy Platform CLI to import the image library.

Build the data product from the `src/RestaurantMaster` folder, deploy it to a new data location, import the image
library from `resources/image-libraries/restaurantmaster`, then load the demo data
(see [Demo data and loading](#demo-data-and-loading)).

## Model structure

The data product has 22 entities, 31 relationships and 16 lists of values, organized in five groups:

| Group | Entities |
|---|---|
| Hub | Restaurant |
| Restaurant details (children of Restaurant) | Opening hours, Service, Contact point, Localized name, Status history, Operator, Organization assignment, Restaurant identifier |
| Operators | Franchisee, Legal entity |
| Organization | Organization unit |
| Reference data | Country, State / province, Brand, Lifecycle status, Lifecycle status reason, Identifier type, Source system, Service type, Building type, Location type |

The full list of entities, attributes, relationships and lists of values is in [model_structure.md](model_structure.md).

### Key design choices

- **A common restaurant ID shared by every system.** Real Estate issues it when a site enters the pipeline
  (`R` followed by 7 digits, for example `R0000123`). Every other system stores and sends the same ID. The ID has no
  meaning: a restaurant keeps it when its brand or operator changes.
- **ID matching, not fuzzy matching.** Because every system sends the same ID, Restaurant is an *ID-matched* entity:
  records with the same ID are consolidated into one golden record automatically, with no match rules to tune. The
  same applies to Legal Entity, keyed on its tax ID (`US-` or `CA-` followed by 9 digits).
- **Children are basic entities with keys built from the restaurant ID.** Each child row has the key its source
  system sends, in the form `<RestaurantID>-<suffix>` (for example `R0000123-POS-4471`). A row sent again updates the
  same record instead of creating a duplicate.
- **Start date only for successive periods.** Status history, operators and organization assignments have a start date
  but no end date. A period ends when the next one starts, so overlaps and gaps cannot happen, and a planned change is
  a row with a future date.

## Main entities

### Restaurant

One golden record per physical restaurant, fed by six publishers:

| Publisher | Code | What it sends for the restaurant |
|---|---|---|
| Real Estate / Lease | `RE` | Creates the restaurant: site, address, coordinates, lease and construction dates, square footage, *Relocated from* |
| ERP (Finance) | `ERP` | Cost center |
| POS Fuego Street Taqueria | `POSF` | The restaurant ID only, which shows the POS knows the restaurant |
| POS Kettle & Crust | `POSK` | Same |
| POS Bluebird Biscuit Co. | `POSB` | Same |
| Data stewardship (hub) | `HUB` | Public name, main phone, brand, lifecycle, facility profile |

The restaurant details (identifiers, operators, hours and the others) are separate basic entities. In a real project
each one is loaded by the system that owns it, for example ERP for the operators; the demo data loads them all through
the hub.

**Matching:** ID-matched on the restaurant ID. A record without the ID is rejected; it is never matched on name or
address.

**Survivorship:** each attribute is owned by one system, so conflicts are rare. The default rule ranks Real Estate,
then ERP, then the hub, then the POS systems. Attributes the hub owns (name, phone, brand, lifecycle, facility
details) and those Real Estate or ERP own have their own rule, which keeps the owner's value even when other systems
send nothing. A steward's correction of a golden value is kept until the source sends a different value.

**Enrichers:**
- The address is standardized and Canadian postal codes are formatted as `A1A 1A1`.
- The main phone is written as `+1` followed by 10 digits.
- Three flags record which systems publish the restaurant (Real Estate, ERP, POS).
- After consolidation, the public channel status follows the lifecycle status, the time zone defaults to the state's,
  and two check keys flag possible duplicates.

**Validations:** the restaurant ID format, the brand (required beyond the pipeline stage), the coherence between the
lifecycle status and its dates, and two unique keys: no two restaurants share a Site ID, and no two restaurants of
the same brand share an address (a likely mistyped ID).

**Self-reference:** *Relocated from* links a relocated restaurant to the one it replaces. The new site gets a new ID.

### Legal entity

The company that signs the lease and the franchise agreement and is billed: a franchisee company or one of the
group's own companies. ID-matched on its tax-based key and fed by ERP and Real Estate. ERP wins conflicts, then Real
Estate, then the hub. The key format is validated after consolidation.

### Franchisee

The franchise group behind one or more legal entities, possibly across brands. The group's own companies roll up to a
"Corporate" franchisee. Maintained in the hub.

### Organization unit and the hierarchies

Each unit belongs to one of three hierarchies, with a parent unit (self-reference) for up to four levels:

| Hierarchy | Levels |
|---|---|
| Finance | Region, then Area |
| Operations | Region, then Area, then District |
| Marketing | One Market per brand and advertising area |

A validation keeps each parent in the same hierarchy, prevents loops, and requires a brand on Marketing markets only.
Restaurants are placed in each hierarchy through *Organization assignments*, which keep the history of realignments.

### Restaurant details

| Entity | What it holds | Main rule |
|---|---|---|
| Opening hours | Regular weekly hours per channel and special hours for a date | A regular row needs a day, a special row a date; times are HH:MM and close after open unless overnight |
| Service | Services and amenities, such as drive-thru or delivery with a given partner | A delivery service names its partner; other services do not |
| Contact point | Extra phones, fax, emails, website, ordering and social links | Email and link formats; phones normalized |
| Localized name | The public name per language (French in Quebec) | One name per language |
| Status history | Lifecycle statuses over time, with reason and comment | One row per start date; the reason must belong to the status |
| Operator | Which legal entity operates the restaurant, the ownership type and agreement | A franchised operator needs an agreement number |
| Organization assignment | The restaurant's unit in each hierarchy over time | The unit must belong to the selected hierarchy |
| Restaurant identifier | Each system's own ID (ERP number, POS ID, delivery merchant IDs, listing IDs) | One row per system, type, value and start date |

Every child key must start with the restaurant ID followed by a dash.

## Model components

### Enrichers

11 enrichers standardize addresses and phone numbers, build the business keys that keep child rows unique, record
which systems publish each restaurant, and derive the public channel status and time zone. Details and expressions:
[enrichers.md](enrichers.md).

### Validations

21 validation rules and 8 unique keys. A failing record is not certified and appears under *Data stewardship > Records
in error*. Details and conditions: [validations.md](validations.md).

### Survivorship

See [Restaurant](#restaurant) and [Legal entity](#legal-entity). Basic entities have no consolidation: the latest load
or edit wins.

### Workflows

Four workflows, each with a steward task and an approval task. The approver can approve and publish, or reject and
send the change back to the steward.

| Step | Who can do it | Who is notified by email |
|---|---|---|
| Start | Any user, from the restaurant's options menu | Nobody |
| Steward task | The user who started the workflow | That user only |
| Approval task | Any user, by claiming it from the available tasks | Only the user who claims it; open approvals are not emailed to everyone |

Workflow instances are managed by the `semarchyAdmin` role.

| Workflow | Started from | What the steward does |
|---|---|---|
| Onboard a restaurant | A restaurant published by Real Estate (worklist *Awaiting onboarding*) | Completes brand, public name, organization assignments, planned dates, intended operator and French name |
| Change restaurant data | Any restaurant | Edits the restaurant and its details |
| Change lifecycle status | Any restaurant | Records the new status, reason and start date (today or planned) |
| Transfer operator | Any restaurant | Records the new operator from the closing date: legal entity, ownership type, agreement |

A relocation is handled as two steps: Real Estate publishes the new restaurant with *Relocated from*, a steward
onboards it, and the old restaurant goes through *Change lifecycle status* to *Relocated*.

### Data stewardship

The *Data stewardship* folder of the application holds:

- **Records in error:** one view each for Restaurant, Legal entity, Franchisee, Organization unit and the eight
  restaurant details, with the records that failed a validation; for Restaurant and Legal entity, also the source
  records rejected at load.
- **Worklists:** checks that do not block a record but need a steward's attention:

| Worklist | What it lists |
|---|---|
| Awaiting onboarding | Restaurants published by Real Estate that no steward has onboarded yet (no brand) |
| Listed but incomplete | Restaurants shown on public channels without a name, full address, coordinates or main phone |
| Address to check | State outside the country, or coordinates outside the US and Canada |
| Open but unknown to ERP or POS | Open restaurants that ERP or the POS never published: a broken integration or a mistyped ID |
| Missing operator or status history | Restaurants beyond the pipeline without a started operator or status-history row |
| Franchisee companies without a group | Franchisee companies not yet attached to their franchisee group |

### The application

The *Restaurant Master* application is organized as:

- **Restaurants:** the restaurant list with built-in filters (Open, Temporarily closed, Pipeline, Closed), and a
  *Restaurant details* folder with one view per child entity. A restaurant record shows its details as tabs, a map of
  its location, its current operator, and its record lineage and change history.
- **Operators:** franchisees and legal entities.
- **Organization:** organization units shown as a tree.
- **Reference data:** the ten reference lists.
- **Data stewardship:** records in error and worklists.
- **Administration:** the model documentation and one CSV import action per entity.

On the folder pages, every view (restaurants, operators, organization, the restaurant details, the reference lists,
the worklists and the records-in-error views) has its own picture, and so does each data import action (the
entity's picture with an import badge), from the `restaurantmaster` image library.

### Data retention

A retention policy keeps golden and master history for 7 years, source data for 2 years, deleted-record traces for 3
years and source errors for 6 months. It only takes effect once a purge schedule is configured on the data location.

## Work for developers

### Using the accelerator early in a project

- Deploy it as-is with the demo data to show business users the target experience: one restaurant record, its
  details, the workflows and the worklists.
- Replace the demo data with an extract from each source system to measure the real data quality: which records
  arrive without the common ID, which restaurants are unknown to a system, which addresses collide.
- Review the attributes and lists of values with the business. Most projects adjust lifecycle statuses, service
  types and identifier types first.

### Common customizations

- **Roles:** create separate steward, approver, consumer and integration roles on the platform, then change the
  privilege grants to those roles. In the workflows, set the start role (`initiatorRequiredRole`) and give the
  approval task an approver role (`assigneeRequiredRole`) for a real four-eyes process. Restrict the personal data
  (franchisee principal, organization unit manager) for consumers.
- **Publishers:** rename or add publishers to match the customer's systems, and update the survivorship rules that
  name them.
- **No common ID in the sources:** if a system cannot store the common restaurant ID, Restaurant has to become a
  fuzzy-matched entity with match rules on name, brand and address. This is a significant change.
- **Geocoding:** add an enricher that calls a geocoding service to fill the coordinates when Real Estate does not
  send them.
- **More hierarchies or levels:** add a hierarchy type to the list of values and adjust the hierarchy validation.
- **Dashboards:** a data-quality dashboard and a portfolio dashboard (restaurants by brand, status and country) are
  natural next steps.

### Loading data in production

- Each publisher sends records through the REST loads API, with its publisher code and the common restaurant ID.
- Send the restaurant ID and the legal entity key trimmed and in upper case: an ID-matched key cannot be cleaned
  before matching, so a variant spelling creates a second record.
- Load in dependency order: reference data, then franchisees, legal entities and restaurants, then the restaurant
  details.
- Send only changed records: every record sent goes through certification again and creates a new history version,
  even when nothing changed.

See the [Semarchy documentation](https://docs.semarchy.com) for the loads API, deployment and the purge schedule.

## Demo data and loading

The demo data is in `resources/demo-data`: 2,066 fictional records for about 60 restaurants, with deliberate defects
so the stewardship screens have something to show. It comes in two forms with the same content:

- **One REST call:** `API Import-curl/RestaurantMaster.json` loads and certifies everything in one batch. The command
  is in [HowTo_CallInitDataLoadCurl.md](../resources/demo-data/API%20Import-curl/HowTo_CallInitDataLoadCurl.md).
- **CSV files:** `ImportData/01_Country.csv` to `22_RestaurantOperator.csv`, one per entity, imported in number order
  from *Administration > Data import* in the application.

Load the data once, into an empty data location. The [demo-data README](../resources/demo-data/README.md) lists what
each file contains, what to show in a demo, and the expected counts and errors to check the load against.
