from os import path
import re


def findbags(findx, baglist):
    found = []
    for bags in baglist:
        if bags[2] == findx:
            found.append(bags[0])
            found += findbags(bags[0], baglist)
    return found


def getbags(datalist):
    baglist = list()
    for val in datalist:
        x = val.split(" contain ")
        bag0 = x[0].replace(" bags", "")
        bagx = x[1].split(", ")
        for bag in bagx:
            bag = re.sub(r' bag.*', '', bag)
            if bag[0].isdigit():
                i = bag.find(" ")
                num = int(bag[:i])
                bag = bag[i+1:]
            else:
                num = 0
            baglist.append([bag0, num, bag])
    return baglist


def countbags(findx, baglist):
    count = 0
    for bags in baglist:
        if bags[0] == findx:
            count += bags[1]*(1 + countbags(bags[2], baglist))
        # print(bags,count)
    return count


def main():
    # check for file, exit if file not found
    fname = "input.txt"
    if not path.exists(fname):
        print("Error - ", fname, " not found")
        raise SystemExit()

    # read file into list, strip /n
    with open(fname) as f:
        datalist = f.read().splitlines()
    f.close()

    findx = "shiny gold"
    print("Part 1: ", len(set(findbags(findx, getbags(datalist)))))
    print("Part 2: ", countbags(findx, getbags(datalist)))


if __name__ == "__main__":
    main()
