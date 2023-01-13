import sys

n = int(sys.stdin.readline())

def solution(n):
    i = 0
    j = n
    while i <= j:
        d = (i + j) // 2
        if d ** 2 < n:
            i = d + 1
        else:
            j = d - 1
    return i

print(solution(n))
