# OOP
## 1. 객체지향 프로그래밍

### 절차지향
- 데이터와 해당 데이터를 처리하는 함수가 분리
- 함수 호출의 흐름이 중요

### 객체 지향
- 데이터와 해당 데이터를 처리하는 메소드를 하나의 클래스로 묶음
- 객체 간 상호작용과 메세지 전달이 중요

## 2. Class
- 타입을 표현하기 위한 방법, 객체를 생성하기 위한 설계도

### 객체
- 클래스에서 정의한 것을 토대로 메모리에 '할당'된 것 속성과 행동으로 구성된 모든 것
```python
# name의 타입은 str클래스
# name은 str클래스의 인스턴스
name = 'Alice'
print(type(name))
```

### 클래스
- 파이썬에서 타입을 표현하는 방법
```python
class Person:
# 클래스 변수
  blood_color = 'red'
# 생성자, self > this랑 똑같은 의미 생성된 객체를 지목
  def __init__(self,name):
    # 인스턴스 변수, 객체마다 별도로 저장되는 속성값, 생성될때마다 생성자에서 초기화
    self.name = name

  def singing(self):
    return f'{self.name}가 노래합니다.'

iu = Person()
iu.method()
iu.attribute()
```
- 클래스를 정의하면, 클래스와 해당하는 이름공간 생성
- 인스턴스르 만들면 인스턴스 객체가 생성되고 독립적이 이름공간 생성
- 인스턴스에서 특정 속성에 접근하면. 인스턴스 -> 클래스 순으로 탐색

```python
class Person:
  # instance_name.name = 으로 접근가능
  # Person.name으로 접근가능 nuknown 출력됨
  # 딱히 좋은 구성은 아니다, 클래스 변수와 인스턴스 변수를 분리할 필요가있음 
  name = 'nuknown'

  def talk(self):
    # 객체 자신을 호출해서 name값을 받아와 그것을 출력
    print(self.name)
  
```
- 각 인스턴스는 독립된 메모리 공간을 가져 같은 이름의 변수라도 다른 값을 적용하고 각각의 인스턴스의 같은 이름의 변수에 다른 값을 따로따로 저장해 그것을 분별해가며 접근 가능하다.

```python
class Person:
  count = 0
  # Person클래스 생성자를 호출하면서 Person의 변수인 count를 관리
  def __init__(self,name):
    self.name = name
    Person.count +=1
  
  # 인스턴스 메소드, 클래스 내부에 정의되는 메소드의 기본
  # 첫 매개변수로 자신을 전달받음
  def instance_method(self, arg1, ...):
    pass
```
### @classmethod
```python
class Person
# 클래스변수
  count = 0
  def __init__(self,name):
  #인스턴스 변수
    self.name = name
  #Person.increse_person(1)
    Person.count += 1

  @classmethod
  def increse_person(cls,num)
    cls.count += num
  
  @classmethod
  def number_of_population(cls):
    print(f'인구수는 {cls.count}입니다.')

Person.number_of_population()
```
- 클래스 메소드.
- 인스턴스가 접근하는게 아니라 클래스 자체에서 접근하는 함수
- class에서 관리하는 값에 접근하는데 사용


## method의 종류
1. 인스턴스 메소드
- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메소드
- 인스턴스의 상태조작 또는 동작 수행
- 첫 매개변수로 self 자신을 받음
- 생성자도 인스턴스 메소드

2. 클래스 메소드
- @classmethod 데커레이터 사용
- 첫인자로 cls(클래스) 사용
- 클래스 변수에 접근 가능
- 생성자 포함 인스턴스 메소드 변수에 접근 불가능
- 클래스 변수 : 클래스 정의에서 메소드 밖에있는 변수를 클래스 변수라 칭하는데 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수. 

3. 정적 메소드
- 부모 클래스에서 정의된 staticmethod는 자식클래스에서 call가능
- 클래스 변수에는 접근가능
- 생성자 포함 인스턴스 메소드 속성에는 접근불가능
- 주로 유틸리티성 함수를 위한 용도
- 클래스의 어떠한 속성에도 변화를 일으키지 않으며 입력이 들어오면 항상 같은 출력을 반환하는순수 함수들 

### 추가
- 인스턴스들은 클래스와 관계없는 개별의 인스턴스 변수들을 가질 수 있다
- 다만 인스턴스들을 관리하는 인스턴스 메소드는 클래스 내에서만 선언하고 정의할 수 있기때문에 클래스로 생성된 객체인 인스턴스에서 자신의 행동을 만들수는 없다.
- 인스턴스에서 클래스변수에 접근을 해 바꾸려는 시도를 하게된다면 자신의 인스턴스 변수를 새로 생성해 값을 할당하는 행동이다, 다만 인스턴스 메소드에서 클래스 변수에 접근은 가능해서 출력하거나 더하기등은 할 수 있다.