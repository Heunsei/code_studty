# n장의 카드 1부터 N까지 존재
# 1번 카드가 맨위, N이 제일아래
# 시간초과
# 삽입 삭제를 한번할때마다 O(N)필요 그걸 n 번가깝게 하니까 N^2
T = int(input())
card = [i for i in range(1, T+1)]
#print(card)
# 1빼고 2를 마지막으로 append
# 3빼고 4를 pop and append
result = []
while len(card) != 1:
    card.pop(0)
    tmp = card.pop(0)
    #print('tmp =', tmp)
    card.append(tmp)
print(' '.join(map(str, card)))