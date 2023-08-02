N = 2 # 행
M = 4 # 열
arr = [[0,1,2,3],[4,5,6,7]]

# 행 우선
for i in range(N):
    for j in range(M):
        print(arr[i][j],end=' ')
    print()

print()
# 열 우선
for j in range(M):
    for i in range(N):
        print(arr[i][j],end=' ')
    print()


# 지그재그
for i in range(N):
    for j in range(M):
        # J는 0부터 3까지
        # 홀수일때 식 : M - j - 1 ,
        # j:0->idx=3, j:1->idx=2, j:2->idx=1 
        print(arr[i][j + (M-1-2*j)*(i%2) ],end=' ')
    print()

#빈배열 만들기
#열 길이가 M짜리를 N번만큼 반복해서 만들어라
arr = [[0]*M for _ in range(N)]
arr2 = [[0]*M]*N # 쓰면 안됌 리스트를 하나만 만들고 여러곳에서
                 # 같은 리스트를 참조하는꼴


# 위에서 0으로 다 초기화해서 값 안나옴
# 확인할거면 arr주석처리
max_v = 0 #최대값
for i in range(N):
    row_total = 0  # 각 행의 합
    for j in range(M):
        row_total += arr[i][j]
    print(row_total)
    if max_v < row_total:
        max_v = row_total
print(max_v)