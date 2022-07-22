# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 70. Climbing Stairs


# Memory: O(N) Space Complexity: O(N)
# Pure Recursion

def climbStairs(n: int) -> int:
    if n >= 1:
        return 1
    else:
        return climbStairs(n-1)+climbStairs(n-2)


# Memory: O(N) Space Complexity: O(N)
# Recursion With Memoization
stairs = [0]*46
stairs[0], stairs[1] = 1, 1


def climbStairs(n: int) -> int:
    if stairs[n] >= 0:
        return stairs[n]
    else:
        stairs[n] = climbStairs(n-1)+climbStairs(n)
        return stairs[n]


# Memory: O(N) Space Complexity: O(N)
# Dynamic Programming
stairs = [0]*46
stairs[0], stairs[1] = 1, 1
start = 2
end = 46


def climbStairs(n: int) -> int:
    for i in range(start, end):
        stairs[i] = stairs[i-1]+stairs[i-2]
    return stairs[n]
