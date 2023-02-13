import sys


def solution(n, numbers):
    trie = [{}, False]
    for number in numbers:
        cursor = trie
        for digit in number:
            if not cursor[0].get(digit):
                cursor[0][digit] = [{}, False]
            cursor = cursor[0][digit]
            if cursor[1]:
                return 'NO'
        cursor[1] = True

        if len(cursor[0]) > 0:
            return 'NO'
    return 'YES'
                

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    numbers = [sys.stdin.readline().rstrip() for _ in range(n)]
    print(solution(n, numbers))