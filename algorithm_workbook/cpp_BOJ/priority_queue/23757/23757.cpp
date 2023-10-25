#include <iostream>
#include <iterator>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
std::priority_queue<int> present;
std::priority_queue<int> children;


int main(){

    std::cin >> N >> M;
    
    for(int i{0}; i<N; i++){
        int a;
        cin >> a;
        present.push(a);
    }



    return 0;
}