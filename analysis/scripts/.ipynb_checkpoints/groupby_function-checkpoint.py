import pandas as pd
import numpy as np

def groupby_reset(col):
    colname = "'%s'" % col
    df = (
        pd.groupby([colname]).sum()
        .sort_values('Global_Sales', ascending = False)
        .reset_index(col_level = 1)
    )
    
    return df
