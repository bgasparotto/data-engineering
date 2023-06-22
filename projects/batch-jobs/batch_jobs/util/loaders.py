from pyspark.sql import DataFrame


def load_into_s3(df: DataFrame) -> None:
    df.show()  # WIP
