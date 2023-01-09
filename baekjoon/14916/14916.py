import sys

def solution(n):
    if n % 5 == 0:
        return n // 5
    s = n // 5
    for i in reversed(range(s + 1)):
        rest = n - i * 5
        if rest % 2 == 0:
            return i + rest // 2
    return -1

n = int(sys.stdin.readline())
print(solution(n))
