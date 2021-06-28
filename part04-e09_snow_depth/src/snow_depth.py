#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv", index_col=0)
    df_des=df.describe()
    return df_des.loc["max"]["Snow depth (cm)"]

def main():
    print(f"Max snow depth: {snow_depth()}")
    

if __name__ == "__main__":
    main()
