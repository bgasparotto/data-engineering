from airflow.models.dag import get_last_dagrun
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.db import provide_session
from sqlalchemy.orm.session import Session


# noinspection PyUnusedLocal
@provide_session
def get_execution_of_storage_dag(*args, session: Session, **kwargs):
    storage_last_run = get_last_dagrun("storage", session)
    return storage_last_run.execution_date


class AtLeastOnceDagRunSensor(ExternalTaskSensor):
    def __init__(
            self,
            task_id: str,
            external_dag_id: str,
            **kwargs,
    ):
        super().__init__(
            task_id=task_id,
            external_dag_id=external_dag_id,
            poke_interval=15,  # seconds
            timeout=5 * 60,  # 5 minutes
            execution_date_fn=get_execution_of_storage_dag,
            **kwargs,
        )
