blood_types = ['A', 'B', 'A', 'O','AB','A']

new_dict = {}

# 메소드를 사용하지 않는 방법
for blood_type in blood_types:
    # 기존키가 이미 존재하는지 검사
    if blood_type in new_dict:
        # 기존 키 값 증가
        new_dict[blood_type] += 1
    # 키가 존재하지 않을 때를 고민
    else:
        new_dict[blood_type] = 1
print(new_dict)

# .get()메소드 사용
for blood_type in blood_types:
    # blood_type에 값이 없을땐 blood의 값을 0으로 설정
    # 그게 아니면 value를 +1을 해서 저장
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
print(new_dict)

# set_default()
for blood_type in blood_types:
    # 없으면 만들고 value에 0넣어줌
    # 만약 있으면 setdefault무시하고 1만더함
    new_dict.setdefault(blood_type,0)
    new_dict[blood_type] +=1