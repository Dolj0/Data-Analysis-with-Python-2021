#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    df.replace(to_replace={'Re':None}, inplace=True)
    df.replace(to_replace={'New':None}, inplace=True)
    df_drop = df.dropna()
    
    df_sub = df_drop[(df_drop['Pos']>df_drop['LW'].astype(int))]

    return df_sub

def main():
    print(special_missing_values())
    return

if __name__ == "__main__":
    main()
