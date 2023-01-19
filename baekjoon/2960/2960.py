import sys

def solution(n, k):
    array = [0 for _ in range(n-1)]
    cnt = 0
    i = 0
    while True:
        if i == len(array):
            break
        if array[i] == 0:
            j = i
            while True:
                if j >= len(array):
                    break
                if array[j] == 0:
                    array[j] = 1
                    cnt += 1
                if cnt == k:
                    return j + 2
                j += i + 2
        i += 1

n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, k))
