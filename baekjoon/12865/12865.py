import sys

def find(rest, i):
    if i == n:
        return 0

    if dp[rest][i] != -1:
        return dp[rest][i]
    
    if items[i][0] > rest:
        return find(rest, i + 1)
        
    dp[rest][i] = max(items[i][1] + find(rest - items[i][0], i + 1), find(rest, i + 1))
    
    return dp[rest][i]
    
def solution(n, k, items):
    return find(k, 0)

n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
items = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
dp = [[-1 for _ in range(n+1)] for _ in range(k+1)]

print(solution(n, k, items))
