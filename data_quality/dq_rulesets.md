# AWS Glue Data Quality (DQDL) Rulesets (Examples)

These rulesets represent the quality checks applied on the **transform (Iceberg) tables**
before serving data in Redshift.

## Sessions table rules (example)
- user_id must be complete
- session_id must be complete
- user_id length = 36
- session_id length = 36
- song_id must be complete
- price must be <= 2

Example DQDL snippet:
Rules = [
  IsComplete "user_id",
  IsComplete "session_id",
  ColumnLength "user_id" = 36,
  ColumnLength "session_id" = 36,
  IsComplete "song_id",
  ColumnValues "price" <= 2
]

## Users table rules (example)
- user_id must be complete
- user_id should be unique (> 95%)
- user_lastname must be complete
- user_name must be complete
- user_since must be complete

Example DQDL snippet:
Rules = [
  IsComplete "user_id",
  Uniqueness "user_id" > 0.95,
  IsComplete "user_lastname",
  IsComplete "user_name",
  IsComplete "user_since"
]
