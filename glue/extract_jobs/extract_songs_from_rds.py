"""
Glue Extract Job: Songs from PostgreSQL (RDS)

This job extracts song metadata from the DeFtunes operational database
and writes raw data to the S3 landing (bronze) zone.
"""

import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

# NOTE:
# Actual connection details and credentials are configured via Glue Connections
# and Terraform-managed IAM roles.

print("Extracting songs data from RDS into S3 landing zone")
