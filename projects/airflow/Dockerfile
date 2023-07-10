FROM batch-jobs:latest AS batch

FROM apache/airflow:2.6.2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
COPY dags /opt/airflow/dags
COPY --from=batch /app/db /app/db
ADD operators /opt/airflow/plugins/operators

ENTRYPOINT  [ "/entrypoint.sh" ]
