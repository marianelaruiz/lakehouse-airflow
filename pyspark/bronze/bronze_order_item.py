from pyspark.sql import SparkSession

# Create sparkSession
spark = SparkSession.builder \
    .appName("BronzeOrderItem") \
    .getOrCreate()

# Input JSON path
AIRFLOW_HOME="/home/marianela/Documentos/BulkConsulting/Cursos/3-Engenharia-de-dados/3-Apache-Airflow/lakehouse-airflow"
input_path = f"{AIRFLOW_HOME}/lakehouse/landing/order_item.json"

# Exit route in Parquet format
output_path = f"{AIRFLOW_HOME}/lakehouse/bronze/order_item.parquet"

# read JSON
df = spark.read.json(input_path)

# Writing like Parquet
df.write.mode("overwrite").parquet(output_path)

print("✅ Bronze transformation completed: JSON → Parquet")

spark.stop()