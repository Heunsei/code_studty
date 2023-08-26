# 체스판
import sys
sys.stdin = open('input.txt')


# 시작 좌표, 왼쪽 상단의 색깔
def count_color(pos_i, pos_j, color):
    ans = 0
    line_count = 1
    for i in range(pos_i, pos_i+8):
        idx_count = 1
        for j in range(pos_j, pos_j + 8):
            #print('val , idx, line', arr[i][j],idx_count,line_count)
            # 색을 설정한 줄
            if line_count % 2 == 1:
                # 줄의 인덱스가 짝수 일떄 
                if idx_count % 2 == 0:
                    if arr[i][j] == color:
                        ans += 1
                # 줄의 인덱스가 홀수 일때
                elif idx_count % 2 != 0:
                    if arr[i][j] != color:
                        ans += 1
                idx_count += 1
            # 짝수 줄일떄
            else:
                if idx_count % 2 == 0:
                    if arr[i][j] != color:
                        ans += 1
                    # 줄의 인덱스가 홀수 일때
                elif idx_count % 2 != 0:
                    if arr[i][j] == color:
                        ans += 1
                idx_count += 1
        line_count += 1
    #print(ans)
    return ans

N, M = map(int, input().split())
arr = [input() for _ in range(N)]


d = count_color(0, 0, 'W')
ans = 987654321
for i in range(N-7):
    for j in range(M-7):
        w_count = count_color(i, j, 'W')
        b_count = count_color(i, j, 'B')
        compare = min(w_count,b_count)
        if compare < ans:
            ans = compare
print(ans)