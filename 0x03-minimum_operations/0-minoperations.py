#!/usr/bin/python3
"""
execute only two operations
"""


def minOperations(n):
    """
    write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
    """
    op_count = 0
    i = 2
    while n > 1:
        while n % i == 0:
            op_count += i
            n = n // i
        i += 1
    return op_count