def num():
    a, b = input().split(' ')
    a, b = int(a), int(b)
    if -100000 <= a <= 100000:
        if -100000 <= b <= 100000:
            print(f'a = {a}')
            print(f'b = {b}')
    else:
        print('다시 입력하세요.')

num()