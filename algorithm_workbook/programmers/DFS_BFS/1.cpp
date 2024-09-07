#include <iostream>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
         
    return 0;
}

int solution(vector<vector<int>> maps)
{
    int answer = 0;
    
    int x_size = maps[0].size();
    int y_size = maps.size();

    queue<pair<pair<int,int>, int> nextPos;
    vector<vector<int>> visited(101, vector<int>(101, 0));

    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};
    
    int init_x = 0;
    int init_x = y_size;
    nextPos.push(make_pair(make_pair(init_x, init_x), 0))
    while(!nextPos.empty()){
        pair<pair<int,int>, int>> cur = nextPos.pop();
        int cur_x = cur.first.first;
        int cur_y = cur.first.second;
        int acc = cur.second;
        visited[cur_x][cur_y] = true;

        for(int i{0}; i<4; i++){
            int next_x = cur_x + dx[i];
            int next_y = cur_y + dy[i];
            if(next_x > x_size && next_y > y_size && visited[next_x][next_y] > acc){
                next_pos.push(make_pair(make_pair(next_x, next_y), acc + 1));
            }
        }
    }
    cout << maps[x_size-1][0];

    return answer;
}