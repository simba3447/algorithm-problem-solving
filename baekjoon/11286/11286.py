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
        if len(heap) - 1 >= 2 * i + 2:
            index = find_min(heap[i], heap[2 * i + 1], heap[2 * i + 2])
            if index == 1:
                heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                i = 2 * i + 1
            elif index == 2:
                heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
                i = 2 * i + 2
            else:
                break

        elif len(heap) - 1 == 2 * i + 1:
            index = find_min(heap[i], heap[2 * i + 1])
            if index == 1:
                heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                i = 2 * i + 1
            else:
                break
        else:
            break

def insert(x):
    heap.append(x)
    i = len(heap) - 1
    while i != 0:
        j = (i - 1) // 2
        if (abs(heap[j]) < abs(heap[i])) or (abs(heap[j]) == abs(heap[i]) and heap[j] < heap[i]):
            break
        heap[j], heap[i] = heap[i], heap[j]
        i = j

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0: find()
    else: insert(x)
