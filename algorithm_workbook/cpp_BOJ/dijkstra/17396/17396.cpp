#include <iostream>
#include <vector>
#include <queue>
#define INF 10000000000000;

using namespace std;

int N, M;
int ward[100'000];
vector<pair<long long, int>> graph[100'000];
long long dist[100'000];


long long dijkstra(int cost, int start){
    priority_queue<pair<long long, int>, vector<pair<long long,int>>, greater<pair<long long, int>>> pq;
    pq.push({cost, start});
    dist[start] = 0;
    while(!pq.empty()){
        long long cost = pq.top().first;
        int current = pq.top().second;
        if(current == N-1) return dist[current];
        pq.pop();

        if(cost>dist[current]) continue;

        for(int i{0}; i<graph[current].size(); i++){
            long long next_cost = graph[current][i].first;
            int next_node = graph[current][i].second;
            if(dist[next_node] > (long long)next_cost + (long long)cost){
                dist[next_node] = (long long)next_cost + (long long)cost;
                pq.push({dist[next_node], next_node});
            }
        }
    }
    return -1;
}


int main(){
   std::cin >> N >> M;
   for(int i{0}; i<N; i++){
        std::cin >> ward[i];
        dist[i] = INF; 
   }

    for(int i{0}; i<M; i++){
        int start, end, acc;
        std::cin>> start >> end >> acc;
        // 와드에 안걸려야하고, 
        if((!ward[start] && !ward[end]) || (start == N-1 || end == N-1)){
            graph[start].push_back({acc, end});
            graph[end].push_back({acc, start});
        }
    }
    std::cout << dijkstra(0,0);
}