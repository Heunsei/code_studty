# 값을 역으로 돌리고 비교

def compare(num1, num2):
    if int(num1) > int(num2):
        return num1
    else :
        return num2

compare_num1, compare_num2 = list(map(list,input().split(' ')))

compare_num1.reverse()
compare_num2.reverse()

compare_num1 = ''.join(compare_num1)
compare_num2 = ''.join(compare_num2)

# print(compare_num1,compare_num2)

print(compare(compare_num1,compare_num2))

