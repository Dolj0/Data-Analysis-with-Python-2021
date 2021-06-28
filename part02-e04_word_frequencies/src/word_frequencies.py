#!/usr/bin/env python3

def word_frequencies(filename):

    l = []
    freq_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            linesplit = line.split()
            linestripped = [item.strip("""!"#$%&'()*,-./:;?@[]_""") for item in linesplit]
            for item in linestripped:
                l.append(item)
    lKey = set(l)
    for items in lKey:
        freq = l.count(items)
        freq_dict[items] = freq

    return freq_dict

def main():
    
    pass

if __name__ == "__main__":
    main()
