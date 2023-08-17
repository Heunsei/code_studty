# 프렛의 수
import sys
input = sys.stdin.readline

N, P = map(int, input().split())
arr = [[] * P for _ in range(N)]

count = 0
# 줄의 번호, 프렛의 번호
# count를 저장하다 반환
def ans(n,p):
    global count
    if len(arr[n]) == 0:
        arr[n].append(p)
        count += 1
    else:
        if arr[n][-1] < p:
            arr[n].append(p)
            count += 1

        if arr[n][-1] > p:
            while arr[n][-1] > p:
                arr[n].pop()
                count += 1
                if len(arr[n]) == 0:
                    break
                if arr[n][-1] == p:
                    arr[n].pop()
                    count -= 1
                    break
            arr[n].append(p)
            count += 1

for _ in range(N):
    # 줄의 번호, 눌러야하는 프렛의 번호
    n, p = map(int, input().split())
    ans(n, p)
print(count)
    #print(arr)
    