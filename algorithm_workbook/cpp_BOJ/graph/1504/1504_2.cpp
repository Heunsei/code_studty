#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

const int INF =  987654321;
int N, E, v1, v2, res = INF;
int to_v1,v1_to_n, v1_v2, to_v2, v2_to_n;
int course1, course2;
int dist[801];
vector<pair<int, int>> graph[801];

void dijkstra(int start){
	for(int i = 0; i <= N;i++){
		dist[i] = INF;
	}
	dist[start] = 0;
	priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> q;
	q.push({0,start});
	while(!q.empty()){
		int cur = q.top().second;
		int curDist = q.top().first;
		q.pop();
		for(int i = 0; i<graph[cur].size(); i++){
			int next = graph[cur][i].first;
			int nextDist = graph[cur][i].second;
			if(dist[next] > nextDist + curDist){
				dist[next] = nextDist + curDist;
				q.push({dist[next],next});
			}
		}
	}
}

int main(){
	cin >> N >> E;
	while(E--){
		int a,b,c;
		cin >> a >> b >> c;
		graph[a].push_back({b,c});
		graph[b].push_back({a,c});	
	}
	cin >> v1 >> v2;

	dijkstra(1);
	to_v1 = dist[v1];
	to_v2 = dist[v2];

	dijkstra(v1);
	v1_to_n = dist[N];
	v1_v2 = dist[v2];

	dijkstra(v2);
	v2_to_n = dist[N];

	course1 = to_v1 + v1_v2 + v2_to_n;
	course2 = to_v2 + v1_v2 + v1_to_n;
	res = (course1 >= course2) ? course2 : course1;
	if(v1_v2>=INF || course2>=INF) cout << -1;
	else cout << res ;

}