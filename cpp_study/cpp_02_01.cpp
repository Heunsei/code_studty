// 트리, 상하 반전
#include<iostream>
#include<queue>
#include<string>

// 구조체 설정
struct node
{
  std::string position;
  node* first;
  node* second;
};

struct org_tree
{
  node* root;
  // 루트 노드를 생성하는 생성자
  static org_tree creat_org_sturcture(const std::string& pos)
  {
    org_tree tree;
    tree.root = new node{pos, NULL, NULL};
    return tree;
  };
  // 노드의 왼쪽부터 순회
  static node* find(node* root, const std::string& value)
  {
    if(root == NULL)
      return NULL;
    
    if(root -> position == value)
      return root;
    
    auto firstFound = org_tree::find(root->first, value);

    if(firstFound != NULL)
      return firstFound;
    
    return org_tree::find(root->second, value);
  }

  // find를 활용해 삽입함수 작성
  bool addSubordinate(const std::string& manager, const std::string& subordinate)
  {
    auto managerNode = org_tree::find(root, manager);
    if(!managerNode)
    {
      std::cout << manager << "을(를)찾을 수 없습니다" << std::endl;
      return false;
    }

    if(managerNode->first && managerNode->second)
    {
      std::cout << manager << "아래에 추가할 수가 없습니다" << std::endl;
      return false;
    }
    
    if(!managerNode -> first)
      managerNode -> first = new node {subordinate, NULL, NULL};
    else
      managerNode -> second = new node {subordinate, NULL, NULL};
    std::cout << manager << "아래에" << subordinate << "를 추가했습니다"
    << std::endl;

    return true;
  }
  // 레벨순회 구현
  static void levelOrder(node* start)
  {
    if(!start)
      return;
    std::queue<node*> q; // FIFO
    q.push(start);

    while(!q.empty())
    {
     int size = q.size();
      for(int i = 0; i < size; i++)
      {
        auto current = q.front();
        q.pop();

        std::cout << current-> position <<", ";
        if(current->first)
         q.push(current->first);
        if(current->second)
         q.push(current->second);
     }
      std::cout << std::endl;
    }
  }
};

int main()
{
  auto tree = org_tree::creat_org_sturcture("CEO");
  tree.addSubordinate("CEO","부사장");
  tree.addSubordinate("부사장","IT부장");
  tree.addSubordinate("부사장","마케팅부장");
  tree.addSubordinate("IT부장", "보안팀장");
  tree.addSubordinate("IT부장", "앱개발팀장");
  tree.addSubordinate("마케팅부장", "물류팀장");
  tree.addSubordinate("마케팅부장", "홍보팀장");
  org_tree::levelOrder(tree.root);
}