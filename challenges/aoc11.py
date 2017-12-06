from os import system as run_cmd


def aoc11():

    run_cmd("cls")
    print("Advent of Code 2017 - Jim de Vries")
    print("Day 1, Challenge 1", "\n")

    captcha = input("The captcha: ").strip()

    clist = list(captcha)
    matches = []
    index = 0
    for i in clist[:-1]:
        if clist[index+1] == i:
            matches.append(int(i))
        index += 1
    if clist[-1] == clist[0]:
        matches.append(int(clist[-1]))
    print("The result: " + str(sum(matches)))
