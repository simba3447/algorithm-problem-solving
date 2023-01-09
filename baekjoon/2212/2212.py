import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
array = [int(i) for i in sys.stdin.readline().split()]

def solution(n, k, array):
    array.sort()

    d_array = [array[i+1] - array[i] for i in range(len(array) - 1)]
    d_array.sort()

    d_array = d_array[:len(array) - k]

    return sum(d_array)

print(solution(n, k, array))
