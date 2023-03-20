import sys


def find(i, selected, rest):
    if i == m:
        sequence_set.add(tuple(selected))
    else:
        for number in rest:
            selected_ = [i for i in selected]
            selected_.append(number)
            rest_ = [i for i in rest]
            rest_.pop(rest_.index(number))
            find(i + 1, selected_, rest_)


n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
numbers = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
sequence_set = set()
find(0, [], numbers)
sequence_list = list(sequence_set)
sequence_list.sort()
for sequence in sequence_list:
    print(*sequence)
