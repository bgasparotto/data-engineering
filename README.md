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
- [hive-metastore](projects/hive-metastore) - Hive standalone metastore for mapping partitioned parquet files on S3.

## Running all together

1. Build the Spark batch jobs container:

```shell
docker build -f projects/batch-jobs/Dockerfile -t batch-jobs:latest ./projects/batch-jobs
```

2. Run Docker Compose:

```shell
docker compose up --build
```

## Inspecting stuff

- View Airflow at http://localhost:8080 with user `admin` and password `admin`.
- Monitor Trino at http://localhost:8081 with user `trino`.
- Watch the Docker tasks being spawned with `watch -n1 docker ps`.

## Querying data

- Query the **datalake** on `jdbc:trino://localhost:8081/hive` with user `trino` and no password.
- Query the **data warehouse** on `jdbc:postgresql://localhost:5432/data_warehouse` with user `postgres` and
  password `password`.
- If you are curious, query the **hive metastore** on `jdbc:postgresql://localhost:5452/hive` with user `postgres` and
  password `password`.

## Intellij

1. Load one of the projects such as [batch-jobs](projects/batch-jobs) as a project itself.
2. Follow the respective `README.md` for build and run instructions.

## Notes and Concepts

- [SQL](notes/sql.md)
