#include<iostream>
#include<vector>

// enum클래스의 멤버의 타입을 정해줄 수 있다
enum class city : int
{
  MOSCOW,
  LONDON,
  SEOUL,
  SEATTLE,
  DUBAI,
  SYDNEY
};

// 연산자 정의

std::ostream& operator<<(std::ostream& os, const city c)
{
  switch(c)
  {
    case city::LONDON:
      os << "런던";
      return os;

    case city::MOSCOW:
      os << "모스크바";
      return os;
    
    case city::DUBAI:
      os << "두바이";
      return os;

    case city::SYDNEY:
      os << "시드니";
      return os;
    case city::SEATTLE:
      os << "시애틀";
      return os;
    default:
      return os;
  }
}

struct graph
{
  std::vector<std::vector<int>> data;

  // 생성자
  graph(int n)
  {
    // n만큼의 데이터를 미리 확보를 해 재할당이 일어나지 않도록 한다 
    data.reserve(n);
    // 기본값(0)으로 초기화된 n개만큼의 원소를 가지는 벡터 선언
    std::vector<int> row(n);
    // 벡터를 처음부터 끝까지 -1로 바꿈
    std::fill(row.begin(), row.end(), -1);

    for(int i = 0; i < n; i ++)
    {
      data.push_back(row);
    }
  }

  void addEdge(const city c1, const city c2, int dis)
  {
    std::cout << "에지 추가" << c1 << "-" << c2 << "-" << dis << std::endl;
    auto n1 = static_cast<int>(c1);
    auto n2 = static_cast<int>(c2);
    // 양 방향의 거리를 저장
    data[n1][n2] = dis;
    data[n2][n1] = dis;
  }

  void removeEdge(const city c1, const city c2)
  {
    std::cout << "에지 삭제" << c1 << "-" << c2 << std::endl;
    auto n1 = static_cast<int>(c1);
    auto n2 = static_cast<int>(c2);
    data[n1][n2] = -1;
    data[n2][n1] = -1;
  }
};

int main()
{

}