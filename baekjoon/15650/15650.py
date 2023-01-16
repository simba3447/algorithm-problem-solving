import sys

def find(n, m, array):
    if len(array) == 0:
        start = 0
    else:
        start = array[-1]

    for i in range(n + 1):
        if i <= start:
            continue
        temp = array.copy()
        temp.append(i)
        if m == 1:
            for item in temp:
                print(item, end=" ")
            print()
        find(n, m - 1, temp)
    return

def solution(n, m):
    find(n, m, [])

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

solution(n, m)