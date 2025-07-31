import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import Union, List, Dict
from schemas import CleaningConfig  # our Pydantic model

def fill_missing_values(df: pd.DataFrame, strategy: str = "mean", fill_value: Union[str, int, float, None] = None) -> pd.DataFrame:
    """
    Fill missing values in the DataFrame using a specified strategy.

    Parameters:
    - df: The input DataFrame
    - strategy: "mean", "median", "mode", or "constant"
    - fill_value: Value to use when strategy is "constant"

    Returns:
    - A new DataFrame with missing values filled
    """
    match strategy:
        case "mean":
            df = df.fillna(df.mean(numeric_only=True))
        case "median":
            df = df.fillna(df.median(numeric_only=True))
        case "mode":
            df = df.fillna(df.mode().iloc[0])
        case "constant":
            df = df.fillna(fill_value)
    
    return df



def drop_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Drop specified columns from the DataFrame.

    Parameters:
    - df: The input DataFrame
    - columns: A list of column names to drop

    Returns:
    - A new DataFrame with specified columns removed
    """

    df = df.drop(columns=columns)
    
    return df
    


def rename_columns(df: pd.DataFrame, rename_map: Dict[str, str]) -> pd.DataFrame:
    """
    Rename columns in the DataFrame.

    Parameters:
    - df: The input DataFrame
    - rename_map: A dictionary mapping old column names to new names

    Returns:
    - A new DataFrame with columns renamed
    """
    df = df.rename(columns=rename_map)

    return df
    


def encode_categoricals(df: pd.DataFrame, columns: List[str], method: str = "onehot") -> pd.DataFrame:
    """
    Encode categorical variables using one-hot or label encoding.

    Parameters:
    - df: The input DataFrame
    - columns: A list of column names to encode
    - method: "onehot" or "label"

    Returns:
    - A new DataFrame with encoded columns
    """
    
    match method:
        case "onehot":
            df = pd.get_dummies(df,columns=columns)
        case "label":
            for col in columns:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col])
    
    return df

def clean_data(df: pd.DataFrame, config: CleaningConfig) -> pd.DataFrame:
    """Apply cleaning transformations based on CleaningConfig."""

    if config.drop:
        df = drop_columns(df, config.drop)
    
    if config.rename:
        df = rename_columns(df, config.rename)
    
    if config.fillna:
        df = fill_missing_values(df, config.fillna.strategy, config.fillna.value)
    
    if config.encode:
        df = encode_categoricals(df, config.encode.columns, config.encode.method)
    
    return df