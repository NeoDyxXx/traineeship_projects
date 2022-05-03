from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def _training_model():
    return '''Airflow полезно было бы использовать для каких нибудь задач которые должны переодически повторятся.
    До пустим переодическое обучение нейросети, репликация баз данных, парсеринг данных, очистка мусора в веб приложениях и т.д.
    Что касается оркестрации, ее можно использовать для паралелизации и последовательного выполнения задач. На данных момент точно не знаю, как работает аркестрация в Airflow,
    но если прикинуть, допустим можно выполнить первый кусок кода, затем запустить сразу несколько для вычислений и вконце когда все завершаться выполнить последнюю задачу.'''

with DAG("my_dag",
    schedule_interval="@daily", start_date=days_ago(1), catchup=False) as dag:

        training_model_A = PythonOperator(
            task_id="training_model_A",
            python_callable=_training_model
        )