def solution(number, k):
    temp = number
    s = 0
    for _ in range(k):
        for i in range(s, len(number) - 1):
            if int(number[i]) < int(number[i + 1]):
                temp = number[:i] + number[i+1:]
                if i > 0:
                    s = i - 1
                break
        if number != temp:
            number = temp
        else:
            number = number[:-1]
    answer = number
    return answer

# print(solution("1924", 2), "94")
# print(solution("1231234", 3), "3234")
# print(solution("4177252841", 4), "775841")