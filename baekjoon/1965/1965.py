import sys

sys.setrecursionlimit(10 ** 6)

def find(i, last):
    if i == n:
        return 0

    if dp[i][last] != -1:
        return dp[i][last]
    
    if array[i] > last:
        result = max(1 + find(i + 1, array[i]), find(i + 1, last))
    else:
        result = find(i + 1, last)
    
    dp[i][last] = result
    return result

def solution(n, array):
    return find(0, 0)

n = int(sys.stdin.readline())
array = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
dp = [[-1 for _ in range(1001)] for _ in range(1001)]

print(solution(n, array))