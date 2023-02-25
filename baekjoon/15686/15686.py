import sys
from itertools import combinations


def solution(n, m, city):
    house_list = []
    chicken_list = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house_list.append((i, j))
            elif city[i][j] == 2:
                chicken_list.append((i, j))
    
    result = 10 ** 8
    for combination in combinations(chicken_list, m):
        sum_distance = 0
        for y2, x2 in house_list:
            distance = 10 ** 8
            for y1, x1 in combination:
                distance = min(distance, abs(y1 - y2) + abs(x1 - x2))
            sum_distance += distance
        result = min(result, sum_distance)
    return result

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
city = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
print(solution(n, m, city))
