import sys

def find(n, m, array):
    for i in range(1, n + 1):
        if i in array:
            continue
        temp = array.copy()
        temp.append(i)
        if m == 1:
            for item in temp:
                print(item, end=" ")
            print()
            continue
        find(n, m-1, temp)


def solution(n, m):
    find(n, m, [])
        
n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

solution(n, m)
