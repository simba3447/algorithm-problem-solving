import sys


def solution(n, m, array):
    result = 0
    for i in range(n - 1):
        for j in range(m - 1):
            result = max(result, array[i][j] + array[i]
                         [j+1] + array[i+1][j] + array[i+1][j+1])

    for i in range(n - 3):
        for j in range(m):
            result = max(result, array[i][j] + array[i+1]
                         [j] + array[i+2][j] + array[i+3][j])

    for i in range(n):
        for j in range(m - 3):
            result = max(result, array[i][j] + array[i]
                         [j+1] + array[i][j+2] + array[i][j+3])

    for i in range(n - 2):
        for j in range(m - 1):
            all_sum = 0
            for di in range(3):
                for dj in range(2):
                    all_sum += array[i + di][j + dj]
            result = max(result, all_sum - array[i][j+1] - array[i+1][j+1])
            result = max(result, all_sum - array[i+1][j] - array[i+2][j])
            result = max(result, all_sum - array[i][j] - array[i+1][j])
            result = max(result, all_sum - array[i+1][j+1] - array[i+2][j+1])
            result = max(result, all_sum - array[i][j+1] - array[i+2][j])
            result = max(result, all_sum - array[i][j] - array[i+2][j+1])
            result = max(result, all_sum - array[i][j] - array[i+2][j])
            result = max(result, all_sum - array[i][j+1] - array[i+2][j+1])

    for i in range(n - 1):
        for j in range(m - 2):
            all_sum = 0
            for di in range(2):
                for dj in range(3):
                    all_sum += array[i + di][j + dj]
            result = max(result, all_sum - array[i][j] - array[i][j+1])
            result = max(result, all_sum - array[i+1][j+1] - array[i+1][j+2])
            result = max(result, all_sum - array[i+1][j] - array[i+1][j+1])
            result = max(result, all_sum - array[i][j+1] - array[i][j+2])
            result = max(result, all_sum - array[i][j] - array[i+1][j+2])
            result = max(result, all_sum - array[i+1][j] - array[i][j+2])
            result = max(result, all_sum - array[i][j] - array[i][j+2])
            result = max(result, all_sum - array[i+1][j] - array[i+1][j+2])

    return result


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()]
         for _ in range(n)]
print(solution(n, m, array))
