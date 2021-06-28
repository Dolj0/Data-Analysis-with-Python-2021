#!/usr/bin/env python3

def detect_ranges(L):
    L = sorted(L)
    listR = list([])
    tupleList = [0, 0]
    listRange = list([])

    for i in range(0, len(L)):
        x=L[i]
        if x+1 in L:
            if x+1 > tupleList[0] and x+1 <= tupleList[1]:
                continue
            else:
                tupleList.clear()
                tupleList.append(x)
                
                for f in range(0, len(L)-(L.index(x))):
                    if x+2+f in L:
                        listRange.append(x+2+f)
                        continue
                    else:
                        tupleList.append(x+2+f)
                        break
                listR.append(tuple(tupleList))
        elif x in listRange:
            continue
        elif x > tupleList[0] and x < tupleList[1]:
            continue
        else:
            listR.append(x)

    return listR

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
