#!/usr/bin/env python3

def reverse_dictionary(d):

    s={}
    
    for i in d:
        for j in d[i]:
            try:
                s[j].append(i)
            except:
                s[j] = [i]
    

    return (s)

def main():

    pass

if __name__ == "__main__":
    main()
