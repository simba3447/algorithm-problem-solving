import sys

def solution(a, b):
    for i in range(len(a) + 1):
        dp[i][0] = i
    for i in range(len(b) + 1):
        dp[0][i] = i
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != b[j]:
                dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
            else:
                dp[i+1][j+1] = dp[i][j]
    return dp[-1][-1]

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
dp = [[-1 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
print(solution(a, b))
