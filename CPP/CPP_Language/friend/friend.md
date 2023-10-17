# 프렌드
- 프렌드 클래스 : 프렌드로 지정한 클래스의 멤버는 지정한곳의 클래스 멤버를 직접참조 가능
- 프렌드 함수 : 두 객체를 비교할때 씀
	- 클래스 멤버가 아닌 특수한 엑세스 권한이 부여되는 일반적인 외부 함수
- 프렌드 외부함수 : 두 객체를 가지고 연산을 하는 경우 사용


## 특징
- 1. 지정할 개체의 시작부분에 friend를 명시
- 2. 프렌드로 설정한 개체는 그 클래스의 멤버가 아니므로 public이나 pirvate같은 접근 지정자의 영향을 받지 않는다.
- 3. 프렌드 함수의 원형은 비록 클래스 안에 포함되어 있으나 멤버 함수는 아니며 본체는 외부에서 따로 정의한다.
- 4. 프렌드 함수는 클래스 내부의 모든 멤버 변수를 사용할 수 있으며 어떤 멤버함수도 호출이 가능함

- 다른 클래스의 멤버함수를 프렌드로 설정
```cpp
class Rect;

class RectManager {
public:
	bool equals(Rect r, Rect s);
};


class Rect {
private:
	int width, height;

public:
	Rect(int width, int heght) {
		this->width = width;
		this->height = heght;
	}

	// RectManager 클래스의 equals() 멤버를 프렌드로 선언
	friend bool RectManager::equals(Rect r, Rect s);
    // > rect의 private 멤버들에 접근 가능
};

bool RectManager::equals(Rect r, Rect s) {
	if (r.width == s.width && r.height == s.height)
		return true;
	else
		return false;
}
```

- 전체 클래스를 프렌드로 설정
```cpp
class Rect;

class RectManager {
public:
	bool equals(Rect r, Rect s);
	void copy(Rect& dest, Rect& src);
};


class Rect {
private:
	int width, height;

public:
	Rect(int width, int heght) {
		this->width = width;
		this->height = heght;
	}

	// RectManager 클래스를 프렌드 함수로 선언
	friend RectManager;
};

bool RectManager::equals(Rect r, Rect s) {
	if (r.width == s.width && r.height == s.height)
		return true;
	else
		return false;
}
void RectManager::copy(Rect& dest, Rect& src) {
	dest.width = src.width;
	dest.height = src.height;
}
```

```cpp
class B;

class A {
public:
   int Func1( B& b );

private:
   int Func2( B& b );
};

class B {
private:
   int _b;

   // A::Func1 is a friend function to class B
   // so A::Func1 has access to all members of B
   friend int A::Func1( B& );
};

int A::Func1( B& b ) { return b._b; }   // OK
int A::Func2( B& b ) { return b._b; }   // C2248
```
- 클래스 멤버로 프렌드 함수가 지정되면 위 코드의 A는 B의 모든 멤버에 접근이 가능하다. 내 안에 지정된 친구는 내 모든 멤버에 접근이 가능하다