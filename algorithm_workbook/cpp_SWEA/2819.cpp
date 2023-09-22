#include <iostream>
#include <set>
#include <string>

using namespace std;

char board[4][4];
set<string> s;
int T, tc;
int result;
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};

void dfs(int x, int y, int cnt ,string num){
  if(cnt == 7){
    s.insert(num);
    return;
  }
  for(int k=0;k<4;k++){
    int nx = x + dx[k];
    int ny = y + dy[k];
    if(nx<0 || nx >=4 || ny<0 || ny >=4) continue;
    dfs(nx,ny,cnt+1,num+board[nx][ny]);
  }
}


int main(){
  cin >> T;
  for(tc=1; tc<=T; tc++){
    s.clear();
    for(int i=0; i<4; i++){
      for(int j=0; j<4; j++){
        cin >>board[i][j];
      }
    }
    for(int x=0; x<4; x++){
      for(int y=0; y<4; y++){
         dfs(x,y,0,"");
        }
      }
    cout << '#' << tc << ' ' << s.size() << endl;
    }
  return 0;
}