#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

typedef pair<int,int> info;
vector<vector<info>> A;
vector<bool> visited;
// 시작 정점에서부터 해당 정점까지의 거리를 기록할 vector
vector<int> a_distance;
void BFS(int node);
int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);std::cout.tie(NULL);
    
    // 입력 정점
    int V;
    std::cin >> V;
    A.resize(V+1);
    // 입력 정점 저장
    for(int i{0}; i<V; i++){
        int S;
        cin >> S;
        while(true){
            int n,m;
            cin >> n;
            if(n == -1){
                break;
            }
            cin >> m;
            A[S].push_back(make_pair(n,m));
        }
    }
    visited = vector<bool>(V+1, false);
    a_distance = vector<int>(V+1, 0);
    int MAX = 1;
    BFS(1);
    for(int i{2}; i<=V; i++){
        if(a_distance[MAX]<a_distance[i]){
            MAX = i;
        }
    }
    fill(visited.begin(), visited.end(), false);
    fill(a_distance.begin(), a_distance.end(), 0);
    BFS(MAX);
    sort(a_distance.begin(), a_distance.end());
    cout << a_distance[V] << "\n";
    return 0;
}
void BFS(int index){
    queue<int> q;
    q.push(index);
    visited[index] = true;
    while(!q.empty()){
        int now = q.front();
        q.pop();
        for(auto i : A[now]){
            if(!visited[i.first]){
                visited[i.first] = true;
                q.push(i.first);
                a_distance[i.first] = a_distance[now] + i.second;
            }
        }
    }
}