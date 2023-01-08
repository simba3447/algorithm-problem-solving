import sys

cache = [-1 for _ in range(21)]

def solution(n):
    if n == 0: return 0
    if n == 1: return 1
    if cache[n] == -1: 
        cache[n] = solution (n - 2) + solution(n - 1)

    return cache[n]

n = int(sys.stdin.readline())

print(solution(n))
