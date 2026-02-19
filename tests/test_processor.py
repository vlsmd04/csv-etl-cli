import pandas as pd
from etl.processor import clean_data, derive_features


def test_clean_data_removes_nulls():
    df = pd.DataFrame(
        {
            "credit_limit": [1000, None],
            "num_cards_issued": [2, 1],
            "acct_open_date": ["2023-01-01", "2023-02-01"],
        }
    )

    result = clean_data(df)

    assert result["credit_limit"].isnull().sum() == 0


def test_derive_features_adds_year_and_ratio():
    df = pd.DataFrame(
        {
            "credit_limit": [1000],
            "num_cards_issued": [2],
            "acct_open_date": ["2023-01-01"],
        }
    )

    result = derive_features(df)

    assert "acct_open_year" in result.columns
    assert result["acct_open_year"].iloc[0] == 2023
    assert "credit_per_card" in result.columns
    assert result["credit_per_card"].iloc[0] == 500