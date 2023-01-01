import sys

n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(sys.stdin.readline().rstrip())

def solution(n, array):
    items = get_items_set(array)
    if len(items) == 1:
        return str(items.pop())
    n = int(n/2)
    lu_array = [i[:n] for i in array[:n]]
    ru_array = [i[n:] for i in array[:n]]
    ld_array = [i[:n] for i in array[n:]]
    rd_array = [i[n:] for i in array[n:]]

    return "({}{}{}{})".format(solution(n, lu_array),solution(n, ru_array),solution(n, ld_array),solution(n, rd_array))

def get_items_set(array):
    elements = set()
    for item in array:
        for i in item:
            elements.add(i)
    
    return elements

print(solution(n, array))