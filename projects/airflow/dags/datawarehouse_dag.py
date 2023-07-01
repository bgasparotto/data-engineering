from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
        "datawarehouse",
        start_date=datetime(2009, 1, 1),
        schedule_interval="0 5 * * *",
        default_args={
            'retries': 6,
            'retry_delay': timedelta(minutes=10)
        }
) as dag:
    import_national_grid_demand = DockerOperator(
        task_id="import_national_grid_demand",
        image="batch-jobs:latest",
        environment={
            "AWS_ENDPOINT": "http://localstack:4566",
            "POSTGRES_HOST": "postgres:5432",
        },
        container_name="import_national_grid_demand_{{ ds }}",
        command="bash -c 'spark-submit --packages=$SPARK_EXTRA_PACKAGES batch_jobs/datalake/import_national_grid_demand.py --partition {{ ds }}'",
        network_mode="data-engineering_default",
        auto_remove="True",
        docker_url="tcp://docker-proxy:2375",
    )

    national_grid_demand_by_day = DockerOperator(
        task_id="national_grid_demand_by_day",
        image="batch-jobs:latest",
        environment={
            "AWS_ENDPOINT": "http://localstack:4566",
            "POSTGRES_HOST": "postgres:5432",
        },
        container_name="national_grid_demand_by_day_{{ ds }}",
        command="bash -c 'spark-submit --packages=$SPARK_EXTRA_PACKAGES batch_jobs/datawarehouse/national_grid_demand_by_day.py --partition {{ ds }}'",
        network_mode="data-engineering_default",
        auto_remove="True",
        docker_url="tcp://docker-proxy:2375",
    )

    import_national_grid_demand >> national_grid_demand_by_day
