#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

int V, E, from, to, cost;
int u, v, w;
long long ans;
bool visit[10001];
vector<pair<int, int>> graph[10001];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // 오름차순 우선순위 큐

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

    // 간선 정보 저장
	cin >> V >> E;
    // graph에 간선정보들 저장 i번째 vector에 {next, cost저장}
	for (int i = 0; i < E; i++)
	{
		cin >> from >> to >> cost;
		graph[from].push_back(make_pair(to, cost));
		graph[to].push_back(make_pair(from, cost));
		// graph[to].emplace_back(from, cost);
	}

	pq.push(make_pair(0, 1)); // 가중치는 0, 1번 노드부터 시작

	while (!pq.empty())
	{   
		int now_weight = pq.top().first;
		int now_node = pq.top().second;
		pq.pop();

		// 방문체크
		if (visit[now_node]) continue;

		visit[now_node] = true; // 방문 표시

		ans += now_weight;  // 현재 가중치 값 추가

		// 다음 정점들을 우선순위 큐에 삽입
        // 현재 노드에있는 간선의 개수만큼 for문 진행, first는 다음 노드 위치 second는 가중치
		for (int i = 0; i < graph[now_node].size(); i++)
		{
			int next_node = graph[now_node][i].first;
			int next_weight = graph[now_node][i].second;

			pq.push(make_pair(next_weight, next_node));
		}
	}
	cout << ans << '\n';
}