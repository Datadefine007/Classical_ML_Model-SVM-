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

# Create a list of tuples with the new data (20 records)
new_data = [
    ("Sophia", 52000, 26, "Vancouver", "ABC Inc Canada"),
    ("Liam", 61000, 31, "Toronto", "XYZ Corp Canada"),
    ("Emma", 74000, 36, "Montreal", "123 Ltd Canada"),
    ("Noah", 79000, 29, "Calgary", "PQR Enterprises Canada"),
    ("Ava", 56000, 33, "Edmonton", "456 Company Canada"),
    ("Jackson", 73000, 38, "Ottawa", "LMN Solutions Canada"),
    ("Isabella", 68000, 28, "Quebec City", "789 Industries Canada"),
    ("Lucas", 91000, 43, "Winnipeg", "DEF Limited Canada"),
    ("Aria", 63000, 30, "Halifax", "GHI Corporation Canada"),
    ("Ethan", 75000, 35, "Saskatoon", "JKL Co Canada"),
    ("Mila", 82000, 40, "Regina", "MNO Enterprises Canada"),
    ("Oliver", 69000, 32, "Victoria", "PST Inc Canada"),
    ("Amelia", 87000, 37, "Hamilton", "UVW Corporation Canada"),
    ("William", 64000, 27, "London", "XYZ Ltd Canada"),
    ("Sophie", 94000, 42, "Windsor", "123 Solutions Canada"),
    ("Mason", 60000, 34, "Oshawa", "ABC Co Canada"),
    ("Lily", 79000, 39, "Barrie", "456 Enterprises Canada"),
    ("Elijah", 66000, 29, "Kingston", "789 Ltd Canada"),
    ("Harper", 96000, 45, "Niagara Falls", "DEF Solutions Canada"),
    ("Logan", 63000, 31, "Sudbury", "GHI Corporation Canada")
]

# Create a DataFrame using the schema and new data
new_df = spark.createDataFrame(new_data, schema=schema)

# Show the new DataFrame
new_df.show()









