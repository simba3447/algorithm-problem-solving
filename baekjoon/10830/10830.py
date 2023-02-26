import sys


def mult(n, a, b=None):
    if b is None:
        b = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (a[i][k] * b[k][j]) % 1000
            result[i][j] %= 1000
    return result


def square(n, b, array):
    if b == 1:
        return array

    a = solution(n, b // 2, array)
    result = mult(n, a, a)
    if b % 2 == 1:
        result = mult(n, result, array)

    return result

def solution(n, b, array):
    result = square(n, b, array)
    result = mult(n, result)

    return result


n, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
for row in solution(n, b, array):
    print(*row)
