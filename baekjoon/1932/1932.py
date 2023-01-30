import sys

def solution(i, j):
    if i == n:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    dp[i][j] = triangle[i][j] + max(solution(i + 1, j), solution(i + 1, j + 1))
    return dp[i][j]
    
n = int(sys.stdin.readline())
triangle = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

print(solution(0, 0))