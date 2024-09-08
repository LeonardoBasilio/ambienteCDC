from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Define Kafka source
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "dbserver1.cdc.client") \
    .option("startingOffsets", "earliest") \
    .load()

# Decode the key and value columns from bytes to strings
df = df.withColumn("key", col("key").cast("string"))
df = df.withColumn("value", col("value").cast("string"))

# Start processing the stream
query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()