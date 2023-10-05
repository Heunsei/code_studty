### this pointer
- 현재 오브젝트의 주소를 담은 키워드
- class scope 안에서만 사용가능
- data member 또는 method 에접근하기 위해 사용
- *this로 역참조 가능

### class and const
```cpp
const Player villain {"villain", 100, 50};
villain.set_name("Nice_Guy"); // error
std::cout << villain.get_name() << std::endl //error
```
- 아래의 출력문은 villain 오브젝트의 값을 변경하지 않는데도 컴파일러가 에러를 일으킨다, 컴파일러는 get_name이라는 method가 잠재적으로 내부의 값을 변경할 수도 있다고 추측하기 때문에 에러를 일으키는것 
```cpp
const Player villainP{"villain", 100, 55};
void display_player_name(const Player &p){
  cout << p.get_name() << endl;
}
display_player_name(villain) // error  
``` 
- 해결법
> 클래스를 정의하는 과정에서 method 뒤에 const를 붙인다
 std::string get_name() const;

 # static class members
 - 특정 객체에 종속되지 않고 해당 클래스의 모든 객체에 공유된다. static 멤버 변수는 생성자에서 초기화 될 수 없으며, 클래스 외부에서도 딱히 초기화 과정이 필요가 없다.

# Friend 함수
- 수평적인 관계의 클래스간의 멤버 변수를 공유 해야할 때 주로 쓰임, 하나의 클래스에서 다른 클래스이 내부 데이터에 접근 해야할 경우 프렌드를 써서 권한을 주는 경우.
- 자신의 개체뿐만이 아닌 다른 타입의 개체를 접근하는 것이 가능해지기 때문에 코드의 확장이 수월
- 클래스 안의 함수 앞에 friend를 붙여줌으로써 friend함수 선언
- 멤버접근자를 사용하지않고 바로 접근이 가능하게 해줌
- 클래스에서 만약 friend 클래스를 넣어주면 해당 클래스는 친구의 private 멤버에 접근이 가능해짐