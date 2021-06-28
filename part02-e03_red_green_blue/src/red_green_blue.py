#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):

    l = []
    regExpression = r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)'

    with open(filename, 'r') as f:
        next(f)
        for line in f:
            l.append('\t'.join(re.search(regExpression, line).groups()))

    return l


def main():
    pass

if __name__ == "__main__":
    main()
