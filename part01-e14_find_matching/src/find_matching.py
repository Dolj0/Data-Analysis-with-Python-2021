#!/usr/bin/env python3

def find_matching(L, pattern):

    d=[]

    for str, value in enumerate(L):
        if pattern in value:
            d.append(str)

    print(d)
    
    return(d)


def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    pass

if __name__ == "__main__":
    main()
