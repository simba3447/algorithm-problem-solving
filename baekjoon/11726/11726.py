import sys


sys.setrecursionlimit(10 ** 5)


def find(n, i):
    if n < i:
        return 0
    elif n == i:
        return 1

    if dp[i] != -1:
        return dp[i]

    result = (find(n, i + 1) + find(n, i + 2)) % 10007
    dp[i] = result
    return dp[i]


def solution(n):
    return find(n, 0)


dp = [-1 for _ in range(1001)]
n = int(sys.stdin.readline())
print(solution(n))
