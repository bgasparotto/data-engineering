from pyspark import SparkConf
from pyspark.sql import SparkSession


def get_or_create() -> SparkSession:
    conf: SparkConf = SparkConf()
    conf.set("spark.hadoop.fs.s3a.endpoint", "http://localhost:4566")
    conf.set("spark.hadoop.fs.s3a.access.key", "test_key_id")
    conf.set("spark.hadoop.fs.s3a.secret.key", "test_access_key")
    conf.set("spark.hadoop.fs.s3a.path.style.access", "true")
    conf.set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.1")

    return SparkSession.builder.config(conf=conf).getOrCreate()
