#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

static int dx[] = {0, 1, 0, -1};
static int dy[] = {1, 0, -1, 0};
static int A[101][101];
static bool visited[101][101];
static int N,M;
void BFS(int i, int j);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M;
    for(int i{0}; i<N; i++){
        string s;
        cin >> s;
        for(int j{0}; j<M; j++){
            // string to int
            A[i][j] = s[j] - '0';
        }
    }
    BFS(0,0);
    cout << A[N-1][M-1];
    return 0;
}
void BFS(int i, int j){
    queue<pair<int, int>> q;
    q.push(make_pair(i,j));
    while (!q.empty()){
        int now[2];
        now[0] = q.front().first;
        now[1] = q.front().second;
        q.pop();
        visited[i][j] = true;
        for(int k{0}; k<4; k++){
            int x = dx[k] + now[0];
            int y = dy[k] + now[1];
            if(x >= 0 && y>=0 && x<N && y<M){
                if(!visited[x][y] && A[x][y] != 0){
                    visited[x][y] = true;
                    A[x][y] = A[now[0]][now[1]] + 1;
                    q.push(make_pair(x,y));
            }
            }
        }
    }
}