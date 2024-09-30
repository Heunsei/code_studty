#include <iostream>
#include <queue>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    bool arr[101][101] = {false, };
    bool visited[101] = {false, };

    int num;    // 컴퓨터의 수
    int pair;   // 입력받을 짝의 수
    queue<int> q; // 1번부터 들어가 다음 좌표 확인
    cin >> num;
    cin >> pair;
    q.push(1);

    for(int i{0}; i<pair; i++){
        int a,b;
        cin >> a >> b;
        arr[a][b] = true;
        arr[b][a] = true;
    }

    while (!q.empty()){
        int nxt = q.front();
        q.pop();
        visited[nxt] = true;
        for(int i{0}; i<101; i++){
            if(arr[nxt][i] && !visited[i]){
                q.push(i);
            }
        }
        if(visited[nxt]) {
            continue;
        }else {
            visited[nxt] = true;
        }
    }
    int res = 0;
    for(int i{1}; i<=num; i++){
        if(visited[i]){
            // cout << "visited 확인" << i << '\n';
            res++;
        }
    }    
    cout << res-1;
}