#!/usr/bin/env python3
import sys

def extract_numbers(s):
    x = s.split()
    l=[]
    for item in x:
        try:
            i=int(item)
            l.append(i)
        except ValueError:
            try:
                i=float(item) 
                l.append(i)
            except ValueError:
                pass

            

    return l

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
