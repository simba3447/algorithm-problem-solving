import sys

def solution(n):
    return "SK" if n % 2 == 1 else "CY"

n = int(sys.stdin.readline())
print(solution(n))
