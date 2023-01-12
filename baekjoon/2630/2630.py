import sys

n = int(sys.stdin.readline())
array = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]

def check(array):
    elements = set()
    for item in array:
        for i in item:
            elements.add(i)
    
    if len(elements) == 1:
        return elements.pop()
    return 2


def solution(n, array):
    if n == 1:
        color[array[0][0]] += 1
        return
    
    ele = check(array)
    if ele != 2: 
        color[ele] += 1
        return
    n = n // 2
    solution(n, [i[:n] for i in array[:n]])
    solution(n, [i[n:] for i in array[:n]])
    solution(n, [i[:n] for i in array[n:]])
    solution(n, [i[n:] for i in array[n:]])

color = [0, 0]

solution(n, array)
print(color[0])
print(color[1])