# COVID-19 Data Analysis using Databricks

## Overview
This project explores the relationship between **COVID-19 vaccination rates, case rates, and mortality** across continents using **Databricks and PySpark**. The analysis uses data from **Our World in Data** and aims to determine whether higher vaccination rates correlate with lower COVID-19 cases and mortality.

## Technologies Used
- **Databricks** (Cloud-based big data analysis)
- **PySpark** (Distributed data processing)
- **Pandas** (Data manipulation and analysis)
- **Data Sources**: Our World in Data, World Bank, Wikipedia

---

## Setup Instructions
### 1. Set Up Databricks
1. **Create a Free Databricks Account**
   - Sign up for [Databricks Community Edition](https://databricks.com/product/faq/community-edition) or start a [Databricks Free Trial](https://docs.databricks.com/en/getting-started/free-trial.html).
2. **Launch Databricks and Create a New Cluster**
   - Select an appropriate runtime (recommended: **Databricks Runtime 10.4 LTS**).
3. **Upload Dataset**
   - Download the **OWID_COVID19_data_4_Project5.csv** file and upload it to **DBFS (Databricks File System)**.

### 2. Load & Explore Data
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("COVID Analysis").getOrCreate()

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("dbfs:/FileStore/OWID_COVID19_data_4_Project5.csv")

display(df)
```

### 3. Data Cleaning & Filtering
```python
from pyspark.sql.functions import col

df = df.filter((col('people_fully_vaccinated_per_hundred') > 0) & (col('new_cases_per_million') > 0))
display(df)
```

### 4. Extract Month & Year
```python
from pyspark.sql.functions import month, year

df = df.withColumn("month", month("date"))
df = df.withColumn("year", year("date"))

df = df.filter((df["year"] == 2021) & (df["month"].isin([9, 10])))
```

### 5. Calculate Averages per Continent
```python
from pyspark.sql.functions import avg

avg_df = df.groupBy("continent", "month").agg(
    avg("people_fully_vaccinated_per_hundred").alias("avg_vaccination"),
    avg("new_cases_per_million").alias("avg_new_cases"),
    avg("excess_mortality").alias("avg_excess_mortality")
)
display(avg_df)
```

### 6. Visualization
- Use **Databricks' built-in plotting tools**:
```python
display(avg_df.orderBy("continent", "month"))
```

### 7. Correlation Analysis
```python
correlation = avg_df.stat.corr("avg_vaccination", "avg_new_cases")
print("Correlation:", correlation)
```

### 8. Generate Summary Statistics
```python
summary = avg_df.describe()
display(summary)
```

### 9. Reporting Findings
- **Interpret the correlation and trends between vaccination rates, new cases, and mortality.**
- **Summarize in a final report.**

---

## Submission
Submit **two files** named after your email username:
1. **Results Screenshot File** (e.g., `yourname_results.doc`)
2. **Databricks Notebook File** (e.g., `yourname_project5.dbc`)
University Of Cincinnati 

---

## Conclusion
By following this guide, you will successfully **analyze COVID-19 trends using Databricks and PySpark**, gaining insights into the impact of vaccinations on case rates and mortality.

🚀 Happy Analyzing!

