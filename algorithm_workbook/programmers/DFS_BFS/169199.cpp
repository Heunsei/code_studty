#include <string>
#include <vector>
#include <queue>
using namespace std;

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

bool is_outside(int x, int y, int x_len, int y_len) {
    if(x < 0 || x >= x_len || y < 0 || y >= y_len) return true;
    else return false;
}

int solution(vector<string> board) {
    int answer = 0;
    pair<int, int> start;
    pair<int, int> goal;
    int x_len = board[0].size();
    int y_len = board.size();
    vector<vector<bool>> visited (y_len, vector<bool> (x_len, false));
    
    for(int y{0}; y<y_len; y++) {
        for(int x{0}; x<x_len; x++){
            if(board[y][x] == 'R') start = {x,y};
            if(board[y][x] == 'G') goal = {x,y};
        }
    }
    
    queue<pair<pair<int,int>, int>> q;
    q.push({start, 1});
    bool isDone = false;
    int res;
    while(!q.empty() && !isDone){
        pair<int,int> cur_pos = q.front().first;
        int cnt = q.front().second;
        q.pop();
        for(int k{0}; k<4; k++){
            int next_x = cur_pos.first;
            int next_y = cur_pos.second;
            while(!is_outside(next_x + dx[k],next_y + dy[k],x_len,y_len) && board[next_y + dy[k]][next_x + dx[k]] != 'D'){
                next_x += dx[k];
                next_y += dy[k];
            }
            if(visited[next_y][next_x]) continue;
            if(next_x == goal.first && next_y == goal.second) {isDone = true; res=cnt;}
            if(next_x == cur_pos.first && next_y == cur_pos.second) continue;
            q.push({{next_x, next_y}, cnt+1});
            visited[next_y][next_x] = true;
        }
    }
    if(isDone) return res;
    else return -1;
}
