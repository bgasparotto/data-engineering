import pytest
from pyspark.sql.types import StructType, StructField, DateType, IntegerType

from batch_jobs.datalake.national_grid_demand import process
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
            ("01-APR-2009", 1, 37910, 38704, 33939, 1403, 54, 0, 0),
            ("01-APR-2009", 2, 38047, 38964, 34072, 1403, 53, 0, 0),
            ("2022-01-01", 1, 21940, 23275, 20513, 6527, 2412, 13670, 0),
            ("2022-01-01", 2, 22427, 23489, 21021, 6527, 2554, 13670, 0),
        ],
        [
            "SETTLEMENT_DATE",
            "SETTLEMENT_PERIOD",
            "ND",
            "TSD",
            "ENGLAND_WALES_DEMAND",
            "EMBEDDED_WIND_CAPACITY",
            "EMBEDDED_WIND_GENERATION",
            "EMBEDDED_SOLAR_CAPACITY",
            "EMBEDDED_SOLAR_GENERATION"
        ]
    )


def test_process_returns_expected_schema(df_test_input):
    expected_schema = StructType([
        StructField("settlement_date", DateType()),
        StructField("settlement_period", IntegerType()),
        StructField("national_demand", IntegerType()),
        StructField("transmission_system_demand", IntegerType()),
        StructField("england_wales_demand", IntegerType()),
        StructField("embedded_wind_capacity", IntegerType()),
        StructField("embedded_wind_generation", IntegerType()),
        StructField("embedded_solar_capacity", IntegerType()),
        StructField("embedded_solar_generation", IntegerType()),
        StructField("dt", DateType()),
    ])

    df_result = process(df_test_input)

    assert df_result.schema == expected_schema


def test_process_returns_expected_data(df_test_input):
    expected_data = [
        ("2009-04-01", "1", "37910", "38704", "33939", "1403", "54", "0", "0", "2009-04-01"),
        ("2009-04-01", "2", "38047", "38964", "34072", "1403", "53", "0", "0", "2009-04-01"),
        ("2022-01-01", "1", "21940", "23275", "20513", "6527", "2412", "13670", "0", "2022-01-01"),
        ("2022-01-01", "2", "22427", "23489", "21021", "6527", "2554", "13670", "0", "2022-01-01"),
    ]

    df_result = process(df_test_input)

    actual_data = [tuple(str(col) for col in row) for row in df_result.collect()]
    assert actual_data == expected_data
