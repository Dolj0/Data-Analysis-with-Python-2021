#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    
    df['Suicide/Pop'] = df['suicides_no']/df['population']

    df2 = df.groupby('country')

    df2 = df2['Suicide/Pop'].mean()
    
    return df2

    
def suicide_weather():
    weather = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col=0, header=0)
    #make dataframe
    weather = weather[0]
    weather = weather.iloc[:,0].str.replace("\u2212", "-").astype(float)

    fraction = suicide_fractions()
    
    df = pd.merge(weather, fraction, left_index=True, right_index=True)
    corr = df.corr(method='spearman').iloc[0,1]

    #shapes
    suicide = fraction.shape[0]
    temp = weather.shape[0]
    common = df.shape[0]

    return (suicide, temp, common, corr)

def main():
    suicide, temp, common, spearman = suicide_weather()
    print(f"Suicide DataFrame has {suicide} rows")
    print(f"Temperature DataFrame has {temp} rows")
    print(f"Common DataFrame has {common} rows")
    print(f"Spearman correlation: {spearman}")
    return

if __name__ == "__main__":
    main()


