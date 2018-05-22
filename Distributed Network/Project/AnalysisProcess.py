# Import
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

df = spark.read.json("hdfs://master:9000/Analysis/190518/1208.json")
df.show()
