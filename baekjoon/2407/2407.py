import sys

def solution(n, m):
    if m * 2 > n:
        m = n - m
    answer = 1
    for i in range(m):
        answer *= n - i
    for i in range(m):
        answer = answer // (i + 1)
    return answer

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, m))