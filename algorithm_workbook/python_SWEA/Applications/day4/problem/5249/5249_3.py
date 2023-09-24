# 크루스칼
def find_set(x):
    if root[x] == x:
        return x
    else:
        return find_set(root[x])

def mst():
    # 모든 간선에 대해 조사가 되었는지 판별
    cnt = 0
    result = 0  # 전체 가중치의 합
    idx = 0     # 조사 대상
    while cnt < V:
        x = find_set(arr[idx][0])
        y = find_set(arr[idx][1])
        # 사이클이 형성되지 않을때
        if x != y:
            result += arr[idx][2]
            cnt += 1
            root[y] = x
        idx += 1
    return result

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    # 사이클을 모두 제거 한뒤
    # 가중치 기준으로 오름차순 정렬되어 있는 정보를 토대로 이어주기
    arr.sort(key=lambda x:x[2])
    print(arr)
    # 본인을 루트로 가지는 루트 형태
    root = list(range(V+1))
