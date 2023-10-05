https://www.adservio.fr/post/composition-vs-inheritance
# Inheritance 상속
- 현존하는 클래스에대한 재사용을 허락하는것
- 새 클래스는 존재하던 클래스를 기반으로 하지만 개별적으로 수정해 유니크하게 만들 수 있다
- 공통의 속성을 모아 여러번 일 하는것을 막아줌

## 1. 용어와 문법
### 1. Terminology
- Base Class : 부모 클래스
- Derived Class : 자식 클래스
- Is-A relationship
    - 기초클래스의 기능의 전부를 파생 클래스도 수행할 수 있는 상태
    - public 상속
- Generalization : 일반화 
    - 비슷한 클래스들을 하나의 클래스로 합치는 것
- Specialization : 특수화

### 2. Notation
```cpp
class Account{
  // balance, deposit, withdraw  
};

class Saving_Account : public Accunt{

};
```

## 2. Inheritance and composition
- 둘 다 현존하는 클래스를 재사용 하는것
- 1. Inheritance 에서 오브젝트와 클래스는 tightly하게 묶여있다
    - 수정이 권장되지 않는다는 뜻, 부모클래스, super클래스의 변화가 자식클래스에 대해 리스크있는 변화를 야기할수있음
    
- 2. Composition 에서 오브젝트와 클래스가 loosely하게 이어져있음
    - 코드가 망가질 걱정없이 컴포넌트들을 바꿀 수 있음
    - 좀더 유연한 사용이 가능
### 상속의 장점
- Facilitates easy reusability of code from parent class without having to copy it
- Provides a clear, hierarchical structure so you can break a model into simple, accessible components.

## 3. Deriving(파생) classes from existing class
- types of inheritance in c++
    - public
        - Establishes 'is-a' relationship between derived and base classes
    - private and protected
        - Establishes 'derived class has a base class' relationship
        - different from composition

## 4. Access with public inheritance
- public inheritance
    - Base Class : pulbic a, protected b, private c,
    - Derived Class : public a, protected b, c > no access 
- pritected inheritance (is-a 관계가 아님)
    - Base Class : pulbic a, protected b, private c,
    - Derived Class : protected a, protected b, c > no access 
- private inheritance (is-a 관계가 아님)
    - Base Class : pulbic a, protected b, private c,
    - Derived Class : private a, private b, c > no access 
    
## 5. constructor and destructors
- 상속 클래스는 부모 클래스의 생성자, 파괴자, 오버로딩된 대입연산자, 프렌드함수들을 상속받지 않음
- 상속 클래스의 생성자, 파괴자, 대입연산자들은 base클래스 버전을 부를 수 있음
- 파생 클래스에서 기반클래스의 생성자를 명시적으로 호출해야함.

## 상속에서의 복사 이동 생성자.
- 기본적으로 base class에서 상속되지 않음
```cpp
// 파생클래스에서 생성자 옆에 기본적으로 baseclass 생성자를 호출
Derived::Derived(const Derived &other)
    : Base(other), {Derived initialization list}
{
    //code
}
```