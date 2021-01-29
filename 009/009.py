from os import path
import time


def p1(datalist, pre):
    i = pre
    while i < len(datalist):
        findx = datalist[i]
        sub = set(datalist[i-pre:i])
        found = False
        for val in sub:
            if findx - val in sub:
                found = True
                break
        if not found:
            return findx
        i += 1


def p2(datalist, pre):
    inval = p1(datalist, pre)
    i = 0
    listlen = len(datalist)
    while i < listlen:
        j = i
        i += 1
        if datalist[j] < datalist[j+1]:
            minx, maxx = datalist[j], datalist[j+1]
        else:
            maxx, minx = datalist[j], datalist[j+1]
        sumx = minx + maxx
        j += 2
        while j < listlen and sumx < inval:
            x = datalist[j]
            sumx += x
            if x < minx:
                minx = x
            elif x > maxx:
                maxx = x
            j += 1
        if sumx == inval:
            return minx + maxx


def main():
    # check for file, exit if file not found
    fname = "input.txt"
    if not path.exists(fname):
        print("Error - ", fname, " not found")
        raise SystemExit()

    # read file into list, strip /n
    with open(fname) as f:
        datalist = [int(line) for line in f.readlines()]
    f.close()

    pre = 25
    print("Part 1: ", p1(datalist, pre))
    print("Part 2: ", p2(datalist, pre))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
