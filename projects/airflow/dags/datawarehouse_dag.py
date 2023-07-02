from datetime import datetime, timedelta

from airflow import DAG

from operators.spark_docker_operator import SparkBatchDockerOperator

with DAG(
        "datawarehouse",
        start_date=datetime(2009, 1, 1),
        schedule_interval="0 5 * * *",
        default_args={
            'retries': 6,
            'retry_delay': timedelta(minutes=10)
        }
) as dag:
    import_national_grid_demand = SparkBatchDockerOperator(
        spark_script="batch_jobs/datalake/import_national_grid_demand.py",
        partition="{{ ds }}",
    )

    national_grid_demand_by_day = SparkBatchDockerOperator(
        spark_script="batch_jobs/datawarehouse/national_grid_demand_by_day.py",
        partition="{{ ds }}",
    )

    import_national_grid_demand >> national_grid_demand_by_day
