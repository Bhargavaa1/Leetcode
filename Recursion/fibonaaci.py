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

# fibNums = [0]*31
# def fib(n: int) -> int:
#     if n <= 1:
#         return n
#     elif fibNums[n] != 0:
#         return fibNums[n]
#     else:


