import sys
from collections import deque


def solution(n, array):
    tree = {}
    for i in range(n):
        tree[i + 1] = []
    for item in array:
        tree[item[0]].append(item[1])
        tree[item[1]].append(item[0])

    parents = [0 for _ in range(n)]
    q = deque([1])
    while q:
        item = q.popleft()
        for i in tree[item]:
            if parents[i-1] == 0:
                parents[i-1] = item
                q.append(i)
    
    for i in range(1, n):
        print(parents[i])
        

n = int(sys.stdin.readline())
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n - 1)]

solution(n, array)