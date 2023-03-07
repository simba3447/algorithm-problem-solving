import sys
import heapq


def solution(k, operations):
    deleted = [False for _ in range(k)]
    asc_heap = []
    desc_heap = []
    for i in range(k):
        op, n = operations[i]
        if op == 'I':
            heapq.heappush(asc_heap, (n, i))
            heapq.heappush(desc_heap, (-n, i))
        elif op == 'D' and n == -1:
            while asc_heap and deleted[asc_heap[0][1]]:
                heapq.heappop(asc_heap)
            if asc_heap:
                _, i = heapq.heappop(asc_heap)
                deleted[i] = True
        elif op == 'D' and n == 1:
            while desc_heap and deleted[desc_heap[0][1]]:
                heapq.heappop(desc_heap)
            if desc_heap:
                _, i = heapq.heappop(desc_heap)
                deleted[i] = True
    
    while asc_heap and deleted[asc_heap[0][1]]:
        heapq.heappop(asc_heap)
    while desc_heap and deleted[desc_heap[0][1]]:
        heapq.heappop(desc_heap)
    if len(asc_heap) == 0:
        print("EMPTY")
    else:
        print(-desc_heap[0][0], asc_heap[0][0])
            
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    operations = []
    for _ in range(k):
        op, n = sys.stdin.readline().rstrip().rsplit()
        n = int(n)
        operations.append((op, n))
    solution(k, operations)
