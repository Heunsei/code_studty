#include <iostream>
#include <vector>

using namespace std;

int K;
int input[10024];
vector<int> tree[10];

void inorder(int depth, int start, int end){
    if(start>=end) return;
    int mid = (start + end) / 2;
    tree[depth].push_back(input[mid]);
    inorder(depth+1, start, mid);
    inorder(depth+1, mid+1, end);
}

int main(){
    std::cin >> K;
    int num;
    int index = 0;
    while(cin >> num){
        input[index++] = num;
    }
    inorder(0,0,index);
    for(int i{0}; i<K; i++){
        for(auto node:tree[i]){
            std::cout << node << ' ';
        }
        std::cout << '\n';
    }
}