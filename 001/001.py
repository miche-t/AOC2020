from os import path

def part1(datalist, sumto):
    for x in datalist:
        diffx = sumto - int(x)
        # if str(diffx) in datalist
        try:
            y = datalist.index(str(diffx))
        except ValueError:
            y = -1
        else:
            print(int(x), diffx)
            return int(x) * diffx


def part2(datalist, findnum, numsum):
    if numsum == 1:
        # find a given number in the given list
        # if found, return the value, else return "N/A"
        try:
            i = datalist.index(str(findnum))
        except ValueError:
            # print("not found", datalist, findnum, numsum)
            return "N/A"
        else:
            print(findnum)
            return findnum
    else:
        for i in range(0,len(datalist)):
            x = int(datalist[i])
            # print(datalist, findnum, numsum, i, x)
            y = part2(datalist[i+1:], findnum-x, numsum-1)
            if type(y) == int:
                print(x)
                return x*y
            if len(datalist)-i-1 < numsum:
                # print("insufficient", datalist, findnum, numsum, i, x)
                break

def main():
    # check for file
    # exit if file not found
    if not path.exists("input.txt"):
        print("Error - input.txt not found")
        raise SystemExit()

    # read file into list, strip /n
    with open("input.txt") as f:
        datalist = f.read().splitlines()
    f.close()

    # check total entries >= number of entries required
    # exit if insufficient data
    findnum1 = 2020
    numsum1 = 2
    findnum2 = 2020
    numsum2 = 3
    if len(datalist) < numsum1:
        print("Error - input.txt insufficient data for Part 1")
    else:
        print("Part 1", "[", findnum1, "|", numsum1, "]")
        print("Product: ", part1(datalist, findnum1))

    if len(datalist) < numsum2:
        print("Error - input.txt insufficient data for Part 2")
    else:
        # Exits after the first answer is found.
        # Does not list all possible answers.
        # Assume all entries are integers.
        print("Part 2:", "[", findnum2, "|", numsum2, "]")
        print("Product: ", part2(datalist, findnum2, numsum2))


if __name__ == "__main__":
  main()