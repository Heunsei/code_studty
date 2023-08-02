# 상속
1. 코드 재사용
- 기존 클래스의 속성과 메소드를 재사용 가능
2. 계층 구조
- 부모 클래스와 자식 클래스 간의 관계를 표현,구체적 클래스 작성 가능

```python
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def talk(self):
    print(f'안녕, {self.name} 입니다')

class Professor(Person):
  def __init__(self,name,age,department):
    Person.__init__(self,name,age)
    self.department = department
  
class Student(Person):
  def __init__(self,name,age,gpa):
    # 다중 상속도 가능
    super().__init__(name,age)
    self.gpa = gpa
```
3. 다중상속
```python
class Person:
  def __init__(self.name):
    self.name = name

  def greeting(self):
    return f'안녕, {self.name}'

class Mom(Person):
  gene = 'XX'

  def __init__(self.name):
    super().__init__(name)

  def swim(self):
    return '엄마가 수영'


class Dad(Peron):
  gene = 'XY'

  def __init__(self.name):
    super().__init__(name)

  def walk(self):
    return '아빠가 걷기'


class FirstChild(Dad,Mom):
  def swim(self):
    return '첫째가 수영'
  
  def cry(self):
    return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영. Mom에 있는건 무시
print(baby1.walk()) # 아빠가 걷기
print(baby.gene()) # XY, 상속에서 상위인 Dad의 gene을 가져옴
```

# 에러와 예외
1. 문법오류
- invalid syntax > 문법오류
- assign to literal > 잘못된 할당
- EOL > end of line
- EOF > end of file
2. 예외(exception)
- 프로그램 실행 중에 감지되는 에러
- 내장 예외 > 예외상황을 나타내는 예외 클래스들
- zeroDivisionError > 나누기 또는 모듈연산의 두 번째 인자가 0일때 발생
- NameError > 지역 또는 전역 이름을 찾을 수 없을때
- TypeError > 타입 불일치, 인자 초과, 인자 타입 불일치
- 인자누락
- ValueError > 연산이나 함수에 문제가 없지만 부적절한 값을받았거나 구체적인 설며이 안될때
- indexError > 시퀀스 인덱스가 범위를 벗어났을때 발생
- KeyError > 딕셔너리에 키가 없어용
- ModuleNotFoundError > 모듈이 없어용
- ImportError > 임포트할 이름이 없어용
- KeyvoardInterrupt > ctrl-c or delete 누를 때 발생, 무한루프 시 강제 종료
- IndentationError > 잘못된 들여쓰기와 관련된 문법 오류

# 예외 처리
- try & except
```python
try:
  #에외가 발생할 수 있는 코드
except 예외:
  # 예외 처리 코드
```

```python
try:
  num = int(input('100으로 나눌 값을 입력하시오:'))
  print(100 / num)

#except (ValueError,ZeroDivision): 묶어서도 처리가능
#  print('제대로 입력해주세요')
# 에러도 상속 계층 구조가 있으므로 예외를 처리할때 하위 예외 클래스를 먼저 써야함
except ValueError:
  print('숫자를 넣어주세요')
except ZeroDivisionError:
  print('0으로 나눌 수 없습니다.')
except:
  print('Error')
```