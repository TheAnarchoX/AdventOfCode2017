import os
from os import system as run_cmd
import glob
import importlib
challenges = [os.path.basename(x)[:-3] for x in glob.glob('challenges/*.py')]

challenges.remove("__init__")
run_cmd("cls")
print("Advent of Code 2017 - Jim de Vries", '\n')
print("Challenges made: ")


for c in challenges:
    cc = c[-1]
    if len(c) == 5:
        cday = c[3]
    else:
        cday = c[3:4]
    print("Challenge "+cday+"."+cc)

target = input("\nWhich challenge would you like to see (e.g.: 32 for day 3, challenge 2):").strip()
module = importlib.import_module('challenges.aoc'+target)
func = getattr(module, 'aoc'+target)
func()
