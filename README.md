# Data Engineering

Data Engineering code examples for batch processing with Python, PySpark, Airflow and AWS/Localstack.

This project attempts to put together a few data technology tools and concepts in a simple way, including
batch processing, task orchestration and usage of different data storages.

## Disclaimer

This project uses _docker compose_ to provide services that comprise the stack, including:
- **Localstack** for AWS S3 with initial datasets and S3 bucket as the datalake
- **Postgres** as the data warehouse storage
- **Airflow** for task orchestration
- **Trino** for the query engine
- **Hive Metastore** for data catalogue
- **Docker** for container management

## Projects

- [batch-jobs](projects/batch-jobs) - Spark scripts with pyspark.
- [airflow](projects/airflow) - Airflow DAGs and operators that run the batch jobs.

## Running all together

1. Build the Spark batch jobs container:
```shell
docker build -f projects/batch-jobs/Dockerfile -t batch-jobs:latest ./projects/batch-jobs
```

2. Run Docker Compose:
```shell
docker compose up --build
```

3. (Optional) View Airflow at http://localhost:8080 with user `admin` and password `admin`.

4. (Optional) Watch the Docker tasks being spawned with `watch -n1 docker ps`.

## Intellij

1. Load one of the projects such as [batch-jobs](projects/batch-jobs) as a project itself.
2. Follow the respective `README.md` for build and run instructions.

## Notes and Concepts

- [SQL](notes/sql.md)
