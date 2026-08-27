import pandas as pd


def clean_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Numerical columns
    numerical_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for column in numerical_columns:

        df[column] = df[column].fillna(
            df[column].median()
        )

    # Categorical columns
    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for column in categorical_columns:

        df[column] = df[column].fillna(
            "Unknown"
        )

    return df
