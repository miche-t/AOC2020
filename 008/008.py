from os import path


def get_oplist(datalist):
    oplist = []
    for val in datalist:
        op = val[:3]
        arg = int(val[4:])
        oplist.append([op, arg])
    return oplist


def p1(oplist):
    acc = 0
    done = set()
    i = 0
    while i < len(oplist):
        op = oplist[i][0]
        arg = int(oplist[i][1])
        done.add(i)
        if op == "nop":
            i += 1
        elif op == "acc":
            acc += arg
            i += 1
        elif op == "jmp":
            i += arg
        if i in done:
            return [False, acc]
    return [True, acc]


def p2(oplist):
    res = p1(oplist)
    if res[0]:
        return res
    i = 0
    while i < len(oplist):
        if oplist[i][0] in {'nop', 'jmp'}:
            op0 = oplist[i][0]
            if op0 == 'nop':
                oplist[i][0] = 'jmp'
            else:
                oplist[i][0] = 'nop'
            res = p1(oplist)
            if res[0]:
                return res
            oplist[i][0] = op0
        i += 1
    return res


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

    oplist = get_oplist(datalist)
    print("Part 1: ", p1(oplist))
    print("Part 2: ", p2(oplist))


if __name__ == "__main__":
    main()
