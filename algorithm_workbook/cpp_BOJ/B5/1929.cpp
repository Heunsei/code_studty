#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 정수론
// 소수 구하기 BOJ - S3
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    // M 이상 N 이하.
    int M, N;
    cin >> M >> N;
    vector<int> num (N+1, 0);
    // 배열 초기화
    for(int i{2}; i < N+1; i++){
        num[i] = i;
    }
    num[0] = 0;
    // 배열을 순회하며 소수가 아닌 부분을 지우는 작업 실행
    for(int i{1}; i<N+1; i++){
        if(num[i] == 0) continue;
        for(int j{i*2}; j<=N; j+=i){
            num[j] = 0;
        }
    }
    for(auto i : num){
        if(i < M || i > N) continue;
        if(i != 0){
            cout << i << '\n';
        }
    }
}
