from os import path

def part1(datalist):
    validpass = 0
    for i in datalist:
        line = i.split(' ')
        x = line[0].split('-')
        min = int(x[0])
        max = int(x[1])
        char = line[1].split(':')[0]
        pw = line[2]
        numchar = pw.count(char)
        if numchar >= min and numchar <= max:
            validpass += 1
    return validpass

def part2(datalist):
    validpass = 0
    for i in datalist:
        line = i.split(' ')
        x = line[0].split('-')
        first = int(x[0])-1
        second = int(x[1])-1
        char = line[1].split(':')[0]
        pw = line[2]
        if pw[first] == char and pw[second] != char:
            validpass +=1
            print(char, pw, first, second, pw[first], pw[second], "1st")
        else:
            if pw[first] != char and pw[second] == char:
                validpass += 1
                print(char, pw, first, second, pw[first], pw[second], "2nd")
            else:
                print(char, pw, first, second, pw[first], pw[second], "no")

    return validpass


def main():
    # check for file, exit if file not found
    if not path.exists("input.txt"):
        print("Error - input.txt not found")
        raise SystemExit()

    # read file into list, strip /n
    with open("input.txt") as f:
        datalist = f.read().splitlines()
    f.close()

    print("Part 1:", part1(datalist))
    print("Part 2: ", part2(datalist))

if __name__ == "__main__":
  main()