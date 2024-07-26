from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
with DAG(
    'import_db',
    default_args={
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(seconds=3)
    },
    description='import_db DAG',
    #schedule_interval=timedelta(days=1),
    schedule="10 4 * * *",
    start_date=datetime(2024, 7, 12),
    catchup=True,
    tags=['simple', 'bash', 'etl', 'shop'],
) as dag:
    task_start = EmptyOperator(
            task_id ='start',
            )

    task_get_data= BashOperator(
            task_id ='get_data',
            bash command="""
            echo "get_data"
            """
            )
    task_save_data= BashOperator(
            task_id ='save_data',
            bash command="""
            echo "save_data"
            """
            )

    task_end = EmptyOperator(
            task_id ='end',
            )


    task_start >> task_get_data >> task_save_data >> task_end
