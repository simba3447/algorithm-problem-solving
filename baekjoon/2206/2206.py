import sys
from collections import deque

def solution(n, m, array):
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
    vertors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()
        if x == m - 1 and y == n - 1:
            return visited[w][y][x]

        for i, j in vertors:
            xa = x + i
            ya = y + j
            if xa not in range(m) or ya not in range(n) or visited[0][ya][xa] or (w == 1 and visited[1][ya][xa]):
                continue
            
            if w == 0:
                if array[y][x] == 0:
                    visited[w][ya][xa] = visited[w][y][x] + 1
                    q.append((xa, ya, w))
                else:
                    visited[w + 1][ya][xa] = visited[w][y][x] + 1
                    q.append((xa, ya, w + 1))
            else:
                if array[y][x] == 0:
                    visited[w][ya][xa] = visited[w][y][x] + 1
                    q.append((xa, ya, w))
    return -1
    
n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]
print(solution(n, m, array))