#!/usr/bin/python3
def add(a, b):
    return 98 + (a ** b)

import dis
dis.dis(add)
