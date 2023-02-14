import sys
from collections import deque

def solution(n, m, k, x, graph):
    distance = [0 for _ in range(n)]
    q = deque([x])
    
    while q:
        v = q.popleft()
        for vout in graph[v]:
            if vout != x and distance[vout - 1] == 0:
                distance[vout - 1] = distance[v - 1] + 1
                q.append(vout)
    
    exist = False
    for i in range(len(distance)):
        if distance[i] == k:
            exist = True
            print(i + 1)
    if not exist:
        print(-1)


n, m, k, x = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
graph = {i + 1:[] for i in range(n)}
for _ in range(m):
    s, e = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[s].append(e)

solution(n, m, k, x, graph)