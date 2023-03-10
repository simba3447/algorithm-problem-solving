import sys


def solution(n, x):
    x_unique = list(set(x))
    x_unique.sort()
    x_dict = {x_unique[i]: i for i in range(len(x_unique))}

    for i in x:
        print(x_dict[i], end=' ')


n = int(sys.stdin.readline())
x = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
solution(n, x)
