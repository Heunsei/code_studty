# 8/21 강의 연습


def preorder(n):
    if n:  # 존재하는 정점이면
        print(n)  # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


V = int(input())  # 정점의 수
E = V - 1  # tree의 간선의 수는 정점의 수보다 1만큼 작다
arr = list(map(int, input().split()))

# 부모를 인덱스로 자식을 저장
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
# 자식을 인덱스로 부모 저장
par = [0] * (V+1)
for i in range(E):
    # 왼쪽 / 오른쪽 자식의 인덱스는 i * 2 / i * 2 +1
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:  # 자식1이 비어있다면
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p  # 자식을 인덱스로 부모 저장

# 루트를 찾는 작업
# 전체를 탐색하라고 하면 루트를 찾는 작업이 필요하다
root = 1
while par[root] != 0:
    root += 1

print(ch1)
print(ch2)
print(par)
preorder(root)