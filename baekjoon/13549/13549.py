import sys
from collections import deque

def solution(n, k):
    q = deque([n])
    visited = {n: 0}

    while q:
        current = q.popleft()
        
        if current == k:
            return visited[current]

        for i in [current * 2, current + 1, current - 1]:
            if i not in visited and 0 <= i <= 10 ** 5:
                if i == current * 2:
                    q.appendleft(i)
                    visited[i] = visited[current]
                else:
                    q.append(i)
                    visited[i] = visited[current] + 1

n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, k))