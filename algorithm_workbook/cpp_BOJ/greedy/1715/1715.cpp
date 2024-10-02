#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    priority_queue<int, vector<int>, greater<int>> cards;
    cin >> N;

    for(int i{0}; i<N; i++){
        int tmp;
        cin >> tmp;
        cards.push(tmp);
    }
    int cnt = 0;

    while(!cards.empty()){
        // N 이 1일 경우 메로리 초과 발생.
        // 조건문으로 탈출
        if(N==1){
            break;
        }
        int first = cards.top();
        cards.pop();
        int second = cards.top();
        cards.pop();
        cnt += (first + second);
        if(cards.empty()){
            break;
        }
        cards.push(first+second);
    }
    cout << cnt;
}