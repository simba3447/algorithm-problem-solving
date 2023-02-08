import sys
from collections import deque

def solution(n, m, graph, indegree):
    result = [1 for _ in range(n)]
    q = deque([])
    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i+1)

    while q:
        current = q.popleft() 
        for item in graph[current]:
            indegree[item - 1] -= 1
            if indegree[item - 1] == 0:
                result[item - 1] += result[current - 1]
                q.append(item)
    return result
        
n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
graph = {i + 1: [] for i in range(n)}
indegree = [0 for _ in range(n)]

for i in range(m):
    a, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    graph[a].append(b)
    indegree[b-1] += 1

print(*solution(n, m, graph, indegree))
