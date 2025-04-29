import os
from pyspark.sql import SparkSession

def revome_prefix_from_columns(df, prefix):
    for col in df.columns:
        if col.startswith(prefix):
            df = df.withColumnRenamed(col, col.replace(prefix, ""))
    return df

# Create sparkSession
spark = SparkSession.builder.appName("SilverOrderItem").getOrCreate()

# Input PARQUET path
AIRFLOW_HOME = os.getenv("AIRFLOW_HOME")
PROJECT_PATH = os.path.dirname(AIRFLOW_HOME)

input_path = f"{PROJECT_PATH}/lakehouse/bronze/order_item.parquet"

# Exit route in Parquet format
output_path = f"{PROJECT_PATH}/lakehouse/silver/order_item.parquet"

# Read parquet
df = spark.read.parquet(input_path)
df = revome_prefix_from_columns(df, "order_item_")
df.write.mode("overwrite").parquet(output_path)

spark.stop()