#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int A[50][50];
bool visited[50][50];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
void BFS(int x, int y);
void init(int x, int y);

int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    int T;
    cin >> T;
    for (int i{0}; i<T; i++){
        int x_len, y_len, K;
        cin >> x_len >> y_len >> K;
        init(x_len, y_len);
        // 배추 위치 입력
        for(int j{0}; j<K; j++){
            int n,m;
            // x좌표 y좌표 순서
            cin >> n >> m;
            A[m][n] = 1;
        }
        BFS(x_len, y_len);
    }
    return 0;
}

void BFS(int x, int y){
    int cnt = 0;
    queue<pair<int,int>> q;
    for(int i{0}; i<y; i++){
        for(int j{0}; j<x; j++){
            if(A[i][j] == 1 && !visited[i][j]){
                q.push(make_pair(j,i));
                visited[i][j] = true;
                while(!q.empty()){
                    pair<int,int> now = q.front();
                    visited[now.second][now.first] = true;
                    q.pop();
                    for(int v{0}; v<4; v++){
                        int nx = now.first + dx[v];
                        int ny = now.second + dy[v];
                        if(A[ny][nx] == 1 && !visited[ny][nx] && nx>=0 && ny>=0 && nx<x && ny<y){
                            q.push(make_pair(nx,ny));
                            visited[ny][nx] = true;
                        }
                    }
                }
                cnt++;
            }
        }
    }
    cout << cnt << "\n";
}

void init(int x, int y){
    for(int i{0}; i<y; i++){
        for(int j{0}; j<x; j++){
            A[i][j] = 0;
            visited[i][j] = false;
        }
    }
}