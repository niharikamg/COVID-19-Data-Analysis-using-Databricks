# 🦠 COVID-19 Vaccination vs Mortality – Global Analysis using Databricks (by Niharika MG)

Hey there! 👋 I’m Niharika MG, and this is a data science project where I explore how COVID-19 vaccination rates impacted new cases and excess mortality across continents. I used **Databricks**, **PySpark**, and **Pandas**, combining datasets from **Our World in Data**, the **World Bank**, and **Wikipedia**.

Let’s find out: Did more vaccines really mean fewer cases and deaths?

---

## 🔍 What I Did

- Cleaned and loaded the OWID COVID dataset in Databricks.
- Focused on **September & October 2021** – peak vaccination months.
- Filtered out noisy or missing data for more reliable results.
- Aggregated and analyzed metrics by **continent**.
- Filled in missing GDP per capita data using trusted sources.
- Ran **correlation analysis** between:
  - Vaccination % vs New COVID cases  
  - Vaccination % vs Excess Mortality
- Visualized everything using Databricks' built-in chart tools.

---

## 🧪 Tools Used

- Databricks (Community Edition)
- PySpark & Pandas
- DBFS (Databricks File System)
- Our World in Data CSV
- World Bank GDP data
- Wikipedia (for backup GDP info)

---

## 📊 Key Findings

> 🌍 Continents with **higher vaccination rates** (especially in October 2021) showed **lower new case rates** and **reduced excess mortality**.

- **Africa** lagged in vaccination and had more case spikes.
- **Europe** and **North America** showed higher vaccination + better outcomes.
- There’s a **moderate negative correlation** between vaccines and cases.
- Visualizations make this super clear — check the plots in my notebook!

---

## 📚 Data Sources

- OWID: [https://ourworldindata.org/covid-vaccinations](https://ourworldindata.org/covid-vaccinations)
- World Bank: [https://data.worldbank.org](https://data.worldbank.org)
- Wikipedia: [GDP (PPP) by country](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita)

---

## 📝 Final Thoughts

Data doesn’t lie — vaccines *did* help reduce both cases and excess deaths. 📉  
This was a great hands-on experience combining data cleaning, transformation, analysis, and storytelling using Databricks.

---

## 🙋‍♀️ About Me

**Niharika MG**  
Data Science • Python • PySpark • Visualization  
Reach me: mgniharikaa@gmail.com
Let's connect!

---

## 🛑 License

Educational use only. Attribution appreciated 😊
