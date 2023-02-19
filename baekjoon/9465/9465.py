import sys


def solution(n, array):
    dp = [[0 for _ in range(3)] for _ in range(2)]

    for i in range(n):
        prev = dp[i % 2]
        curr = dp[i % 2 - 1]
        curr[0] = max(prev[1], prev[2]) + array[0][i]
        curr[1] = max(prev[0], prev[2]) + array[1][i]
        curr[2] = max(prev[0], prev[1])
    return max(dp[n % 2])

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    array = [[int(i) for i in input().split()] for _ in range(2)]
    print(solution(n, array))