#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
// BOJ - 1016
// 제곱 ㄴㄴ 수
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    // 접근 방법.
    // -> 문제의 조건 상 min 과 max의 차이는 최대 1'000'000
    // -> 전체 범위를 구하는게 아닌 min 과 max의 사이만 구하기
    long min, max;
    cin >> min >> max;
    // 길이 만큼만 체크할 배열 선언.
    vector<bool> check(max-min+1);
    // 초기화
    for(long i{2} ; i * i <= max; i++){
        // 돌려쓸 제곱값
        long pow = i * i;
        // 이친구를 돌려쓰면서 제곱 ㄴㄴ 수를 찾아냄
        long mul_idx = min / pow;
        if(min % pow != 0){
            mul_idx++;
        }
        // cout << "pow : " << pow << " " << mul_idx << '\n';
        for(long j{mul_idx}; j*pow <= max; j++){
            check[(int)((j*pow)-min)] = true;
        }
    }
    int cnt = 0;

    for(auto i : check){
        if(!i) cnt++;
    }
    cout << cnt;
}