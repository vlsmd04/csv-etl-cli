import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw dataframe:
    - Type casting
    - Null handling
    - Basic formatting
    """

    # Convert credit_limit (remove $ if exists)
    df["credit_limit"] = (
        df["credit_limit"].astype(str).str.replace("$", "", regex=False)
    )

    df["credit_limit"] = pd.to_numeric(df["credit_limit"], errors="coerce")

    # Convert num_cards_issued to numeric
    df["num_cards_issued"] = pd.to_numeric(df["num_cards_issued"], errors="coerce")

    # Convert dates
    df["acct_open_date"] = pd.to_datetime(df["acct_open_date"], errors="coerce")

    # Handle nulls
    df.fillna(
        {
            "credit_limit": 0,
            "num_cards_issued": 0,
        },
        inplace=True,
    )

    return df


def derive_features(df):
    df["acct_open_date"] = pd.to_datetime(df["acct_open_date"], errors="coerce")

    df["acct_open_year"] = df["acct_open_date"].dt.year

    df["credit_per_card"] = df["credit_limit"] / df["num_cards_issued"].replace(0, 1)

    today = pd.Timestamp.today()
    df["account_age_years"] = (today - df["acct_open_date"]).dt.days / 365

    return df