#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
#define INF 987654321

int N, M;
vector<pair<int,int>> graph[50'001];
int dist[50'001];

void input(){
    std::cin >> N >> M;
    for (int i{0}; i<N+1; i++){
        // 거리를 INF로 초기화
        dist[i] = INF;
    }

    for(int i{0}; i<M; i++){
        int a, b, c;
        std::cin >> a >> b >> c;
        graph[a-1].push_back({b-1, c});
        graph[b-1].push_back({a-1, c});
    }
}

int solve(int start, int end){
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    // 시작 가중치 0, 시작 좌표 입력
    pq.push({0, start});
    dist[start] = 0;
    while(!pq.empty()){
        int c_cost = pq.top().first;
        int c_pos = pq.top().second;

        if(c_pos == end-1) return c_cost;
        pq.pop();

        if(c_cost > dist[c_pos]) continue;
        for (int i{0}; i<graph[c_pos].size(); i++){
            int next_pos = graph[c_pos][i].first;
            int next_cost = graph[c_pos][i].second;

            if (dist[next_pos] > next_cost + c_cost){
                dist[next_pos] = next_cost + c_cost;
                pq.push({dist[next_pos], next_pos});
            }
        }
    }
    return -1;
}

int main(){
    ios_base::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);
    
    input();
    std::cout << solve(0, N) << std::endl;
    return 0;
}