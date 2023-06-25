import os

from pyspark.sql import DataFrame


def load_parquet_into_s3(df: DataFrame, bucket: str, path: str) -> None:
    path = f"s3a://{bucket}/{path}"
    df.write.partitionBy("dt").parquet(path, mode="overwrite")


def load_table_into_db(df: DataFrame, db: str, table_name: str) -> None:
    host = os.getenv("POSTGRES_HOST", "localhost:5432")
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "password")

    df.write \
        .format("jdbc") \
        .option("url", f"jdbc:postgresql://{host}/{db}") \
        .option("dbtable", table_name) \
        .option("user", user) \
        .option("password", password) \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()
