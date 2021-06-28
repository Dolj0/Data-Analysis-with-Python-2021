#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv", index_col=0)
    df_below = df[(df["Air temperature (degC)"]<0)]
    return df_below.shape[0]

def main():
    print(f"Number of days below zero: {below_zero()}")
    return
    
if __name__ == "__main__":
    main()
