#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    a = pd.Series(s.index.values, s.values)
    return a

def main():
    s = pd.Series([1,2,3,4,5], index=list("abcde"))
    print(inverse_series(s))
    return

if __name__ == "__main__":
    main()
