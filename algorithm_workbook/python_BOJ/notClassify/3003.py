# 킹 퀸 룩 비숍 나이트 폰
to_check = list(map(int,input().split()))
origin = [1, 1, 2, 2, 2, 8]
#print(to_check)
result = []
for i in range(len(to_check)):
    result.append(origin[i] - to_check[i])
to_print = ' '.join(map(str, result))
print(to_print)