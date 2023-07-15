import sys
from collections import deque


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
paths = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n + m)]

def solution(n, m, paths):
    paths_dict = {}
    visited = [False for _ in range(101)]
    for x, y in paths:
        paths_dict[x] = y

    q = deque([(1, 0)])

    while q:
        current, attempts = q.popleft()

        if current == 100:
            return attempts
        elif current > 100:
            pass
        elif visited[current]:
            pass
        else:
            visited[current] = True
            for i in range(1, 7):
                next = current + i
                while next in paths_dict:
                    next = paths_dict[next]
                q.append((next, attempts + 1))

print(solution(n, m, paths))
