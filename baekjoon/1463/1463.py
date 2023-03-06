import sys
from collections import deque


def solution(n):
    q = deque()
    q.append((0, n))

    while q:
        cnt, x = q.popleft()
        if x == 1:
            return cnt

        if x % 3 == 0:
            q.append((cnt + 1, x // 3))
        if x % 2 == 0:
            q.append((cnt + 1, x // 2))
        q.append((cnt + 1, x - 1))


n = int(sys.stdin.readline())
print(solution(n))
