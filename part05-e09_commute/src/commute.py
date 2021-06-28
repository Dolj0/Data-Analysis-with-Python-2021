#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date():

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how='all')
    df = df.dropna(axis = 1, how = "all")

    column = df.iloc[:,0]

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

    df = df.iloc[:,1:]

    df_con = pd.concat([df_4, df], axis = 1)

    return df_con

def bicycle_timeseries():

    df = split_date()
    
    df["Date"] = pd.to_datetime(df[["Day", "Month", "Year", "Hour"]], dayfirst=True)

    df = df.drop(["Day", "Month", "Year", "Hour", "Weekday"], axis=1)
    df = df.set_index("Date")
  
    return df


def commute():
    df=bicycle_timeseries()
    df = df["2017-08-01":"2017-08-31"]
    df["Weekday"] = df.index.weekday
    df["Weekday"] = df["Weekday"]+1
    df = df.groupby('Weekday').sum()
    return df
    
def main():
    print(commute())
    plt.plot(commute())
    plt.show()
    return


if __name__ == "__main__":
    main()
