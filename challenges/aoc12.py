from os import system as run_cmd


def aoc12():

    run_cmd("cls")
    print("Advent of Code 2017 - Jim de Vries")
    print("Day 1, Challenge 2", "\n")

    captcha = input("The captcha: ").strip()

    clist = list(captcha)
    cl = len(clist)
    hl = round(cl/2)
    matches = []
    index = 0

    for i in clist:
        if index < hl:
            ni = index + hl
        else:
            ni = index - hl
        if clist[ni] == i:
            matches.append(int(i))
        index += 1

    print("The result: " + str(sum(matches)))
