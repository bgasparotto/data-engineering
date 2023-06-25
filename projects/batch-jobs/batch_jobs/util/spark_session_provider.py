import os

from pyspark import SparkConf
from pyspark.sql import SparkSession


def get_or_create() -> SparkSession:
    aws_endpoint = os.getenv("AWS_ENDPOINT", "http://localhost:4566")
    aws_access_key = os.getenv("AWS_ACCESS_KEY", "test_key_id")
    aws_secret_key = os.getenv("AWS_SECRET_KEY", "test_access_key")

    conf: SparkConf = SparkConf()
    conf.set("spark.hadoop.fs.s3a.endpoint", aws_endpoint)
    conf.set("spark.hadoop.fs.s3a.access.key", aws_access_key)
    conf.set("spark.hadoop.fs.s3a.secret.key", aws_secret_key)
    conf.set("spark.hadoop.fs.s3a.path.style.access", "true")
    conf.set(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.3.1,org.postgresql:postgresql:42.6.0"
    )

    return SparkSession.builder.config(conf=conf).getOrCreate()
