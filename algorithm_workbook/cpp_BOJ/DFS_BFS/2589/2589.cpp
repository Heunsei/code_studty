#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

string arr[51];
int dist[51][51];
int max_res;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int N, M;

void bfs(int x, int y){
    queue<pair<int,int>> q;
    for(int i{0}; i<N; i++){
        for(int j{0}; j<M; j++){
            dist[i][j] = -1;
        }
    }
    q.push({x,y});
    dist[x][y] = 0;
    while(!q.empty()){
        int cur_x = q.front().first;
        int cur_y = q.front().second;
        q.pop();
        for(int k{0}; k<4; k++){
            int nx = cur_x + dx[k];
            int ny = cur_y + dy[k]; 
            if(nx<0||ny<0||nx>=N||ny>=M) continue;
            if(dist[nx][ny] != -1 || arr[nx][ny] == 'W') continue;
            dist[nx][ny] = dist[cur_x][cur_y]+1;
            max_res = max(dist[nx][ny], max_res);
            q.push({nx,ny});
        }
    }
}



int main(){
    std::cin >> N >> M;
    for(int i{0}; i<N; i++) std::cin >> arr[i];
    for(int i {0}; i<N; i++){
        for(int j{0}; j<M; j++){
            if(arr[i][j] == 'L')
                bfs(i,j);
        }
    }
    std::cout << max_res;
}
