#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    positive = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    negative = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    # return ("{0},{1}".format(positive,negative))
    return (positive,negative)


def main():
    print("print(solve_quadratic(1,-3,2))")
    print(solve_quadratic(1, -3, 2))
    print("print(solve_quadratic(1,2,1))")
    print(solve_quadratic(1,2,1))
    

if __name__ == "__main__":
    main()

