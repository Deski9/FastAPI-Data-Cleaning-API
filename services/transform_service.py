import pandas as pd
from transform import clean_data
from schemas import CleaningConfig
from sklearn.preprocessing import LabelEncoder


def apply_cleaning(file, config: CleaningConfig):
    df = pd.read_csv(file)
    df_cleaned = clean_data(df, config)
    return df_cleaned




