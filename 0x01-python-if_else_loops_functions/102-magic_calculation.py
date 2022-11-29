#!/usr/bin/python3
# Author - Daniel Boateng

def magic_calculation(a, b, c):
    """Match bytecode provided in the task."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
