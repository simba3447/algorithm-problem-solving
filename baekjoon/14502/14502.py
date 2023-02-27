import sys
from itertools import combinations
from collections import deque


def solution(n, m, array):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    entry = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                entry.append((i, j))

    answer = 0
    for combination in combinations(entry, 3):
        cnt = 0
        array_copy = [[i for i in row] for row in array]
        for i, j in combination:
            array_copy[i][j] = 1
        q = deque()
        for i in range(n):
            for j in range(m):
                if array_copy[i][j] == 2:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            array_copy[i][j] = 2

            for id, jd in moves:
                if 0 <= i + id < n and 0 <= j + jd < m and array_copy[i+id][j+jd] == 0:
                    q.append((i+id, j+jd))

        for i in range(n):
            for j in range(m):
                if array_copy[i][j] == 0:
                    cnt += 1
        answer = max(answer, cnt)

    return answer


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()]
         for _ in range(n)]
print(solution(n, m, array))
