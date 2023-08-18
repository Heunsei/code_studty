# 직사각형
# xy 좌하단 좌표 pq 우상단 좌표
# 겹치는 질때, 선분으로 만날때, 점으로 만날때 때, 분리될 때 케이스를 분리
# 두 직사각형의 공통 부분을 조사해서 출력

for _ in range(4):
    # 0 1 2 3 4 5 6 7
    po = list(map(int, input().split()))

    # 만나지 않을 때
    if po[2] < po[4] or po[0] > po[6] or po[1] > po[7] or po[3] < po[5]:
        print('d')
        continue
    # 점으로 만날 때
    if (po[2] == po[4] and po[3] == po[5]) or (po[0] == po[6] and po[1] == po[7]) or (po[0] == po[6] and po[3] == po[5])or (po[2] == po[4] and po[1] == po[7]):
        print('c')
        continue

    # 선으로 만날 때
    if po[2] == po[4] or po[0] == po[6] or po[3] == po[5] or po[1] == po[7]:
        print('b')
        continue
    print('a')
    continue
