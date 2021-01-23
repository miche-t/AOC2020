from os import path


# FFFFFFF = 0 -> F == 0
# BBBBBBB = 127 -> B == 1
# LLL = 0 -> L == 0
# RRR = 7 -> R == 1
def getseatID(seat):
    x = seat[:7]
    x = x.replace('F', '0')
    x = x.replace('B', '1')
    y = seat[7:]
    y = y.replace('L', '0')
    y = y.replace('R', '1')
    return int(x,2)*8+int(y,2)


def p1(datalist):
    seatID = 0
    for i in datalist:
        s = getseatID(i)
        if seatID < s:
            seatID = s
    return seatID


def p2(datalist):
    empties = list()
    seatIDs = list()
    for i in range(0,128):
        x = format(i, '07b')
        x = x.replace('0', 'F')
        x = x.replace('1', 'B')
        for j in range(0,8):
            y = format(j,'03b')
            y = y.replace('0', 'L')
            y = y.replace('1', 'R')
            seat = x + y
            try:
                datalist.index(seat)
            except ValueError:
                # seat not found
                empties.append(getseatID(seat))
            else:
                # seat found
                seatIDs.append(getseatID(seat))

    seatmin = min(seatIDs)
    seatmax = max(seatIDs)
    seatID = [i for i in empties if i > seatmin and i < seatmax]
    return seatID


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

    print("Part 1:", p1(datalist))
    print("Part 2:", p2(datalist))

if __name__ == "__main__":
  main()