# 현재 조사 위치
# r : 최대 조사 대상 수
def perm(now, r):
    if now == r:
        print(check)
        return
    else:
        # 완전 검색을 통해서 조사
        for i in range(len(num)):
            if not visited[i]:
                continue
            visited[i] = True
            check[now] = num[i]
            perm(now + 1, r)
            visited[i] = False


num = [1, 2, 3]
# 한번 사용하고나면 사용 할 수 없음을 기록하기위한 visited
# 원본과 같거나 한칸 크게 만듬
visited = [0] * len(num)
check = [0] * len(num)

