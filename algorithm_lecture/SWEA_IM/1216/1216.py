import sys
input = sys.stdin.readline
def get_max(N):
    while True:
        for i in range(100):
            for j in range(101 - N):
                temp = arr[i][j:j + N]
                # print(temp)
                temp_len = len(temp)
                # 짝수일 때
                if N % 2 == 0:
                    left = list(temp[:N // 2])
                    # print(left)
                    right = list(temp[N // 2:])
                    # print(right)
                    right.reverse()
                    if left == right:
                        return N
                # 홀수일 때
                else:
                    left = list(temp[:N // 2])
                    # print(left)
                    right = list(temp[N // 2 + 1:])
                    # print(right)
                    right.reverse()
                    if left == right:
                        return N

        for j in range(100):
            for i in range(101 - N):
                temp = []
                for k in range(N):
                    temp.append(arr[i + k][j])
                # print(temp)
                temp_len = len(temp)
                # 짝수일 때
                if N % 2 == 0:
                    left = list(temp[:N // 2])
                    # print(left)
                    right = list(temp[N // 2:])
                    # print(right)
                    right.reverse()
                    if left == right:
                        return N
                # 홀수일 때
                else:
                    left = list(temp[:N // 2])
                    # print(left)
                    right = list(temp[N // 2 + 1:])
                    # print(right)
                    right.reverse()
                    if left == right:
                        return N
        N -= 1


for tc in range(1,11):
    # 찾아야하는 회문의 길이
    t = int(input())
    arr = [input() for _ in range(100)]
    res = get_max(100)
    print(f'#{tc} {res}')