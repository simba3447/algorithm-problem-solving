import sys
from collections import deque

def solution(m, n, h, array):
    vector = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    elapsed_days = 0

    unripped_tomato = 0
    ripped_tomato = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if array[z][y][x] == 0:
                    unripped_tomato += 1
                elif array[z][y][x] == 1:
                    ripped_tomato.append((z, y, x, 0))

    while ripped_tomato:
        z, y, x, days = ripped_tomato.popleft()
        
        for i, j, k in vector:
            if 0 <= z + i < h and 0 <= y + j < n and 0 <= x + k < m and array[z + i][y + j][x + k] == 0:
                array[z + i][y + j][x + k] = 1
                unripped_tomato -= 1
                elapsed_days = days + 1
                ripped_tomato.append((z + i, y + j, x + k, days + 1))

    if unripped_tomato == 0:
        return elapsed_days
    else:
        return -1
                    
m, n, h = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [[[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)] for _ in range(h)]

print(solution(m, n, h, array))
