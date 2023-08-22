T = int(input())

def inorder(node):
    global count
    if node <= N:
        inorder(node*2)
        count += 1
        tree[node] = count
        inorder(node*2+1)

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    count = 0
    inorder(1)
    print(tree)