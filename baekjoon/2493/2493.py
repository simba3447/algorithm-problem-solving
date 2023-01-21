import sys

def solution(n, array):
    stack = []

    for i in range(len(array)):
        exist = False
        while len(stack) > 0:
            item = stack.pop()
            if item[1] > array[i]:
                print(item[0] + 1, end=" ")
                stack.append(item)
                stack.append((i, array[i]))
                exist = True
                break
            
        if not exist:
            print(0, end=" ")
            stack.append((i, array[i]))


n = int(sys.stdin.readline())
array = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
solution(n, array)