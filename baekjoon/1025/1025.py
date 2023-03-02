import sys


def check_square(value):
    return value == int(value ** 0.5) ** 2


def solution(n, m, array):
    result = -1
    for i in range(n):
        for j in range(m):
            for i_diff in range(-8, 9):
                for j_diff in range(-8, 9):
                    if i_diff == j_diff == 0:
                        continue
                    num = 0
                    i_copy = i
                    j_copy = j
                    while 0 <= i_copy < n and 0 <= j_copy < m:
                        num = num * 10 + array[i_copy][j_copy]
                        if check_square(num):
                            result = max(result, num)
                        i_copy += i_diff
                        j_copy += j_diff

    return result


n, m = (int(i) for i in sys.stdin.readline().split())
array = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]

print(solution(n, m, array))
