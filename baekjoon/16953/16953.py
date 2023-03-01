import sys
from collections import deque


def solution(a, b):
    q = deque()
    q.append((1, a))
    cnt = 0

    while q:
        depth, i = q.popleft()
        if cnt != depth:
            cnt += 1
        
        if i == b:
            return cnt

        if i > b:
            continue
        if i * 2 <= 10 ** 9:
            q.append((cnt + 1, i * 2))
        if i * 10 + 1 <= 10 ** 9:
            q.append((cnt + 1, i * 10 + 1))
    return -1


a, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(a, b))