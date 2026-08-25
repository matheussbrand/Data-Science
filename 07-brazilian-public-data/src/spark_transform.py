from pyspark.sql import SparkSession, functions as F
spark=SparkSession.builder.appName("public-data").getOrCreate()
df=spark.read.json("data/raw/municipios.json")
(df.withColumn("municipio",F.upper("nome"))
   .select("municipio","codigo_ibge")
   .write.mode("overwrite").parquet("data/processed/municipios"))
spark.stop()
