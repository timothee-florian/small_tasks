#!/usr/bin/env python3
"""
Created on Fri May  6 21:04:27 2022

@author: Timothee-Florian

Functions to transform a regular JSON into a dataframe where every key combination
as a single column
"""

import pandas as pd
import json
import argparse



def flatten(df, column: str, combine_names: bool = False) -> pd.DataFrame:
    """
    Flatten a column of dictonary.
    
    Args_:
        - df - dataframe to modify
        - column - column of the dataframe to be flattened
        - combine_names - do we combine the original column name with the new ones or do we only use the new ones
        
    Output:
        - df - the modified datataframe
    """
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


def explode_and_flatten(df: pd.DataFrame, column: str, combine_names: bool = False) -> pd.DataFrame:
    """
    Use when a column is a list of dictionaries.
    
    Args_:
        - df - dataframe to modify
        - column - column of the dataframe to be exploded and flattened
        - combine_names - in the flattening step do we combine the original column name with the new ones or do we only use the new ones
        
    Output:
        - df - the modified datataframe
    """
    df = df.explode(column)
    df = flatten(df, column, combine_names)
    return df
    
    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Flattening JSON')
    parser.add_argument('-in', '--path_json', type = str, help = 'Path of the JSON file')
    parser.add_argument('-out', '--path_out', type = str, help = 'Path of the excel or csv file')
    
    args = parser.parse_args()
    
    with open(args.path_json, 'r') as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)#['menu'])
    df2 = flatten(df, 'courses', True)
    df3 = df2.explode('courses_occurrences')
    # df = pd.DataFrame(data)
    # dfp = flatten(df, 'instructors')
    df4 = flatten(df3, 'instructors', True)
    df5 = flatten(df4, 'courses_occurrences', True)
    # df2_5 = flatten(df2, 'courses')
    # df3 = df2.explode('courses')
    # df4 = flatten(df3, 'courses')
    if args.path_out.split('.')[-1] == 'csv':
        df5.to_csv(args.path_out, index = False)
    elif args.path_out.split('.')[-1] == 'xlsx': 
        df5.to_excel(args.path_out, index = False)
    else:
        print('Unsuported file type')
    