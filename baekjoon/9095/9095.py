import sys
from collections import deque


def solution(n):
    q = deque()
    q.append(0)

    cnt = 0
    while q:
        curr = q.popleft()
        if curr == n:
            cnt += 1
            continue
        if curr > n:
            continue
        q.append(curr + 1)
        q.append(curr + 2)
        q.append(curr + 3)

    return cnt


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(solution(n))
