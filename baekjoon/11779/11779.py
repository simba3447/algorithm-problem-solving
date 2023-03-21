import sys
import heapq


def solution(n, m, graph, a, b):
    INF = 10 ** 8

    weights = [INF for _ in range(n)]
    weights[a - 1] = 0
    parent = [-1 for _ in range(n)]
    parent[a - 1] = a - 1
    q = []
    heapq.heappush(q, (0, a, a))

    while q:
        w, curr, prev = heapq.heappop(q)

        if weights[curr - 1] < w:
            continue
        parent[curr - 1] = prev - 1

        for next, w_next in graph[curr]:
            w_total = weights[curr - 1] + w_next
            if w_total < weights[next - 1]:
                weights[next - 1] = w_total
                heapq.heappush(q, (w_total, next, curr))

    print(weights[b - 1])
    curr = b - 1
    path = []
    while True:
        path.append(curr)
        curr = parent[curr]
        if parent[curr] == curr:
            path.append(curr)
            break
    print(len(path))
    for i in reversed(path):
        print(i + 1, end=' ')


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = {i + 1: [] for i in range(n)}
for _ in range(m):
    a, b, w = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[a].append((b, w))
a, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
solution(n, m, graph, a, b)
