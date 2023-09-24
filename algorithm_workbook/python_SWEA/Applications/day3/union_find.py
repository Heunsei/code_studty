parent = [i for i in range(10)]

# find - set
def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])

# union
def union(x, y):
    # 1. 이미 같은 집합인지 check
    x = find_set(x)
    y = find_set(y)
    # 같은 집합
    if x == y:
        return
    # 2. 다른 집합이라면 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def union_set(x,y):                     # x의 대표자를 찾아서 y의 대표자로 바꾸어줌
    parent[find_set(y)] = find_set(x)
    return x

union(0, 1)
union(2, 3)
union(1, 3)

# 대표자 검색
print(find_set(0))
print(find_set(1))

# 같은 그룹인지 확인
t_x = 0
t_y = 1

if find_set(t_x) == find_set(t_y):
    print("같은 집합에 속함")
else:
    print('다른 집합')