import sys
from collections import deque
import time

def solution(n, k, d, graph, in_degree, w):
    q = deque([])
    cost = [0 for _ in range(n)]

    for i in range(n):
        if in_degree[i] == 0:
            q.append(i + 1)
            cost[i] = d[i]
    
    while q:
        item = q.popleft()

        for out in graph[item]:

            cost[out - 1] = max(cost[out - 1], cost[item - 1] + d[out - 1])
            in_degree[out - 1] -= 1
            if in_degree[out - 1] == 0:
                q.append(out)

    return cost[w - 1]

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    d = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    in_degree = [0 for _ in range(n)]
    graph = {i + 1:[] for i in range(n)}
    for _ in range(k):
        x, y = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
        graph[x].append(y)
        in_degree[y-1] += 1
    w = int(sys.stdin.readline())
    
    print(solution(n, k, d, graph, in_degree, w))
