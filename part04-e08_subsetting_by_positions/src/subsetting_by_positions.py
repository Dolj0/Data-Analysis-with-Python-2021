#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t', index_col=0)
    col = df.columns
    
    df_sub = df.iloc[0:10][[col[1], col[2]]]
    return df_sub

def main():
    subsetting_by_positions()
    return

if __name__ == "__main__":
    main()
