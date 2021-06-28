#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):

    l =[]
    regExpression = r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s(.+)'

    with open(filename, 'r') as f:
        for line in f:
            size, month, day, hour, minute, filename = re.search(regExpression,line).groups()
            l.append((int(size),month,int(day),int(hour),int(minute),filename))
                
    return l

def main():
    
    pass

if __name__ == "__main__":
    main()
