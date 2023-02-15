import sys

def solution(graph):
    inf = 10 ** 8
    distance = [inf for _ in range(len(graph))]
    distance[0] = 0

    for _ in range(n):
        updated = False
        for v in range(1, n + 1):
            for vout, wout in graph[v]:
                if distance[vout - 1] > distance[v - 1] + wout:
                    updated = True
                    distance[vout - 1] = distance[v - 1] + wout
        if not updated:
            return "NO"

    if updated:
        return "YES"
    return "NO"

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m, w = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph = {i + 1: [] for i in range(n)}
    for i in range(m + w):
        s, e, t = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
        if i < m:
            graph[s].append((e, t))
            graph[e].append((s, t))
        else:
            graph[s].append((e, -t))
        
    print(solution(graph))