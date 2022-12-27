# First Attempt (Succeed)
# Implement permutation explicitly, list

n = int(input())
k = int(input())
card_list = []
for i in range(n):
    card_list.append(input())

def count_integer(card_list, k):
    integer_list = []
    def count_integer_rec(card_list, k, integer):
        if k == 0:
            if integer not in integer_list:
                integer_list.append(integer)

        for i in range(len(card_list)):
            card = card_list[i]
            rest_card_list = card_list[:i] + card_list[i+1:]
            count_integer_rec(rest_card_list, k-1, integer + card)

    count_integer_rec(card_list, k, '')

    print(len(integer_list))

count_integer(card_list, k)