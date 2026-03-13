
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




#Week-3: AWS Data Lake Architecture
1.S3 Data Lake Structure

* `raw/` – stores original Parquet files generated from the CSV dataset.
* `staging/` – intermediate data used during transformation workflows.
* `curated/` – cleaned and feature-engineered datasets ready for analytics.

2.Data Security

* Amazon S3 **Server-Side Encryption (SSE-S3)** is enabled to encrypt all stored data using AES-256 encryption.

3.Access Control

* AWS **IAM policies** are used to manage secure access to the S3 bucket.
* Access permissions allow controlled operations such as uploading, downloading, and listing objects via AWS CLI and boto3 scripts.

4.Monitoring and Auditing

**AWS CloudTrail** is enabled to log all API activities for auditing and governance.
**AWS Budgets** is configured to monitor project spending and trigger alerts when costs exceed defined thresholds.


#Week - 4: AWS Data Lake Pipeline

Architecture that I followed:
S3 Raw Zone → AWS Glue Crawler → Glue Data Catalog → Glue ETL (PySpark) → S3 Curated Zone (Parquet) → Lake Formation Permissions → Amazon Athena Queries

1. Created an AWS Glue database and configured a Glue Crawler to catalog raw data stored in the S3 raw zone. Verified the discovered schema and partitions in the AWS Glue Data Catalog.
2. Developed an AWS Glue ETL job using PySpark that reads raw CSV data from Amazon S3, performs data cleaning and transformations, and writes the processed data to the curated zone in Parquet format with partitioning.
3. Enabled Glue job bookmarks to support incremental data processing and configured retry settings to improve job reliability and fault tolerance.
4. Configured AWS Lake Formation permissions to control data access. Athena was granted read access to the curated zone while restricting direct access to the raw data.
5. Created a limited IAM user to test and validate Lake Formation access controls for querying curated datasets.
6. Executed SQL queries in Amazon Athena against the curated tables to validate the processed data.
7. Created an optimized CTAS (Create Table As Select) table using Parquet format with Snappy compression and partitioning to improve query performance.
8. Compared query performance between the original curated table and the optimized CTAS table.
9. Observed that partitioning and columnar storage significantly reduced the amount of data scanned, resulting in faster queries and lower Athena query costs.
