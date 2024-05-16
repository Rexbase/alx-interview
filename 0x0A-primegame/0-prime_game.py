#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of
    integers representing
    the Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def isWinner(total_count, boxes):
    """
    Determine if the player who goes first will win the game
    """
    if not boxes or total_count < 1:
        return False
    primes = [0] * (max(boxes) + 1)
    primes[0] = 1
    primes[1] = 1
    for i in range(2, len(primes)):
        if primes[i] == 0:
            for j in range(i * i, len(primes), i):
                primes[j] = 1
    count = sum(1 for box in boxes if primes[box] == 0)
    return count % 2 != 0

