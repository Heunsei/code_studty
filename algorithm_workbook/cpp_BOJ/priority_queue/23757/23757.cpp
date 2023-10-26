#include <iostream>
#include <iterator>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
std::priority_queue<int> present;

int main(){

    std::cin >> N >> M;
    
    for(int i{0}; i<N; i++){
        int a;
        cin >> a;
        present.push(a);
    }

    bool isPass = true;

    for(int i{0}; i<M; i++){
        int child;
        cin >> child;

        if(present.top()>=child){
            present.push(present.top() - child);
            present.pop();
        }
        else isPass = false;
    }
    cout << (isPass ? 1 : 0);
    return 0;
}