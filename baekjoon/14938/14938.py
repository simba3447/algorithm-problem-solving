import sys


def solution(n, m, adj_graph, item):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if adj_graph[i][j] > adj_graph[i][k] + adj_graph[k][j]:
                    adj_graph[i][j] = adj_graph[i][k] + adj_graph[k][j]
    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if adj_graph[i][j] <= m:
                cnt += item[j]
        max_cnt = max(max_cnt, cnt)

    return max_cnt


INF = 10 ** 8
n, m, r = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
adj_graph = [[0 if i == j else INF for j in range(n)] for i in range(n)]

item = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
for _ in range(r):
    a, b, l = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    a -= 1
    b -= 1
    adj_graph[a][b] = adj_graph[b][a] = l
print(solution(n, m, adj_graph, item))
