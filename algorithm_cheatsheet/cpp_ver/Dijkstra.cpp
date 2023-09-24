# include <vector>
# include <iostream>
# include <queue>

# define MAX 100 // 최대 정점의 개수
# define INF 99999999

using namespace std;

vector<int> dijkstra(int start, int V, vector<pair<int,int>> adj[]){
  vector<int> dist(V,INF); // vector dist의 원소 V개를 INF로 초기화
  priority_queue<pair<int, int>> pq;

  dist[start] = 0;
  pq.push(make_pair(0, start));

  while (!pq.empty()){
    // 우선순위 큐는 내림차순
    int cost = -pq.top().first;
    int current = pq.top().second;
    pq.pop();

    // 현재 방문한 정점의 주변 탐색
    for (int i {0}; i < adj[current].size(); i++){
      int next = adj[current][i].first;           // 조사할 다음 정점
      int nCost = cost + adj[current][i].second;  // 방문한 정점을 거쳐서 갔을때의 거리
      if (nCost < dist[next]){  // 기존 비용보다 작으면
        dist[next] = nCost; // 갱신
        pq.push(make_pair(-nCost,next));    //pq에 저장
      }
    }
  }
  return dist;
}

int main()
{
  int V,E;
  vector<pair<int,int>> adj[MAX];
  cout << "정점의 개수 입력 : ";
  cin >> V;
  cout << "간선의 개수 입력 : ";
  cin >> E;

  for (int i = 0; i < E; i++){
    int from, to, cost;
    cout << "그래프 입력 [정점 , 정점 가중치] : ";
    cin >> from >> to >> cost;
    adj[from].push_back(make_pair(to,cost));
    adj[to].push_back(make_pair(from, cost));
  }

  printf("\n===다익스트라결과===\n");
  vector<int> dist = dijkstra(0,V,adj);
  for (int i = 0; i < V; i++){
    printf("0번 정점에서 %d번 정점까지 최단거리 : %d\n",i, dist[i]);
  }
  return 0;
}
  