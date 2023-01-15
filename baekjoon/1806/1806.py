import sys

def solution(n, s, array):
    i = 0
    j = 1

    min_len = 1e9
    
    if array[0] >= s:
        return 1
    
    current_sum = array[0]
    current_len = 1

    while True:
        if j >= n:
            break
        
        current_sum += array[j]
        current_len += 1

        if current_sum >= s:
            while current_sum - array[i] >= s:
                current_sum -= array[i]
                current_len -= 1
                i += 1
                
            if min_len > current_len:
                min_len = current_len
        j += 1
    if min_len == 1e9:
        return 0
    else:
        return min_len
        
        
n, s = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
array = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

print(solution(n, s, array))