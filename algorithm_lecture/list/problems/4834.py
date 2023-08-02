# 카드
T = int(input())
for tc in range(1, T+1):
    num_of_cards = int(input()) # 카드의 수
    card = int(input()) # 카드들
    # card = list(map(lit,input()))

    card_list = []

    for _ in range(num_of_cards):
        c = card % 10
        card //= 10
        card_list.append(c)

    # 카드의 갯수만큼 0을 채운 리스트 생성
    tmp = [0] * 10
    #print(card_list)

    for num in range(num_of_cards):
        tmp[card_list[num]] += 1

    # tmp는 0~9까지 카드들이 몇장있는지 적혀있는 리스트
    many_card = tmp[0]
    card_idx = 0

    for i in range(len(tmp)):
        # >=으로 수정필요
        if tmp[i] > many_card:
            many_card = tmp[i]
            card_idx = i
        elif tmp[i] == many_card:
            card_idx = i
    # print(many_card)
    # print(card_idx)
    # print(tmp)
    print(f'#{tc} {card_idx} {many_card}')
