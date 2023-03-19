import sys
import heapq


def solution(n, graph, s, e):
    INF = 10 ** 8

    cost = [INF for _ in range(n)]
    cost[s - 1] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        c_curr, curr = heapq.heappop(q)
        if c_curr > cost[curr - 1]:
            continue

        for next, c_next in graph[curr]:
            c_total = cost[curr - 1] + c_next
            if c_total < cost[next - 1]:
                cost[next - 1] = c_total
                heapq.heappush(q, (c_total, next))

    return cost[e - 1]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = {i + 1: [] for i in range(n)}
for _ in range(m):
    s, e, c = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[s].append((e, c))
s, e = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, graph, s, e))
