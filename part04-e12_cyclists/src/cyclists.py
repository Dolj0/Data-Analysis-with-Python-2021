#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df_2 = df.dropna(how = "all")
    df_3 = df_2.dropna(axis = 1, how = "all")
    return df_3


def main():
    print(cyclists())
    return
    
if __name__ == "__main__":
    main()


#src\Helsingin_pyorailijamaarat.csv