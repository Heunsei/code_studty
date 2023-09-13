# django template
## 1. template system
- 데이터의 표현을 제어하면서 표현과 관련된 부분들 담당
- 콘텐츠를 변수 값에 따라 바꾸고 싶을 때
- DTL (Django Template Language)
  - html에 프로그래밍적 기능을 추가
```django
def index(request):
  context = {
      'name' : 'jain',
  }
  return render(request, 'articles/index.html', context)

<body>
  <h1>Hello, {{name}}</h1>
</body>
```
## DTL
- 변수 variable
  - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
  - .을 사용해서 변수 속성에 접근 가능
  - {{variable}}
- filter
  -변수를 수정할 때 사용
  - chained가 가능하며 일부 필터는 인자를 받기도 함
  - 약 60개의 built - in - filters를 제공
- tag
  - 반복 또는 논리를 수행하여 제어 흐름을 만듦
  - 일부 태그는 싲가과 종료 태그가 필요
  - {% tag %}
  - {% if %}  {% endif %}
- 주석
  - {# name #}
  - {% comment %} {% endcomment %}

## 템플릿 상속
- 템플릿에 bootstrap을 적용하는법 
- 페이지의 공통 요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의
- 기본 skeleton 템플릿을 작성하여 상속 구조를 구축

## 'form' tag
- 사용자로부터 할당된 데이터를 서버로 전송

## query string parameters
- 사용자의 입력 데이터를 url을 통해 서버로 보내는 방법
- &로 연결된 key=val 쌍
- http://host:port/path?key=value&key=value


# django URLs
- 사용자 클라이언트로부터 데이터를 받아오고 적절한 view 함수를 호출하는 역할

### url dispatcher
- url 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view함수를 연결

### 변수와url
- 템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 url과 템플릿을 작성하는 문제
- variable routing
  - url일부에 변수를 포함시키는것
  - 변수는 view 함수의 인자로 전달 가능
  
