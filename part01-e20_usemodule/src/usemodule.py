#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    triangle.hypothenuse(5,6)
    triangle.area(6,7)

if __name__ == "__main__":
    main()