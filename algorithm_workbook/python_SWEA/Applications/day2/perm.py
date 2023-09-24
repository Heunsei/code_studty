# 순열
# nPr : n개의 요소중 r개를 사용하여 순열

def perm(depth):
    if depth == N:
        print(*com_perm)
        return
    else:
        # 내가 가진 배열의 모든 원소를 매번 사용할 것인지 체크
        for i in range(N):
            # arr의 i번째 요소를 쓴적이 있는지 없는지 판단
            if not visited[i]:
                visited[i] = True
                com_perm[depth] = arr[i]
                perm(depth+1)
                visited[i] = False
arr = [1,2,3]
N = len(arr)
# 내가 perm호출시 i번째 값을 썻는지 확인하는 판별하기 위함
visited = [False] * N
# 찐찐찐찐찐 최종본
com_perm = [0] * N
perm(0)
