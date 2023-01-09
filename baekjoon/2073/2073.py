import sys

d, p = (int(i) for i in sys.stdin.readline().split())

l = [0 for _ in range(p)]
c = [0 for _ in range(p)]

for i in range(p):
    l[i], c[i] = (int(j) for j in sys.stdin.readline().split())
    
def solution(d, p, l, c):
    dp = [0] * (d + 1)
    dp[0] = 1e9

    for i in range(p):
        for j in reversed(range(d + 1)):
            k = j + l[i]
            if k > d: continue
            dp[k] = max(min(dp[j], c[i]), dp[k])
    return dp[d]

print(solution(d, p, l, c))