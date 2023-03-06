import sys
from collections import deque


def solution(m, n, array):
    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    no_tomato_cnt = 0
    ripe_tomato_cnt = 0
    ripe_tomato = deque()
    for i in range(n):
        for j in range(m):
            if array[i][j] == -1:
                no_tomato_cnt += 1
            elif array[i][j] == 1:
                ripe_tomato_cnt += 1
                ripe_tomato.append((0, i, j))

    tomato_cnt = m * n - no_tomato_cnt

    cnt = ripe_tomato_cnt
    while ripe_tomato:
        time, i, j = ripe_tomato.popleft()

        for id, jd in vectors:
            if 0 <= i + id < n and 0 <= j + jd < m and array[i + id][j + jd] == 0:
                cnt += 1
                array[i + id][j + jd] = 1
                ripe_tomato.append((time + 1, i + id, j + jd))

    if cnt == tomato_cnt:
        return time
    return -1


m, n = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()]
         for _ in range(n)]
print(solution(m, n, array))
