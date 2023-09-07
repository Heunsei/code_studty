# bootstrap grid system
- 웹 페이지의 레이아웃을 조정하는 12개의 컬럼

- 꿀팁 ul.nav>li.nav-item*4>a{메뉴 $}
- emmet cheat sheet
- .container. > div 를 바로 컨테이너 넣어서 만들기

## 사용법
- div class ="container"
-   div class ="row"
-     div class="col-4" /div
-   /div
- /div

- row를 12등분해서 나눠서 콘텐츠를 배치

## gutters
- column사이의 여백
- grid system에서 column 사이에 여백 생성
- x축은 padding y축은 margin으로 여백 생성
- x축을 margin을 쓰면 부모축을 벗어나 튀어나올 가능성이 있어서 padding을 사용

## 반응형 웹
- 디바이스의 종류나 화면 크기에 상관없이 일관된 레이아웃 및 사용자 경험을 제공하는 기술
- 12개의 column과 6개의 breakpoints를 사용해 디자인 구현
- xs, sm, md, lg, xl, xxl
- 각각의 설정된 최대 너비 값 이상으로 커지면 grid system 동작이 변경됨
- col 뒤에 -로 연결
- col-sm-4
  - 사이즈가 576 ~ 767 일때 사이즈를 4 차지한다
- col-md-8
  -768이 되면 8칸 차지