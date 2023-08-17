# 연속하는 P일 중 L일만 사용가능
# V 일 짜리 휴가를 시작했을때 캠핑장 최대 사용 기간
tc = 0
while True:
    result = 0
    # L일동안 사용가능 P일간
    # 5 8 20
    L, P, V = map(int, input().split())
    if P + L + V == 0:
        break

    week = V // P
    #print(week)
    # L이 나머지보다 짧을 수도 있으니까 둘중 짧은것을 사용
    day = min(L, V % P)
    #print(day)
    result = week * L + day
    tc += 1
    print(f'Case {tc}: {result}')


