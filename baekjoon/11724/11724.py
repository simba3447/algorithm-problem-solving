import sys
from collections import deque


def solution(n, m, graph):
    visited = [False for _ in range(n)]
    visited_cnt = 0
    cnt = 0

    while visited_cnt != n:
        cnt += 1
        q = deque([visited.index(False) + 1])

        while q:
            curr = q.popleft()
            if visited[curr - 1]:
                continue

            visited[curr - 1] = True
            visited_cnt += 1
            for next in graph[curr]:
                q.append(next)
    return cnt


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
graph = {i + 1: [] for i in range(n)}
for _ in range(m):
    s, e = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[s].append(e)
    graph[e].append(s)
print(solution(n, m, graph))
