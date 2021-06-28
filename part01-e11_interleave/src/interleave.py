#!/usr/bin/env python3

def interleave(*lists):

    listForZip=[]
    returnList=[]

    for x in lists:
        listForZip.append(x)
    zipped = list(zip(*listForZip))
    
    for x in zipped:
        for i in x:
            returnList.append(i)

    return returnList

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
