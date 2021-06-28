#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")

    df.replace(to_replace={'Bush, George':'George Bush'}, inplace=True)
    df.replace(to_replace={'Clinton, Bill':'Bill Clinton'}, inplace=True)
    df.replace(to_replace={'2017 Jan':'2017'}, inplace=True)
    df.replace(to_replace={'two':'2'}, inplace=True)
    df.replace(to_replace={'Mike pence':'Mike Pence'}, inplace=True)
    df.replace(to_replace={'joe Biden':'Joe Biden'}, inplace=True)
    df.replace(to_replace={'Cheney, dick':'Dick Cheney'}, inplace=True)
    df.replace(to_replace={'gore, Al':'Al Gore'}, inplace=True)
    df.loc[0,'Last']=None
    df = df.astype({"President":object, "Start":int, "Last":float, "Seasons":int, "Vice-president":object})

    return df

def main():
    print(cleaning_data())
    return

if __name__ == "__main__":
    main()
