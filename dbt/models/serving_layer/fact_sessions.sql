-- Fact: Sessions / Purchases
-- Source: Redshift Spectrum external schema (Iceberg tables)

select
  session_id,
  user_id,
  song_id,
  session_start_time,
  price
from {{ source('deftunes_transform', 'sessions') }}
