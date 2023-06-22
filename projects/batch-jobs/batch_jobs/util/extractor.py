from pyspark.sql import DataFrame, SparkSession


def extract_csv_from_s3(spark: SparkSession, bucket: str, path: str) -> DataFrame:
    path = f"s3a://{bucket}/{path}"

    return spark.read.option("header", True).csv(path)
