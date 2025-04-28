from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

def bronze():
    print("🔸 Bronze Layer: Copied JSON data.")

def silver():
    print("🔹 Silver Layer: Renamed columns.")

def gold():
    print("✨ Gold Layer: Aggregate data by city and state.")

with DAG(
    dag_id="dag_lakehouse",
    start_date=datetime(2024, 4, 22),
    schedule_interval=None,  # Execute manually
    catchup=False,
    description="Test DAG to simulate Lakehouse architecture",
    tags=["lakehouse", "test"],
) as dag:
    
    PYSPARK_PATH = "/home/marianela/Documentos/BulkConsulting/Cursos/3-Engenharia-de-dados/3-Apache-Airflow/lakehouse-airflow/pyspark"
    
    # Bronze layer
    bronze_task = BashOperator(
    task_id="bronze_layer",
    bash_command= f"""
    spark-submit {PYSPARK_PATH}/bronze/bronze_customers.py &&
    spark-submit {PYSPARK_PATH}/bronze/bronze_orders.py &&
    spark-submit {PYSPARK_PATH}/bronze/bronze_order_item.py
    """
    )

    # Silver layer
    silver_task = BashOperator(
    task_id="silver_layer",
    bash_command= f"""
    spark-submit {PYSPARK_PATH}/silver/silver_customers.py &&
    spark-submit {PYSPARK_PATH}/silver/silver_orders.py &&
    spark-submit {PYSPARK_PATH}/silver/silver_order_item.py
    """
    )

    # Gold layer
    gold_task = BashOperator(
    task_id="gold_report",
    bash_command= f"spark-submit {PYSPARK_PATH}/gold/gold_report.py"    
    )


    #t2 = PythonOperator(task_id="silver_layer", python_callable=silver)
    #t3 = PythonOperator(task_id="gold_layer", python_callable=gold)

    [bronze_task, silver_task] >> gold_task
