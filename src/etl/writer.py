import os
import pandas as pd


def write_partitioned_parquet(df: pd.DataFrame, output_path: str = "output"):
    """
    Writes dataframe as partitioned parquet files by acct_open_year
    """

    os.makedirs(output_path, exist_ok=True)

    df.to_parquet(
        output_path,
        engine="pyarrow",
        partition_cols=["acct_open_year"],
        index=False,
    )

    print(f"Data written to {output_path} partitioned by acct_open_year")