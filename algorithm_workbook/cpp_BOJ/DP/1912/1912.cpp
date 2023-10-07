// n개의 정수로 이루어진 임의의 수열 몇개의수를 구해서 합이 가장큰 합을 구하라
#include <iostream>
#include <limits.h>

using namespace std;

int n;
int arr[100'001];
int dp[100'001];

int main(){
    std::cin >> n;
    for(int i{0}; i<n; i++){
        std::cin >> arr[i];
    }
    int tmp{INT_MIN};
    for(int i{0}; i<n; i++){
        dp[i] = max(arr[i],dp[i-1] + arr[i]);  
        tmp = max(tmp, dp[i]);
    }
    std::cout << tmp;
}
