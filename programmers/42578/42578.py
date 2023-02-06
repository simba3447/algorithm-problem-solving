def solution(clothes):
    dictionary = {}
    for _, category in clothes:
        if dictionary.get(category):
            dictionary[category] += 1
        else:
            dictionary[category] = 1

    cases = 1
    for item in dictionary.values():
        cases *= item + 1
    cases -= 1

    return cases