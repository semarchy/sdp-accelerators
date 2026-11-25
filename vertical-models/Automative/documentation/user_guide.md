# Manufacturing and Automotive Accelerator - User Guide

The Manufacturing model is a multi-domain MDM accelerator for manufacturing and automotive scenarios. It consolidates products and parts, bills of material, suppliers, manufacturers, plants, dealers, vehicles, customers, households, and service history into governed Semarchy xDM applications.

The delivered demo is organized around two applications:
- `Manufacturing` focuses on manufacturing, distribution, and supply-chain use cases.
- `Automotive` focuses on the customer and dealer side of the supply chain, including vehicles, make/model/trim reference data, service appointments, households, and duplicate-review flows.

Related pages:
- [model structure](./model_structure.md)
- [enrichers](./enrichers.md)
- [validations](./validations.md)

## Personas and goals

### Product and Item Steward
Focus: maintain product, part, raw-material, semi-finished-good, and assembly data used across manufacturing and downstream automotive scenarios.

Typical tasks:
- Maintain item families, subfamilies, item attributes, item images, and item conditions.
- Review bills of material and understand where a part is used across assemblies and vehicle trims.
- Support recall analysis by identifying affected items, trims, vehicles, dealers, and customers.

Key activities and screens:
- `Items`, `Item Images`, `Item Bill Of Materials`
- `Item Families`, `Item Sub Families`, `Item Attributes`, `Item Attribute Values`
- `Item Product Trims`, `Item Specific Attributes`, `Item Conditions`, `Item Types`

### Supply Chain and Supplier Steward
Focus: govern supplier, supplier hierarchy, supplier address, manufacturer, plant, and supplied-item relationships.

Typical tasks:
- Maintain supplier profiles, payment terms, addresses, and parent-supplier relationships.
- Review supplier duplicate suggestions and stewardship errors.
- Link suppliers to manufacturer plants, items, and manufacturing facilities to support procurement and supply-chain analysis.

Key activities and screens:
- `Suppliers`, `Supplier Addresses`, `Suggested Matches`, `Review Errors`
- `Supplier Manufacturer Plants`, `Manufacturers`, `Manufacturing Plants`
- `Manufacturing Plant Types`, `Manufacturing Plant Work Shifts`, `Manufacturing Plant Addresses`

### Automotive Customer and Dealer Steward
Focus: manage the customer-facing automotive domain, including customers, households, dealers, vehicles, and service activity.

Typical tasks:
- Review customer enrichment outputs, addresses, households, and duplicate suggestions.
- Maintain dealers, dealer makes, dealer services, service types, and service appointments.
- Connect customer ownership and service history to mastered vehicles.

Key activities and screens:
- `Customers`, `Customer Vehicles`, `Customer Service Appointments`, `Nicknames`
- `Dealer`, `Dealer Services`, `Service`, `Service Types`, `Service Appointment`
- `Suggested Matches`, `Households`, `Review Erroneous Records`

### Automotive Product Steward
Focus: maintain automotive reference and catalog data, including ACES-style make, model, year, trim, option, and feature information.

Typical tasks:
- Browse and maintain makes, models, model years, trims, and vehicles.
- Maintain body size, body style, cylinders, drivetrain, engine aspiration, and transmission reference data.
- Manage option categories, option or feature values, trim options, vehicle options, and product option relationships.

Key activities and screens:
- `Make`, `Models`, `Trim`, `Vehicles`, `Model Years`
- `Body Sizes`, `Body Styles`, `Cylinders`, `Transmission`, `Engine Aspirations`, `Drive Trains`
- `Product Option Categories`, `Trim Option Or Features`, `Option Or Features`, `Product Option Or Feature Values`, `Vehicle Option Or Features`

## Model at a glance

Core sub-models:
- Address and Contact: mastered addresses, country/state/type reference data, and contact records.
- Customer and Ownership: customers, household enrichment, customer vehicles, and service appointments.
- Item Hub and BOM: items, item classifications, item attributes, images, bill of material relationships, and trim usage.
- Supplier, Manufacturer, and Plant: suppliers, supplier hierarchy, manufacturers, plants, work shifts, addresses, and supplied-item relationships.
- Automotive Catalog and Vehicles: make, model, model year, trim, vehicle, and customer/dealer-facing product records.
- Dealer and Service: dealers, dealer makes, services, service types, and dealer-service relationships.
- Automotive Reference and Options: body, drivetrain, engine, transmission, option, feature, and relationship reference data.

Primary navigation groups in the `Manufacturing` application:
- `Item`, `Supplier`, `Manufacturer`, `Location`, `Customer (Retail)`, `Product Data`, `Dealer`, `Dashboards`, `Documentation`

Primary navigation groups in the `Automotive` application:
- `Dealer`, `General`, `Reference Data`, `Vehicle`, `Customer`, `Documentation`

For a detailed list of entities and attributes, see [model structure](./model_structure.md).

## Dashboards and analytics

The Manufacturing application includes dashboard entries for both monitoring and demo walkthroughs:
- `Discovery (Data Profiling)` opens source data profiling.
- `Supplier Dashbaord` focuses on supplier data quality and supply-chain views.
- `Product/ Vehicle Compliance` focuses on product and vehicle compliance signals.

These dashboards complement the mastered model: the dashboards surface quality, supplier, and product signals, while the model provides the governed records and relationships behind the analysis.

## Common journey by persona

### Product and Item Steward
1. Open the `Manufacturing` application.
2. Browse `Item` -> `Items` to inspect item details, classifications, images, and completeness.
3. Use related tabs and relationships to review where an item is manufactured and where it is used in bills of material or vehicle trims.
4. For recall analysis, follow the relationship path from item to product trim, vehicle, dealer, and customer to identify impacted owners.

### Supply Chain and Supplier Steward
1. Open `Supplier` -> `Suppliers` to review supplier profiles and hierarchy information.
2. Review `Suggested Matches` and `Review Errors` before publishing supplier records.
3. Use `Supplier Manufacturer Plants` to connect suppliers, items, manufacturers, plants, and supplier addresses.
4. Open manufacturer and plant records to inspect plant ownership, output type, addresses, and operating details.

### Automotive Product Steward
1. Open the `Automotive` application.
2. Browse `Vehicle` -> `Make`, then drill into models and trims for the selected make.
3. Use `Reference Data` to inspect body, drivetrain, engine, cylinder, and transmission classifications.
4. Use option and feature entities to understand trim-level and vehicle-level equipment relationships.

### Automotive Customer and Dealer Steward
1. Open `Customer` -> `Customer` to review mastered customer records and enrichment outputs.
2. Use `Suggested Matches` to review duplicate suggestions without blindly merging records.
3. Use `Households` to review customers sharing household-level relationships.
4. Open `Dealer` and service screens to inspect dealer services, service appointments, and customer vehicle service history.

## Data quality and enrichment

The model includes:
- Fuzzy matching and duplicate-review flows for customers, suppliers, manufacturers, product vehicles, contacts, and addresses.
- Enrichers for address geocoding, name normalization, phoneticization, phone and email cleansing, householding, Melissa Personator enrichment, SKU normalization, and BOM defaults.
- Validations for customer age, mandatory item-specific attribute values, and supplier founding year.
- Workflows for onboarding customers, dealers, items, and suppliers.
- Model jobs for customer, dealer, item, manufacturer, supplier, vehicle, and full integration loads.

Details:
- Enrichers: [enrichers](./enrichers.md)
- Validations: [validations](./validations.md)

## Demo data and import note

The repository contains several demo-data areas under `resources/demo-data`, including CSV imports, API import examples, original exports, and work-in-progress curl import files. Use the import sequence and command files from the relevant demo-data folder when loading a new environment.

The delivered use-case PDF in this folder remains the narrative walkthrough for demos. These markdown pages document the configured model objects and provide a shorter operational guide for users and implementers.

## Tips for success

- Start with the application aligned to the scenario: `Manufacturing` for item, supplier, manufacturer, plant, and recall flows; `Automotive` for customer, dealer, vehicle, and ACES-style product flows.
- Resolve duplicate suggestions before relying on supplier or customer 360 views.
- Keep item, BOM, and trim relationships complete so recall and impact analysis can traverse from part to owner.
- Use dashboards and related-record tabs together: dashboards show where to focus, and the mastered records explain the relationships behind the signal.
