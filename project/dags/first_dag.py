try:

    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import pandas as pd

    print("All Dag modules are ok ......")
except Exception as e:
    print("Error  {} ".format(e))


def first_function_execute(**context):
    print("Hello World")
    return "Hello World"

with DAG(
        dag_id="first_dag",     # Good idea to give file name as dag_id
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 4, 15),
        },
        catchup=False) as f:

    first_function_execute = PythonOperator(
        task_id="first_function_execute",         # Better to give function name as task_id
        python_callable=first_function_execute
    )
