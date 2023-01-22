import sys

def solution(n):
    while n != 1:
        # print(n)
        for i in range(2, n+1):
            if n % i == 0:
                print(i)
                n = n // i
                break

n = int(sys.stdin.readline())
solution(n)