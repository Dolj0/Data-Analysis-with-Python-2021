#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    
    

    plt.plot([2,4,6,7],[4,3,5,1])
    plt.plot([1,2,3,4],[4,2,3,1])


    plt.axis([0,7,0,5])
    plt.yticks(np.arange(0,5.5,0.5))


    plt.title("title") 
    plt.xlabel("x-axis")       
    plt.ylabel("y-axis")  
    plt.show()
    pass

if __name__ == "__main__":
    main()
