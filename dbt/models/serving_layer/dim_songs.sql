-- Dimension: Songs
-- Source: Redshift Spectrum external schema (Iceberg tables)

select
  song_id,
  song_title,
  artist_id,
  artist_name,
  duration
from {{ source('deftunes_transform', 'songs') }}
