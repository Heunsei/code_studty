#include <iostream>
#include <vector>
#include <queue>

using namespace std;
#define INF 1e9

int N, M, K, X;
// 거리를 저장할 노드들
int d[3000001]; 
// 간선 정보를 저장할 그래프
// 입력값에 가중치가 없으니 int만 저장하는 vector 선언
vector<int> graph[300001];

// 최단거리가 K인 모든 도시들의 번호를 한줄에 하나씩 오름차순으로 출력
void dijkstra(int start){
    // 시작지점 가중치를 0으로설정
    d[start] = 0;
    queue<int> q;
    q.push(start);
    while(!q.empty()){
        // 좌표 가져오기
        int current = q.front();
        q.pop();
        // 현재 좌표에서 연결할 수 있는 노드들을 next로 받아와 비교
        for(int i=0; i<graph[current].size(); i++){
            int next = graph[current][i];
            // 다음값이 이전값을 1더한거보다 더 크면 이 길이 더 짧은거니 거리를 저장
            if(d[next]>d[current]+1){
                d[next] = d[current]+1;
                q.push(next);
            }
        }
    }
}

int main(){
    // 도시의 개수 N, 도로의 개수 M, 거리정보 K, 출발 도시의 번호 X
    cin >> N >> M >> K >> X;
    // 거리를 모두 INF로 초기화
    for(int i{1}; i<=N; i++){
        d[i] = INF;
    }
    for(int i{0}; i<M; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
    }
    dijkstra(X);
    // 도착 가능한지 확인하는 check
    bool check = false;
    for(int i=1; i<=N; i++){
        if(d[i]==K){
            cout << i << endl;
            check = true;
        }
    }
    // 도착 못했으면 -1 출력
    if(!check)  cout << "-1";
    return 0;
}