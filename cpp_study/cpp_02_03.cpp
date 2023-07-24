#include<iostream>
#include<queue>
#include<vector>

struct median
{
  // priority_queue -> 기본적으로 내림차순 정렬
  // 데이터가 중앙값보다 작으면 최대 힙에, 크면 최소 힙에 저장
  std::priority_queue<int> maxHeap;
  // 오름차순으로 변경
  std::priority_queue<int, std::vector<int>,std::greater<int>> minHeap;
  
  void insert(int data)
  {
    if(maxHeap.size() == 0)
    {
      maxHeap.push(data);
      return;
    }

    if(maxHeap.size()== minHeap.size())
    {
      if(data <= get())
        maxHeap.push(data);
      else
        minHeap.push(data);

        return ;
    }

    if(maxHeap.size() < minHeap.size())
    {
      if (data > get())
      {
        maxHeap.push(minHeap.top());
        minHeap.pop();
        minHeap.push(data);
      }
      else
        maxHeap.push(data);

      return;
    }

    if(data > get())
    {
      minHeap.push(maxHeap.top());
      maxHeap.pop();
      maxHeap.push(data);
    }
    else
      minHeap.push(data);
  }
  // 중앙값을 반환하는 함수
  double get()
  {
    if(maxHeap.size() == minHeap.size())
      return (maxHeap.top() + minHeap.top()) / 2.0;

    if(maxHeap.size() < minHeap.size())
      return minHeap.top();

    return maxHeap.top();
  }
};

int main()
{
  median med;

  med.insert(1);
  std::cout << "삽입 후 중앙값 : " << med.get() << std::endl;

  med.insert(5);
  std::cout << "삽입 후 중앙값 : " << med.get() << std::endl;

  med.insert(3);
  std::cout << "삽입 후 중앙값 : " << med.get() << std::endl;

  med.insert(7);
  std::cout << "삽입 후 중앙값 : " << med.get() << std::endl;

  med.insert(12);
  std::cout << "삽입 후 중앙값 : " << med.get() << std::endl;
}