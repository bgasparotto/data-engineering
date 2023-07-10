from datetime import datetime

from airflow import DAG

from operators.trino_sql_operator import TrinoSQLOperator

with DAG(
        "storage",
        start_date=datetime(2009, 1, 1),
        schedule_interval="@once",
        catchup=False,
) as dag:
    migrate_trino_demand = TrinoSQLOperator(
        task_id="migrate_trino_demand",
        directory="demand",
        scripts=[
            "schema.sql",
            "table.sql"
        ]
    )

    migrate_trino_demand
