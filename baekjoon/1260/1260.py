import sys
from collections import deque

def dfs(graph, n, v):
    stack = [v]
    visited = [False for _ in range(n)]

    while stack:
        item = stack.pop()
        if visited[item - 1]:
            continue
        print(item, end=' ')
        visited[item - 1] = True
        for i in reversed(graph[item]):
            stack.append(i)
    print()


def bfs(graph, n, v):
    q = deque([v])
    visited = [False for _ in range(n)]

    while q:
        item = q.popleft()
        if visited[item - 1]:
            continue
        print(item, end=' ')
        visited[item - 1] = True
        for i in graph[item]:
            q.append(i)
    print()

n, m, v = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
graph = {}
for i in range(n):
    graph[i + 1] = []

for _ in range(m):
    a, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

dfs(graph, n, v)
bfs(graph, n, v)