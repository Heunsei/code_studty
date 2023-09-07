from pprint import pprint
# T = 겹칠 종이의 숫자
T = int(input())
arr = [[0] * 10 for _ in range(10)]
# 0 0 10 10
# 2 2 1 1
# tc는 색종이의 순서
# 값이 있던없던 덮어씌울것
for tc in range(1, 1 + T):
    # 좌표 받아오기
    # x,y 니까 j i 순서로
    # wid 는 x 좌표니 j랑 엮어서
    # hig 는 y 좌표니 i랑 엮어서 쓰기
    j, i, wid, hig = map(int, input().split())
    # y 축을 돌면서 x좌표를 관리
    for n in range(i, i+hig):
        # wid 를 빼면 범위안에 한개만 넣어서 길이만큼 복사해서 넣어줘야함
        arr[n][j:j+wid] = [tc] * wid
pprint(arr)

for p in range(1, 1 + T):
    result = 0
    for cnt in range(10):
        result += arr[cnt].count(p)
    print(result)
