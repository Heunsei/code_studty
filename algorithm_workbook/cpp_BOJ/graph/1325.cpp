#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
// BOJ - 1325
// 효율적인 해킹
void search(vector<vector<int>> &vec, vector<bool> &visited, vector<int> &checker, int start);
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N, M;
    cin >> N >> M;
    vector<vector<int>> vec (N+1);
    vector<bool> visited (N+1, false);
    vector<int> checker (N+1, 0);

    for(int i{0}; i<M; i++){
        int from, to;
        cin >> from >> to;
        vec[from].push_back(to);
    }

    for(int i{1}; i<=N; i++){
        search(vec, visited, checker, i);
    }
    int max = 0;
    for(auto i : checker){
        if(max < i){
            max = i;
        }
    }

    vector<int> solve;
    
    for(int i {1}; i<=N; i++){
        if (checker[i] == max){
            solve.push_back(i);
        }
    }
    sort(solve.begin(), solve.end());
    for (auto i : solve){
        cout << i << ' ';
    }
    
}

void search(vector<vector<int>> &vec, vector<bool> &visited, vector<int> &checker, int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        for(int nxt : vec[cur]){
            if(!visited[nxt]){
                visited[nxt] = true;
                q.push(nxt);
                checker[nxt]++;
            }
        }
    }
    for(int i{0}; i<visited.size(); i++){
        visited[i] = false;
    }
}