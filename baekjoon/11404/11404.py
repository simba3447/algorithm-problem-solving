import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

inf = 10 ** 8
graph = [[0 if i==j else inf for i in range(n)] for j in range(n)]

for _ in range(m):
    s, e, w = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[s - 1][e - 1] = min(w, graph[s - 1][e - 1])

for k in range(n):
    for i in range(n):
        for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph:
    for i in row:
        if i == inf: print(0, end=' ')
        else: print(i, end=' ')
    print()