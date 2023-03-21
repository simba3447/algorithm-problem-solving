import sys


def find(value):
    global set_list
    if set_list[value] == value:
        return value

    set_list[value] = find(set_list[value])
    return set_list[value]


def union(a, b):
    global set_list
    global height_list

    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return

    if height_list[root_a] > height_list[root_b]:
        set_list[root_b] = root_a
    else:
        set_list[root_a] = root_b
        if height_list[root_a] == height_list[root_b]:
            height_list[root_b] += 1


def solution(n, m, truth_person_list, party_list):
    for party in party_list:
        person_1 = party[0]
        for person in party[1:]:
            union(person_1 - 1, person - 1)

    if truth_person_list:
        truth_person_1 = truth_person_list[0]
        for truth_person in truth_person_list[1:]:
            union(truth_person_1 - 1, truth_person - 1)

    result = 0
    for party in party_list:
        valid = True
        for person in party:
            if truth_person_list and find(truth_person_list[0] - 1) == find(person - 1):
                valid = False

        if valid:
            result += 1

    return result


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
truth_person_list = [int(i)
                     for i in sys.stdin.readline().rstrip().rsplit()][1:]
party_list = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()][1:]
              for _ in range(m)]

set_list = [i for i in range(n)]
height_list = [0 for _ in range(n)]
print(solution(n, m, truth_person_list, party_list))
