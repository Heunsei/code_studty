// 평범한 배낭
#include <iostream>
using namespace std;

int w[101], v[101];
int d[100010], temp[100010]; // d[i]는 무게가 i일 때, 배낭에 넣을 수 있는 가치의 최대 값
int n, k;

int main(){
    ios::sync_with_stdio(false);
	cin.tie(0);
    // 물건의 수, 준서가 버틸 수 있는 무게
    cin >> n >> k;
    // i번째 물품의 무게와 가치
    for(int i{1}; i<=n; i++){
        std::cin >> w[i] >> v[i]   
    }
    for(int i{1}; i<=n; i++){       // 물건의 번호
        memcpy(temp, d, sizeof(temp));
        for(int j{0}; k<=k; j++){   // j는 무게를 나타냄
            // i번째 물건을 무게가 j(0<=j<=k)인 배낭에 넣어봄
            // 무게가 j+w[i]인 배낭도 가치가 최대가 되는지 확인
            temp[j+w[i]] = max(temp[j+w[i]], d[j]+v[i]);
        }
        for(int j=0; j<=k; j++) d[j] = temp[j]; // d[i] 갱신
    }
    std::cout << d[k];
}