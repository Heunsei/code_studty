#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
 
vector<int> vec[102];
int visit[102];
int maxres, res;
 
void bfs(int a){
  queue<int> q;
  q.push(a);
  visit[a] = 1;
  while (!q.empty()){
    int cur = q.front();
    q.pop();
    for (int i = 0; i < vec[cur].size(); i++){
      int next = vec[cur][i];
      if (visit[next] == 0){
        q.push(next);
        visit[next] = visit[cur] + 1;
        maxres = visit[next];
      }
    }
  }
}
 
int main(void){
  for (int tc = 1; tc <= 10; tc++){
    printf("#%d ", tc);
    memset(visit, 0, sizeof(visit));
    maxres = 0;
    res = 0;
    for (int i = 1; i <= 100; i++)
      vec[i].clear();
 
      int n, s;
      scanf("%d %d ", &n, &s);
 
      for (int i = 0; i < n / 2; i++){
        int a, b;
        scanf("%d %d ", &a, &b);
        vec[a].push_back(b);
      }
      bfs(s);
      for (int i = 1; i <= 100; i++){
        if (maxres == visit[i])
        res = i;
      } 
      printf("%d \n", res);
    }
  return 0;
}