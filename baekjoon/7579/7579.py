import sys


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
dp = [{} for _ in range(n)]
mlist = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
clist = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

dp = [0 for _ in range(10001)]
for i in range(n):
    for j in reversed(range(clist[i], 10001)):
        dp[j] = max(dp[j], dp[j - clist[i]] + mlist[i])

for i in range(10001):
    if dp[i] >= m:
        print(i)
        break