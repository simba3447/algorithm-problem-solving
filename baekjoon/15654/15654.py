import sys

def find(n, m, array):
    for i in range(n):
        if i in array:
            continue
        temp = array.copy()
        temp.append(i)
        if m == 1:
            for item in temp:
                print(a[item], end=" ")
            print()
        find(n, m - 1, temp)
    return

def solution(n, m):
    find(n, m, [])

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
a = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
a.sort()

solution(n, m)