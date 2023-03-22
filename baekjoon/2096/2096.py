import sys


n = int(sys.stdin.readline())
max_dp = [[0 for _ in range(3)] for _ in range(2)]
min_dp = [[0 for _ in range(3)] for _ in range(2)]

for i in range(n):
    j = i % 2
    a, b, c = [int(a) for a in sys.stdin.readline().rstrip().rsplit()]
    max_dp[j] = [a, b, c]
    min_dp[j] = [a, b, c]

    if i > 0:
        max_dp[j][0] += max(max_dp[j - 1][0], max_dp[j - 1][1])
        max_dp[j][1] += max(max_dp[j - 1][0], max_dp[j - 1][1], max_dp[j - 1][2])
        max_dp[j][2] += max(max_dp[j - 1][1], max_dp[j - 1][2])

        min_dp[j][0] += min(min_dp[j - 1][0], min_dp[j - 1][1])
        min_dp[j][1] += min(min_dp[j - 1][0], min_dp[j - 1][1], min_dp[j - 1][2])
        min_dp[j][2] += min(min_dp[j - 1][1], min_dp[j - 1][2])

max_sum = max(max_dp[n % 2 - 1])
min_sum = min(min_dp[n % 2 - 1])
print(max_sum, min_sum)