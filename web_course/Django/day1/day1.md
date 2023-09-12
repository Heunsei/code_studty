# Django
- client & server
  - 서비스 이용의 주체
  - 클라이언트의 요청에 응답하는 주체
- 웹 페이지를 보는 과정
  1. 서버에게 페이지의 html 파일을 달라고 요청
  2. 데이터베이스에서 html파일을 찾아서 응답
  3. 웹 브라우저가 사람이 볼 수 있도록 해석


# 가상 환경 세팅 및 버전관리
- venv 생성
  - $ python -m venv venv
- 활성화
  - $ source venv/Scripts/activate
- 패키지 목록 확인
  - $ pip list
- 의존성 패키지 목록 생성
  - $ pip freeze > requirements.txt
- Django 프로젝트 생성
  - $ django-admin startproject firstpjt .
- Django 서버 실행
  - $ python manage.py runserver