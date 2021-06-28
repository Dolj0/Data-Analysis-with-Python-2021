#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)
    xfit = np.linspace(0,10,100)
    yfit = model.predict(xfit[:, np.newaxis])
    
    a,b = model.coef_[0], model.intercept_
   
    return a, b
    
def main():
    n = 20
    x = np.linspace(0,10,n)
    y = x**2 + 2 * np.random.randn(n)

    a,b = fit_line(x,y)

    print(f"Slope: {a}")
    print(f"Intercept: {b}")

    equ = a*x + b
    plt.plot(x,y, 'o')
    plt.plot(x, equ)
    plt.show()

    
if __name__ == "__main__":
    main()
