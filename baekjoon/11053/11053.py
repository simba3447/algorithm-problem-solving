import sys


sys.setrecursionlimit(10 ** 6)

def solution():
    result = 0
    for i in range(n):
        max_len = find(i)
        if max_len > result:
            result = max_len
    return result

def find(i):
    if i >= n:
        return 0
    
    if dp[i] != -1:
        return dp[i]

    result = 0
    current = a[i]
    for j in range(i+1, n):
        if a[j] > current:
            max_len = find(j)
            if max_len > result:
                result = max_len
    
    dp[i] = result + 1
    return dp[i]

n = int(sys.stdin.readline())
a = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
dp = [-1 for _ in range(1000)]
print(solution())