# Databricks notebook source
print("hello_world")

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Define the schema for the DataFrame
schema = StructType([
    StructField("name", StringType(), True),
    StructField("salary", IntegerType(), True),
    StructField("age", IntegerType(), True),
    StructField("location", StringType(), True),
    StructField("company", StringType(), True)
])

# Create a list of tuples with the data (20 records)
data = [
    ("Alice", 50000, 25, "New York", "ABC Inc"),
    ("Bob", 60000, 30, "San Francisco", "XYZ Corp"),
    ("Charlie", 75000, 35, "Los Angeles", "123 Ltd"),
    ("David", 80000, 28, "Chicago", "PQR Enterprises"),
    ("Eva", 55000, 32, "Boston", "456 Company"),
    ("Frank", 70000, 40, "Seattle", "LMN Solutions"),
    ("Grace", 65000, 27, "Denver", "789 Industries"),
    ("Henry", 90000, 45, "Austin", "DEF Limited"),
    ("Ivy", 60000, 29, "Atlanta", "GHI Corporation"),
    ("Jack", 72000, 33, "Miami", "JKL Co"),
    ("Kelly", 78000, 38, "Dallas", "MNO Enterprises"),
    ("Leo", 68000, 31, "Houston", "PST Inc"),
    ("Mia", 85000, 36, "Phoenix", "UVW Corporation"),
    ("Nathan", 63000, 26, "Portland", "XYZ Ltd"),
    ("Olivia", 92000, 42, "San Diego", "123 Solutions"),
    ("Paul", 58000, 34, "Minneapolis", "ABC Co"),
    ("Quincy", 77000, 39, "Detroit", "456 Enterprises"),
    ("Rachel", 67000, 28, "Charlotte", "789 Ltd"),
    ("Sam", 95000, 44, "San Antonio", "DEF Solutions"),
    ("Tom", 61000, 30, "Las Vegas", "GHI Corporation")
]

# Create a DataFrame using the schema and data
df = spark.createDataFrame(data, schema=schema)

# Show the DataFrame
df.show()

