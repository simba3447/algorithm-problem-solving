import sys
    
def find(y, x, n, array):
    if x == n - 1 and y == n - 1:
        return True
    if x >= n or y >= n:
        return False

    if cache[y][x] != None:
        return cache[y][x]

    d = array[x][y]
    result = find(y, x + d, n, array) or find(y + d, x, n, array)
    cache[y][x] = result
    return result

def solution(n, array):
    if find(0, 0, n, array):
        return "YES" 
    return "NO"

c = int(sys.stdin.readline())

for _ in range(c):
    n = int(sys.stdin.readline())

    cache = [[None for _ in range(n)] for _ in range(n)]
    array = [[int(i) for i in sys.stdin.readline().rstrip().split()] for _ in range(n)]
    print(solution(n, array))


