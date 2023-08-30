import sys
sys.stdin = open('input.txt')

# row : 현재 조사 대상
# chosen : 선택 대상
def perm(row, chosen):
    if row == N:
        for i in chosen:
            print(data[i],end=' ')
        print()
        return

    for i in range(N):
        # i 번째에 쓰겠다고 이전에 판정된 적이 있다면
        # 현재 조사 대상을 쓸 수 없으므로
        if i in chosen:
            continue
        chosen[row] = i
        perm(row + 1, chosen)
        chosen[row] = -1
        

for tc in range(1,5):
    N = 6
    data = input()
    # i번째에 들어 갈 수 있는 수 0, N-1까지를 제외
    chosen = [-1] * N
    perm(0,chosen)