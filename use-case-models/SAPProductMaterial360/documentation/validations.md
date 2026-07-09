# Validations Documentation

This table summarizes the row-level validations defined in the SAP Product / Material 360 model.

| Entity | Name | Label | Description | Condition | Scope |
|---|---|---|---|---|---|
| Product | EffectiveDates | Effective Dates | Effective To must not be before Effective From. | EffectiveTo is null or EffectiveFrom is null or EffectiveTo >= EffectiveFrom | PRE_CONSO |
| Material | PlanningQuantities | Planning Quantities | Safety stock and reorder point must not be negative. | (SafetyStock is null or SafetyStock >= 0) and (ReorderPoint is null or ReorderPoint >= 0) | PRE_CONSO |
| ProductClassification | ClassificationDates | Classification Dates | Valid To must not be before Valid From. | ValidTo is null or ValidFrom is null or ValidTo >= ValidFrom | PRE_CONSO |
| ProductRelationship | RelationshipDates | Relationship Dates | Effective To must not be before Effective From. | EffectiveTo is null or EffectiveFrom is null or EffectiveTo >= EffectiveFrom | PRE_CONSO |
