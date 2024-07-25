#include <iostream>
#include <vector>

using namespace std;
void DFS(int start, int x);
bool check(int n);
static int N;
int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    cin >> N;
    // 1자리 수의 소수는 2,3,5,7
    // 2,3,5,7을 맨 처음으로 시작하는 숫자를 이용해 각 자리의 소수 판별 후 모두 성립한다면 출력
    DFS(2,1);
    DFS(3,1);
    DFS(5,1);
    DFS(7,1);
    return 0;
}

bool check(int n){
    for(int i{2}; i<n; i++){
        if(n%i == 0){
            return false;
        }
    }
    return true;
}

void DFS(int start, int x){
    if(x == N){
        cout << start << "\n";
    }
    for(int i{1};i<10;i++){
        if(check(start * 10 + i)){
            DFS(start*10+i, x+1);
        }
    }
}