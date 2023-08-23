import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    # M 초동안 K개의 붕어빵
    # N명의 사람이 시간을 두고 방문
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    print(N,M,K)