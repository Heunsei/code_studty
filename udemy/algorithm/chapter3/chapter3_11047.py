# 동전
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
# coin에 있는 요소들을 조합해서 작은 수를 이용해서 K완성
coins.reverse()

ans = 0
for coin in coins():
    ans += K // coin
    K &= coin
    print(f'coin : {coin}, K = {K}')
print(ans)