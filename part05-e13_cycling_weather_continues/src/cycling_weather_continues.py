#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model

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

def bicycle_timeseries(station):

    df = split_date()

    
    df["Date"] = pd.to_datetime(df[["Day", "Month", "Year"]], dayfirst=True)
   

    df = df.drop(["Day", "Month", "Year", "Hour", "Weekday"], axis=1)
    df = df.set_index("Date")
    df = df.loc['2017-01-01':'2017-12-31']
    df["sum"] = df.sum(axis=1)
    df =df.fillna(method='ffill')
    df =df.fillna(0)
    df = df.groupby(df.index)[station].sum().reset_index()
    df = df.set_index("Date")

    return df

def merger(station):
    df_cyc = bicycle_timeseries(station)

    df_wea = pd.read_csv('src/kumpula-weather-2017.csv')
    df_wea.rename(columns={"d":"Day", "m":"Month", "Time":"Hour"}, inplace=True)
    df_wea['Hour'] = df_wea['Hour'].str[0:2]
    df_wea["Date"] = pd.to_datetime(df_wea[["Day", "Month", "Year", "Hour"]], dayfirst=True)
    df_wea = df_wea.drop(["Day", "Month", "Year", "Hour", "Time zone"], axis=1)

    df_wea = df_wea.set_index("Date")
    
    merge = pd.merge(df_cyc, df_wea, how='inner', left_index=True, right_index=True)
    
    return merge

def cycling_weather_continues(station):

    df = merger(station)

    print(df)

    df = df.fillna(method='ffill')

    x = df.loc[:, ['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = df.loc[:, station]

    model = linear_model.LinearRegression(fit_intercept=True)

    model.fit(x, y)

    return model.coef_, model.score(x,y)
    
def main():
    station = 'Merikannontie'
    coef, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")
    return

if __name__ == "__main__":
    main()


