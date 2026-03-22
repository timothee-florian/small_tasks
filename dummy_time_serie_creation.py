# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:58:55 2024

@author: bronner
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta 


start_time = '2024-01-01 00:00:00' 
end_time = '2024-01-01 23:59:00'    
time_frame = '1min'                  


date_range = pd.date_range(start=start_time, end=end_time, freq=time_frame)

def creat_dummy_timeseries(date_range, sym):
    

    num_rows = len(date_range)
    
    # Generate random price data for Open, High, Low, Close, and Volume
    # For simplicity, let's assume EUR/USD prices between 1.1000 and 1.1500
    np.random.seed(42)  # For reproducibility
    
    # Generate random price data (open, high, low, close)
    open_prices = np.random.uniform(1.1000, 1.1500, size=num_rows)
    high_prices = open_prices + np.random.uniform(0.0001, 0.0010, size=num_rows)  # Slightly higher than open
    low_prices = open_prices - np.random.uniform(0.0001, 0.0010, size=num_rows)   # Slightly lower than open
    close_prices = np.random.uniform(low_prices, high_prices, size=num_rows)      # Close within high-low range
    
    # Generate random volume data (let's assume volumes between 1000 and 5000 per minute)
    volumes = np.random.randint(1000, 5000, size=num_rows)
    
    # Create the DataFrame
    df = pd.DataFrame({
        'datetime': date_range,
        'Open': open_prices,
        'High': high_prices,
        'Low': low_prices,
        'Close': close_prices,
        'Volume': volumes
    })
    df['sym'] = sym
    return df
dfs = []
for sym in ['EURUSD', 'CHFUSD']:
    dfs += [creat_dummy_timeseries(date_range, sym)]
    
df = pd.concat(dfs).sort_values(by = ['datetime', 'sym'])
 

def create_swift_day_data(df, n_day): 
    df = df.copy()
    df['datetime'] = df['datetime'] + timedelta(days=n_day)
    renaming = dict()
    for c in df.columns:
        if c not in ['datetime', 'sym']:
            renaming[c] = f'{c}_lag_{n_day}_days'
    df = df.rename(columns = renaming)
    return df

def create_swift_hour_data(df, n_hour): 
    df = df.copy()
    df['datetime'] = df['datetime'] + timedelta(hours=n_hour)
    renaming = dict()
    for c in df.columns:
        if c not in ['datetime', 'sym']:
            renaming[c] = f'{c}_lag_{n_hour}_days'
    df = df.rename(columns = renaming)
    return df

# df['datetime_plus_7_day'] = df['datetime'] + timedelta(days= 7)
df_lag_day =  create_swift_day_data(df, n_day= 7)
df_lag_hour =  create_swift_hour_data(df, n_hour= 1)


dff =pd.merge(df, df_lag_hour, left_on=['datetime','sym'], right_on=['datetime','sym'])



