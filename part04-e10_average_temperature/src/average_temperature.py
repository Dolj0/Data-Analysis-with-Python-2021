#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv", index_col=0)
    df_july = df[(df["m"]==7)]
    df_mean = df_july.mean()
    
    return df_mean["Air temperature (degC)"]

def main():
    print(f"Average temperature in July: {average_temperature():.1f}")
    return

if __name__ == "__main__":
    main()
