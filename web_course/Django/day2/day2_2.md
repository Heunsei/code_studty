# url 패턴을 관리하는법
- 프로젝트의 urls에서 관리하기에는 양이 너무 방대해 지므로 app에 따라서 url을 관리하는 영역을 나눔
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # include를 임포트해서 주소를 관리
  # articles로 진행되는 주소를 articles 에있는 urls.py 파일이 관리하도록 변경
  path('articles/', include('articles.urls')),
  # pages로 진행되는 주소를 pages 에있는 urls.py 파일이 관리하도록 변경
  path('pages/', include('pages.urls')),
]
```
- 각각의 어플리 케이션에 urls.py를 만들어서 관리해야함

# 전역적으로 base.html 템플릿을 공유하는법
- settings.py에 있는 TES의 'DIRS' 의 내용을
- BASE_DIR/'templates'로 변경
- 베이스에 있는 templates 파일에 있는 애들도 찾아줘
- 애플리케이션에 있는 templates의 html은 extends base.html (템플릿 이름임) 만써도 템플릿 적용 가능

# URL 별칭
- 링크의 주소 대신에 별칭을 사용하려면 url매핑에 name을 사용
- path('', views.index, name='index')

# URL namespace
- 다른 앱의 동일한 이름의 url 별칭을 사용했을 때 발생할 수 있는 문제를 예방하기 위해 app에서 url을 관리할때 위에 app_name = 'n_name'을 선언해서 중복되는 별칭 사용시의 문제를 예방한다