output_list = []
for i in range(int(input())):
    input_list = list(map(int, input().split(" ")))
    family_num = input_list.pop(0)
    input_list.sort()
    temp = 0
    upper_bound = (family_num // 2) if family_num % 2 == 0 else (family_num + 1) // 2
    for j in range(upper_bound):
        temp += input_list[-j - 1] - input_list[j]
    output_list.append(temp)

for k in output_list:
    print(k)
