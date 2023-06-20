from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col

from batch_jobs.util.extractor import extract_from_csv
from batch_jobs.util.loaders import load_into_db


def transform(df_demand: DataFrame) -> DataFrame:
    return df_demand.select(
        "settlement_date",
        "settlement_period",
        col("nd").alias("national_demand"),
        col("tsd").alias("transmission_system_demand"),
        "england_wales_demand",
        "embedded_wind_capacity",
        "embedded_wind_generation",
        "embedded_solar_capacity",
        "embedded_solar_generation",
    )


if __name__ == "__main__":
    spark: SparkSession = SparkSession.builder.getOrCreate()

    df_input: DataFrame = extract_from_csv(spark, "national_grid_demand/demanddata_2009.csv")
    df_output: DataFrame = transform(df_input)
    load_into_db(df_output)

    spark.stop()
