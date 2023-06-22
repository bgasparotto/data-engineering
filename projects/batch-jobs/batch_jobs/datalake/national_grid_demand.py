from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, to_date, coalesce

from batch_jobs.util import spark_session_provider
from batch_jobs.util.extractor import extract_from_s3
from batch_jobs.util.loaders import load_into_s3


def transform(df_demand: DataFrame) -> DataFrame:
    return df_demand.select(
        col("settlement_date"),
        col("settlement_period").cast("int"),
        col("nd").cast("int").alias("national_demand"),
        col("tsd").cast("int").alias("transmission_system_demand"),
        col("england_wales_demand").cast("int"),
        col("embedded_wind_capacity").cast("int"),
        col("embedded_wind_generation").cast("int"),
        col("embedded_solar_capacity").cast("int"),
        col("embedded_solar_generation").cast("int"),
    ).withColumn(
        "settlement_date",
        coalesce(
            to_date("settlement_date"),
            to_date("settlement_date", "dd-MMM-yyyy")
        )
    ).orderBy(
        "settlement_date",
        "settlement_period",
    )


if __name__ == "__main__":
    spark: SparkSession = spark_session_provider.get_or_create()

    df_input: DataFrame = extract_from_s3(spark, "demand")
    df_output: DataFrame = transform(df_input)
    load_into_s3(df_output)

    spark.stop()
