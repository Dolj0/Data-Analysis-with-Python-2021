#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    
    x = df.loc[:, 'X1':'X5']
    y = df.loc[:, 'Y']

    model = LinearRegression(fit_intercept=False)
    model.fit(x, y)

    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i in range(len(coefficients)):
        print(f"Coefficient of X{i+1} is {coefficients[i]}")
    
if __name__ == "__main__":
    main()

