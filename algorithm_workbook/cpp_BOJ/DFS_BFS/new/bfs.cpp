#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int, int> edge;
static vector<vector<edge>> A;
static vector<bool> visited;
static vector<int> m_distance;
void BFS(int node);

int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    
    int V;
    std::cin >> V;
    A.resize(V+1);
    for(int i{0}; i<V; i++){
        int S;
        std::cin >> S;
        while(true){
            int E,V;
            std::cin >> E;
            if(E == -1){
                break;
            }
            std::cin >> V;
            A[S].push_back(edge(E,V));
        }
    }
    m_distance = vector<int>(V+1,0);
    visited = vector<bool>(V+1, false);
    BFS(1);
    int MAX = 1;
    for(int i{2}; i<=V; i++){
        if(m_distance[MAX] < m_distance[i]){
            MAX = i;
        }
    }
    fill(m_distance.begin(), m_distance.end(),0);
    fill(visited.begin(), visited.end(), false);
    BFS(MAX);
    sort(m_distance.begin(), m_distance.end());
    std::cout << m_distance[V] << "\n";
    return 0;
}

void BFS(int index){
    queue<int> q;
    q.push(index);
    visited[index] = true;
    while(!q.empty()){
        int now = q.front();
        q.pop();
        for(edge i: A[now]){
            if(!visited[i.first]){
                visited[i.first] = true;
                q.push(i.first);
                m_distance[i.first] = m_distance[now] + i.second;
            }
        }
    }
}