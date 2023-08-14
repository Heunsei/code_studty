# 체크할 배열, 시작점 필요
# 종료지점도 필요(모든 원소의 개수가 종료시점)
# 총합 = 누적값

def solution(arr, end, result):
    if result != 10:
        return
    for i in range(1, end+1):
        if arr[i]:
            print(data[i], end=' ')
    print()

def backtracking(arr, now, end, result):
    global count
    if result > 10:
        return
    count += 1
    # 후보군 목록 만들기
    # 부분 집합의 원소로 now번째의 값을 쓸거냐 안쓸거냐
    c = [0] * 2
    
    # 조사를 진행할 조건
    if now == end:
        solution(arr, end, result)
    else:
        # 조사할 원소가 남아있으니까 다음원소 조사
        now += 1
        # arr 의 now 값을 쓸 수 있을지 판별하는 후보군
        # arr, 지금까지 사용한 원소 인덱스도 사용, 최대원소 갯수, 후보군 목록에 기록
        nCandidates = construct_candidates(c)
        # 후보군의 수 만 큼 반복해서 조사
        for i in range(len(nCandidates)):
            arr[now] =c[i]
            if arr[now]: # 현재 조상 대상을 쓰기로 했다면
                # now 번째 원소를 쓰기로 했으면
                # 부분집합의 합의 누적 값이 now 번째 원소의 값 만큼 증가
                backtracking(arr, now, end, result + data[now])
            else:
                # now번째 원소를 안쓴날
                backtracking(arr, now, end, result)

def construct_candidates(c):
    c[0] = True
    c[1] = False
    return c

# 유망성조사
# 후보군의 수 (지금 안쓸거래)

data = list(range(11))
NMAX = 12
count = 0
arr = [0] * NMAX
backtracking(arr, 0, 10, 0)