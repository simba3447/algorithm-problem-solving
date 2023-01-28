import sys

def solution(a, b):
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[-1][-1]

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
print(solution(a, b))