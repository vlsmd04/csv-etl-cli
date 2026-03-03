
---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/csv-etl-cli.git
cd csv-etl-cli

# CSV ETL CLI Project

## Project Overview
1. A GitHub repository was created with a proper Python project structure.
2. A command-line tool was created to run the project easily from the terminal.
3. Local CSV files are used as input for the project.
4. Data cleaning was implemented to handle missing values and correct data types.
5. New columns were created from existing data to improve data usability.
6. The cleaned data is saved in Parquet format for better storage and performance.
7. Output files are organized by date for easy access.
8. Configuration settings are managed using a YAML file or environment variables.
9. Logging was added to track execution details and errors.
10. A scheduler was created using Windows Task Scheduler to run the script daily.



#Week-2: End-to-End Data Engineering Pipeline – PostgreSQL & PySpark

1.Designed and implemented a normalized PostgreSQL schema (trips, vendors, zones) and ingested sample trip data.
2.Developed 10+ advanced SQL queries using CTEs and window functions for daily/weekly KPIs and Top-N analytics.
3.Performed query optimization analysis using EXPLAIN ANALYZE and documented performance insights.
4.Built a scalable PySpark ETL pipeline to ingest raw CSV trip data.
5.Enriched fact data by joining with a dimension (zone lookup) dataset.
6.Computed daily aggregates (avg/median trip duration by zone) using distributed processing.
7.Persisted results as partitioned Parquet files for efficient downstream analytics.
8.Validated Spark outputs against PostgreSQL results to ensure data accuracy.
9.Benchmarked performance by tuning Spark partitions and enabling broadcast joins.
10.Demonstrated end-to-end data validation, performance tuning, and production-style pipeline design.
