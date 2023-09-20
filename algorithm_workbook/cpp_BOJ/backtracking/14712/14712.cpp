#include <iostream>
#include <vector>

using namespace std;
int N, M, res;
int arr[26][26];
int dx[3] = {-1, 0, -1};
int dy[3] = {0, -1, -1};

bool check(int x, int y){
    int cnt{0};
    for(int i{0}; i<3; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx>=0 && ny>=0 && nx<N && ny<M){
            if(arr[nx][ny]) cnt++;
        }
    }
    if(cnt == 3) return false;
    return true;
}

void backtracking(int x, int y){
    if(x == N-1 && y == M){
        res++;
        return;
    }
    if(y==M){
        y=0;
        x++;
    }
    arr[x][y] = 1;
    if(check(x,y)) backtracking(x,y+1);
    arr[x][y] = 0;
    backtracking(x,y+1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> N >> M;
    backtracking(0,0);
    cout << res;
}
