# 1~12까지 숫자가 있음
# N개의 원소를 가지고
# 원소의 합이 k인 부분집합의 개수

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    # 집합 A는 다음과 같은 형태
    test_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    count = 0
    # 2^len(test_case)만큼 부분집합이 존재하니 비트연산으로 밀어주기
    for i in range(1 << len(test_case)):
        tmp = [] # 조건에 맞는 부분집합들을 저장하고,확인할 임시 리스트
        for j in range(len(test_case)):
            # i가 1일때 000000000001 랑 1 10 100 1000 ``````를 비교
            if i & (1 << j):
                tmp.append(test_case[j])
        # N은 원소의 수, K는 부분집합 원소들의 합
        # tmp를 반복시켜 sum과 길이를 구할 수 있음
        if len(tmp) == N and sum(tmp) == K:
            print(tmp)
            count += 1

    print(f'#{tc} {count}')


