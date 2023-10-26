#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;

int arr[5][5];
int check[5][5];
int r,c;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int cnt = 0;

bool solve(int x, int y){
    stack<pair<int,pair<int,int>>> stk;
    stk.push({0,{x,y}});

    while(!stk.empty()){
        int cost = stk.top().first;
        int x = stk.top().second.first;
        int y = stk.top().second.second;
        // cout << x << " " << y << " " << check[x][y] << endl;

        if (check[x][y] == 2) return true;

        arr[x][y] = -1;
        stk.pop();

        if (cost>=3) continue;

        for(int k{0}; k<4; k++){
            int nx = x + dx[k];
            int ny = y + dy[k];
            if(nx<0 || ny<0 || nx>4 || ny>4) continue;
            if(arr[nx][ny] == -1) continue;
            if(arr[nx][ny] == 1) {
                check[nx][ny] = check[x][y] + 1;
            }else{
                check[nx][ny] = check[x][y];
            }
            stk.push({cost+1, {nx,ny}});
        }
    }
    return false;
}

int main(){
    for(int i{0}; i<5; i++){
        for(int j{0}; j<5; j++){
            cin >> arr[i][j];
            check[i][j] = 0;
        }
    }
    cin >> r >> c;
    bool result = solve(r, c);
    // cout << "result : " << result << endl;
    if(result) cout << 1;
    else cout << 0;
}