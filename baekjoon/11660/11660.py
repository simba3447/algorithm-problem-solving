import sys

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
board = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        result = board[j][i]
        if i - 1 >= 0:
            result += dp[j][i - 1]
        if j - 1 >= 0:
            result += dp[j - 1][i]
        if i - 1 >= 0 and j - 1 >= 0:
            result -= dp[j - 1][i - 1]
        dp[j][i] = result

for _ in range(m):
    x1, y1, x2, y2 = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    result = dp[x2 - 1][y2 - 1]
    if x1 - 2 >= 0:
        result -= dp[x1 - 2][y2 - 1]
    if y1 - 2 >= 0:
        result -= dp[x2 - 1][y1 - 2]
    if x1 - 2 >= 0 and y1 - 2 >= 0:
        result += dp[x1 - 2][y1 - 2]
    print(result)