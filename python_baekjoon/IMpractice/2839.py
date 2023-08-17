# 설탕배달
# 3kg 봉지와 5kg 으로 조합가능한 개수중 가장 작은걸 출력
T = int()
box = 5000
# T가 5의 배수인지 검사
if T % 5 == 0:
    tmp = T//5
    if tmp < box:
        box = tmp
# T가 3의 배수인지 검사
if T % 3 == 0:
    tmp = T//3
    if tmp < box:
        box = tmp
    