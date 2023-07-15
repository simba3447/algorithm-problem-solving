import sys

def solution(n, mbti_list):
    mbti_dict = {}
    for mbti in mbti_list:
        if mbti not in mbti_dict:
            mbti_dict[mbti] = 0
        if mbti_dict[mbti] < 3:
            mbti_dict[mbti] += 1
        else:
            return 0
    
    mbti_list = []
    for mbti, cnt in mbti_dict.items():
        for _ in range(cnt):
            mbti_list.append(mbti)

    n = len(mbti_list)
    distances = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(4):
                if mbti_list[i][k] != mbti_list[j][k]:
                    distances[i][j] += 1

    min_distance = 100

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                min_distance = min(min_distance, distances[i][j] + distances[j][k] + distances[i][k])


    return min_distance

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    mbti_list = sys.stdin.readline().rstrip().rsplit()
    print(solution(n, mbti_list))
