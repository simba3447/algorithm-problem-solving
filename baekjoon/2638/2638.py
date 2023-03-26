import sys
from collections import deque


VECTOR = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def expose(y, x):
    air_q = deque([(y, x)])
    while air_q:
        y, x = air_q.popleft()
        if not (0 <= y < n or 0 <= x < m) or board[y][x] == 1 or board[y][x] == 2:
            continue

        board[y][x] = 2
        for dy, dx in VECTOR:
            air_q.append((y + dy, x + dx))


def exposed(y, x):
    return sum([board[y + yd][x + xd] == 2 for yd, xd in VECTOR]) >= 2


def solution(n, m):
    expose(0, 0)

    cheeze_q = deque()
    for y in range(1, n - 1):
        for x in range(1, m - 1):
            if board[y][x] == 1 and exposed(y, x):
                cheeze_q.append((y, x, 1))

    result = 0
    while cheeze_q:
        y, x, t = cheeze_q.popleft()

        if board[y][x] == 2 or not exposed(y, x):
            continue

        result = t

        board[y][x] = 2
        for dy, dx in VECTOR:
            if board[y + dy][x + dx] == 0:
                air_q = deque([(y + dy, x + dx)])
                while air_q:
                    i, j = air_q.popleft()
                    if not (0 <= i < n or 0 <= j < m) or board[i][j] == 2 or board[i][j] == 1:
                        continue

                    board[i][j] = 2
                    for di, dj in VECTOR:
                        if board[i + di][j + dj] == 1 and exposed(i + di, j + dj):
                            cheeze_q.append((i + di, j + dj, t + 1))

                        air_q.append((i + di, j + dj))

        for dy, dx in VECTOR:
            if board[y + dy][x + dx] == 1 and exposed(y + dy, x + dx):
                cheeze_q.append((y + dy, x + dx, t + 1))

    return result


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
board = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()]
         for _ in range(n)]
print(solution(n, m))
