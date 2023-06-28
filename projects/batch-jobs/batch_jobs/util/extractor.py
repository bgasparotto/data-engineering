from pyspark.sql import DataFrame, SparkSession

from batch_jobs.util.args_parser import DatePartition


def extract_csv_from_s3(spark: SparkSession, bucket: str, path: str) -> DataFrame:
    path = f"s3a://{bucket}/{path}"

    return spark.read.option("header", True).csv(path)


def extract_parquet_from_s3(
        spark: SparkSession,
        bucket: str,
        path: str,
        partition: DatePartition,
) -> DataFrame:
    path = f"s3a://{bucket}/{path}/{partition}/"

    return spark.read.parquet(path)
