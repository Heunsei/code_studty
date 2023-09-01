# 정식이의 은행 업무
# 복습 필요
# 2진수 N자리수가 있다면 N개만큼의 후보가 생김
# 3진수는 각자리가 1,2,3 중 하나
T = int(input())
for tc in range(1, T+1):
    A = input()         # 2진수
    B = list(map(int, input()))   # 3진수

    N = len(A)  # N 자릿수 2진수
    M = len(B)  # M 자릿수 3진수

    ans = 0

    binary = int(A, 2)  # 정수로 변환
    bin_list = [0] * N  # 각 비트를 반전시킨 N개의 수 저장
    for i in range(N):  # 각 자리를 반전시킨 2진수 만들기
        bin_list[i] = binary ^ (1 << i)    # i번째 수를 반전
    
    for i in range(M):  # 3진수의 B[i] 자리를 바꾼 숫자 만들기
        num1 = 0    # 바꾼 자리수를 저장할 임시변수
        num2 = 0    # 바꾼 자리수를 저장할 임시변수
        for j in range(M):
            if i != j:
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]
            else:
                num1 = num1*3 + (B[j] + 1) % 3
                num2 = num2*3 + (B[j] + 2) % 3
        if num1 in bin_list:
            ans = num1
            break
        if num2 in bin_list:
            ans = num2
            break
    print(f'#{tc} {ans}')

