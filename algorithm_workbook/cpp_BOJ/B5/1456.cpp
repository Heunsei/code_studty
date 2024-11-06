#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
// BOJ - 1456
// 거의 소수
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    long long A, B;
    cin >> A >> B;
    // A 이상 B 이하의 거의 소수의 갯수 출력
    // 거의 소수 > 어떤 수가 소수의 N 제곱 꼴일 때
    // A와 B의 크기는 10^14
    long long end = sqrt(B);
    vector<long long> number(end+1, 0);

    for (int i{2}; i<end+1; i++){
        number[i] = i;
    }
    for(int i{2}; i<end+1; i++){
        if(number[i] == 0) continue;
        for(int j{i*2}; j<end+1; j+=i){
            number[j] = 0;
        }
    }
    int sol = 0;
    for(long long i : number){
        // 소수가 아닌 경우 continue
        if (i == 0) continue;
        // 잡고 돌아줄 기준점 설정
        double tmp = i;
        while(tmp <= B){
            if(tmp*i <= B){
                tmp *= i;
                if(tmp >= A && tmp <= B) sol++;
            }else break;
        }
    }
    cout << sol;
}
