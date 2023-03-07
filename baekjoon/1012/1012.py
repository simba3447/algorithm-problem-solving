import sys
from collections import deque


def solution(m, n, k, points):
    VECTORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    points_set = set()
    for x, y in points:
        points_set.add((x, y))
    cnt = 0

    while len(points_set) != 0:
        q = deque()
        cnt += 1
        point = points_set.pop()
        q.append(point)
        while q:
            x, y = q.popleft()
            for xd, yd in VECTORS:
                if 0 <= x + xd < m and 0 <= y + yd < n and (x + xd, y + yd) in points_set:
                    points_set.remove((x + xd, y + yd))
                    q.append((x + xd, y + yd))
    return cnt

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    points = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(k)]
    print(solution(m, n, k, points))

    