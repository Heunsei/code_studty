#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
// BOJ - 18352
// 특정 거리의 도시 찾기
vector<int> search (vector<vector<int>> &graph, int start, int size);
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    // 도시의 개수, 도로의 개수, 거리정보, 출발 도시 번호
    int N, M, K, X;
    cin >> N >> M >> K >> X;
    vector<vector<int>> graph(N+1);
    for(int i{0}; i<M; i++){
        int A, B;
        cin >> A >> B;
        graph[A].push_back(B);
    }
    for(auto i : graph){
        sort(i.begin(), i.end());
    }
    vector<int> pass = search(graph, X, N);
    bool isNone = true;
    for(int i{1}; i<N+1; i++){
        if(pass[i] == K){
            isNone = false;
            cout << i << '\n';
        }
    }
    if(isNone) cout << -1;
}

vector<int> search (vector<vector<int>> &graph, int start, int size) {
    vector<int> dis_from_start(size+1, -1);
    queue<int> q;
    q.push(start);
    dis_from_start[start] = 0;
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        for(int nxt : graph[cur]){
            if(dis_from_start[nxt] == -1){
                dis_from_start[nxt] = dis_from_start[cur]+1;
                q.push(nxt);
            }
        }
    }
    return dis_from_start;
}