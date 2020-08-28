from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.email import send_email_smtp
import os, sys

        
def print_hello():
    s =f"Oy lad I'll hook ya gabba! {sys.version}"
    print(s + " inside here!")  # This does not get printed w `airflow test...`
    # raise Exception("testing failures")
    body = "this is the body"
    header = "this is the header"
    address = "thmsmcclintock@gmail.com"
    mail_cmd = f"echo \"{body}\" | mail -s \"{header}\" {address}"
    os.system(mail_cmd)
    return s

default_args = {
"owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 6, 6),
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

# Note - if the dag_id changes you need to rerun `airflow scheduler`
dag = DAG(
        dag_id="example",
        description="My tutorial DAG",
        schedule_interval="11 * * * *",
        default_args=default_args,
        catchup=False,
)

t1 = DummyOperator(task_id="dummy_task", retries=3, dag=dag)

t2 = PythonOperator(task_id="hello_task", python_callable=print_hello, dag=dag)

# Set downstrem for t1
t1 >> t2
# equivalent to
# t2.set_upstream(t1)
