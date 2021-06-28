#!/usr/bin/env python3

def merge(L1, L2):
    L = L1+L2

    for i in range(len(L)-1):
        
        min_index = i
        
        for j in range(i+1, len(L)):
        
            if L[j] < L[min_index]:
                min_index = j
        
        L[i], L[min_index] = L[min_index], L[i]
    
    return L

def main():
    L1=[1,5,9,12]
    L2=[2,6,10]
    
    print(merge(sorted(L1),sorted(L2)))
    pass

if __name__ == "__main__":
    main()
