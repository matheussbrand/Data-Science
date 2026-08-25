from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
with DAG("financial_pipeline", start_date=datetime(2026,1,1), schedule="@daily", catchup=False) as dag:
    extract=BashOperator(task_id="extract", bash_command="python /opt/airflow/src/extract_api.py")
    transform=BashOperator(task_id="transform", bash_command="python /opt/airflow/src/transform.py")
    extract >> transform
