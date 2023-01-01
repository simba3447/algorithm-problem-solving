import sys

k = int(sys.stdin.readline())

def solution(k):
    if k == 1:
        return 0
    n = 1
    while True:
        if n * 2 >= k:
            break
        n *= 2
    return 1 if solution(k-n) == 0 else 0

print(solution(k))
