#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int width;
int T, I;
int arr[305][305];
int x, y, end_x, end_y;
std::queue<pair<int,int>> q;

int dx[8] = {-1, -2, -2, -1, 1, 2, 2, 1};
int dy[8] = {-2, -1, 1, 2, -2, -1, 1, 2};

void bfs(int x, int y){
    q.push({x,y});
    arr[x][y] = 0;
    while(!q.empty()){

        int cx = q.front().first;
        int cy = q.front().second;

        if (cx==end_x && cy==end_y){
            cout << arr[cx][cy] << std::endl;
            while(!q.empty()) q.pop();
            return;
        }
        q.pop();

        for(int k{0}; k<8; k++){
            int nx = cx + dx[k];
            int ny = cy + dy[k];

            if(nx<0 || ny<0 || nx>I || ny>I) continue;
            if(arr[nx][ny]!=-1) continue;

            q.push({nx,ny});
            arr[nx][ny] = arr[cx][cy] + 1;
        }
    } x 
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    // 반복횟수 입력
    std::cin >> T;
    while(T--){
        std::cin >> I;

        for(int i{0}; i<I; i++){
            for(int j{0}; j<I; j++){
                arr[i][j] = -1;
            }
        }

        cin >> x >> y;
        cin >> end_x >> end_y;
        bfs(x,y);

        for(int i{0}; i<I; i++){
            for(int j{0}; j<I; j++){
                arr[i][j] = -1;
            }
        }
    }

}