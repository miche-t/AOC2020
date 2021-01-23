from os import path
import re


def checknum(num, min, max):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        return (min <= num <= max)


# Part 1
# byr(Birth Year)
# iyr(Issue Year)
# eyr(Expiration Year)
# hgt(Height)
# hcl(Hair Color)
# ecl(Eye Color)
# pid(Passport ID)
# cid(Country ID)
def p1(datalist):
    fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    validpass = 0
    i = 0
    line = ""
    while i <= len(datalist):
        if i == len(datalist) or len(datalist[i]) == 0:
            if len(line) > 0:
                ppdata = line.split(" ")
                checkfields = [s for s in ppdata if any(xs in s for xs in fields)]
                if len(checkfields) == 7:
                    validpass += 1
            line = ""
        else:
            if len(line) > 0:
                line += ' '
            line += datalist[i]
        i += 1
    return validpass


# Part 2
# byr(Birth Year) - four digits; at least 1920 and at most 2002.
# iyr(Issue Year) - four digits; at least 2010 and at most 2020.
# eyr(Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt(Height) - a number followed by either cm or in: If cm, the number must be at least 150 and at most 193. If in, the number must be at least 59 and at most 76.
# hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
# ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid(Passport ID) - a nine - digit number, including leading zeroes.
# cid(Country ID) - ignored, missing or not.
def p2(datalist):
    byrmin = 1920
    byrmax = 2002
    iyrmin = 2010
    iyrmax = 2020
    eyrmin = 2020
    eyrmax = 2030
    hgtcmmin = 150
    hgtcmmax = 193
    hgtinmin = 59
    hgtinmax = 76
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pidmin = 000000000
    pidmax = 999999999
    # fields excluding "cid"
    fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    validpass = 0
    i = 0
    line = ""
    while i <= len(datalist):
        if i == len(datalist) or len(datalist[i]) == 0:
            if len(line) > 0:
                checkfields = line.split(" ")
                ppdata = [s for s in checkfields if any(xs in s for xs in fields)]
                if len(ppdata) == len(fields):
                    for j, val in enumerate(ppdata):
                        fval = val.split(":")[0]
                        if len(fval) != 3:
                            break
                        dval = val.split(":")[1]
                        if fval == "byr" and not checknum(dval, byrmin, byrmax):
                            break
                        elif fval == "iyr" and not checknum(dval, iyrmin, iyrmax):
                            break
                        elif fval == "eyr" and not checknum(dval, eyrmin, eyrmax):
                            break
                        elif fval == "hgt":
                            unit = dval[len(dval)-2:].lower()
                            if not ((unit == "cm" and checknum(dval[:len(dval)-2], hgtcmmin, hgtcmmax)) or \
                                    (unit == "in" and checknum(dval[:len(dval)-2], hgtinmin, hgtinmax))):
                                break
                        elif fval == "hcl":
                            rg6 = re.compile("^#([A-Fa-f0-9]{6})$")
                            if len(dval) != 7 or not re.search(rg6, dval):
                                break
                        elif fval == "ecl":
                            try:
                                z = ecl.index(dval)
                            except ValueError:
                                break
                        elif fval == "pid":
                            if len(dval) != len(str(pidmax)) or not checknum(dval, pidmin, pidmax):
                                break
                        if j == len(ppdata)-1:
                            validpass += 1
                line = ""
        else:
            if len(line) > 0:
                line += ' '
            line += datalist[i]
        i += 1
    return validpass


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
