#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    int N;
    cin >> N;
    queue<int> q;
    for(int i{1}; i<=N; i++){
        q.push(i);
    }

    while(q.size()!=1){
        int first = q.front();
        q.pop();
        cout << first << " ";
        int sec = q.front();
        q.pop();
        q.push(sec);
    }
    cout << q.front();

    return 0;
}
