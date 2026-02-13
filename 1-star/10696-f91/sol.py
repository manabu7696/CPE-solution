def f91(n):
    if n <= 100:
        return f91(f91(n + 11))
    else:
        return n - 10

while True:
    x = int(input())
    if x == 0:
        break
    print(f'f91({x}) = {f91(x)}')