"""
Glue Transform Job: Songs -> Iceberg (Silver)

Reads raw songs data from S3 landing (bronze),
cleans/casts fields, adds metadata columns, and writes to
S3 transform zone (silver) as Apache Iceberg tables registered in Glue Catalog.
"""

print("Transforming songs data and writing Iceberg table to transform zone")
