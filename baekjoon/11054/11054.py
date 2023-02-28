import sys

sys.setrecursionlimit(10 ** 5)

def find(i, prev, mode): # mode: 0 - increase / 1 - decrease
    global a
    global n
    global dp
    if i >= n:
        return 0
    if dp[i][prev][mode] != -1:
        return dp[i][prev][mode]
    if mode == 0:
        if a[i] > prev:
            result = max(1 + find(i + 1, a[i], 0), find(i + 1, prev, 0))
        elif a[i] < prev:
            result = max(find(i + 1, prev, 0), 1 + find(i + 1, a[i], 1))
        else:
            result = find(i + 1, prev, 0)

    elif mode == 1:
        if a[i] < prev:
            result = max(1 + find(i + 1, a[i], 1), find(i + 1, prev, 1))
        else:
            result = find(i + 1, prev, 1)
    
    dp[i][prev][mode] = result
    return result
    
def solution(n, a):
    return find(0, 0, 0)


n = int(sys.stdin.readline())
a = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
dp = [[[-1 for _ in range(2)] for _ in range(1001)] for _ in range(n + 1)]
print(solution(n, a))