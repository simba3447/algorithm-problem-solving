import sys
from queue import PriorityQueue

INF = 10 ** 8

def dijkstra(n, graph):
    distance = [INF for _ in range(n)]
    distance[0] = 0

    q = PriorityQueue()
    q.put((0, 0))

    while not q.empty():
        _, v = q.get()
        for vout in range(n):
            if vout == v:
                continue

            wout = graph[v][vout]
            w_total = distance[v] + wout
            if w_total < distance[vout]:
                distance[vout] = w_total
                q.put((w_total, vout))

    if distance[n-1] == INF:
        return -1
    return int(distance[n-1] * 1000)
    
        
n, w = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
m = float(sys.stdin.readline())

position = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
edges = [[int(i) - 1 for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(w)]

graph = [[INF for _  in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if i == j:
            graph[i][j] = 0
            continue
        x1, y1 = position[i]
        x2, y2 = position[j]
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if d <= m:
            graph[i][j] = graph[j][i] = d

for u, v in edges:
    graph[u][v] = graph[v][u] = 0

print(dijkstra(n, graph))