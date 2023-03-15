import sys


def pick(curr, start):
    if len(curr) == m:
        print(*curr)
        return

    for i in range(start, n):
        next = [i for i in curr]
        next.append(numbers[i])
        pick(next, i)


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
numbers = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
numbers.sort()
pick([], 0)
