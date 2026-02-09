for i in range(int(input())):
    a = int(input())
    b = int(input())
    if a % 2 == 0:
        a += 1
    if b % 2 == 0:
        b -= 1
    print(f'Case {i + 1}: {(a + b) * ((b - a) // 2 + 1) // 2}')