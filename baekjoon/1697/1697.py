import sys
from collections import deque


def solution(n, k):
    min_time = {n: 0}
    q = deque()
    q.append(n)

    while q:
        position = q.popleft()

        if position == k:
            return min_time[k]

        for next in (position + 1, position - 1, position * 2):
            if next in min_time or not 0 <= next <= 10 ** 5:
                continue
            min_time[next] = min_time[position] + 1
            q.append(next)


n, k = [int(i) for i in sys.stdin.readline().rstrip().split()]
print(solution(n, k))
