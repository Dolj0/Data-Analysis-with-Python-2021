#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1,2)
    ax[0].plot(a[:,0], a[:,1])
    ax[1].scatter(a[:,0], a[:,1], s=a[:,3], c=a[:,2])
    
  
    plt.show()

    pass

def main():
    a = np.array([[1,2,3,4],[1,2,3,4]])
    subfigures(a)
    pass

if __name__ == "__main__":
    main()
