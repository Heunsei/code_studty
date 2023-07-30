# 다이얼
dials = ['ABC','DEF', 'GHI', 'JKL','MNO', 'PQRS', 'TUV', 'WXYZ']

numbers = list(input())
count = 0
# 입력받은 리스트 만큼 순회
for num in range(len(numbers)):
    # 다이얼 안에있는 리스트들 순회
    for dial in dials:
        # 만약 입력받은 리스트의 num번째 원소가 dial에 있으면 그 다이얼의 index만큼 숫자 증가
        # dial은 세개 또는 네개의 알파벳으로 이루어진 String, dials는 string의 집합임
        # 안에 있다면 ~ ABC 안에 있는거니까 ABC의 index를 3 더해서 count에 넣어주겠다 이런뜻
        if numbers[num] in dial:
            count += dials.index(dial)+3
print(count)
    