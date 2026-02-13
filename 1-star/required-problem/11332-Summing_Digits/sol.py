def digit_sum(x):
    sum = 0
    while x >= 10:
        sum += x % 10
        x = x // 10
    sum += x
    return sum

while True:
    x = int(input())
    if x == 0:
        break
    while x >= 10:
        x = digit_sum(x)
    print(x)