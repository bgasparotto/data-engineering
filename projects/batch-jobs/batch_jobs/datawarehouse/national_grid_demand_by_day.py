from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import avg, min, max, round, first, to_date

from batch_jobs.util import spark_session_provider
from batch_jobs.util.extractor import extract_parquet_from_s3
from batch_jobs.util.loader import load_table_into_db


def process(df_demand: DataFrame) -> DataFrame:
    return df_demand.agg(
        first(to_date("settlement_date")).alias("date"),
        max("national_demand").alias("max_national_demand"),
        min("national_demand").alias("min_national_demand"),
        round(avg("national_demand")).cast("long").alias("avg_national_demand"),
        max("transmission_system_demand").alias("max_transmission_system_demand"),
        min("transmission_system_demand").alias("min_transmission_system_demand"),
        round(avg("transmission_system_demand")).cast("long").alias("avg_transmission_system_demand"),
    )


if __name__ == "__main__":
    spark: SparkSession = spark_session_provider.get_or_create()

    partition: str = "2009-04-01"

    df_input: DataFrame = extract_parquet_from_s3(spark, bucket="datalake", path="demand", partition=partition)
    df_output: DataFrame = process(df_input)
    load_table_into_db(df_output, db="data_warehouse", table_name="national_grid_demand_by_day")

    spark.stop()
