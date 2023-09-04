// std::list 삽입 또는 삭제 함수 사용
#include<iostream>
#include<list>

int main()
{
  std::list<int> list1 = {1, 2, 3, 4, 5};
  list1.push_back(6);
  list1.insert(next(list1.begin()), 0); // 첫원소 뒤에 0삽입
  list1.insert(list1.end(), 7);

  list1.pop_back();
}