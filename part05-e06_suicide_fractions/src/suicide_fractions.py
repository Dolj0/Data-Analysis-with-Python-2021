#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    
    df['Suicide/Pop'] = df['suicides_no']/df['population']

    df2 = df.groupby('country')

    df2 = df2['Suicide/Pop'].mean()
    
    return df2

def main():
    print(suicide_fractions())
    return

if __name__ == "__main__":
    main()
