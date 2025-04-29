def solution(array):
    array_num = list(array)
    array_num.sort()
    answer = array_num[len(array_num) // 2]
    return answer