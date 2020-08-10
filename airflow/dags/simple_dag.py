from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import sys

# this function and the one below are from this page:
# https://forum.astronomer.io/t/can-i-get-email-notifications-when-tasks-succeed/408
        
def print_hello():
    s =f"Oy lad I'll hook ya gabba! {sys.version}"
    print(s + " inside here!")  # This does not get printed w `airflow test...`
    # raise Exception("testing failures")
    return s

default_args = {
"owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 6, 6),
    "email_on_failure": True,
    "email_on_retry": False,
    #"email": "thmsmcclintock@gmail.com",
    #"on_success_callback": task_success_callback,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

# Note - if the dag_id changes you need to rerun `airflow scheduler`
dag = DAG(
        dag_id="example",
        description="My tutorial DAG",
        schedule_interval="30 * * * *",
        default_args=default_args,
        catchup=False,
)

t1 = DummyOperator(task_id="dummy_task", retries=3, dag=dag)

t2 = PythonOperator(task_id="hello_task", python_callable=print_hello, dag=dag)

# Set downstrem for t1
t1 >> t2
# equivalent to
# t2.set_upstream(t1)
