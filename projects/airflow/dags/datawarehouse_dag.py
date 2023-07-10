from datetime import datetime, timedelta

from airflow import DAG

from operators.at_least_once_dag_run_sensor import AtLeastOnceDagRunSensor
from operators.spark_docker_operator import SparkBatchDockerOperator
from operators.trino_sql_operator import TrinoSQLOperator

with DAG(
        "datawarehouse",
        start_date=datetime(2009, 1, 1),
        schedule_interval="0 5 * * *",
        default_args={
            'retries': 6,
            'retry_delay': timedelta(minutes=10)
        }
) as dag:
    storage_ready_sensor = AtLeastOnceDagRunSensor(
        task_id="storage_ready_sensor",
        external_dag_id="storage",
    )

    import_national_grid_demand = SparkBatchDockerOperator(
        spark_script="batch_jobs/datalake/import_national_grid_demand.py",
        partition="{{ ds }}",
    )

    national_grid_demand_by_day = SparkBatchDockerOperator(
        spark_script="batch_jobs/datawarehouse/national_grid_demand_by_day.py",
        partition="{{ ds }}",
    )

    sync_query_engine_metadata = TrinoSQLOperator(
        task_id="sync_demand_metadata",
        directory="demand",
        scripts=[
            "use.sql",
            "sync.sql"
        ]
    )

    storage_ready_sensor >> import_national_grid_demand >> [national_grid_demand_by_day, sync_query_engine_metadata]
