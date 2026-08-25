from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
with DAG("data_quality", start_date=datetime(2026,1,1), schedule="@daily", catchup=False) as dag:
    quality=BashOperator(task_id="validate", bash_command="python /opt/airflow/src/validate.py")
