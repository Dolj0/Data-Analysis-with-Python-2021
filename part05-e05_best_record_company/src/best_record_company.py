#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    best_pub = df.groupby('Publisher')
    best_pub1 = best_pub['WoC'].sum()
    best_pub1 = best_pub1.sort_values(ascending=False)
    publis_df = best_pub1.index[0]
    df_pub = df[df.Publisher == publis_df]
    return df_pub


def main():
    print(best_record_company())
    return
    

if __name__ == "__main__":
    main()
