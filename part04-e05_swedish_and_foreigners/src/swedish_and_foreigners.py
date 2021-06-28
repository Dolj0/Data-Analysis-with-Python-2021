#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep='\t', index_col=0)
    df_muni = df[1:312]
    df_boolmask = df_muni[(df_muni["Share of foreign citizens of the population, %"]>5)&(df_muni["Share of Swedish-speakers of the population, %"]>5)]

    return df_boolmask[["Population","Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]

def main():
    print(swedish_and_foreigners().head())
    return

if __name__ == "__main__":
    main()
