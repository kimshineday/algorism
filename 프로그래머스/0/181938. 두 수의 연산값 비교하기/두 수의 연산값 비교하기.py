def solution(a, b):
    x = 2 * a * b
    a = str(a)
    b = str(b)
    y = a + b
    if x > int(y):
        return x
    else:
        return int(y)