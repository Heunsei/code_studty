# 비트연산
arr = [1, 2, 3, 4, 5]

n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=', ')
    print(f'case : {i}')
print()
# 경우의 수는 2^n
# n번만큼 왼쪽으로 shift
# 1000 2의 0 1 2 (3승)
# 0001 은 2^0 > 1,
# for i in range(1<<n):
#     for j in range(n):

#         if i &  (1<<j):
#             print(arr[j],end=', ')
#     print()
# print()

# for x in range(1<<N):
#     result = 0
#     # x번의 경우ㅡ의 수가 1일때
#     # n번만큼 0을 shift해주고 0*n+1부터 시작
#     # 00001
#     # 00010   (1<<1)
#     for y in range(N):
#         if x & (1<<y):
#             result += numbers[y]
#     if result == 0:
#         print(1)
#         break