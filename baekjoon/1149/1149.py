import sys

dp = [[0 for _ in range(3)] for _ in range(1001)]

def solution(n, array):
    for i in range(1, n + 1):
        current = array[i-1]
        for j in range(3):
            index = [0,1,2]
            index.pop(j)
            dp[i][j] = min(dp[i-1][k] + array[i-1][j] for k in index)
    
    return min(dp[n])

n = int(sys.stdin.readline())
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
print(solution(n, array))
