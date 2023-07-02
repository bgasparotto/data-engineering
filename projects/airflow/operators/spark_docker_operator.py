from airflow.providers.docker.operators.docker import DockerOperator


class SparkBatchDockerOperator(DockerOperator):
    def __init__(
            self,
            spark_script: str,
            partition: str,
            **kwargs,
    ):
        spark_script_short_name = spark_script.split('/')[-1].replace(".py", "")

        super().__init__(
            task_id=spark_script_short_name,
            image="batch-jobs:latest",
            environment={
                "AWS_ENDPOINT": "http://localstack:4566",
                "POSTGRES_HOST": "postgres:5432",
            },
            container_name=f"{spark_script_short_name}_{partition}",
            command=f"bash -c 'spark-submit --packages=$SPARK_EXTRA_PACKAGES {spark_script} --partition {partition}'",
            network_mode="data-engineering_default",
            auto_remove="True",
            docker_url="tcp://docker-proxy:2375",
            **kwargs,
        )
