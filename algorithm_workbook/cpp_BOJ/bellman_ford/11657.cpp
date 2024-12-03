#include<iostream>
#include<vector>
#include<tuple>
#include<algorithm>
#include<limits.h>
using namespace std;

typedef tuple<int, int, int> edge;
static vector<long> dist;
static vector<edge> edges;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N, M;
    // 도시의 개수
    // 버스 노선의 개수
    cin >> N >> M;
    dist.resize(N+1);
    std::fill(dist.begin(), dist.end(), LONG_MAX);
    
    for(int i{0}; i<M; i++){
        int s,e,w;
        cin >> s >> e >> w;
        edges.push_back({s,e,w});
    }
    dist[1] = 0;
    // 최초 기록 반복은 정점의 개수 - 1 만큼
    for(int i{0}; i<N; i++){
        for(int j{0}; j<M; j++){
            edge data = edges[j];
            int start = get<0>(data);
            int end = get<1>(data);
            int time = get<2>(data);
            if(dist[start] != LONG_MAX && dist[end] > dist[start] + time) {
                dist[end] = dist[start] + time;
            }
        }
    }
    // for(auto i : dist){
    //     cout << i << " ";
    // }
    bool isCicle = false;
    for(int j{0}; j<M; j++){
        edge data = edges[j];
        int start = get<0>(data);
        int end = get<1>(data);
        int time = get<2>(data);
        if(dist[start] != LONG_MAX && dist[end] > dist[start] + time) {
            isCicle = true;
        }
    }
    if(isCicle){
        cout << "-1";
    } else {
        for(int i{2}; i<N+1; i++){
            if(dist[i] == LONG_MAX) cout << "-1" << '\n';
            else cout << dist[i] << '\n';
        }
    }
}
