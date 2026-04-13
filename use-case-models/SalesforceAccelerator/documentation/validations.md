# Validations Documentation

This table summarizes the validations defined in the model, including their entity, name, label, description, and condition.

| Entity      | Name                 | Label                | Description                                   | Condition                                      |
|-------------|----------------------|----------------------|-----------------------------------------------|------------------------------------------------|
| Account     | YearStarted          | Year Started         | Year cannot be 5 digit                        | COALESCE(SEM_SUBSTRING(SEM_NUMBER_TO_CHAR(YearStarted) , 5, 1), '') = '' |
| Campaign    | EndDate              | End Date             | End date should be greater than Start date    | EndDate >= StartDate                           |
| AccountContactRelation | EndDate    | End Date             | Start date should not be greater than end date| EndDate >= StartDate                           |
