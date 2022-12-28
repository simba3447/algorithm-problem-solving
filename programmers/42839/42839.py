def solution(numbers):
    s = set()
    
    def check_prime(number):
        if number == 0 or number == 1: return False

        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    
    def find(n, rest_numbers):
        if len(n) != 0 and check_prime(int(n)):
            s.add(int(n))
        if len(numbers) == 0: return
        for i in range(len(rest_numbers)):
            find(n + rest_numbers[i], rest_numbers[:i] + rest_numbers[i+1:])
    
    find('', numbers)
    answer = len(s)
    return answer
