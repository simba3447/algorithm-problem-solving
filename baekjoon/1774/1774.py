import sys

def prim(n):
    INF = 10 ** 8
    added = [False for _ in range(n)]
    min_weight = [INF for _ in range(n)]

    result = 0
    min_weight[0] = 0

    for _ in range(n):
        min_v = None
        min_distance = INF
        for i in range(n):
            if not added[i] and min_distance > min_weight[i]:
                min_v = i
                min_distance = min_weight[i]

        added[min_v] = True
        result += min_distance
        for i in range(n):
            if not added[i] and min_weight[i] > graph[min_v][i]:
                min_weight[i] = graph[min_v][i]
    
    return result

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

graph = [[0 for _ in range(n)] for _ in range(n)]
vertices = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
edges = [[int(i) - 1 for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(m)]

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[j]
        graph[i][j] = graph[j][i] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for i, j in edges:
    graph[i][j] = graph[j][i] = 0

print('{:.2f}'.format(round(prim(n), 2)))