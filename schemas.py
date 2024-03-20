from pyspark.sql.types import *

# Define the schema for the DataFrame

example_spark = StructType([
    StructField("Country name", StringType(), True),
    StructField("Series name", StringType(), True),
    StructField("Value", FloatType(), True),
    StructField("value_percentile", FloatType(), True)
])

example_pandas = {
    "Country name": str,
    "Series name": str,
    "Value": float,    
    "value_percentile": float
}