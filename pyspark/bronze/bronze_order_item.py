import os
from pyspark.sql import SparkSession

# Create sparkSession
spark = SparkSession.builder \
    .appName("BronzeOrderItem") \
    .getOrCreate()

# Input JSON path
AIRFLOW_HOME = os.getenv("AIRFLOW_HOME")
PROJECT_PATH = os.path.dirname(AIRFLOW_HOME)

input_path = f"{PROJECT_PATH}/lakehouse/landing/order_item.json"

# Exit route in Parquet format
output_path = f"{PROJECT_PATH}/lakehouse/bronze/order_item.parquet"

# read JSON
df = spark.read.json(input_path)

# Writing like Parquet
df.write.mode("overwrite").parquet(output_path)

print("✅ Bronze transformation completed: JSON → Parquet")

spark.stop()