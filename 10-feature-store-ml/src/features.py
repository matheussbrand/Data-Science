from pyspark.sql import SparkSession, functions as F
spark=SparkSession.builder.appName("feature-store").getOrCreate()
events=spark.read.parquet("data/events")
features=(events.groupBy("customer_id")
          .agg(F.count("*").alias("orders_30d"),
               F.sum("amount").alias("revenue_30d"),
               F.avg("amount").alias("avg_order_value")))
features.write.mode("overwrite").parquet("data/features/customer_features")
spark.stop()
