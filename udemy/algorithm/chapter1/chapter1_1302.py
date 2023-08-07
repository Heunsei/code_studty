# 가장 많이 팔린 책의 제목을 출력
# key와 value가 묶여있는 딕셔너리를 사용
N = int(input())
sell = {}
for i in range(N):
    book = input()
    if book in sell:
        sell[book] += 1
    else:
        sell.setdefault(book, 1)

max_book = 0
# max_book = max(sell.values())
for book, num in sell.items():
    if num > max_book:
        max_book = num
candi = []
for k, v in sell.items():
    if v == max_book:
        candi.append(k)
# print(sorted(candi)[0])
candi.sort()
print(candi[0])