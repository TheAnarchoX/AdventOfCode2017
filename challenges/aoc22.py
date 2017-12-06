from os import system as run_cmd
import itertools


def aoc22():

    run_cmd("cls")
    print("Advent of Code 2017 - Jim de Vries")
    print("Day 2, Challenge 2", "\n")

    fname = 'challenges/aoc21input.txt'

    with open(fname) as f:
        content = f.readlines()
    result = 0
    for c in content:
        print("Line " + str(content.index(c) + 1))
        d = c.replace("\t", ",")
        d = d.replace("\n", "")
        clist = list(map(int, d.split(",")))
        for i in itertools.combinations(clist, 2):
            if max(i) % min(i) == 0:
                result += max(i) / min(i)
                break
    print("The result: " + str(result))

