-- Dimension: Users
-- Source: Redshift Spectrum external schema (Iceberg tables)

select
  user_id,
  user_name,
  user_lastname,
  user_since,
  country_code
from {{ source('deftunes_transform', 'users') }}
