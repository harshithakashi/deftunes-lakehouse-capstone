"""
Glue Transform Job: API JSON -> Iceberg (Silver)

Reads raw users/sessions JSON from S3 landing (bronze),
normalizes nested fields, cleans/casts columns, adds metadata,
and writes Iceberg tables to the transform zone registered in Glue Catalog.
"""

print("Transforming API JSON data and writing Iceberg tables to transform zone")
