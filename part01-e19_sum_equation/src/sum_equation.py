#!/usr/bin/env python3

def sum_equation(L):

    if len(L)==0:
        return('0 = 0')
    sumT = sum(L)
    L1=list(map(str, L))
    s=""

    for item in L1:
        s=' + '.join(L1)
    
    s=s+" = "+str(sumT)
    print(s)
    
    return(s)

def main():
    sum_equation([2,5,2,5])
    pass

if __name__ == "__main__":
    main()
