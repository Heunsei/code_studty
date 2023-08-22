import sys
sys.stdin = open('input.txt')

# 6
def order(now):
    if now:
        order(left[now])
        order(right[now])
        if tree[now] == '+':
            tree[now] = int(tree[left[now]]) + int(tree[right[now]])
        elif tree[now] == '-':
            tree[now] = int(tree[left[now]]) - int(tree[right[now]])
        elif tree[now] == '*':
            tree[now] = int(tree[left[now]]) * int(tree[right[now]])
        elif tree[now] == '/':
            tree[now] = int(tree[left[now]]) // int(tree[right[now]])


for tc in range(1, 11):
    N = int(input())
    node = []
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        node.append(input().split())

    for c in node:
        if len(c) == 4:
            tree[int(c[0])] = c[1]
            left[int(c[0])] = int(c[2])
            right[int(c[0])] = int(c[3])
        else:
            tree[int(c[0])] = c[1]

    #print(tree)
    #print(f'{tc} left', left)
    #print(f'{tc} right',right)

    order(1)
    print(f'#{tc} {tree[1]}')

