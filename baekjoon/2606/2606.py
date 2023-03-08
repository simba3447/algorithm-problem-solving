import sys
from collections import deque


def solution(v, graph):
    visited = [False for _ in range(v)]
    q = deque()
    q.append(1)
    cnt = 0
    while q:
        curr = q.popleft()
        if visited[curr - 1]:
            continue
        visited[curr - 1] = True
        cnt += 1

        for next in graph[curr]:
            q.append(next)
    cnt -= 1
    return cnt


v = int(sys.stdin.readline())
graph = {i + 1: [] for i in range(v)}
e = int(sys.stdin.readline())
for _ in range(e):
    s, e = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[s].append(e)
    graph[e].append(s)
print(solution(v, graph))
