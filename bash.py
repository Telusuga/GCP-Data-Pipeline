import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime as dt,timedelta
from airflow.operators.bash_operator import BashOperator



default_args={
  'retries':1,
  'retry_delay':timedelta(minutes=1)
}

dag= DAG(
  start_date=dt(2024,3,30),
  dag_id='v1',
  schedule_interval='30 17 * * *',
  default_args=default_args,
  catchup=False
) 


d1=DummyOperator(
  task_id='start',
  dag=dag
)


d2=DummyOperator(
  task_id='end',
  dag=dag
)


t1=BashOperator(
  task_id='Bask_check',
  bash_command='python /home/airflow/gcs/dags/scripts/gcs_push.py',
  dag=dag
)


d1 >> t1 >> d2
