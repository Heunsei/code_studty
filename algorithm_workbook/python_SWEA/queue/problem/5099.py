# pizza
from collections import deque
T = int(input())
for tc in range(1, T+1):
    # 화덕크기, 피자개수
    N, M = map(int, input().split())
    
    # 치즈량을 저장하는 리스트
    pizza = list(map(int, input().split()))
    
    # 인덱스와 치즈를 전부 저장하는 deque
    idx_cont = deque()
    for i in range(1, M+1):
        idx_cont.append((i, pizza[i-1]))
    while True:
        idx, cheese = idx_cont.popleft()
        cheese //= 2
        if cheese == 0:
            idx_cont.append((idx, cheese))
        else:
            idx_cont.insert(N-1, (idx, cheese))

        if idx_cont[-1][1] == 0:
            idx_cont.pop()

        if len(idx_cont) == 1:
            print(f'#{tc} {idx_cont[0][0]}')
            break
