# 첫줄엔 테스트케이스
# 둘째 줄에 각 날의 매매가
# 최대값을 찾기
# 거꾸로 돌면서 max값을 정하고 그것을 빼면서 계산

T = int(input())
for tc in range(1, T+1):
    day_len = int(input())
    days = list(map(int, input().split()))
    days.reverse()
    result = 0
    # 돌려서 처음부터 생각
    max_val = days[0]
    for i in range(1, len(days)):
        if max_val - days[i] > 0:
            result += max_val - days[i]

        if days[i] > max_val:
            max_val = days[i]

    print(f'#{tc} {result}')