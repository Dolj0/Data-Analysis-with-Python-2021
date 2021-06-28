#!/usr/bin/env python3

def distinct_characters(L):

    s=list()
    d={}

    for i in range(0, len(L)):
        s.append(len(set(L[i])))

    for i in range(0, len(L)):
        d[L[i]]=s[i]    
    
    return d
    

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
