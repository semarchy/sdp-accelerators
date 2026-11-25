# Manufacturing Assets Data Model

The Manufacturing Assets domain captures the full lifecycle of industrial equipment across factories, production lines, machines, maintenance activities, and supporting reference data. This guide inventories every entity delivered in the accelerator and summarizes how they connect.

## Core Domain Entities

| Entity | Description | Key Attributes | Primary Relationships |
| --- | --- | --- | --- |
| **Factory** | Master record for a manufacturing site. | `FactoryID`, `Name`, `Address`, `Region`, `FactorySize` | Linked to `FactoryType`, `OperationalStatus`, `Country`; parent of `ProductionLine` via `ProductionLineFactory`. |
| **ProductionLine** | Production line or cell inside a factory. | `ProductionLineID`, `Name`, `Code`, `Capacity`, `StartDate`, `EndDate` | Child of `Factory`; classified by `LineType` and `ProductionLineStatus`; parent of `Machine`. |
| **Machine** | Physical asset performing production tasks. | `MachineID`, `SerialNumber`, `TypeModel`, `InstallationDate`, `LastMaintenanceDate`, `NextScheduledMaintenance`, `WarrantyExpiryDate` | Located on a `ProductionLine`; qualified by `MachineStatus`, `CriticalityLevel`; parent of `DigitalTwin`, `IoTDevice`, `MaintenanceSchedule`, `Product` links. |
| **DigitalTwin** | Virtual representation of a machine. | `TwinID`, `ModelVersion`, `StartDate`, `SimulationCapabilities`, `DataSourcesLinked` | Child of `Machine` via `DigitalTwinMachine`; governed by `DigitalTwinStatus`. |
| **IoTDevice** | Connected sensor/device attached to a machine. | `DeviceID`, `Manufacturer`, `Model`, `FirmwareVersion`, `InstallationDate`, `DataCollected` | Child of `Machine` via `IoTDeviceMachine`; typed by `IoTDeviceType` and `IoTDeviceStatus`. |
| **MaintenanceSchedule** | Planned or executed maintenance event. | `ScheduleID`, `ScheduledDate`, `PerformedDate`, `MaintenanceProvider`, `MaintenanceCost`, `DescriptionOfWork` | Targets `Machine` (`MaintenanceScheduleMachine`); typed by `MaintenanceType`; owns `MaintenanceScheduleSparePart`. |
| **MaintenanceScheduleSparePart** | Spare parts consumed by maintenance. | `MaintenanceScheduleID`, `QuantityUsed` | Junction between `MaintenanceSchedule` and `SparePart`; quantity validated by SemQL rule. |
| **SparePart** | Replaceable part or consumable. | `PartID`, `Name`, `Description`, `UnitOfMeasure`, `Category` | Linked to `Supplier` (`SparePartSupplier`); referenced by `MaintenanceScheduleSparePart`. |
| **Product** | Finished good produced on machines. | `ProductID`, `Name`, `SKU`, `LifecycleStatus` | Categorized by `ProductCategory` and `UnitOfMeasure`; optionally linked to `Machine` (`ProductMachine`). |
| **Supplier** | External/internal supplier organization. | `SupplierID`, `Name`, `ContactInformation`, `RiskRating` | Classified by `SupplierType`, `ApprovedStatus`, `Country`; provides `SparePart`. |

## Reference and Lookup Entities

| Entity | Description | Key Attributes | Consumed By |
| --- | --- | --- | --- |
| **ApprovedStatus** | Approval states for suppliers. | `ApprovedStatusID`, `StatusName` | `Supplier` via `SupplierApprovedStatus`. |
| **Country** | Country/region master list. | `CountryID`, `CountryName` | `Factory` (`FactoryCountry`), `Supplier` (`SupplierCountry`). |
| **CriticalityLevel** | Machine criticality ratings. | `CriticalityLevelID`, `LevelName` | `Machine` through `MachineCriticalityLevel`. |
| **DigitalTwinStatus** | Lifecycle states for digital twins. | `StatusID`, `StatusName` | `DigitalTwin` (`DigitalTwinStatus`). |
| **FactoryType** | Factory classifications (assembly, etc.). | `TypeID`, `TypeName` | `Factory` (`FactoryTypeFactory`). |
| **IoTDeviceStatus** | Operational states for IoT devices. | `StatusID`, `StatusName` | `IoTDevice` (`IoTDeviceStatus`). |
| **IoTDeviceType** | Device type catalog (sensor, gateway, …). | `TypeID`, `TypeName` | `IoTDevice` (`IoTDeviceType`). |
| **LineType** | Production line categories. | `LineTypeID`, `LineTypeName` | `ProductionLine` (`ProductionLineLineType`). |
| **MachineStatus** | Machine status values (operational, down). | `StatusID`, `StatusName` | `Machine` (`MachineStatus`). |
| **MaintenanceType** | Preventive/corrective maintenance categories. | `MaintenanceTypeID`, `TypeName` | `MaintenanceSchedule` (`MaintenanceScheduleMaintenanceType`). |
| **OperationalStatus** | Factory operational readiness states. | `OperationalStatusID`, `StatusName` | `Factory` (`FactoryOperationalStatus`). |
| **ProductCategory** | Product grouping catalog. | `CategoryID`, `CategoryName` | `Product`. |
| **ProductionLineStatus** | Availability states for production lines. | `StatusID`, `StatusName` | `ProductionLine` (`ProductionLineStatus`). |
| **SupplierType** | Supplier segmentation (OEM, distributor). | `SupplierTypeID`, `TypeName` | `Supplier` (`SupplierSupplierType`). |
| **UnitOfMeasure** | Units for quantity tracking. | `UnitOfMeasureID`, `UnitName` | `Product` (`ProductUnitOfMeasure`), `SparePart` attributes. |

## Complex Types and Shared Structures

- **AssetLocation**: Complex type reused by `Factory`, `ProductionLine`, and `Machine` to capture narrative description, floor zone, GPS coordinates, and environmental conditions for physical placement.

## Navigation & Presentation Assets

- Collection views (`*.CollectionView.seml`) define the default list/table layouts per entity, surfacing key identifiers and status columns.
- Display cards highlight contextual information—for example, `MaintenanceScheduleDisplayCard` combines maintenance type and performed date for quick scanning.
- Business views bundle hierarchies (e.g., factories → production lines → machines) so stewards can browse related records in one navigation tree.

With these entities and supporting structures, the accelerator delivers a governed, end-to-end view of manufacturing assets, their operational context, and the master data required to manage them.
