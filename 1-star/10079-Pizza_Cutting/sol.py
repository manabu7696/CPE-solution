while True:
    x = int(input())
    if x < 0:
        break
    print(1 + x * (1 + x) // 2)