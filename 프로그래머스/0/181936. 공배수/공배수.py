def solution(number, n, m):
    if number % n == number % m:
        if number % n == 0:
            answer = 1
        else :
            answer = 0
    else:
        answer = 0
    return answer