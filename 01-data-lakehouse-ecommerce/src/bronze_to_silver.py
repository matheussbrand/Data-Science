from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("ecommerce-lakehouse").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True).csv("data/raw/orders.csv")

silver = (
    df.dropDuplicates(["order_id"])
      .withColumn("order_date", F.to_date("order_date"))
      .withColumn("total_amount", F.col("quantity") * F.col("unit_price"))
      .filter(F.col("order_id").isNotNull())
)

silver.write.mode("overwrite").partitionBy("order_date").parquet("data/processed/silver/orders")
spark.stop()
