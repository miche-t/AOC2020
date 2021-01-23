from os import path

def trees(datalist, right, down):
    count = 0
    col = right
    row = down
    for i in range(1, len(datalist)):
        if row > len(datalist):
            break
        line = datalist[row]
        if col >= len(line):
            col = col % len(line)
        if line[col] == "#":
            count += 1
        col += right
        row += down
    print(count)
    return count

def main():
    fname = "input.txt"
    # check for file, exit if file not found
    if not path.exists(fname):
        print("Error - ", fname, " not found")
        raise SystemExit()

    # read file into list, strip /n
    with open(fname) as f:
        datalist = f.read().splitlines()
    f.close()


    # Part 1
    print("Part 1: ", trees(datalist, 3, 1))

    # Part 2
    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    part2 = trees(datalist, 1, 1)
    part2 *= trees(datalist, 3, 1)
    part2 *= trees(datalist, 5, 1)
    part2 *= trees(datalist, 7, 1)
    part2 *= trees(datalist, 1, 2)
    print("Part 2: ", part2)


if __name__ == "__main__":
  main()