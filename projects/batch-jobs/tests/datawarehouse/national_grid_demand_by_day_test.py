import pytest
from pyspark.sql.types import StructType, StructField, DateType, IntegerType, LongType, StringType

from batch_jobs.datawarehouse.national_grid_demand_by_day import process
from batch_jobs.util import spark_session_provider


@pytest.fixture(autouse=True)
def run_before_and_after_tests(spark):
    yield

    spark.stop()


@pytest.fixture()
def spark():
    return spark_session_provider.get_or_create()


@pytest.fixture()
def df_test_input(spark):
    return spark.createDataFrame(
        [
            ("2009-04-01", 1, 37910, 38704, 33939, 1403, 54, 0, 0),
            ("2009-04-01", 2, 38047, 38964, 34072, 1403, 53, 0, 0),
            ("2009-04-01", 3, 21940, 23275, 20513, 1403, 60, 0, 0),
        ],
        [
            "settlement_date",
            "settlement_period",
            "national_demand",
            "transmission_system_demand",
            "england_wales_demand",
            "embedded_wind_capacity",
            "embedded_wind_generation",
            "embedded_solar_capacity",
            "embedded_solar_generation"
        ]
    )


def test_process_returns_expected_schema(df_test_input):
    expected_schema = StructType([
        StructField("date", DateType()),
        StructField("max_national_demand", LongType()),
        StructField("min_national_demand", LongType()),
        StructField("avg_national_demand", LongType()),
        StructField("max_transmission_system_demand", LongType()),
        StructField("min_transmission_system_demand", LongType()),
        StructField("avg_transmission_system_demand", LongType()),
        StructField("unit", StringType(), False),
    ])

    df_result = process(df_test_input)

    assert df_result.schema == expected_schema


def test_process_returns_expected_data(df_test_input):
    expected_data = [
        ("2009-04-01", "38047", "21940", "32632", "38964", "23275", "33648", "MW"),
    ]

    df_result = process(df_test_input)

    actual_data = [tuple(str(col) for col in row) for row in df_result.collect()]
    assert actual_data == expected_data
