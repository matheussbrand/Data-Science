from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import *

spark=SparkSession.builder.appName("orders-stream").getOrCreate()
schema=StructType([
    StructField("event_id",IntegerType()), StructField("customer_id",IntegerType()),
    StructField("amount",DoubleType())
])
raw=(spark.readStream.format("kafka").option("kafka.bootstrap.servers","kafka:9092")
     .option("subscribe","orders").load())
events=raw.select(F.from_json(F.col("value").cast("string"),schema).alias("e")).select("e.*")
agg=(events.withWatermark("timestamp","1 minute") if "timestamp" in events.columns else events)
query=agg.writeStream.format("console").outputMode("append").start()
query.awaitTermination()
