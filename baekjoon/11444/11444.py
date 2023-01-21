import sys

def mat_mult(a, b):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += a[i][k] * b[k][j]
            answer[i][j] %= 1000000007
    return answer
            

def solution(n):
    matrix = [[1, 1], [1, 0]]
    if n == 1:
        return matrix

    temp = solution(n//2)
    if n % 2 == 0:
        return mat_mult(temp, temp) 
    else:
        return mat_mult(mat_mult(temp, temp), matrix)

n = int(sys.stdin.readline())
print(solution(n)[0][1])
