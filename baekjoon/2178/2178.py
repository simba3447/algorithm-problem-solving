import sys
from collections import deque


def solution(n, m, array):
    q = deque([(0, 0, 1)])
    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        y, x, t = q.popleft()

        if y == n - 1 and x == m - 1:
            return t

        if array[y][x] == 0:
            continue

        array[y][x] = 0
        for i, j in vectors:
            if 0 <= y + i < n and 0 <= x + j < m and array[y + i][x + j] == 1:
                q.append((y + i, x + j, t + 1))


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]

print(solution(n, m, array))
