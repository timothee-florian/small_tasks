#!/usr/bin/env python3
"""
Created on Fri May  6 21:04:27 2022

@author: bronner

Functions to transform a regular JSON into a dataframe where every key combination
as a single column
"""

import pandas as pd
import json



def flatten(df, column: str, combine_names: bool = False) -> pd.DataFrame:
    """Flatten a column of dictonary."""
    original_cols = list(df.columns)
    
    column_id = original_cols.index(column)
    previous_cols = original_cols[:column_id]
    after_cols = original_cols[column_id + 1:]
    
    temp_previous_df = df[previous_cols]
    temp_after_df = df[after_cols]
    temp_df = df[column].apply(pd.Series)
    
    if combine_names:
        cols_name = temp_df.columns 
        temp_df.columns = list(map(lambda col: f'{column}_{col}', cols_name))
        
    out =  pd.concat([temp_previous_df, temp_df, temp_after_df], axis=1)
    return out



if __name__ == '__main__':
    
    with open('test.json', 'r') as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)#['menu'])
    df2 = df.explode('items')
    df3 = flatten(df2, 'items')
    # df = pd.DataFrame(data)
    # dfp = flatten(df, 'instructors')
    # df2 = df.explode('instructors')
    # df2_5 = flatten(df2, 'courses')
    # df3 = df2.explode('courses')
    # df4 = flatten(df3, 'courses')