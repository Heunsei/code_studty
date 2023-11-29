#include <iostream>
#include <queue>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N; // 1번부터 N번까지 번호가 붙어있음. 1번카드가 맨위에 N번카드가 맨아래 위치
    // 맨위에 있는 카드를 버리고 제일 위에있는 카드를 제일 아래에 있는 카드로 이동
    // 카드가 한장 남을 때 까지 반복
    queue<int> q;
    cin >> N;
    for(int i{1}; i<=N; i++){
        q.push(i);
    }

    while (q.size() > 1){
        q.pop();
        q.push(q.front());
        q.pop();
    }

    cout << q.front();

    return 0;
}