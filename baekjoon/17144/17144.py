import sys


def solution(r, c, t, array):
    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    machine_r = []
    for i in range(r):
        if array[i][0] == -1:
            machine_r.append(i)
            
    for _ in range(t):
        new_array = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if array[i][j] == -1:
                    new_array[i][j] = array[i][j]
                    continue
                temp = array[i][j]
                for id, jd in vectors:
                    if 0 <= i + id < r and 0 <= j + jd < c and array[i + id][j + jd] != -1:
                        new_array[i + id][j + jd] += array[i][j] // 5
                        temp -= array[i][j] // 5
                new_array[i][j] += temp

        temp_array = [[i for i in row] for row in new_array]

        i = machine_r[0]
        temp_array[i][1] = 0
        for j in range(1, c - 1):
            temp_array[i][j + 1] = new_array[i][j]
        for k in range(1, i + 1):
            temp_array[k - 1][c - 1] = new_array[k][c - 1]
        for j in range(1, c):
            temp_array[0][j - 1] = new_array[0][j]
        for k in range(0, i-1):
            temp_array[k + 1][0] = new_array[k][0]
        
        i = machine_r[1]
        temp_array[i][1] = 0
        for j in range(1, c - 1):
            temp_array[i][j + 1] = new_array[i][j]
        for k in range(i, r - 1):
            temp_array[k + 1][c - 1] = new_array[k][c - 1]
        for j in range(1, c):
            temp_array[r - 1][j - 1] = new_array[r - 1][j]
        for k in range(i + 2, r):
            temp_array[k - 1][0] = new_array[k][0]

        array = temp_array

    result = 0
    for row in array:
        for i in row:
            result += i
    result += 2

    return result

r, c, t = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(r)]
print(solution(r, c, t, array))