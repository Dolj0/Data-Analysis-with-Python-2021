#!/usr/bin/env python3

def main():
    for x in [1,2,3,4,5,6]:
        for a in [1,2,3,4,5,6]:
            if x+a==5:
                print(f"({x},{a})".format(x,a))


if __name__ == "__main__":
    main()
