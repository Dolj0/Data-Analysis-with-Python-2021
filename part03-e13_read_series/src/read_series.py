#!/usr/bin/env python3

import pandas as pd
import numpy as np

def read_series():
    s=pd.Series([], dtype='object')
    values = []
    indexes = []
    while True:
        print("User Input:")
        x=input()
        if len(x) == 0:
            return pd.Series(values, indexes)
        else:
            try:
                index, value = x.split()
                indexes.append(index) 
                values.append(value)
            except:
                raise Exception
            

    

def main():
    print(read_series())
    pass

if __name__ == "__main__":
    main()
