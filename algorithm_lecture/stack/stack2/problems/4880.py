T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    peo = list(map(int, input().split()))
    start = 0
    end = N
    mid = (start + end) // 2

    peo_left = peo[start:mid]
    peo_right = peo[mid:end]

    def rsp(p1, p2):


    for i in range(len(peo_left)-1):
