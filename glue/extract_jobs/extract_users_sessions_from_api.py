"""
Glue Extract Job: Users and Sessions from DeFtunes API

This job extracts user and session data from REST APIs
and stores raw JSON data in the S3 landing (bronze) zone.
"""

print("Extracting users and sessions data from API into S3 landing zone")
