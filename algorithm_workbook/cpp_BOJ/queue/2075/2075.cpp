#include <iostream>
#include <queue>

using namespace std;

int N;
priority_queue<int, vector<int>, greater<int>> q;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    std::cin >> N;
    int temp;
    for(int i{0}; i<N*N; i++){
        std::cin >> temp;
        q.push(temp);
        if(q.size() > N) q.pop();
    }
    std::cout << q.top();
    return 0;
}