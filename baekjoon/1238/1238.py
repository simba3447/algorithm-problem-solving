import sys
from collections import deque


INF = 10 ** 6


def dijkstra(n, x, graph, reverse):
    q = deque()
    q.append(x - 1)
    distance = [INF for _ in range(n)]
    distance[x - 1] = 0

    while q:
        curr = q.popleft()
        for i in range(n):
            if curr == i:
                continue

            if reverse:
                if distance[i] > distance[curr] + graph[i][curr]:
                    distance[i] = distance[curr] + graph[i][curr]
                    q.append(i)
            else:
                if distance[i] > distance[curr] + graph[curr][i]:
                    distance[i] = distance[curr] + graph[curr][i]
                    q.append(i)

    return distance


def solution(n, x, graph):
    distance = dijkstra(n, x, graph, False)
    distance_reverse = dijkstra(n, x, graph, True)

    result = 0
    for i in range(n):
        result = max(result, distance[i] + distance_reverse[i])

    return result


n, m, x = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
graph = [[0 if i == j else INF for j in range(n)] for i in range(n)]
for _ in range(m):
    s, e, t = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[s - 1][e - 1] = t
print(solution(n, x, graph))
