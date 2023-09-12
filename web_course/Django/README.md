# 시작하기 전에..

## 프로젝트 관리
- TIL, 학습하는 각종 폴더, 관통 pjt
- git으로 관리중
- gitignore
  - 이제는 필수래요 
  - 가상환경은 git으로 관리 안할거라 > 넘무거움
  - requirements.txt로 패키지 관리

### 가상환경 생성
```bash
# 항상 작업 위치 확인하기.
# venv 라는 이름으로 가상환경 생성
$ python -m venv venv
```
### 가상환경 실행
```bash
# 있는지 확인
$ ls
$ source {folder_name}/Scripts/activate
# 가상환경 상태 확인
$ pip list
```
## Django 설치
```bash
$ source venv/Scripts/activate
# .2버전 설치
$ pip install django
```
### 다른 작업환경을 위한 설정
```bash
$ pip freeze > requirements.txt

# txt에 적힌 내용을 기반으로 설치
$ pip install -r requirements.txt
```

## Django 프로젝트 생성.
```bash
# offline
$ django -admin startproject offline  
$ cd offline

# 현재 작업 위치에 프로젝트 생성
$ django -admin startproject offline .
```
### Django 서버 실행
```bash
# manage.py로 서버를 실행
$ python manage.py runserver
```

### app 생성 및 등록
```bash
$ python manage.py startapp atricles
```
```python
# settings.py
INSTALLED_APPS에 저장
```

### articles app의 메인 페이지 화면에 띄우기
1. client 가 요청 보낼 경로 지정하기 -> url
2. 특정 경로에 요청이 왔을때 적절한 처리하기  -> views.py
3. 적절한 처리 과정에서 template이 필요하다면 작성  -> templates/*.html
4. 작성된 temlplate을 사용자에게 반환 -> viesw에 정의한 함수의 return