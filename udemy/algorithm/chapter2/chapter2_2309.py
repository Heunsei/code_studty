# 일곱난쟁이 문제
# 이전에는 하나하나 포문 돌리면서 합이
# 총합 - 100 일때 둘 더한게 계산한 값이랑 같으면 둘을 출력하는 방식으로
# 9개의 숫자중에 7개 뽑아서 합이 100 인걸 뽑는다
# 조합으로 사용

from itertools import combinations
heights = [int(input()) for _ in range(9)]
# 출력은 세트 형식
for combi in combinations(heights, 7):
    if sum(combi) = 100:
        for height in sorted(comni):
            print(height)
        # 여러개 있을때 하나만 출력하고 멈추기
        break