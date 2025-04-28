from pyspark.sql import SparkSession

# Create sparkSession
spark = SparkSession.builder \
    .appName("BronzeCustomers") \
    .getOrCreate()

# Ruta del JSON de entrada
AIRFLOW_HOME="/home/marianela/Documentos/BulkConsulting/Cursos/3-Engenharia-de-dados/3-Apache-Airflow/lakehouse-airflow"
input_path = f"{AIRFLOW_HOME}/lakehouse/landing/customers.json"

# Ruta de salida en formato Parquet
output_path = f"{AIRFLOW_HOME}/lakehouse/bronze/customers.parquet"

# read JSON
df = spark.read.json(input_path)

# Writing like Parquet
df.write.mode("overwrite").parquet(output_path)

print("✅ Bronze transformation completed: JSON → Parquet")

spark.stop()
