import heapq
import sys


n = int(sys.stdin.readline())
q = []
for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        heapq.heappush(q, -i)
    elif len(q) == 0:
        print(0)
    else:
        print(-heapq.heappop(q))
