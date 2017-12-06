from os import system as run_cmd
from math import sqrt, ceil, floor

def side_length(number):
    side = ceil(sqrt(number))
    side = side if side % 2 != 0 else side + 1
    return side
def aoc31():

    run_cmd("cls")
    print("Advent of Code 2017 - Jim de Vries")
    print("Day 3, Challenge 1", "\n")

    input = 289326
    side = side_length(input)
    steps_axi = (side-1)/2
    axi = [side**2 - ((side-1) * i) - floor(side/2) for i in range (0,4)]
    steps_in = min([abs(axis- input) for axis in axi])
    steps_total = steps_axi + steps_in
    result = steps_total
    print("The result: " + str(result))
