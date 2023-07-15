import sys


n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

if n == 1:
    print(numbers[-1])
else:
    dp[0] = 0
    dp[1] = numbers[0]
    dp[2] = numbers[0] + numbers[1]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + numbers[i - 2] + numbers[i - 1], dp[i - 2] + numbers[i - 1])

    print(dp[-1])