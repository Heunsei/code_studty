#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
// BOJ - 1707
// 이분 그래프
static vector<vector<int>> a;
static vector<int> checker;
static vector<bool> visited;
static bool isPass;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int K;
    // test case
    cin >> K;
    for(int t{0}; t<K; t++){
        int V, E;
        // 정점 개수, 간선 개수
        cin >> V >> E;
        // 저장 벡터 생성
        a.resize(V+1);
        checker.resize(V+1);
        visited.resize(V+1);
        isPass = true;
        for(int i{0}; i<E; i++){
            // 시작 정점과 도착 정점 정보 입력.
            int S, E;
            cin >> S >> E;
            a[S].push_back(E);
            a[E].push_back(S);
        }
        for(int i{0}; i<V; i++){
            if(isPass){
                DFS(i);
            } else {
                break;
            }
        }
        if(isPass) cout << "YES" << "\n";
        else cout << "NO" << "\n";
        // 정답 결과 출력수 사용 vector 초기화
        for(int i{0}; i<=V; i++){
            a[i].clear();
            visited[i] = false;
            checker[i] = 0;
        }
    }
}

void DFS(int start){
    visited[start] = true;
    for(int nxt : a[start]){
        if(!visited[start]){
            // 이전 정점과 다른 그룹으로 체크
            checker[nxt] = (checker[start] + 1) % 2; 
            DFS(nxt);
        } else if (checker[start] == checker[nxt]){
            isPass = false;
        }
    }
}