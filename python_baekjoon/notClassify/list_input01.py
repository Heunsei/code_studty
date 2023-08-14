# 학생수를 받아올 리스트작성
students = []
# 28명만 받을꺼니까 0~27까지 (28번)
# append를 사용해서 빈 리스트에 삽입
for i in range(28):
    stu = int(input())
    students.append(stu)
none = []
# 1_30까지 번호 있는지 순회
for num in range(1,31):  
    # 어차피 작은순으로 비교하니까 프린트만 해도되지 않을까?
    if num not in students:
        none.append(num)
# 어차피 비교할 리스트요소가 두개밖에 없으니 간단히 작성
# min(none) 이래쓸수 있단다;
if none[0] > none[1]:
    print(none[1])
    print(none[0])
else :
    print(none[0])
    print(none[1])
    
