import sys

n, m, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
rtree = [0 for _ in range(n * 4)]

a = [int(sys.stdin.readline()) for _ in range(n)]

def init(start, end, index):
    if start == end:
        rtree[index] = a[start]
    else:
        rtree[index] = init(start, (start + end) // 2, index * 2 + 1) + init((start + end) // 2 + 1, end, index * 2 + 2)
    return rtree[index]

def _find(start, end, index, rstart, rend):
    if start > rend or end < rstart:
        return 0
    if start <= rstart and end >= rend:
        return rtree[index]
    
    rmid = (rstart + rend) // 2
    return _find(start, end, index * 2 + 1, rstart, rmid) + _find(start, end, index * 2 + 2, rmid + 1, rend)

def find(start, end):
    return _find(start, end, 0, 0, n - 1)

def _update(index, diff, rindex, rstart, rend):
    if index < rstart or index > rend:
        return
    
    rtree[rindex] += diff
    
    if rstart == rend:
        return

    rmid = (rstart + rend) // 2
    if rstart <= index <= rmid:
        _update(index, diff, rindex * 2 + 1, rstart, rmid)
    elif rmid + 1 <= index <= rend:
        _update(index, diff, rindex * 2 + 2, rmid + 1, rend)

def update(index, value):
    diff = value - a[index]
    a[index] = value
    _update(index, diff, 0, 0, n - 1)

init(0, n - 1, 0)
for _ in range(m + k):
    op, b, c = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    if op == 1:
        update(b - 1, c)
    else:
        print(find(b - 1, c - 1))
