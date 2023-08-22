import sys
sys.stdin = open('input.txt')

def inorder(num, N):
    global count
    if num <= N:
        inorder(num*2,N)
        count += 1
        tree[num] = count
        inorder(num*2+1,N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 6 / 8 / 15
    tree = [0] * (N+1)
    count = 0
    inorder(1, N)
    #print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')