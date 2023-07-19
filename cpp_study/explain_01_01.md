# 연속된 자료 구조와 연결된 자료 구조
## 1. 연속된 자료구조
- 모든 원소를 단일 메모리 chunk에 저장한다, 원소들은 모두 같은 타입을 사용 
첫 메모리 주소를 시작 주소(BA)라 칭하고 두번 째 원소의 위치는 BA + sizeof(type)이다, i 번째 원소에 접근하려면 BA + i + sizeof(type)사용

- 배열의 유형엔 크게 정적 배열과, 동적 배열이 존재한다. 정적 배열은 선언된 블록이 끝나면 소멸되지만
동적 배열은 생성 시점과 해제 시점을 자유롭게 결정 가능.

### 1. 정적 배열은 int arr[size]; 의 형태로 나타냄
### 2. C에서 동적 배열은 int* arr = (int*)malloc(size * sizeof(int)); 형태로 선언
### 3. cpp에서 동적 배열은 int* arr = new int[size];로 선언

- 정적 배열은 스택 메모리에 할당 -> 함수를 벗어나면 자동으로 해제
- 동적 배열은 힙 메모리에 할당 -> 사용자가 직접 해제하기 전 까지 유지
- 캐시 지역성, 하나의 원소에 접근할 때, 그 옆에 있는 원소 몇개도 캐시로 가져옴

## 2. 연결된 자료구조
- 연결된 자료구조는 node라 하는 여러개의 청크에 데이터를 저장, 연결 리스트의 기본 구조에서 각각의 노드는 저장할 데이터와 다음 노드를 가르키는 포인터를 가지고 있음. 맨 마지막 노드는 자료의 끝을 나타내는 NULL을 가짐.

- 특정 원소에 접근 하려면 head부분 부터 next포인터를 따라 이동해야함
원소 접근 시간은 노드 개수에 비례하며 시간 복잡도로 O(n)

- 연결 리스트에서 새 원소를 추가 하려면 각 node의 next포인터를 수정해야함
원소가 메모리에 연속적으로 저장된 것이 아니라서 캐시 지역성을 기대하긴 힘듬

## 3. std :: array
```bash
# 크기가 10인 int 타입 배열
std::array<int, 10> arr1;

arr1[0] = 1;
std::cout << "arr1 배열의 첫 원소 : " << arr1[0] << std::endl;

std::arrt<int, 4> arr2 = {1, 2, 3, 4};
std::cout << "arr2의 모든 원소";

for(int i = 0 ; i < arr2.size(); i++)
{
    std::cout << arr2[i] << " ";
}
std::cout << std::endl;

# 출력>> arr1 배열의 첫 번쨰 원소 : 1 ;
# 출력>> arr2의 모든 원소 : 1 2 3 4  
# [] 연산자 또는 .at(offset)으로 원소 접근 가능

# 배열을 차례대로 접근하는 경우, 
std::arr<int, 5> arr3 = {1, 3, 5, 7, 9};
for(auto element : arr3)
    std::cout << element <<' ';

for(auto it = arr.begin(); it != arr.end(), it++)
{
    auto element =(*it);
    std::cout << element << ' ';
}
```

## 4. std::vector
### 4-1. array의 단점을 보완한 자료구조
- std::array의 크기는 컴파일 시간에 결정되는 상수여야함.
- std::array는 크기가 고정되어 있어 원소를 추가하거나 삭제할 수 없음.
- std::array는 항상 스택 메모리를 사용
```cpp
// 벡터 선언
std::vector<int> vec;                   //크기가 0인 벡터
std::vector<int> vec = {1, 2, 3, 4, 5}; //지정 초기값으로 선언된 벡터
std::vector<int> vec(10);               //크기가 10인 벡터
std::vector<int> vec(10,5);             //크기가 10이고 모든원소가 5

// 원소 추가
push_back(val):
    if size < capacity
// 마지막 원소를 다음에 val 저장
// 벡터크기 증가
// return;
vec.insert(int begin(),0); // 맨 앞에 0 추가
vec.insert(find(vec.begin(), vec.end(), 1),4); // 1앞에 4추가

if vector is already full
// 2 * size 만큼 메모리 새로 할당
// 새로 할당한 메모리로 기존 원소 전부 복사/이동
// 데이터 포인터를 새로 할당한 메모리 주소로 지정
// 마지막 원소 다음에 val을 저장하고 벡터 크기를 1만큼 증가

pop_back() // 맨 마지막 원소 제거
earse(vec.begin()) or erase(vec.begin() + 1 , vec.begin() + 4);
clear() // 모든 원소 삭제
shrink_to_fit() //여분 메모리 해제
```
### 4-2  std::vector 할당자
- 할당자는 메모리 할당과 해제,그 동작에서 데이터를 손상시키지 않도록 주의해야함

### 5. std::forward_list
- 연결자료 구조, forward_list는 첫 원소를 제외한 나머지 원소에 직접 접근하는것을 허락하지않음
### 5-1 원소 삽입 및 삭제
```cpp
std::forward_list<int> fwd_list = {1, 2, 3};
fwd_list.push_front(0); // 맨 앞에 0추가
auto it = fwd_list.begin();
fwd_list.insert_after(it, 5); /맨 처음 원소 뒤에 5추가
fwd_list.insert_after(it, 6); /맨 처음 원소 뒤에 5추가, it 위치가 변하는 듯 함
```

```cpp
std::forward_list<int> fwd list = {1, 2, 3};
fwd_list.pop_front(); // 맨앞 원소 삭제
it = fwd.list.begin();
fwd_list.erase_after(it); // 맨 앞 다음 원소 삭제
fwd_list.erase_after(it,fwd_list.end());
remove() // 등호 연산이 지원되어야 사용 가능
remove_if() // 조건자 사용으로 true를 반환하는 데이터를 삭제
```

## 5-2 정령 sort()
```cpp
list1.sort(); // 오름 차순
list1.sort(std::greater<int>); // 내림 차순으로 변경
list1.reverse() // 역순 정령
list1.unique() // 붙어있는 원소끼리 같은지 판단후 삭제
list1.unique([](int a, int b){return (b-a)-2;});
// 앞 원소 보다 2 이상 크지 않으면 삭제
```