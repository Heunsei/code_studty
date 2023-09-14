#include <stdio.h>
#include <vector>
#include <queue>
#define INF 987654321
using namespace std;

int n,e,v1,v2;
int a,b,c;
// 노드에 인접영역과 가중치를 저장
vector<pair<int,int>>node[805];
int value[805];
priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>> >pq;
// 다익스트라를 p1에 대해 p2에 대해 두번 돌리면 된다
// 그 거리값을 value에 저장
void Dij(int k){
	for(int i=1;i<=n;i++)
		value[i] = INF;
	value[k] = 0;
	pq.push(make_pair(0,k));
	// pq는 vector > 크기가 안정해져있음
	while(!pq.empty()){
		// pair 자료구조의 첫번째 두번째를 X, U에 저장
		// X는 거리값, U는 두번째 정점
		int X = pq.top().first;
		int U = pq.top().second;
		pq.pop();
		
		for(int i=0;i<node[U].size();i++){
			// 이어진 간선과 가중치가 저장된 node에서 값을 추출
			// u번째 노드의 요소들을 돌면서 value에 최소값을 갱신
			int V = node[U][i].first;
			int W = node[U][i].second;
			if(X+W<value[V]){
				value[V] = X+W;
				pq.push(make_pair(value[V],V));
			}
		}
	}
}

int main(){	
	scanf("%d %d",&n,&e);
	
	for(int i=0;i<e;i++){
		scanf("%d %d %d",&a,&b,&c);
		node[a].push_back(make_pair(b,c));
		node[b].push_back(make_pair(a,c));
	}
	
	scanf("%d %d",&v1,&v2);
	
	long long int v1_1,v1_v2,v1_n,v2_1,v2_n;
	
	Dij(v1);
	v1_1 = value[1];
	v1_v2 = value[v2];
	v1_n = value[n];
	Dij(v2);
	v2_1 = value[1];
	v2_n = value[n];
	
	long long int ans1 = v1_1 + v1_v2 + v2_n;
	long long int ans2 = v2_1 + v1_v2 + v1_n;
	long long int ans = ans1 < ans2 ? ans1 : ans2;
	
	if(ans>=INF) ans = -1;
	
	printf("%lld",ans);
	
	return 0;
}