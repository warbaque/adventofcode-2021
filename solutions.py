#! /usr/bin/env python3

import sys
import re
import itertools
import numpy
import time
from functools import lru_cache
from collections import deque, defaultdict, Counter

inputs = dict((f"day{i+1}", f"inputs/{i+1}") for i in range(25))


# https://adventofcode.com/2021/day/1
def day1(input):
    numbers = [int(i) for i in input.split()]
    sliding_sums = [sum(x) for x in zip(numbers, numbers[1:], numbers[2:])]

    print(sum(x1 > x0 for x0, x1 in zip(numbers, numbers[1:])))
    print(sum(x1 > x0 for x0, x1 in zip(sliding_sums, sliding_sums[1:])))


# https://adventofcode.com/2021/day/2
def day2(input):
    commands = input.strip().split('\n')
    r = re.compile(r'(\S+) (\d+)')

    move = {
        'forward'   : lambda x: x,
        'up'        : lambda x: x * (-1j),
        'down'      : lambda x: x * (+1j),
    }

    pos1 = 0
    pos2 = 0
    for cmd in commands:
        direction, length = r.match(cmd).groups()
        pos1 += move[direction](int(length))
        if direction == 'forward':
            pos2 += int(length) * (1 + pos1.imag * 1j)

    print(int(pos1.real * pos1.imag))
    print(int(pos2.real * pos2.imag))



def profiler(method):
    def wrapper(*arg, **kw):
        t0 = time.time()
        ret = method(*arg, **kw)
        print(f'[{method.__name__}] {time.time()-t0:2.5f} sec', file=sys.stderr)
        return ret
    return wrapper

@profiler
def solver(day):
    with open(inputs[day], "r") as f:
        globals()[day](f.read())

@profiler
def all_days(*args, **kwargs):
    for i in range(25):
        if f"day{i+1}" not in globals():
            break
        print(f"===== DAY {i+1:2d} =====")
        solver(f"day{i+1}")
        print()

globals()[sys.argv[1]](*sys.argv[2:])
