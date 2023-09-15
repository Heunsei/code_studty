# ORM
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술
- 장고와 db와의 소통

# 설치해야할 것
- pip install ipython
- pip install django-extenstions

## QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구 > API를 사용해 sql이 아닌 python코드로 데이터를 처리
- Article.objects.all()
- modelclass.manager.QuertsetAPI

### Query
- 1. 데이터베이스에 특정 데이터를 보여달라는 요청
- 2. 쿼리문을 작성한다
  - 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다
- 3. 파이썬으로 작성한 코드가 orm으로 인해 sql로 변한되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 orm이 queryset이라는 자료 형태로 변환하여 전달
### QuerySet
- 데이터베이스에게 전달받은 객체 목록(데이터 모음)
  - 순회가능
- Django ORM으로 만들어진 자료형
- 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델의 인스턴스로 반환됨
- 반환받은 쿼리셋 데이터는 인덱스로 하나하나 접근
- 모음이라 하나로 들어오니까 접근할때 인덱스 쓰기!

# 데이터 조작을 sql이 아닌 python언어로 하겠다

# shell
- python manage.py shell_plus

# 데이터 객체 만들기
## 1.
## 2. 

### save()
- 객체를 데이터베이스에 저장하는 메소드

# READ
- all()
  - Article.objects.all()
  - 전체 데이터 조회
- get()
  - Article.objects.get()
  - 단일 데이터 조회
  - 찾을 수 없을때 error
  - 여러개 동시에 나오면 error
  - pk(id)와 같이 고유성을 보장하는 조회에서 사용
- filter()
  - Article.objects.filter(location = 'to_find')
  - 특정 조건 데이터 조회
  - 조건에 맞지 않으면 빈 쿼리셋 반환
  - 결과값에 상관없이 쿼리셋으로 반환

# Update (get이랑 자주 쓸거)
- 수정할것을 get으로 변수에 담아두고 수정
- 인스턴스 변수를 변경 후 save메소드 호출

# Delete
- instance_name.delete()
- 바로 삭제 save할 필요도없슴
- 잘 선택하고 지우면 끝

