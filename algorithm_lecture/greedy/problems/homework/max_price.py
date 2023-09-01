# 최대 상금
# 순열 문제래 / 여러번 바뀐게 이전꺼에 저장이 되어있으니 굳이 보러갈 필요가업슴
# 강사님 코드

# 정수를 문자열로 바꾸는 함수
def swap(cards, i, j):
    #cards = list(map(str, str(cards)))
    arr = [0] * N
    arr[i], arr[j] = arr[j], arr[i]
    num = list(''.join(arr))
    for k in range(N):
        num = (num * 10) + int(cards[k])
    return num


# 순열 대상 / 현재 위치 / 조사횟수
def perm(cards, now, r):
    global reusult
    # 내가 만들 수 있는 모든 경우의 수를 순회 해서
    for i in range(720):
        if memo[now][i] == 0;
            memo[now][i] = cards
            break
        elif memo[r][i] == cards:
            return
    if now == r:
        # 최대값 갱신
        if cards > result:
            result = cards
        return
    else:
        for i in range(N-1):
            for j in range(N):
                cards = swap(cards, i, j)
                perm(cards, now + 1, r)
    

T = int(input())
# R번째 일때 만들어 질 수있는 최대경우의 수를 기록할 리스트
# 0번째의 경우의 수

# 설명을 들어도 잘.. ㅁㄹ룩[ㅔㅆ다
# 각 횟수차 마다 들어갈 수 있는 최대의 경우의 수
# 순열의 경우 N에 대한 모든 경우의 수가 N! 최대 N -> 6


for tc in range(1, T+1):
    memo = [[0] * 720 for _ in range(11)]
    cards, r = list(map(int, input().split()))
    N = len(str(cards))
    reusult = 0
    
    # 돌릴 대상, 시작점, 끝점
    perm(cards, 0, r)