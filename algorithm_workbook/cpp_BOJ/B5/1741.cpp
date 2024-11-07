#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
// BOJ - 1747
// 소수 & 팰린드롬
bool isPass(int number);
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    // N보다 크거나 같고, 소수, 펠린드롬인 가장 작은 수.
    int N;
    cin >> N;

    vector<int> number(10'000'000, 0);
    
    for(int i{2}; i<10'000'000; i++){
        number[i] = i;
    }

    for(int i{2}; i<10'000'000; i++){
        if(number[i] == 0) continue;
        for(int j{i*2}; j<10'000'000; j += i){
            number[j] = 0;
        }
    }
    int init = N;
    for(int i{init}; i<10'000'000; i++){
        if(number[i] == 0) continue;
        if(isPass(number[i])){
            cout << number[i];
            break;
        }
    }
}

bool isPass(int number){
    string str = to_string(number);
    int left, right;
    left = 0;
    right = str.length() - 1;
    bool pass = true;
    while(left <= right){
        if(str[left] != str[right]){
            pass = false;
            break;
        }
        left++;
        right--;
    }
    return pass;
}
