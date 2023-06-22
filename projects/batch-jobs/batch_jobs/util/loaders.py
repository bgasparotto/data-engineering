from pyspark.sql import DataFrame


def load_parquet_into_s3(df: DataFrame, bucket: str, path: str) -> None:
    path = f"s3a://{bucket}/{path}"
    df.write.partitionBy("dt").parquet(path, mode="overwrite")
