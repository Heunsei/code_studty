#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<int> input_value(n,0);
    // 정답 인덱스를 저장할 스택.
    stack<int> stk;

    for(int i {0}; i<n; i++){
        cin >> input_value[i];
    }



    return 0;
}