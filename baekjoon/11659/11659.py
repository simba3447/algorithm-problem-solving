import sys

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
numbers = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
partial_sum = [0]
for i in range(n):
    partial_sum.append(numbers[i] + partial_sum[-1])

for _ in range(m):
    i, j = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    print(partial_sum[j] - partial_sum[i-1])