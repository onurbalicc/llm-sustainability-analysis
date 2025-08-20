# src/features.py

import pandas as pd

def extract_time_features(df):
    """Add time-based features from timestamp."""
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['dayofweek'] = df['timestamp'].dt.dayofweek
    df['is_weekend'] = df['dayofweek'] >= 5
    return df

def add_rolling_features(df, window=3):
    """Add rolling mean and std for each node."""
    df = df.sort_values(by=['node', 'timestamp'])
    df['rolling_mean'] = df.groupby('node')['watts'].transform(lambda x: x.rolling(window).mean())
    df['rolling_std'] = df.groupby('node')['watts'].transform(lambda x: x.rolling(window).std())
    return df
