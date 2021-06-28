#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    #print(a)
    #a_squared = a**2
    #a_squared_length = a_squared.sum(axis=1)
    

    # print(a_squared)
    # print(a_squared_length)
    # print(a_length)

    return np.sqrt((a**2).sum(axis=1))

def main():
    arr = np.array([[1,2],[4,5],[7,8]])
    print(vector_lengths(arr))
    pass

if __name__ == "__main__":
    main()
