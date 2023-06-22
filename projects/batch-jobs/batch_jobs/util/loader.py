from pyspark.sql import DataFrame


def load_parquet_into_s3(df: DataFrame, bucket: str, path: str) -> None:
    path = f"s3a://{bucket}/{path}"
    df.write.partitionBy("dt").parquet(path, mode="overwrite")


def load_table_into_db(df: DataFrame, db: str, table_name: str) -> None:
    df.write \
        .format("jdbc") \
        .option("url", f"jdbc:postgresql://localhost:5432/{db}") \
        .option("dbtable", table_name) \
        .option("user", "postgres") \
        .option("password", "password") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()
