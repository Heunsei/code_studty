# python 데이터 구조
1. 메소드 호출 방법
- 메소드 : 객체에 속한 함수
- 'hello'.cpaitalize() 데이터 타입 객체.메소드()

2. 문자열 조회, 탐색 및 검증 메소드
- s.find(x) > x의 첫 번째 위치를 반환. 없으면 -1
- s.index(x) > x의 첫 번째 위치를 반환. 없으면 오류발생
- s.isalpha() > 알파벳 여부 판별, 문자열이 알파벳만 있는지
- s.isupper() > 대문자 여부, 전부 대문자인지
- s.islower() > 소문자 여부, 전부 소문자 인지
- s.istitle() > 타이틀 형식 여부

3. 문자열 조작 메소드(새 문자열을 반환)
- s.replace(ole,new[, count]) > 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
- s.strip([chars]) > 공백이나 특정 문자를 제거
- s.split(sep = None, maxsplit = -1) > 공백이나 특정 문자를 기준으로 분리해서 리스트로 반환
- 'separator'.join([iterable]) > 구분자로 iterabla을 합침, 하나의 문자열로 연결함
- s.capitalize() 가장 첫 글자를  대문자로 변경
- s.title() > 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자,나머진소문자로 변경
- s.upper() 전부 대문자로 변경
- s.lower() 전부 소문자로 변경
- s.swapcase() 대문자 소문자를 서로 변경

4. 리스트 값 추가 및 삭제 메소드
- L.append(x) > 리스트 마지막에 항목x을 추가
- L.extend(m) > iterable m의 모든 항목들을 리스트 끝에 추가(+=), 반복 가능한 객체의 모든 항목을 추가한다
- L.insert(i, x) > 리스트 인덱스 i에 x를 삽입
- L.remove(x) > 리스트의 왼쪽에 있는 항목x을 하나만 제거, 없으면 에러뜸
- L.pop() > 맨 오른쪽 항목을 반환 후 제거
- L.pop(i) > 인덱스 i에 있는 항목을 반환 후 제거
- L.clear() > 리스트의 모든 항목 삭제

5. 리스트 탐색 및 정렬 메소드
- L.index(x, start, end) > 리스트에 있는 항목 중 가장 왼쪽에 있는(첫번째) 항목 x의 인덱스를 반환
 - L.reverse() > 리스트를 거꾸로 정렬
 - L.sort() > 리스트를 정렬
 - L.count(x) > 항목 x의 개수를 반환

