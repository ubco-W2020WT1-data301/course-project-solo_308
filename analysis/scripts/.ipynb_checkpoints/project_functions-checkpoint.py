import pandas as pd
import numpy as np

def load_and_process(urlOrPath):
    df = (
        pd.read_csv(urlOrPath)
        .dropna()
        .reset_index(col_level = 1)
        .drop(['index'], axis = 1)
    )

    return df

def groupby_sort_reset(col, dfx):
    df = (
        dfx.groupby(["'%s'" % col]).sum()
        .sort_values('Global_Sales', ascending = False)
        .reset_index(col_level = 1)
    )
    
    return df
