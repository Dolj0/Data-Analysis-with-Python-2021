#!/usr/bin/env python3

import pandas as pd

def top_bands():
    ban_df = pd.read_csv("src/bands.tsv", sep="\t")
    
    uk_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    
    ban_df['Band'] = ban_df['Band'].str.upper()

    df = pd.merge(uk_df, ban_df, left_on=['Artist'], right_on=['Band'])

    return df

def main():
    print(top_bands())

    return

if __name__ == "__main__":
    main()
