import sys
import pandas as pd
from etl.processor import clean_data, derive_features
from etl.writer import write_partitioned_parquet


def main():
    if len(sys.argv) < 2:
        print("Please provide input CSV file path")
        sys.exit(1)

    file_path = sys.argv[1]

    print(f"Reading file: {file_path}")
    df = pd.read_csv(file_path)

    print("Cleaning data...")
    df = clean_data(df)

    print("Deriving features...")
    df = derive_features(df)

    print("Writing partitioned parquet...")
    write_partitioned_parquet(df)

    print("ETL completed successfully 🚀")
