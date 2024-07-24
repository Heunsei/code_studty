#include <iostream>
#include <vector>
using namespace std;
static vector<vector<int>> A;
static vector<bool> visited;
void DFS(int v);
int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    int N, M;

    std::cin >> N >> M;
    A.resize(N+1);
    visited = vector<bool>(N+1,false);
    for(int i{0};i <M; i++){
        int u,v;
        std::cin >> u >> v;
        A[u].push_back(v);
        A[v].push_back(u);
    }
    int count = 0;
    for(int i{1}; i<N+1; i++){
        if(!visited[i]){
            count ++;
            DFS(i);
        }
    }
    cout << count << "\n";
    return 0;
}

void DFS(int v){
    if(visited[v]){
        return;
    }
    visited[v] = true;
    for(int i: A[v]){
        if(visited[i]==false){
            DFS(i);
        }
    }
}