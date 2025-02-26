from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, month, year

# Initialize Spark Session
spark = SparkSession.builder.appName("COVID Analysis").getOrCreate()

# Load Data
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("dbfs:/FileStore/OWID_COVID19_data_4_Project5.csv")

# Filter & Process Data
df = df.filter((col('people_fully_vaccinated_per_hundred') > 0) & (col('new_cases_per_million') > 0))
df = df.withColumn("month", month("date"))
df = df.withColumn("year", year("date"))
df = df.filter((df["year"] == 2021) & (df["month"].isin([9, 10])))

# Compute Averages
avg_df = df.groupBy("continent", "month").agg(
    avg("people_fully_vaccinated_per_hundred").alias("avg_vaccination"),
    avg("new_cases_per_million").alias("avg_new_cases"),
    avg("excess_mortality").alias("avg_excess_mortality")
)

# Show Aggregated Data
avg_df.show()
