#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    a = load()
    print(a)
    sepal_len, petal_len = a[:,0], a[:,2]
    print(sepal_len, petal_len)
    
    return scipy.stats.pearsonr(sepal_len, petal_len)[0]

def correlations():
    a = load()
    matrix = np.corrcoef(a, rowvar=False)
    
    return matrix

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
