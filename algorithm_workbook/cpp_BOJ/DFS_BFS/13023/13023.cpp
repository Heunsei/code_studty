#include <iostream>
#include <vector>

using namespace std;

static vector<vector<int>> A;
static vector<bool> visited;
bool isArrived = false;
void DFS(int now, int depth);
int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    int N, M;
    cin >> N >> M;
    A.resize(N);
    visited = vector<bool>(N, false);
    // 인접 리스트를 채워주는 과정
    for(int i{0}; i<M; i++){
        int s,e;
        cin >> s >> e;
        A[s].push_back(e);
        A[e].push_back(s);
    }

    for(int i{0}; i<N; i++){
        DFS(i,1);
        if(isArrived) break;
    }

    if(isArrived){
        cout << 1 << "\n";
    }else{
        cout << 0 << "\n";
    }
    return 0;
}
void DFS(int now, int depth){
    // 이미 도착해있거나 깊이가 5가되면 5명이므로 true로 바꾸고 return
    if(depth == 5 || isArrived){
        isArrived = true;
        return;
    }
    visited[now] = true;
    for(int i : A[now]){
        if(!visited[i]){
            DFS(i, depth+1);
        }
    }
    visited[now] = false;
}