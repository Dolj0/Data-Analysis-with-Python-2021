#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        cmd = input("Choose a shape (triangle, rectangle, circle): ")
        if cmd == 'triangle':
            cmdBase = input("Give base of the triangle: ")
            cmdHeight= input("Give height of the triangle: ")
            triangle(int(cmdBase), int(cmdHeight))
        elif cmd == 'rectangle':
            cmdBase = input("Give width of the rectangle: ")
            cmdHeight= input("Give height of the rectangle: ")
            rectangle(int(cmdBase), int(cmdHeight))
        elif cmd == 'circle':
            cmdBase = input("Give radius of the circle: ")
            circle(int(cmdBase))
        elif cmd == '':
            break
        else:
            print("Unknown shape!")

def triangle(Base, Height):
    print(f"The area is {0.5*Base*Height:3f}")

def rectangle(Base, Height):
    print(f"The area is {Base*Height:3f}")

def circle(Radius):
    print(f"The area is {3.14159265*Radius*Radius:3f}")

if __name__ == "__main__":
    main()
