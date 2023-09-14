# Django-MODEL
- model을 통해 DB를 관리
- DB의 테이블을 정의하고 데이터를 조작가능한 blue-print제공
- id title content 등을 가진 설계도를 만드는 것을 models.py에서 진행
- 클래스 형식으로 작성

## 만드는법
- 1. django.db.models 모듈의 Model 클래스를 상속(models.Model)
- 2. class 아래에 선언한 클래스 변수명으로 테이블의 Field(col)을 생성
- 3. models.(Data_type) 테이블 필드의 데이터 타입을 선언
    - DB의 데이터 타입을 일치화 시킴
- 4. model Fiedl 클래스의 키워드 인자
    - max_length > 길이를 제약 시킴
    - 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙
    - 숫자만 저장되도록, 문자의 길이를 제약시키는 등

## Migrations
- models 클래스의 변경사항을 DB에 최종 반영
- 설계도 초안 만들기 -[makemigrations]-> migration파일 -[migrate]-> db.sqlite3(DB)

### 핵심 명령어
- 설계도 작성
  - $ python manage.py makemigrations
- DB에 반영
  - $ pyhton manage.py migrate

### 설계가 바뀌어서 필드를 추가해야 할 때
- 추가 모델 필드 작성
- python manage.py makemigrations
  - 무결성 검사때문에 그냥 못넣음
    - 1. 장고가 제공해주는걸 쓰기
    - 2. 직접 수정하기
- 새로운 값을 추가할 때 이전값이 있을 수있으므로 그값을 비워서 넣을수 없으니 추가 과정이 필요
- 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록 함

## model-field
- 1. charField() 길이의 제한이 있는 문자열을 넣을 때 사용
  - max_length 필수인자
- 2. TextField()
  - 글자 수가 많을 때 사용
- 3. DateTimeFiedld()
  - 1. auto_now > 저장될 때마다 자동으로 시간 갱신
  - 2. auto_now_add > 처음 생성 될 때만 시간 저장

# Admin site
- 관리자 사이트
- automatic admin interface
  - 자동으로 관리자 인터페이스 제공
- 설계도 클래스 들은 어플리케이션의 admin.py에 등록하지 않으면 admin사이트에서 사용할 수 없다


## DB초기화
- 1. migration 파일삭제
  - migrations 폴더 삭제 xxxxxxxx
  - __init__py 삭제 xxxxxxxxx
- 2. db.sqlite3 파일 삭제

## 기타 명령어
- $ python manage.py showmigrations
- $ python manage.py sqlmigrate article 0001
  - 어떤 앱의 몇번째 설계도를 볼거냐?
  - migrations 파일이 sql언어로 어떻게 번역되어 db로 가는지 확인하는 명령어