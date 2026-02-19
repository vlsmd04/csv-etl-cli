import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)


def run_etl(input_path: str, output_path: str, partition_column: str):
    logger.info("Starting ETL process")

    df = pd.read_csv(input_path)
    logger.info(f"Read {len(df)} records")

    if partition_column not in df.columns:
        raise ValueError(f"{partition_column} not found in dataset")

    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    for value, partition_df in df.groupby(partition_column):
        partition_path = output_dir / f"{partition_column}={value}.parquet"
        partition_df.to_parquet(partition_path, index=False)
        logger.info(f"Wrote partition: {partition_path}")

    logger.info("ETL process completed successfully")