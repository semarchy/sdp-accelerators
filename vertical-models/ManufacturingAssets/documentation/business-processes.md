# Business Processes and Authoring Flows

The accelerator packages guided authoring experiences, automated validations, and a collaborative workflow so stewards can manage manufacturing assets with confidence.

## Authoring Steppers

- **Author Factories (`AuthorFactories.Stepper.seml`)**  
  Captures factory master data and children (production lines, machines, suppliers). The stepper normalizes `Region` through the `RegionNormalization` enricher and enforces mandatory/foreign-key checks on `Name`, `Address`, operational status, and factory type. Child collections inherit equivalent constraints to ensure production lines and machines reference valid code lists.

- **Author Machines (`AuthorMachines.Stepper.seml`)**  
  Provides core machine attributes (serial number, type, status, location). Specialized steppers extend this base form for downstream tasks:
  - `AuthorMachinesProducts` assigns finished products to machines.
  - `AuthorMachinesDigitalTwins` maintains digital twin records and links them to machines, invoking the workflow enricher to refresh derived data.
  - `AuthorMachinesIoTDevices` manages IoT devices attached to machines, also using the workflow enricher trigger workaround to guarantee execution.

- **Author Maintenance Schedules (`AuthorMaintenanceSchedules.Stepper.seml`)**  
  Guides users through scheduling maintenance events and capturing the spare parts consumed. The stepper executes the `MaintenanceScheduleNormalization` enricher and applies validations that enforce required keys (`ScheduleID`, `ScheduledDate`), machine and maintenance-type references, non-negative cost/quantities, and chronological performed dates. Child spare-part records must reference a valid part and comply with the `QuantityUsedNonNegative` SemQL rule.

- **Reference Data Steppers**  
  Each reference entity (statuses, types, categories) exposes a lightweight stepper so administrators can maintain controlled vocabularies without leaving the application shell.

## Enrichers

| Enricher | Scope | Purpose |
| --- | --- | --- |
| `RegionNormalization` | Factory | Uppercases and trims the factory region to harmonize values before validation. |
| `WorkflowEnricher` | Machine | Workaround enricher executed from machine-centric steppers to refresh workflow-driven attributes when authoring related collections. |
| `MaintenanceScheduleNormalization` | MaintenanceSchedule | Cleans `ScheduleID`, `MaintenanceProvider`, `DescriptionOfWork`, and `PartsUsed` to remove leading/trailing spaces and enforce uppercase identifiers. |

## Validation Highlights

- **Mandatory & Foreign Keys**: All business-critical identifiers and lookups (factory type, operational status, machine assignments, maintenance type) are enforced in their respective steppers.
- **SemQL Checks**:
  - `SizeMinValue` ensures factories exceed the configured minimum size.
  - `MaintenanceCostNonNegative` blocks negative maintenance costs.
  - `PerformedDateAfterScheduled` ensures performed dates are not earlier than scheduled dates.
  - `QuantityUsedNonNegative` keeps spare-part quantities at zero or above.

## Workflow: Edit Machine Assets

The `EditMachineAssets` workflow orchestrates collaborative updates across the machine hierarchy:

1. **Initiation** – A data steward launches the workflow from a machine selection and completes the base `AuthorMachines` form.
2. **Parallel Authoring** – Once machine details are saved, the workflow opens a parallel block:
   - **Products branch** (BusinessUser role) updates machine-product associations through the `AuthorMachinesProducts` stepper.
   - **Digital assets branch** (DataSteward role) sequences `AuthorMachinesDigitalTwins` followed by `AuthorMachinesIoTDevices` to maintain digital twins and IoT devices.
3. **Submission** – An automation step triggers the `INGEST_WKF` job to consolidate changes before the workflow ends.

Notifications, assignee defaults, and “keep data” behavior are configured to streamline collaboration while preserving in-progress updates.

## Application Shell

The `Asset Management` application (`DefaultApplication.Application.seml`) exposes:

- Global search scopes for machines, factories, and production lines.
- Navigation folders for production, maintenance, and administration activities.
- Quick actions for My Tasks and global search, ensuring workflow participants can easily reach their assignments.
