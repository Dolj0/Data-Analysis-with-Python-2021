#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):

    arr_x = np.arange(n)
    arr_y = arr_x.reshape((n,1))
    arr = arr_y*arr_x

    print(arr)

    return arr

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
