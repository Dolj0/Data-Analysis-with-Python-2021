#!/usr/bin/env python3

import sys
import math

def summary(filename):

    list = []
    sum = 0
    average = 0
    std = 0

    with open(filename, 'r') as f:
        for line in f:
            try:
                list.append(float(line))
            except:
                pass
    
    for i in list:
        sum=sum+i
    average = sum/len(list)

    for j in list:
        std = std + ((j-average)**2)
    std = math.sqrt(std/(len(list)-1))

    return (sum,average,std)

def main():
    files = sys.argv[1:]
    for item in files:
        sm, av, std = summary(item)
        print(f"File: {item} Sum: {sm:.6f} Average: {av:.6f} Stddev: {std:.6f}")


if __name__ == "__main__":
    main()
