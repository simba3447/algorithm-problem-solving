import sys


def solution(n):
    if dp[n] != -1:
        return dp[n]

    if n == 0:
        result = (1, 0)
    elif n == 1:
        result = (0, 1)
    else:
        i1, j1 = solution(n - 1)
        i2, j2 = solution(n - 2)
        result = (i1 + i2, j1 + j2)

    dp[n] = result
    return dp[n]


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [-1 for _ in range(41)]
    print(*solution(n))
