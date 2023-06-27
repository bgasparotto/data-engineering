ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}-bookworm

ARG PYTHON_VERSION
ARG AIRFLOW_VERSION=2.6.2

ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
RUN pip install apache-airflow-providers-docker

COPY ./entrypoint.sh /entrypoint.sh
COPY dags /root/airflow/dags

ENTRYPOINT  [ "./entrypoint.sh" ]
