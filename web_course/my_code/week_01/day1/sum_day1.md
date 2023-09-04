# 1. web page의 구성요소
- 1. Structure > HTML
- 2. Styling > CSS
- 3. Behavior > JS

## 1. HTML
- Hyper Text markup Language
- 1. hyper text > 웹 페이지를 다른 페이지로 연결하는 링크
- 2. markup language > 태그를 이용하여 문서나 데이터의 구조를 명시하는 언어

## 1.2 HTML의 구조
- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
- 속성
  - 1.요소 이름과 속성 사이에 공백이 있어야 함
  - 2.하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
  - 3.속성 값은 열고 닫는 따옴표로 감싸야 함
  - 4.나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  - 5.CSS에서 해당 요소를 선택하기 위한 값으로 활용됨

- DOCTYPE html
  - 해당 문서가 html로 문서라는 것을 나타냄

- html /html
  - <열린태그><닫힌태그>
  - 전체 페이지의 콘텐츠를 포함

- title /title
  - 브라우저 탭 및 즐겨찾기 시 표시되는 부분의 제목으로 사용

-  head /head
  - HTML 문서에 관련된 설정, 설명 등
  - 사용자에게 보이지 않음

- body /body>
  - 페이지에 표시되는 모든 컨텐츠

## 1.3 HTML 구조 태그
- Heading & paragraphs
  - h1 ~ 6, p

- lists
  - ol, ul, li

- Empasis & Importance
  - em, string


## 2. CSS
- 웹 페이지의 디자인과 레이아웃을 구성하는 언어
- css 구문
```css
h1 {
  color:blue;
  fint-size: 30px;
}
```
## 2.1 CSS Selectirs
- 기본선택자
  - 전체(*) 선택자
  - 요소(tag) 선택자
  - 클래스(Class) 선택자
  - 아이디(id) 선택자
  - 속성(attr)선택자
- 결합자
  - 자손결합자 ("" (sapce))
    - 첫 번째 요소의 자손 요소들선택
    - p span은 p 안에 있는 모든 span을 선택
  - 자식 결합자(>)
    - 첫 번째 요소의 직계 자식만 선택
    - ul > li은 ul 안에있는 모든 li를 선택

## 3. 우선순위
- 동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 했을 때 어떤 규칙이 적용되는지 결졍

- 우선순위 높은 순
  1. importance
    - !importatne
  2. liline 스타일
  3. 선택자
    - id 선택자 > class 선택자 > 요소 선택자
  4. 소스 코드 순서