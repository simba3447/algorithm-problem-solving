import sys

def eval(index, rstart, rend):
    if lazy[index]:
        if rstart != rend:
            lazy[index * 2] = not lazy[index * 2]
            lazy[index * 2 + 1] = not lazy[index * 2 + 1]
        rlen = rend - rstart + 1
        rtree[index] = rlen - rtree[index]
        lazy[index] = False

def _flip(start, end, index, rstart, rend):
    if start > rend or end < rstart:
        return 0
    else:
        eval(index, rstart, rend)

        if start <= rstart and end >= rend:
            lazy[index] = True
            rlen = rend - rstart + 1
            result = rlen - rtree[index]
            return result - rtree[index]

        if not (start <= rstart and end >= rend):
            rmid = (rstart + rend) // 2
            prev = rtree[index]
            rtree[index] += _flip(start, end, index * 2, rstart, rmid)
            rtree[index] += _flip(start, end, index * 2 + 1, rmid + 1, rend)
            return rtree[index] - prev

def flip(start, end):
    _flip(start, end, 1, 0, n - 1)

def _count(start, end, index, rstart, rend):
    if start > rend or end < rstart:
        return 0
    else:
        eval(index, rstart, rend)

        if start <= rstart and end >= rend:
            return rtree[index]

        else:
            rmid = (rstart + rend) // 2
            return _count(start, end, index * 2, rstart, rmid) + _count(start, end, index * 2 + 1, rmid + 1, rend)
    
def count(start, end):
    return _count(start, end, 1, 0, n - 1)

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
rtree = [0 for _ in range(4 * n)]
lazy = [False for _ in range(4 * n)]

for _ in range(m):
    o, s, t = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    s -= 1
    t -= 1
    if o == 0:
        flip(s, t)
    else:
        print(count(s, t))
