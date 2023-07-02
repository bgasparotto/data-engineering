import os
from dataclasses import dataclass

import psycopg2


@dataclass
class DbEnv:
    host: str = os.getenv("POSTGRES_HOST", "localhost:5432")
    user: str = os.getenv("POSTGRES_USER", "postgres")
    password: str = os.getenv("POSTGRES_PASSWORD", "password")


class PsycopgDbContext:
    def __init__(self, db: str) -> None:
        db_env = DbEnv()
        host, port = db_env.host.split(":")

        self.db_conf = {
            "host": host,
            "port": port,
            "database": db,
            "user": db_env.user,
            "password": db_env.password,
        }

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_conf)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
