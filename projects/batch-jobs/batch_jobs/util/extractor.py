from pyspark.sql import DataFrame, SparkSession


def extract_from_s3(spark: SparkSession, short_path: str) -> DataFrame:
    path = f"s3a://national-grid-eso/{short_path}"

    return spark.read.option("header", True).csv(path)
