import sys

def solution(n, q, array):
    occupied = [False for _ in range(n + 1)]
    for item in array:
        current = item
        valid = True
        min_occupied = item
        while current != 1:
            if occupied[current]:
                valid = False
                min_occupied = current
            current = current // 2
        
        if not valid:
            print(min_occupied)
        else:
            occupied[item] = True
            print(0)


n, q = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [int(sys.stdin.readline()) for _ in range(q)]

solution(n, q, array)