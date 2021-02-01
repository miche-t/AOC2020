from os import path
import time


def p1(datalist):
    datalist.append(datalist[len(datalist)-1]+3)
    joltx = 0
    diff1 = 0
    diff3 = 0
    while len(datalist) != 0:
        adapter = sorted(i for i in datalist if i <= joltx+3)[0]
        if adapter - joltx == 1:
            diff1 += 1
        elif adapter - joltx == 3:
            diff3 += 1
        joltx = adapter
        datalist.remove(adapter)
    print(diff1, diff3)
    return diff1*diff3


def getcombos(combolist, x, combocount):
    # skip to next adapter if there is only 1 possible option
    while len(combolist[x]) == 1:
        x = combolist[x][0]

    # end of list if no next adapter
    if combolist[x] == []:
        return 1

    # if the count for this adapter has been calculated before, return the saved result
    if x in combocount:
        return combocount[x]

    # otherwise perform the count and save the result for this adapter
    count = 0
    for i in combolist[x]:
        count += getcombos(combolist, i, combocount)
    combocount[x] = count
    return count


def p2(datalist):
    datalist.insert(0, 0)
    diff = 3
    combos = {}
    i = 0
    end = len(datalist)
    while i < end:
        joltx = datalist[i]
        a = [x for x in datalist if joltx < x <= joltx + diff]
        combos[joltx] = a
        i += 1
    combocount = {}
    print(combos)
    return getcombos(combos, 0, combocount)


def main():
    # check for file, exit if file not found
    fname = "input.txt"
    if not path.exists(fname):
        print("Error -", fname, "not found")
        raise SystemExit()

    with open(fname) as f:
        # read file into list, strip /n
        # datalist = f.read().splitlines()
        # read file as integers into list
        # datalist = [int(line) for line in f.readlines()]
        # read file as integers into sorted list
        datalist = sorted([int(line) for line in f.readlines()])
    f.close()

    if len(datalist) == 0:
        print(fname, "- No data found")
    else:
        print("Part 1: ", p1(datalist.copy()))
        print("Part 2: ", p2(datalist.copy()))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
