#!/usr/bin/python3
"""
execute operations
"""


def minOperations(n):
    """
    write a method that calculates
    """
    op_count = 0
    i = 2
    while n > 1:
        while n % i == 0:
            op_count += i
            n = n // i
        i += 1
    return op_count
