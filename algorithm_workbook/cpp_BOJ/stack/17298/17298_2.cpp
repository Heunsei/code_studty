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
    // 첫 input value
    vector<int> input_value(n,0);
    vector<int> answer(n,0);

    stack<int> stk;
    // 최초 index 주입
    stk.push(0);

    for(int i {0}; i<n; i++){
        cin >> input_value[i];
    }
    
    for(int i {1}; i<n; i++){
        while(!stk.empty() && input_value[stk.top()] < input_value[i]){
            answer[stk.top()] = input_value[i];
            stk.pop();
        }
        stk.push(i);
    }
    while(!stk.empty()){
        answer[stk.top()] = -1;
        stk.pop();
    }

    for(auto i : answer){
        cout << i << " ";
    }

    return 0;
}