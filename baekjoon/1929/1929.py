import sys

def solution(m, n):
    array = [0 for _ in range(n - 1)]

    i = 0
    while i < n - 1:
        if array[i] == 0:

            num = i + 2
            if num >= m:
                print(num)
            j = i
            while j < n - 1:
                array[j] = 1
                j += num
        i += 1
            
    return 0

m, n = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

solution(m, n)