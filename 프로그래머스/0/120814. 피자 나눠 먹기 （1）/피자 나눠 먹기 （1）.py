def solution(n):
    x, y = divmod(n, 7)
    if y > 0:
        return x + 1
    else:
        return x