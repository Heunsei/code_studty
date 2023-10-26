#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dp[101][100'001];
int weight[101];        // 물건의 무게
int val[101];           // 물건의 가치
// 준서가 필요하다 생각하는 갯수 N개, 버틸 수 있는 무게K
int N, K;
int main(){
    ios_base::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);

    std::cin >> N >> K;
    for(int i{1}; i<=N; i++){
        cin >> weight[i] >> val[i];
    }

    for(int i{1}; i<=N; i++){
        for(int j{1}; j<=K; j++){
            // 내가 담을 무게 j, weight[i]에 있는 무게보다 커야 테이블에 넣을것
            if(j >= weight[i])
            // 선택 x / 선택 o
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + val[i]);
            // 물건을 못넣는 경우
            else
                dp[i][j] = dp[i-1][j];
        }
    }
    cout << dp[N][K];
    return 0;
}