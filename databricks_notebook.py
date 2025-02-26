# Databricks Notebook: COVID-19 Analysis

# Import Libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max, avg, stddev, expr, month, year

# Initialize Spark Session
spark = SparkSession.builder.appName("COVID Analysis").getOrCreate()

# Load Data
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("dbfs:/FileStore/OWID_COVID19_data_4_Project5.csv")

# Display Data
display(df)

# Data Cleaning & Filtering
df = df.filter((col('people_fully_vaccinated_per_hundred') > 0) & (col('new_cases_per_million') > 0))

# Create Month and Year Columns
df = df.withColumn("month", month("date"))
df = df.withColumn("year", year("date"))

# Filter for September & October 2021
df = df.filter((df["year"] == 2021) & (df["month"].isin([9, 10])))

# Calculate Averages
avg_df = df.groupBy("continent", "month").agg(
    avg("people_fully_vaccinated_per_hundred").alias("avg_vaccination"),
    avg("new_cases_per_million").alias("avg_new_cases"),
    avg("excess_mortality").alias("avg_excess_mortality")
)

# Display Aggregated Data
display(avg_df)

# Correlation Analysis
correlation = avg_df.stat.corr("avg_vaccination", "avg_new_cases")
print("Correlation:", correlation)
