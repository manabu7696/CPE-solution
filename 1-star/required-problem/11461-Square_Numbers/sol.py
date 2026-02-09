def bound_cal(x:int, is_low = False):
    for i in range(1, 1000):
        if i ** 2 <= x and (i + 1) ** 2 > x:
            if i ** 2 == x and is_low:
                return i - 1
            return i

def lower_bound(a:int):
    return bound_cal(a, True)

def upper_bound(b:int):
    return bound_cal(b)

def ans_counter(a:int, b:int):
    return upper_bound(b) - lower_bound(a)

def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(ans_counter(a, b))

main()