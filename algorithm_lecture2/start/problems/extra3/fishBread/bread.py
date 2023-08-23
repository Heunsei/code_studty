import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    # M 초동안 K개의 붕어빵
    # N명의 사람이 시간을 두고 방문
    N, M, K = map(int, input().split())
    book_list = {}
    people = list(map(int, input().split()))
    for man in people:
        if man not in book_list:
            book_list.setdefault(man, 1)
        else:
            book_list[man] += 1

    print(book_list)