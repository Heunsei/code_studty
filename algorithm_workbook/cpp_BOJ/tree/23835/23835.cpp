#include <iostream>
#include <vector>

using namespace std;

// 방의 개수, 쿼리의 수
int N, N_Q;
// 쿼리의 종류(1,2), 시작지점, 끝지점
int query ,start, target;
vector<int> tree[1001];
int milk[1001] = {0, };
bool visited[1001];

// 출발하는 방을 제외하고 i번째로 방문하는 방에 i개의 우유 전달

bool solve(int start, int target, int count){
    visited[start] = true;
    if (start==target){
        milk[start] += count;
        return true;
    }

    for(int next : tree[start]){
        if (visited[next]) continue;
        if (solve(next, target, count+1)){
            milk[next] += count;
            return true;
        } 
    }
    return false;
}


int main(){
    // 방의 개수 입력
    std::cin >> N;
    
    for(int i{0}; i<N-1; i++){
        // 양뱡향 연결
        cin >> start >> target;
        tree[start].push_back(target);
        tree[target].push_back(start);
    }
    
    std::cin >> N_Q;
    
    for(int i{0}; i<N_Q; i++){
        std::cin >> query >> start;
        if (query == 1){
            std::cin >> target;
            // 방문배열 초기화
            for(int i{0}; i<N+1; i++) visited[i] = false;
            solve(start, target, 0);
        }else{
            std::cout << milk[start] << std::endl;
        }
    }
    return 0;
}