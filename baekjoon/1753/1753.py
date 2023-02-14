import sys
from queue import PriorityQueue

def solution(v, e, k, graph):
    inf = 10 ** 8
    distance = [inf for _ in range(v)]
    distance[k - 1] = 0

    q = PriorityQueue()
    q.put((0, k))

    while not q.empty():
        w, v = q.get()
        for vout, wout in graph[v]:
            w_total = distance[v - 1] + wout
            if w_total < distance[vout - 1]:
                distance[vout - 1] = w_total
                q.put((w_total, vout))
    for item in distance:
        if item == inf:
            print("INF")
        else:
            print(item)
    
v, e = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
k = int(sys.stdin.readline())
graph = {i + 1: [] for i in range(v)}
for _ in range(e):
    i, j, w = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[i].append((j, w))

solution(v, e, k, graph)
    