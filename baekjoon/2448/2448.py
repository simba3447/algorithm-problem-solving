import sys


def solution(i):
    if i == 1:
        print('*', end='')
    elif i == 2:
        print('* *', end='')
    elif i == 3:
        print('*****', end='')
    else:
        n = 3
        while n * 2 < i:
            n *= 2
        length = solution(i - n)
        rest = n * 2 - length
        print(' ' * rest, end='')
        solution(i - n)

    return i * 2 - 1


n = int(sys.stdin.readline())
for i in range(n):
    print(' ' * (n - i - 1), end='')
    solution(i + 1)
    if i != n - 1:
        print(' ' * (n - i), end='')
    print()
