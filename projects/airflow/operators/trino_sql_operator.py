from typing import List

from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


class TrinoSQLOperator(SQLExecuteQueryOperator):
    base_path: str = "/app/db/trino"

    def __init__(
            self,
            task_id: str,
            directory: str,
            scripts: List[str],
            **kwargs,
    ):
        super().__init__(
            task_id=task_id,
            conn_id="trino_hive",
            max_active_tis_per_dag=1,
            sql=self.read_scripts(directory, scripts),
            **kwargs,
        )

    def read_scripts(self, directory: str, scripts: List[str]) -> List[str]:
        return [self.read_script(directory, script) for script in scripts]

    def read_script(self, directory: str, script: str) -> str:
        path = f"{self.base_path}/{directory}/{script}"

        with open(path, "r") as script_file:
            return script_file.read().replace(";", "")
