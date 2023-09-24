#include <iostream>
#include <vector>
#include <queue>

using namespace std;
#define INF 1e9

int N, M, K, X;
int d[3000001]; 
vector<int> graph[300001];

void dijkstra(int start){
    d[start] = 0;
    queue<int> q;
    q.push(start);
    while(!q.empty()){
        int current = q.front();
        q.pop();
        for(int i=0; i<graph[current].size(); i++){
            int next = graph[current][i];
            if(d[next]>d[current]+1){
                d[next] = d[current]+1;
                q.push(next);
            }
        }
    }
}

int main(){
    cin >> N >> M >> K >> X;
    for(int i{1}; i<=N; i++){
        d[i] = INF;
    }
    for(int i{0}; i<M; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
    }
    dijkstra(X);
    bool check = false;
    for(int i=1; i<=N; i++){
        if(d[i]==K){
            cout << i << endl;
            check = true;
        }
    }
    if(!check)  cout << "-1";
    return 0;
}