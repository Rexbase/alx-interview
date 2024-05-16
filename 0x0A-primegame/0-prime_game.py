#!/usr/bin/python3

""" Task 0. Prime Game """


def is_prime(number):
    """Checks if a number is prime or not"""
    if number < 2:
        return False
    for i in range(2, int(number**1/2) + 1):
        if number % i == 0:
            return False
    return True


def maria_vs_ben(n):
    """Determines if Maria or Ben wins after a turn"""
    prime_count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count % 2 == 1


def isWinner(x, nums):
    """Returns the name of the player that won the most rounds"""

    if x < 1 or x >= 10000 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if maria_vs_ben(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
