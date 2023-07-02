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

1. Load the subproject [batch-jobs](projects/batch-jobs) as a project itself.
2. Follow its [README.md](projects/batch-jobs/README.md) instructions.
