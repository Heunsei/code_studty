# 한사람이 M번 공을 받으면 게임이 종료
# M번보다 적게 받은 사람이 공을 던질때 횟수가 홀수면 시계 방향으로 l번째
# 짝수면 반시계방향으로 L번째

# N명이 원형으로 앉아있음
N, M, L = map(int, input().split())

arr = [0] * N
idx = 0
# 0 번째는 무조건 1이상
arr[idx] = 1
cnt = 0
while True:
    if arr[idx] == M:
        print(cnt)
        break
    # 짝수 일때
    if arr[idx] % 2 == 0:
        idx = abs((idx - L) %N)
        arr[idx] += 1
        cnt +=1
    # 홀수 일때
    else:
        idx = (idx-L) % N
        arr[idx] += 1
        cnt += 1