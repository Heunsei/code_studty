// BST 구현하기
#include <iostream>

struct node
{
    int data;
    node* left;
    node* right;
};

struct bfs
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
                current = current->left
            return current
        }
}