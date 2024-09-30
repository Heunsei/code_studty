#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    long long N, K;
    
    cin >> N;   // 배열의 크기 입력
    cin >> K;   // 찾아야하는 index 입력 

    long long start = 1;
    long long end = N * N;
    while(start<=end){
        long long mid = (start + end) / 2;
        long long count = 0;
        for(int i{1}; i<=N; i++){
            count += min(mid/i, N);
        }
        if(count >= K){ // 딱 맞다면 한번 더 줄여서 확인을 해봐야함
            // 찾아야 하는 K 보다 갯수가 많다면 end를 줄여 범위를 줄여버림
            end = mid-1;
        }else{
            start = mid+1;
        }
    }
    cout << start;
}