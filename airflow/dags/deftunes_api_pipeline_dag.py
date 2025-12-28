"""
DeFtunes API Pipeline DAG (Placeholder)

Orchestrates:
1) Glue extract users from API -> S3 landing
2) Glue extract sessions from API -> S3 landing
3) Glue transform JSON -> Iceberg (S3 transform)
4) Glue Data Quality ruleset evaluation
5) dbt run (serving layer models)
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="deftunes_api_pipeline_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["deftunes", "api", "glue", "dbt", "lakehouse"],
) as dag:

    start = EmptyOperator(task_id="start")
    extract_users = EmptyOperator(task_id="glue_extract_users")
    extract_sessions = EmptyOperator(task_id="glue_extract_sessions")
    transform = EmptyOperator(task_id="glue_transform_api_json_iceberg")
    dq_check = EmptyOperator(task_id="glue_data_quality_check")
    dbt_run = EmptyOperator(task_id="dbt_run_serving_models")
    end = EmptyOperator(task_id="end")

    start >> [extract_users, extract_sessions] >> transform >> dq_check >> dbt_run >> end
