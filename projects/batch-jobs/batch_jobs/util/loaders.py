from pyspark.sql import DataFrame


def load_into_db(df: DataFrame) -> None:
    df.show()
