
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


#Week - 5: Serverless Data Pipeline
Architecture that I followed:
Client (curl/Postman) → API Gateway (HTTP API) → Lambda (validation + enrichment) → S3 (raw data storage) → Step Functions (workflow orchestration) → Lambda (processing step)

1.Built an HTTP API using Amazon API Gateway with a POST /events endpoint for ingesting JSON events.
2.Integrated the API with AWS Lambda to process incoming requests.
3.Implemented validation and enriched events with metadata such as event_id and received_at.
4.Stored processed data in Amazon S3 using time-based partitioning (year/month/day/hour).
5.Tested end-to-end pipeline using curl to simulate real-time event ingestion.
6.Enabled logging and monitoring using Amazon CloudWatch.
7.Created CloudWatch alarms for:
    -Lambda errors (> 0)
    -API Gateway 5XX errors (> 1)
8.Built a workflow using AWS Step Functions to orchestrate multiple steps.
9.Designed workflow:
     -Start → ingestion Lambda → processing Lambda → End
     -Included retry logic for failure handling
10.Optimized for cost by avoiding paid services (Kinesis, Glue, Athena) and using free-tier alternatives.

#Week - 6: Serverless ETL Data Pipeline
Architecture that I followed:
API Gateway → Lambda → S3 (raw) → Lambda (curation) → S3 (curated) → Lambda (reporting) → S3 (reporting) → Step Functions (orchestration)

1.Built an end-to-end serverless ETL pipeline using AWS services to ingest, process, and analyze event data.
2.Implemented an HTTP endpoint using API Gateway to receive JSON event data (ride events with fare and zone).
3.Stored incoming data in Amazon S3 (raw layer) using a Lambda ingestion function.
4.Developed a curation Lambda (curation-fn) triggered by S3 events to clean and structure raw data into partitioned Parquet-like JSON format.
5.Organized curated data in S3 (curated layer) using time-based partitioning (year/month/day) for efficient querying.
6.Built a reporting Lambda (reporting-fn) to aggregate curated data and generate analytics (total fare, event count, per-zone metrics).
7.Stored aggregated results in S3 (reporting layer) as summary.json.
8.Orchestrated the pipeline using AWS Step Functions, enabling sequential execution of transformation and reporting steps.
9.Implemented logging and monitoring using CloudWatch Logs, and handled edge cases like empty files and invalid JSON.
10.Designed the pipeline to be cost-efficient (Free Tier), scalable, and aligned with real-world data engineering practices.

Due to cost efficient, I had used different tools.
| Original Tool        | Replaced With         |
| Kinesis              | API Gateway + Lambda  |
| Glue Streaming / EMR | Lambda                |
| Athena / Redshift    | Lambda aggregation    |
| Streaming pipeline   | Event-driven pipeline |


#Week - 7: Serverless Data Pipeline
Architecture that I followed:
API Gateway → Lambda → S3 (raw) → Lambda (curation) → S3 (curated) → Lambda (reporting) → S3 (reporting) → Step Functions

1.Designed and implemented an end-to-end serverless ETL pipeline using AWS free-tier services to process user/event data.
2.Built an ingestion layer using API Gateway + Lambda to receive JSON events and store them in Amazon S3 (raw zone) with date-based partitioning.
3.Structured raw data in S3 using a partitioned format (year/month/day/hour) to support scalable processing.
4.Developed a curation Lambda (curation-fn) triggered by S3 events to clean data, extract fields, and transform it into a structured format.
5.Stored transformed data in S3 curated zone, maintaining time-based partitions for efficient downstream processing.
6.Implemented a reporting Lambda (reporting-fn) to aggregate curated data and compute metrics such as total fare, event count, and zone-wise statistics.
7.Saved aggregated outputs in S3 reporting layer as summary.json for analytics consumption.
8.Orchestrated the workflow using AWS Step Functions, enabling controlled execution of curation and reporting stages with error handling.
9.Replaced costly services like Glue, Athena, and Redshift with Lambda-based processing to ensure the entire pipeline runs within free-tier limits.
10.Added logging and monitoring via CloudWatch, and implemented safeguards for handling empty files, invalid JSON, and missing keys.
