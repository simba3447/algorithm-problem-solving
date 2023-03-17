import sys
from collections import deque


def solution(n, k):
    visited = [[False for _ in range(3)] for _ in range(10 ** 5 + 1)]
    q = deque()
    q.append((0, n, 0))
    cnt = 0
    min_time = -1

    while q:
        i, curr, type_ = q.popleft()

        if min_time != -1 and i > min_time:
            break

        if curr == k:
            if min_time == -1:
                min_time = i
            cnt += 1
        
        visited[curr][type_] = True


        for next, type_ in ((curr + 1, 0), (curr - 1, 1), (curr * 2, 2)):
            if 0 <= next <= 10 ** 5 and not visited[next][type_]:
                q.append((i + 1, next, type_))

    print(min_time)
    print(cnt)


n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
solution(n, k)
