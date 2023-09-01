# N개의 자연수가 주어졌을때 합이 K이상이 되는 경우의 수

def DFS():
    global res
    if sum(tmp) == K:
        print(tmp)
        res += 1
        return
    for i in A:
        if i not in tmp:
            tmp.append(i)
            DFS()
            tmp.pop()

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    tmp = []
    res = 0
    DFS()
    print(f'#{tc} {res}')
