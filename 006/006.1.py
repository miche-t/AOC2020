from os import path


def p1(datalist):
    sum = 0
    x = ""
    datalist.append("")
    for val in datalist:
        if val == "":
            sum += len(set(x))
            x = ""
        else:
            x += val
    return sum


def p2(datalist):
    sum = 0
    datalist.append("")
    next = True
    for val in datalist:
        if next:
            x = set(val)
            next = False
        elif val == "":
            sum += len(x)
            next = True
        else:
            x = x & set(val)
    return sum


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

    print("Part 1: ", p1(datalist))
    print("Part 2: ", p2(datalist))


if __name__ == "__main__":
  main()