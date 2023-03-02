import sys


def count(i):
    return bin(i).count("1")


def solution(n, k):
    visited = 0
    cnt = 0
    i = 0
    while True:
        if i == n - 1:
            break
        if not (visited & (1 << i)):
            j = i
            while True:
                if j >= n - 1:
                    break
                if not (visited & (1 << j)):
                    visited |= (1 << j)
                    cnt += 1
                if cnt == k:
                    return j + 2
                j += i + 2
        i += 1


n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, k))
