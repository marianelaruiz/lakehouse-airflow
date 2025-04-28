from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct, count, sum as _sum


# Create sparkSession
spark = SparkSession.builder.appName("GoldLayer").getOrCreate()

# Input PARQUET path
AIRFLOW_HOME = "/home/marianela/Documentos/BulkConsulting/Cursos/3-Engenharia-de-dados/3-Apache-Airflow/lakehouse-airflow"


# Read data from the Silver layer
customers = spark.read.parquet(f"{AIRFLOW_HOME}/lakehouse/silver/customers.parquet")
orders = spark.read.parquet(f"{AIRFLOW_HOME}/lakehouse/silver/orders.parquet")
order_item = spark.read.parquet(f"{AIRFLOW_HOME}/lakehouse/silver/order_item.parquet")

# Join customers with orders
orders_with_customers = orders.join(customers, orders.customer_id == customers.id).select(
            orders["id"].alias("order_id"),
            orders["customer_id"],            
            customers["city"],
            customers["state"]
        )

# Join with order_item
# Note: Some orders don-t have items(left join)
full_data = orders_with_customers.join(order_item, orders_with_customers.order_id == order_item.order_id, "left").select(
            orders_with_customers["order_id"],
            order_item["subtotal"],
            orders_with_customers["city"],
            orders_with_customers["state"]
        )


#full_data.filter(full_data.city == "Norwalk").show(truncate=False)


# Grouping and calculation
summary = full_data.groupBy("city", "state") \
    .agg(
        countDistinct("order_id").alias("order_quantity"),
        _sum("subtotal").alias("total_order_value")
    )

# Save result in Parquet
summary.write.mode("overwrite").parquet(f"{AIRFLOW_HOME}/lakehouse/gold/summary_orders.parquet")

# Show ten rows
summary.show(10, truncate=False)

spark.stop()
