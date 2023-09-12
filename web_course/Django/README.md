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
