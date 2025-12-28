# Deployment (Safe Portfolio Version)

This repo documents the end-to-end design and implementation approach.

In the academic lab:
- Terraform provisions AWS Glue, IAM, S3, Redshift Spectrum, and Redshift schemas.
- Glue jobs extract (bronze) and transform (silver Iceberg).
- Redshift Spectrum queries Iceberg tables.
- dbt builds star schema + BI views (gold).
- Airflow orchestrates daily jobs and triggers Glue + DQ + dbt.

Portfolio note:
- No AWS credentials, console URLs, or endpoints are stored in this repository.
- All values should be injected through environment variables or secret managers.
