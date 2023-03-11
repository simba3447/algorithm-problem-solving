import sys


def solution(n, array):
    array.sort()
    result = 0
    for i in range(n):
        result += array[n - i - 1] * (i + 1)
    return result


n = int(sys.stdin.readline())
array = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, array))
