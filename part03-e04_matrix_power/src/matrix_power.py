#!/usr/bin/env python3

import numpy as np
from functools import reduce
import math

def matrix_power(a, n):

    #print(np.eye(a.shape[0])) <-- Integer??

    x=a
    n_minus = n-1
    if n == 0:
        return np.eye(a.shape[0], dtype=int)
    elif n < 0:
        gen = (a for i in range(abs(n)))
        fun = lambda x,y : x@y
        multiplicated = reduce(fun, gen)
        x = np.linalg.inv(multiplicated)
    else:
        gen = (a for i in range(abs(n)))
        fun = lambda x,y : x@y
        x = reduce(fun, gen)
    
    return(x)

def main():
    
    s=np.array([[1, 6, 7],
    [7, 8, 1],
    [5, 9, 8]])
    n=-2

    print(matrix_power(s, n))
    return

if __name__ == "__main__":
    main()
