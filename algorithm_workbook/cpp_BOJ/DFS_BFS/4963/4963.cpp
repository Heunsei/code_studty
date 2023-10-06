// BOJ 4963 섬의 개수
#include <iostream>
#include <array>
#include <cstring>
#include <queue>

using namespace std;

int w, h;
int graph[51][51];
bool visited[51][51];
std::array<int,8> dx = {0, 1, 0, -1, -1, 1, -1, 1};
std::array<int,8> dy = {1, 0, -1, 0, 1, 1, -1, -1};
queue<pair<int, int>> q;

void bfs(){
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int i{0}; i<8; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx <= 0 || ny <= 0 || nx > h || ny > w)
                continue;
            if(graph[nx][ny] && !visited[nx][ny])
                q.push({nx,ny});
                visited[nx][ny] = true;
        }
    }
}


int main(){
    while(true){
        std::cin >> w >> h;
        int ans = 0;
        
        if(!w && !h) break;

        for(int i{1}; i<=h; i++){
            for(int j{1}; j<=w; j++){
                std::cin >> graph[i][j];
            }
        }

        for(int i{1}; i<=h; i++){
            for(int j{1}; j<=w; j++){
                if(!visited[i][j] && graph[i][j]){
                    q.push({i,j});
                    visited[i][j] = true;
                    bfs();
                    ans ++;
                }
            }
        }
        std::cout << ans << std::endl;
        memset(visited, 0, sizeof(visited));
    }
    return 0;
} 