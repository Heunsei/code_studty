import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    # 찾아야하는 회문의 길이
    N = int(input())
    arr = [input() for _ in range(8)]

    count = 0
    for i in range(8):
        for j in range(9 - N):
            temp = arr[i][j:j + N]
            #print(temp)
            temp_len = len(temp)
            # 짝수일 때
            if N % 2 == 0:
                left = list(temp[:N//2])
                #print(left)
                right = list(temp[N//2:])
                #print(right)
                right.reverse()
                if left == right:
                    count += 1
            # 홀수일 때
            else:
                left = list(temp[:N // 2])
                #print(left)
                right = list(temp[N // 2 + 1:])
                #print(right)
                right.reverse()
                if left == right:
                    count += 1

    for j in range(8):
        for i in range(9 - N):
            temp = []
            for k in range(N):
                temp.append(arr[i+k][j])
            #print(temp)
            temp_len = len(temp)
            # 짝수일 때
            if N % 2 == 0:
                left = list(temp[:N//2])
                #print(left)
                right = list(temp[N//2:])
                #print(right)
                right.reverse()
                if left == right:
                    count += 1
            # 홀수일 때
            else:
                left = list(temp[:N // 2])
                #print(left)
                right = list(temp[N // 2 + 1:])
                #print(right)
                right.reverse()
                if left == right:
                    count += 1

    print(f'#{tc} {count}')