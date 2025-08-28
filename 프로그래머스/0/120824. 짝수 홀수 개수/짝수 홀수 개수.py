def solution(num_list):
    count_x, count_y = 0, 0
    for i in num_list:
        if i % 2 == 0 :
            count_x += 1
        else:
            count_y += 1
    return [count_x, count_y]