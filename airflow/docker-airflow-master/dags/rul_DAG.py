from airflow import DAG
#from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# instantiate DAG
with DAG(
    'rul-workflow',
    default_args={
        'owner': 'Dinush De Alwis', 
        'depends_on_past': False,
        'email': ['dinushdealwis@gmail.com'], 
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        },
    description='Predicting Remaining Useful Life of Turbofan Engines',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 12, 18)
) as dag:

    # load data to raw data folder
    get__data = BashOperator(
        task_id='get_data',
        bash_command="Hello World",
    )

