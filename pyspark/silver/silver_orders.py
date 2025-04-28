from pyspark.sql import SparkSession

def revome_prefix_from_columns(df, prefix):
    for col in df.columns:
        if col.startswith(prefix):
            df = df.withColumnRenamed(col, col.replace(prefix, ""))
    return df

# Create sparkSession
spark = SparkSession.builder.appName("SilverOrders").getOrCreate()

# Input PARQUET path
AIRFLOW_HOME = "/home/marianela/Documentos/BulkConsulting/Cursos/3-Engenharia-de-dados/3-Apache-Airflow/lakehouse-airflow"
input_path = f"{AIRFLOW_HOME}/lakehouse/bronze/orders.parquet"

# Exit route in Parquet format
output_path = f"{AIRFLOW_HOME}/lakehouse/silver/orders.parquet"

# Read parquet
df = spark.read.parquet(input_path)
df = revome_prefix_from_columns(df, "order_")
df.write.mode("overwrite").parquet(output_path)

spark.stop()