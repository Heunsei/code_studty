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
// 다익스트라로 만든 정점까지의 거리를 저장할 배열
int dist[801];
// 노드를 저장하는 그래프
vector<pair<int, int>> graph[801];
// 다익스트라 함수 정의
void dijkstra(int start){
	for(int i = 0; i <= N;i++){
		dist[i] = INF;
	}
	// 시작값을 0으로 초기화
	dist[start] = 0;
	// 우선순위 큐는 기본적으로 내림차순, 오름차순으로 변경
	priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> q;
	// 시작 가중치 / 시작 노드 번호 푸쉬
	q.push({0,start});
	while(!q.empty()){
		// 가중치 / 현재노드 
		int curDist = q.top().first;
		int cur = q.top().second;
		q.pop();
		for(int i = 0; i<graph[cur].size(); i++){
			// 그래프에는 거꾸로 저장 되어 있음
			int next = graph[cur][i].first;
			int nextDist = graph[cur][i].second;
			// 만약 이전에 저장된 dist값이 더 크면 작은걸로 변경
			if(dist[next] > nextDist + curDist){
				dist[next] = nextDist + curDist;
				// 다음 가중치와 좌표를 q에 push
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