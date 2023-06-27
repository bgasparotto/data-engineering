from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.dummy_operator import DummyOperator

with DAG(
        "datawarehouse",
        start_date=datetime(2009, 1, 1),
        schedule_interval="0 5 * * *",
        default_args={
            'retries': 6,
            'retry_delay': timedelta(minutes=10)
        }
) as dag:
    start_dag = DummyOperator(
        task_id="start_dag"
    )

    national_grid_demand_by_day = DockerOperator(
        task_id="national_grid_demand_by_day",
        image="batch-jobs:latest",
        environment={
            "AWS_ENDPOINT": "http://localstack:4566",
            "POSTGRES_HOST": "postgres:5432",
        },
        container_name="national_grid_demand_by_day_{{ ds }}",
        command='spark-submit --packages="org.apache.hadoop:hadoop-aws:3.3.1,org.postgresql:postgresql:42.6.0" batch_jobs/datawarehouse/national_grid_demand_by_day.py --partition {{ ds }}',
        network_mode="data-engineering_default",
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
    )

    end_dag = DummyOperator(
        task_id="end_dag"
    )

    start_dag >> national_grid_demand_by_day >> end_dag
