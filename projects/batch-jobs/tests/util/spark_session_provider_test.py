import pytest

from batch_jobs.util import spark_session_provider


@pytest.fixture(autouse=True)
def run_before_and_after_tests(spark):
    yield

    spark.stop()


@pytest.fixture()
def spark():
    return spark_session_provider.get_or_create()


def test_spark_session_conf_has_aws_config(spark):
    conf = spark.sparkContext.getConf()

    assert conf.get("spark.hadoop.fs.s3a.endpoint") == "http://localhost:4566"
    assert conf.get("spark.hadoop.fs.s3a.access.key") == "test_key_id"
    assert conf.get("spark.hadoop.fs.s3a.secret.key") == "test_access_key"
    assert conf.get("spark.hadoop.fs.s3a.path.style.access") == "true"


def test_spark_session_conf_has_extra_jar_packages(spark):
    conf = spark.sparkContext.getConf()
    spark_jar_packages = conf.get("spark.jars.packages").split(",")

    assert "org.apache.hadoop:hadoop-aws:3.3.1" in spark_jar_packages
    assert "org.postgresql:postgresql:42.6.0" in spark_jar_packages
