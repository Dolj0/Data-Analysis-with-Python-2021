#!/usr/bin/env python3

import numpy as np

def diamond(n):
    arr = np.array([])
    ident = np.eye(n, dtype=int)
    top_left = (ident[::-1][0:n-1])
    bot_left = ident

    # print(ident[::-1])
    # print(top_left)

    left = np.concatenate((top_left, bot_left))
    
    right = (np.rot90(np.rot90(left)))[:,1:]

    whole = np.c_[left, right]

    # print(whole)

    return(whole)


def main():
    diamond(1)
    pass

if __name__ == "__main__":
    main()
