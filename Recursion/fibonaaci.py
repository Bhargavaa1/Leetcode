# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
# 509. Fibonacci Number

# Memory: O(n) Space Complexity: O(n)
# Pure Recursive Solution
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-2)+fib(n-1)


# Memory: O(n) Space Complexity: O(n)
# Recursive Solution with Memoization

fibNums = [0]*31


def fib(n: int) -> int:
    if n <= 1:
        return n
    elif fibNums[n] != 0:
        return fibNums[n]
    else:
        fibNums[n] = fibNums[n-2]+fibNums[n-1]
    return fibNums[n]

# Memory: O(n) Space Complexity: O(n)
# Dynamic Programming


fibNums = [0]*31


def fib(n: int) -> int:
    fibNums[1] = 1
    for i in range(2, 31):
        fibNums[i] = fibNums[i-1]+fibNums[i-2]
    return fibNums[i]
