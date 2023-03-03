import sys
import heapq


def solution(n, c, items):
    INF = 10 ** 6
    result = 0

    items.sort(key=lambda i: i[0])
    q = []
    y_dict = {}

    y_bound = INF
    current_sum = 0
    for i in range(n):
        x, y, v = items[i]
        if y >= y_bound:
            continue
        heapq.heappush(q, (-y, v))
        if y not in y_dict:
            y_dict[y] = 0
        y_dict[y] += 1
        current_sum += v

        if i < n - 1 and x == items[i + 1][0]:
            continue

        while len(q) > c:
            y, _ = q[0]
            y *= -1

            for _ in range(y_dict[y]):
                _, v = heapq.heappop(q)
                current_sum -= v

            y_bound = y

        result = max(result, current_sum)

    return result


n, c = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
items = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()]
         for _ in range(n)]
print(solution(n, c, items))
