#! /usr/bin/env python3

import sys
import re
import itertools
import numpy
import time
from functools import lru_cache
from collections import deque, defaultdict, Counter

inputs = dict((f"day{i+1}", f"inputs/{i+1}") for i in range(25))


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
