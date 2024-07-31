#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

void DFS(int now);
void BFS(int now);
static vector<vector<int>> A;
static vector<bool> visited;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N, M, V;
    cin >> N >> M >> V;
    A.resize(N+1);
    visited = vector<bool>(N+1, false);

    for(int i{0}; i<M; i++){
        int s,e;
        cin >> s >> e;
        A[s].push_back(e);
        A[e].push_back(s);
    }
    for(int i{0}; i<N+1; i++){
        sort(A[i].begin(), A[i].end());
    }
    DFS(V);
    cout << "\n";
    visited.clear();
    visited = vector<bool>(N+1, false);
    BFS(V);

    return 0;
}

void DFS(int now){
    cout << now << " ";
    visited[now] = true;
    for(int i : A[now]){
        if(!visited[i]){
            DFS(i);
        }
    }
}

void BFS(int now){
    queue<int> q;
    q.push(now);
    while(!q.empty()){
        int now = q.front();
        if(!visited[now]){
            cout << now << " ";
        }
        visited[now] = true;
        q.pop();

        for(int i: A[now]){
            if(!visited[i]){
               q.push(i);
            }
        }
    }
}
