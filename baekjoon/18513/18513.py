import sys
from collections import deque

def solution(n, k, s):
    visited = {}
    
    distances = []
    q = deque(s)
    for item in s:
        visited[item] = 0
        
    while q:
        if len(distances) >= k:
            break

        item = q.popleft()
        if item + 1 not in visited:
            visited[item + 1] = visited[item] + 1
            distances.append(visited[item] + 1)
            q.append(item + 1)

        if item - 1 not in visited:
            visited[item - 1] = visited[item] + 1
            distances.append(visited[item] + 1)
            q.append(item - 1)
        
    return sum(distances[:k])

n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
s = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, k, s))