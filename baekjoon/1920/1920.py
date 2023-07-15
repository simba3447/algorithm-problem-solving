import sys

n = int(input())
array = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
m = int(input())
numbers = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array.sort()

for number in numbers:
    i = 0
    j = len(array) - 1

    exists = False
    while i <= j:
        mid = (i + j) // 2
        if array[mid] == number:
            exists = True
            break
        else:
            if i == j:
                break
            if array[mid] > number:
                j = mid
            else:
                i = mid + 1
    if exists:
        print(1)
    else:
        print(0)
