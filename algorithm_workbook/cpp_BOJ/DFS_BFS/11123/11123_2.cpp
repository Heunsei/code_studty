# include <iostream>
# include <queue>

using namespace std;

const int MAX = 101;
int T, H, W;
queue<pair<int, int>> q;
int graph[MAX][MAX];
int visited[MAX][MAX];
int di[] = {0, 1, 0, -1};
int dj[] = {1, 0, -1, 0};
int cnt = 0;


void BFS(int i, int j){
  visited[i][j] = true;
  q.push(make_pair(i, j));
  while(!q.empty()){
    int a = q.front().first;
    int b = q.front().second;
    q.pop();
    for(int k = 0; k < 4; k++){
      int ni = a + di[k];
      int nj = b + dj[k];
      if(ni < 0 || nj < 0 || ni >= H || nj >= W) continue;
      if(!visited[ni][nj] && graph[ni][nj] == 1){
        visited[ni][nj] = true;
        q.push(make_pair(ni,nj));
      }       
    }
  }
}

void reset(){
  for(int i{0}; i<MAX; i++){
    for(int j{0}; j<MAX; j++){
      graph[i][j] = 0;
      visited[i][j] = 0;
    }
  }
  cnt = 0;
}

int main(){
  cin >> T;
  for(int tc{0}; tc < T; tc++){
    // 높이 너비
    cin >> H >> W;

    for(int i{0}; i<H; i++){
      for(int j{0}; j<W; j++){
        char x;
        cin >> x;
        if(x=='#') graph[i][j] = 1;
        else graph[i][j] = 0;
      }
    }

    for(int i{0}; i<H; i++){
      for(int j{0}; j<W; j++){
        if(!visited[i][j] && graph[i][j] == 1){
          BFS(i,j);
          cnt++;
        }
      }
    }
    cout << cnt << endl;
    reset();
  }
}