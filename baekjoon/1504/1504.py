import sys
from queue import PriorityQueue


INF = 10 ** 8


def dijkstra(n, graph, s):
    distance = [INF for _ in range(n)]
    distance[s] = 0
    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        _, v_start = q.get()
        for v_end in range(n):
            if v_end == v_start:
                continue
            w_end = graph[v_start][v_end]
            w_total = distance[v_start] + w_end
            if w_total < distance[v_end]:
                distance[v_end] = w_total
                q.put((w_total, v_end))

    return distance


def solution(n, graph, u, v):

    distance_u = dijkstra(n, graph, u)
    distance_v = dijkstra(n, graph, v)
    path_1 = distance_u[0] + distance_u[v] + distance_v[n - 1]
    path_2 = distance_v[0] + distance_u[v] + distance_u[n - 1]
    min_path = min(path_1, path_2)
    if min_path >= INF:
        return -1
    return min_path


n, e = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
graph = [[0 if i == j else INF for i in range(n)] for j in range(n)]
for _ in range(e):
    a, b, c = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    a -= 1
    b -= 1
    graph[a][b] = graph[b][a] = c
u, v = [int(i) - 1 for i in sys.stdin.readline().rstrip().rsplit()]

print(solution(n, graph, u, v))
