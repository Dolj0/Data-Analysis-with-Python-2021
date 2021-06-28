#!/usr/bin/env python3

import numpy as np
from numpy.core.fromnumeric import prod
from numpy.lib.function_base import angle
import scipy.linalg

def vector_angles(X, Y):
    
    denom_X=np.sqrt((X**2).sum(axis=1))
    denom_Y=np.sqrt((Y**2).sum(axis=1))
    denom=denom_X*denom_Y
    numer = np.sum(X*Y, axis=1)
    frac = numer/denom
    ang = np.arccos(np.clip(frac, -1.0, 1.0))
    
    return np.array(np.degrees(ang))
    
def main():
    x = np.array([[0,2]])
    y = np.array([[3,3]])
    vector_angles(x, y)

if __name__ == "__main__":
    main()
