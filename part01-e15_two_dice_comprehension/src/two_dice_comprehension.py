#!/usr/bin/env python3

def main():
    L=[ f"({x},{a})".format(x,a) for x in [1,2,3,4,5,6]
            for a in [1,2,3,4,5,6]
            if x+a==5]

    for item in L:
        print(item)

if __name__ == "__main__":
    main()
