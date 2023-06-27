FROM apache/airflow:2.6.2

RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --no-cache-dir apache-airflow-providers-docker==3.7.0

COPY ./entrypoint.sh /entrypoint.sh
COPY dags /opt/airflow/dags

ENTRYPOINT  [ "/entrypoint.sh" ]
