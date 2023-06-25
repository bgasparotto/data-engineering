# Data Engineering

Data Engineering code examples for batch processing with Python, Spark and Airflow.

This project attempts to put together some data technology tools and concepts in a simple way, including
batch processing, task orchestration and usage of different data storage technologies.

## Disclaimer

I am constantly adding new jobs and expanding the data architecture in this project. Although I am not squashing
commits, I am trying to ensure the Git history tells a fair story of its evolution :)

This project uses _docker compose_ to provide services that comprise the stack, including:
- **Localstack** for AWS S3 with initial datasets and S3 bucket as the datalake
- **Postgres** as the data warehouse storage
- **Airflow** for task orchestration - work in progress

## Running

1. Run Docker Compose:
```shell
docker compose up -d
```

2. Builder and run the Spark batch jobs container:
```shell
docker build -f projects/batch-jobs/Dockerfile -t batch-jobs:latest ./projects/batch-jobs
docker run --network data-engineering_default -it --rm batch-jobs:latest bash
```

3. Submit a job with `spark-submit`:
```shell
AWS_ENDPOINT="http://localstack:4566" POSTGRES_HOST="postgres:5432" spark-submit --packages="org.apache.hadoop:hadoop-aws:3.3.1,org.postgresql:postgresql:42.6.0" batch_jobs/datalake/national_grid_demand.py
```

## Intellij

1. Load the subproject [batch-jobs](projects/batch-jobs) as a project itself.
2. Follow its [README.md](projects/batch-jobs/README.md) instructions.
