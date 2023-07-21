// BST 구현하기
#include <iostream>

struct node
{
    int data;
    node* left;
    node* right;
};

struct bst
{
    node* root = nullptr;
    node* find(int value)
    {
        return find_impl(root,value);
    }
    private:
        node* find_impl(node* current, int value)
        {
            if(!current)
            {
                std::cout << std::endl;
                return NULL;
            }

            if(current->data == value)
            {
                std::cout << value << "을(를) 찾았습니다" << std::endl;
                return current;
                // 현재 노드의 주소값 반환
            }

            if(value < current->data)
            {
                std::cout << current->data << "에서 왼쪽으로 이동" << std::endl;
                return find_impl(current->left, value);
            }

            std::cout << current->data << "에서 오른쪽으로 이동" << std::endl;
            return find_impl(current->right,value);
        }
    public:
        void insert(int value)
        {
            if(!root)
                root = new node {value, NULL, NULL};
            else
                insert_impl(root, value);
        }
    private:
        void insert_impl(node* current, int value)
        {
            if (value < current->data)
            {   
                if(!current->left)
                    current->left = new node {value, NULL, NULL};
                else 
                // 왼쪽에 있는 '객체'를 주소값으로 반환 하는거라 재귀시 current
                // 는 왼쪽에 있는 객체가 되어버림
                // 추가 할 때마다 node형 객체를 생성해 연결하는것
                    insert_impl(current->left,value);
            }
            else
            {
                if(!current->right)
                    current->right = new node {value, NULL, NULL};
                else 
                    insert_impl(current->right,value);
            }
        }
    public:
        void inorder()
        {
            inorder_impl(root);
        }
    private:
        void inorder_impl(node* start)
        {
            if(!start)
                return;
            inorder_impl(start->left);      // 왼쪽 서브 트리 방문
            std::cout << start->data <<" "; // 현재 노드 출력
            inorder_impl(start->right);     // 오른쪽 서브 트리 방문
        }
    public:
        node* successor(node* start)
        {
            auto current = start->right;
            while(current && current->left)
                current = current->left;
            return current;
        }
        void deleteValue(int val)
        {
            root = delete_impl(root, val);
        }
    private :
        node* delete_impl(node* start, int value)
        {
            if(!start)
                return NULL;
            
            if(value < start->data)
                start->left = delete_impl(start->left,value);
            else if(value > start->data)
                start->right = delete_impl(start->right,value);
            else
            {
                if(!start->left)
                {
                    auto tmp = start -> right;
                    delete start;
                    return tmp;
                }
                if(!start->right)
                {
                    auto tmp = start-> left;
                    delete start;
                    return tmp;
                }
                //자식 노드가 둘 다 있을때
                auto succNode = successor(start);
                start->data = succNode->data;

                //오른쪽 서브트리에서 후속을 찾아서 삭제
                start->right = delete_impl(start->right,succNode->data);
            }
            return start;
        }
};   

int main()
{
    bst tree;
    tree.insert(12);
    tree.insert(10);
    tree.insert(20);
    tree.insert(8);
    tree.insert(15);
    tree.insert(1);
    tree.insert(14);
    tree.insert(45);
    tree.insert(2);
    tree.insert(11);
    tree.insert(22);

    std::cout << "중위순회: ";
    tree.inorder();
    std::cout << std::endl;
}