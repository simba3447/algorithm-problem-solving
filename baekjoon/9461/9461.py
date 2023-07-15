import sys


def solution(n):
    base_data = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if 1 <= n <= 10:
        return base_data[n - 1]
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = solution(n - 1) + solution(n - 5)

    return dp[n]


t = int(sys.stdin.readline())
dp = [-1 for _ in range(101)]
for _ in range(t):
    n = int(sys.stdin.readline())
    print(solution(n))
