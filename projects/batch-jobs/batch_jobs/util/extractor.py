from pyspark.sql import DataFrame, SparkSession

DATASET_BASE_PATH: str = "../../../../datasets"


def extract_from_csv(spark: SparkSession, short_path: str) -> DataFrame:
    path = f"{DATASET_BASE_PATH}/{short_path}"

    return spark.read.option("header", True).csv(path)
