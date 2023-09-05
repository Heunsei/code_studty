# CSS LAYOUT

## 1 CSS Box Model

- 모든 HTML 요소를 사각형 박스로 표현하는 개념

### 1.1 Box 구성 요소
- 1. Content. 콘텐츠가 표시되는 영역.
- 2. Padding. 콘텐츠 주위에 위치하는 공백 영역.
- 3. Border. 콘텐츠와 패딩을 감싸는 테두리 영역.
- 4. Margin. 박스와 다른 요소 사이의 공백.

### 1.2 witdh & height 속성
- 1. 요소의 너비와 높이를 지정, 콘텐츠 영역으로 대상으로함
그래서 예상했던 너비보다 커질 수 있다
- box-size를 border-box로 바꿔서 크기를 정리

### 1.3 Box Type
- 1. display : block;
  - 남는 영역을 마진으로 다 채움
  - 항상 새로운 행으로 나뉨
  - width height 속성을 사용하여 너비와 높이를 지정
  - 기본적으로 width를 지정하지 않으면 inline방향으로 사용공간을 전부 다 씀
  - h1~6, p, div

- 2. display : inline;
  - 인라인 요소의 크기를 제어하려면 block 요소로 변경하거나 inline-block 요소로 변경
  - width와 height 속성을 사용할 수 없음
  - 컨텐츠의 크기에 따라서 결정
  - 수직 방향
    - padding, margins, borders가 적용되나 밀어내긴 불가능
  - 수평 방향
    - padding, margins, borders가 적용되어 다른요소를 밀어낼 수 있음
  - a, img, span

  ### 1.4 기타 display 속성
  - 1. inline-block
    - inline과 block요소 사이의 중간 지점을 제공하는 값
    - block 요소의 특징을 가짐
      - width, height 사용 가능
      - padding, margin 및 border로 인해 다른 요소가 밀려남
    - 줄바뀜을 원하지 않으면서 너비와 높이를 적용하고 싶을 때
  - 2. none
    - 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    - 어떠한 버튼을 누르면 사라지게 하는 또는 나오게 하는 그런 기능을 구현 할 때 사용

## 2 CSS Layout Position
- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
- Display, Position, Float, Flexbox

### 2.1 CSS Position
- 요소를 Normal Flow에서 제거하여 다른 위치로 배치 하는것
- 다른 요소 위에 올리기, 화면 특정 위치에 고정시키기
- Position 유형
  - 1. static
    - 기본값
    - flow에 따라 배치
  - 2. relative
    - 기준점을 잡고 이동
    - static 시절의 위치를 기준으로 이동
    - 요소가 차지하는 공간은 static 일 때랑 같음
    - 이전의 자리를 버리지 않기 때문에 아래 레이아웃이 깨지지 않음
  - 3. absolute
    - 요소를 normal flow에서 제거
    - 이전 자리를 버리고 이동
    - 아래에있던 레이아웃이 위로 딸려 올라 올 수 있다
    - 다른 레이아웃에 영향을 줄 수 있음
    - static이 아닌 부모를 찾아서 올라감
    - 명확한 relative 부모를 찾아주는게 중요
  - 4. fixed
    - 요소를 Normal Flow에서 제거
    - 브라우저 화면 상에 고정(View port)
  - 5. sticky
    - 스크롤에 걸려서 딸려 내려옴
    - 지정한 임계점에 걸려서 내려옴
    - 다음 sticky요소가 나오면 갈아치워짐
- Z - index
  - 정수 값을 사용 해 z축 순서를 지정
  - 더 큰 값을 가진 요소가 작은 값의 요소를 덮음
  - 설정하지 않으면 가장 나중에 생성된요소가 위로 올라옴

## 3 CSS Layout Flexbox
- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
- 공간 배열 및 정렬 가능
### 3.1 구성요소
- Flex Container 가 안의 요소의 배열을 관리
- 주축의 방향을 잘 알아야함
- 좌측이 기본이고 오른쪽으로 움직임
- main axis (주 축)
  - flex item들이 배치되는 기본 축
  - main start에서 시작해서 main end 방향으로 배치
- cross axis (교차 축)
  - main axis에 수직인 축
  - corss start에서 시작해서 cross end 방향으로 배치
- flex container
  - display : flex 혹은 display : inline - flex가 설정된 부모요소
  - 이 컨테이너의 1차 자식 요소들이 Flex item이 됨
  - flexbox 속성 값들을 사용하여 자식요소 flex item들을 배치
### 3.2 레이아웃 구성
- 1. Flex Container 지정
```html
.container{
  height: 500px;
  border: 1px solid black;
  display flex;
}
```
- 2. flex-direction 지정
```html
  flex-direction = column -reverse;
```
- 3. flex-wrap
  - flex item 목록이 flex contaioner의 하나의 행에 들어가지 않을 경우 다른 행에 배치 할 지 결정
- 4. 메인 축 정렬
  - justify-content: flex end 오른쪽 정렬
  - justify-content: center 가운데 정렬
  - justify-content: flex end 오른쪽 정렬
- 5. 교차 축 정렬
  - 여러 행을 위 아래로 이동 warp 사용하면 확인 가능
  - alien-content: flex-start > 
  - alien-content: center > 
- 6. 교차 축이 여러 행이 아닐때
  - 여러행이 되면 정렬이 안됨
  - alien-items: center
- 수직 수평 가운데 정렬
  - main축 center + 교차축 center
- 7. flex-grow
  - 비율 맞춰서 꽉채워라
- 8. flex-basis
