import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = N
for i in A:
    if B > i:
        continue
    n = i - B

    if n != 0:
        if n % C != 0:
            ans += n // C + 1
        else:
            ans += n // C
print(ans)