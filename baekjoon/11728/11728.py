import sys

def solution(n, m, a, b):
    i, j = 0, 0

    while True:
        if i >= n:
            if j >= m:
                return
            print(b[j], end=" ")
            j += 1                
        elif j >= m:
            if i >= n:
                return
            print(a[i], end=" ")
            i += 1
        elif a[i] < b[j]:
            print(a[i], end=" ")
            i += 1
        else:
            print(b[j], end=" ")
            j += 1

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

a = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

solution(n, m, a, b)