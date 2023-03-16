import sys
from collections import deque


def move_ball(ry_, rx_, by_, bx_, dy, dx, board):
    ry = ry_
    rx = rx_
    by = by_
    bx = bx_

    r_finished = False
    b_finished = False
    if rx * dx > bx * dx or ry * dy > by * dy:
        while board[ry + dy][rx + dx] != '#':
            ry += dy
            rx += dx
            if board[ry][rx] == 'O':
                r_finished = True
        while board[by + dy][bx + dx] != '#' and not (not r_finished and by + dy == ry and bx + dx == rx):
            by += dy
            bx += dx
            if board[by][bx] == 'O':
                b_finished = True
    else:
        while board[by + dy][bx + dx] != '#':
            by += dy
            bx += dx
            if board[by][bx] == 'O':
                b_finished = True
        while board[ry + dy][rx + dx] != '#' and not (ry + dy == by and rx + dx == bx):
            ry += dy
            rx += dx
            if board[ry][rx] == 'O':
                r_finished = True

    succeed = r_finished and not b_finished
    failed = b_finished

    return succeed, failed, ry, rx, by, bx


def solution(n, m, board):
    VECTORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'B':
                b_position = (i, j)
            elif board[i][j] == 'R':
                r_position = (i, j)

    q = deque([(1, *r_position, *b_position)])

    while q:
        t, ry_, rx_, by_, bx_ = q.popleft()
        if t > 10:
            break

        for dy, dx in VECTORS:
            finished, failed, ry, rx, by, bx = move_ball(
                ry_, rx_, by_, bx_, dy, dx, board)
            if finished:
                return t
            if not failed:
                q.append((t + 1, ry, rx, by, bx))

    return -1


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
board = [sys.stdin.readline().rstrip() for _ in range(n)]
print(solution(n, m, board))
