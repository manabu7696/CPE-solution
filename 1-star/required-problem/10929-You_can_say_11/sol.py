while True:
    x = int(input())
    if x == 0:
        break
    if x % 11 == 0:
        print(f'{x} is a multiple of 11.')
    else:
        print(f'{x} is not a multiple of 11.')