#include <iostream>
#include <vector>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

vector<int> a[102];
int visited[102];
int max_res, res;

void bfs(int start){
  // bfs를 사용할 queue 선언
  queue<int> q;
  // 맨처음 방문 정점 삽입
  q.push(start);
  // 맨처음을 1로놓고 visited 기록 시작
  visited[start] = 1;
  while(!q.empty()){
    // q.front로 접근해서 값을 받아옴
    // pair 형식으로 선언했으면 first, second등으로 접근가능
    // 여기있는 배열은 일단 쭉늘어진 리스트의 연속이라 생각하자
    int current = q.front();
    // 삭제
    q.pop();
    // a의 현재 방문 정점의 연결 노드들을 전부 확인하는 과정
    for(int i=0; i<a[current].size(); i++){
      int next = a[current][i];
      // 방문 안했으면
      if(visited[next] == 0){
        // queue에 다음 목적지를 넣어주고
        q.push(next);
        // visited에 값 누적
        visited[next] = visited[current] + 1;
        // 얼마나 멀리까지 갔는지 기록
        max_res = visited[next];
      }
    }
  }
}

int main(){
  for(int tc=1; tc<11; tc++){
    printf("#%d ", tc);
    // visited 의 멤버를 모두 0으로 초기화
    memset(visited, 0, sizeof(visited));
    max_res = 0;
    res = 0;
    // 벡터 a를 초기화
    // 벡터를 쓰는것은 빈 이중리스트만들어서 append 하는거랑 비슷하다
    // 생각하면 될거같다
    for(int i{0}; i<=100; i++) a[i].clear();
    // 주어질 연결 정점들의 갯수, bfs를 시작해야할 시작점을 선언    
    int n, start;
    cin >> n >> start;
    // 벡터s에 넣어주기.
    // push_back > append랑 비슷하게 이해해두자
    for(int i{0}; i<n/2; i++){
      int s, e;
      cin >> s >> e;
      a[s].push_back(e);
    }
    bfs(start);
    // 누적해둔 방문 정점들을 모두 찾고 max_res랑 누적값이 같으면 res를 바꿔줌
    for(int i = 0; i<=100; i++){
      if(visited[i] == max_res)
        res = i;
    }
    printf("%d \n",res);
  }
}