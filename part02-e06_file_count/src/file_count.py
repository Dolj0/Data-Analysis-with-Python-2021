#!/usr/bin/env python3

import sys
from typing import SupportsRound

def file_count(filename):

    line_count = 0
    word_count = 0
    char_count = 0

    with open(filename, 'r') as f:
        for line in f:
            char_count = char_count + len(line)
            line_count = line_count + 1
            word_list = line.split()
            word_count = word_count + len(word_list)

    return (line_count, word_count, char_count)

def main():
    files = sys.argv[1:]
    for item in files:
        ln, wr, ch = file_count(item)
        print(f'{ln}\t{wr}\t{ch}\t{item}')
    pass

if __name__ == "__main__":
    main()
