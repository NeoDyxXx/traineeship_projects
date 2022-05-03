from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.models import Variable
from MyOperator import MyOperator


default_args = {
    'owner': 'airflow',
    'retries': 1
}


def secret_function():
    secret_key = Variable.get("secret_key")


with DAG(
    dag_id='secret_vars',
    default_args=default_args,
    schedule_interval='0 11,17 * * *',
    start_date=days_ago(1),
    tags=['POC'],
    max_active_runs=1
) as dag:
    my_operator = MyOperator(
        task_id='Task_1',
        user='yakirik3@gmail.com',
        pwd='jemrjmawyuxhyvpe',
        recipient='kraynov.kirill2015@yandex.ru'
    )