from os import system as run_cmd


def aoc21():

    run_cmd("cls")
    print("Advent of Code 2017 - Jim de Vries")
    print("Day 2, Challenge 1", "\n")

    fname = 'challenges/aoc21input.txt'

    with open(fname) as f:
        content = f.readlines()
    diffs = []
    for c in content:
        d = c.replace("\t", ",")
        d = d.replace("\n", "")
        clist = map(int, d.split(","))
        clist = sorted(clist)
        lowest = clist[0]
        highest = clist[-1]
        diff = highest - lowest
        diffs.append(diff)
    result = sum(diffs)
    print("The result: " + str(result))
