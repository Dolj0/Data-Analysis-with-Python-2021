#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df_2 = df.dropna(how = "all")
    df_3 = df_2.dropna(axis = 1, how = "all")
    
    column = df_3.iloc[:,0]

    df_4 = column.str.split(expand = True)
    df_4.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']

    df_4.replace(to_replace={'ma':'Mon'}, inplace=True)
    df_4.replace(to_replace={'ti':'Tue'}, inplace=True)
    df_4.replace(to_replace={'ke':'Wed'}, inplace=True)
    df_4.replace(to_replace={'to':'Thu'}, inplace=True)
    df_4.replace(to_replace={'pe':'Fri'}, inplace=True)
    df_4.replace(to_replace={'la':'Sat'}, inplace=True)
    df_4.replace(to_replace={'su':'Sun'}, inplace=True)

    months={"tammi":1,"helmi":2,"maalis":3,"huhti" :4,"touko" :5,"kesä":6,"heinä" :7,"elo" :8,"syys" :9,"loka" :10,"marras" :11,"joulu" :12,}
    df_4["Month"] = df_4["Month"].map(months)

    df_4['Hour'] = df_4['Hour'].str[0:2]

    df_4 = df_4.astype({"Weekday":object, "Day":int, "Month":int, "Year":int, "Hour":int})

    #df_4.set_index(list(df_4)['Weekday'])

    


    return df_4

def main():
    print(split_date())
    return
       
if __name__ == "__main__":
    main()

