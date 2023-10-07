// BOJ 2468
// 비가 내렸을때 최대의 안전구역의 갯수를 구하는 문제 
#include <iostream>
#include <queue>
#include <algorithm>
#include <cstring>
using namespace std;

int N;
int nx, ny;
int result = 0;
int max_h = -1;
int cnt = 0;
int arr[101][101];
bool visited[101][101];
queue<pair<int,int>> q;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void bfs(int x, int y){
    q.push({x, y});
    visited[x][y] = true;
    while(!q.empty()){
        int cur_x, cur_y;
        cur_x = q.front().first;
        cur_y = q.front().second;
        q.pop();
        for(int k{0}; k<4; k++){
            nx = cur_x + dx[k];
            ny = cur_y + dy[k];
            if(nx<0 || ny<0 || nx>N || ny>N) continue;
            if(visited[nx][ny]) continue;
            visited[nx][ny] = true;
            q.push({nx,ny});
        }
    }
}

void reset(){
for(int i{0}; i<N; i++){
        for(int j{0}; j<N; j++){
            visited[i][j] = false;
        }
    }
}
int main()
{
    std::cin >> N;
    reset();
    for(int i{0}; i<N;i++){
        for(int j{0}; j<N; j++){
            int hight;
            cin >> hight;
            max_h = max(max_h, hight);
            arr[i][j] = hight;
        }
    }

    for(int i{0}; i<=max_h; i++){
        for(int x{0}; x<N; x++){
            for(int y{0}; y<N; y++){
                if(arr[x][y] <= i) visited[x][y] = true;
            }
        }
        for(int i{0}; i<N; i++){
            for(int j{0}; j<N; j++){
                if(!visited[i][j]){
                    bfs(i,j);
                    cnt++;
                }
            }
        }
        result = max(result,cnt);
        reset();
        cnt = 0;
    }
    std::cout << result;
    return 0;
}