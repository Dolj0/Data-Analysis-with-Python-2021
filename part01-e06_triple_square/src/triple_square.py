#!/usr/bin/env python3


def main():
    
    for i in range(11):
        i=i+1
        t=triple(i)
        s=square(i)
        if t<s:
            break
        print(f"triple({i})=={t} square({i})=={s} ")
        
            


def triple(i):
   return i*3

def square(i):
    return i*i


if __name__ == "__main__":
    main()
