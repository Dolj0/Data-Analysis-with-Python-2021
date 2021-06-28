#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    df_grow = df[(df["Population change from the previous year, %"]>0)]
    percentage = ((df_grow.shape[0])/(df.shape[0]))
    return(percentage)

def main():
    df = pd.read_csv("src/municipal.tsv", sep='\t', index_col=0)
    df_muni = df[1:312]
    percent = growing_municipalities(df_muni) * 100
    print(f"Proportion of growing municipalities: {percent:.1f}%")


if __name__ == "__main__":
    main()
