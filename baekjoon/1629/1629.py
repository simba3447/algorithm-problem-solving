import sys

def solution(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 0:
        result = solution(a, b // 2, c)
        return result ** 2 % c
    else:
        return (solution(a, b - 1, c) * solution(a, 1, c)) % c


a, b, c = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(a, b, c))
