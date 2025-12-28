"""
DeFtunes Songs Pipeline DAG (Placeholder)

Orchestrates:
1) Glue extract songs from RDS -> S3 landing
2) Glue transform songs -> Iceberg (S3 transform)
3) Glue Data Quality ruleset evaluation
4) dbt run (serving layer models)
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="deftunes_songs_pipeline_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["deftunes", "glue", "dbt", "lakehouse"],
) as dag:

    start = EmptyOperator(task_id="start")
    extract = EmptyOperator(task_id="glue_extract_songs")
    transform = EmptyOperator(task_id="glue_transform_songs_iceberg")
    dq_check = EmptyOperator(task_id="glue_data_quality_check")
    dbt_run = EmptyOperator(task_id="dbt_run_serving_models")
    end = EmptyOperator(task_id="end")

    start >> extract >> transform >> dq_check >> dbt_run >> end
