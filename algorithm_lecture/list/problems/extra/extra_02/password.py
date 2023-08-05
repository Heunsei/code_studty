# 문자열을 읽어와서 새로운 리스트에 숫자들의 갯수를 저장
# 정렬하면 순서가 뒤바뀌니까 정렬은 x

# test case 총 10개
for tc in range(1, 11):
    num, card = list(input().split())
    #print(type(num))
    #print(type(card))

    card_list = list(map(int, card))  # 받아온 카드가 str, 변환해서 앞으로 이거사용
    card_idx = 0
    while True:
        if card_list[card_idx] == card_list[card_idx+1]:
            card_list.pop(card_idx)
            card_list.pop(card_idx)
            #삭제하면 처음부터 다시
            card_idx = 0
        elif card_list[card_idx] != card_list[card_idx+1]:
            card_idx += 1

        # 종료 조건
        # card 리스트는 유동적으로 변함
        # 리스트의 길이가 5일때 길이보다 2 작아야 4번째(idx=3)를 의미
        if card_idx + 2 == len(card_list):
            if card_list[card_idx] == card_list[card_idx+1]:
                card_list.pop(card_idx)
                card_list.pop(card_idx)
                break
            else:
                break
    result = ''.join(map(str, card_list))
    print(f'#{tc} {result}')

