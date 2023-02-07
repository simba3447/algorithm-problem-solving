import sys

n = int(sys.stdin.readline())
heap = []

def find_min(*args):
    return args.index(sorted(args, key = lambda x: (abs(x), x))[0])
    
def find():
    global heap
    if len(heap) == 0:
        print(0)
        return

    print(heap[0])
    least = heap.pop()
    if len(heap) != 0:
        heap[0] = least

    i = 0
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        if len(heap) - 1 >= r:
            index = find_min(heap[i], heap[l], heap[r])
            if index == 1:
                heap[i], heap[l] = heap[l], heap[i]
                i = l
            elif index == 2:
                heap[i], heap[r] = heap[r], heap[i]
                i = r
            else:
                break

        elif len(heap) - 1 == l:
            index = find_min(heap[i], heap[l])
            if index == 1:
                heap[i], heap[l] = heap[l], heap[i]
                i = l
            else:
                break
        else:
            break

def insert(x):
    heap.append(x)
    i = len(heap) - 1
    while i != 0:
        j = (i - 1) // 2
        if find_min(heap[i], heap[j]) == 1:
            break
        heap[j], heap[i] = heap[i], heap[j]
        i = j

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0: find()
    else: insert(x)
