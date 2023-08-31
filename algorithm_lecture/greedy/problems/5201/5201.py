import sys
sys.stdin = open('input.txt')

# 화물이 실려있는 N개의 컨테이너를 M대의 트럭으로
# A > B 로 이동
# 총 합이 amout인 조합
T = int(input())
for tc in range(1, T+1):
    # 컨테이너의 수 / 트럭수
    N, M = map(int, input().split())
    # 화물의 무게
    w = list(map(int, input().split()))
    # 트럭의 적재용량
    t = list(map(int, input().split()))
    w.sort()
    t.sort()
    ans = 0
    while w and t:
        truck = t.pop()
        a = w.pop()
        if truck >= a:
            ans += a
        else:
            t.append(truck)
    print(f'#{tc} {ans}')
