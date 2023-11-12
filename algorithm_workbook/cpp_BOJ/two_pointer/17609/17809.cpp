// 회문
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int checkString(string::iterator left, string::iterator right, bool change, string &str){
    while (left < right) {
        if (*left == *right){ // 둘이 같으면 안쪽으로
            left++;
            right--;
        }
        else{
            if (change) {
                if (checkString(left, right-1, false, str) == 0 ||  checkString(left+1, right, false, str) == 0) return 1;
            }
            return 2; 
        }
    }
    return 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    for (int i{0}; i < N; i++){
        string temp;
        cin >> temp;
        auto left = temp.begin();    // 포인터 시작점
        auto right = temp.end() - 1; // 포인터 종료지점
        int result = checkString(left, right, true, temp);
        cout << result << '\n';
    }
    return 0;
}