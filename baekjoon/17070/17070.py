import sys

def solution(n, array):
    VERTICAL = 0
    DIAGONAL = 1
    HORIZONTAL = 2
    stack = [(0, 1, VERTICAL)]
    result = 0

    while stack:
        i, j, t = stack.pop()
        if i >= n or j >= n:
            continue
        if array[i][j] == 1:
            continue
        if t == DIAGONAL and (array[i - 1][j] == 1 or array[i][j - 1] == 1):
            continue
        if i == n -1 and j == n - 1:
            result += 1
            continue

        stack.append((i + 1, j + 1, DIAGONAL))
        if t == VERTICAL or t == DIAGONAL:
            stack.append((i, j + 1, VERTICAL))
        if t == HORIZONTAL or t == DIAGONAL:
            stack.append((i + 1, j, HORIZONTAL))
    return result

n = int(sys.stdin.readline())
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
print(solution(n, array))