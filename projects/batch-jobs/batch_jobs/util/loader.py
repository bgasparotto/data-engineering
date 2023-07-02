from pyspark.sql import DataFrame

from batch_jobs.util.args_parser import DatePartition
from batch_jobs.util.database import PsycopgDbContext, DbEnv


def load_parquet_into_s3(df: DataFrame, bucket: str, path: str) -> None:
    path = f"s3a://{bucket}/{path}"
    df.write.parquet(path, mode="overwrite")


def clean_db_partition(db: str, table_name: str, partition: DatePartition):
    with PsycopgDbContext(db) as db_context:
        sql = f"delete from {table_name} where \"date\" = %s"
        db_context.execute(sql, (partition.value,))


def load_table_into_db(df: DataFrame, db: str, table_name: str) -> None:
    db_env = DbEnv()

    df.write.jdbc(
        url=f"jdbc:postgresql://{db_env.host}/{db}",
        table=table_name,
        properties={
            "user": db_env.user,
            "password": db_env.password,
            "driver": "org.postgresql.Driver",
        },
        mode="append"
    )
