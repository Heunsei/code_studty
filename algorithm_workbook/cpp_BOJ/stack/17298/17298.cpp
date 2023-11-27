#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    cin >> N;
    vector<int> vec(N,0);
    vector<int> answer(N,0);

    for(int i{0}; i<N; i++){
        cin >> vec[i];
    }

    stack<int> stk;
    stk.push(0);

    for(int i{1}; i<N; i++){
        while(!stk.empty() && vec[stk.top()] < vec[i]){
            answer[stk.top()] = vec[i];
            stk.pop();
        }
        stk.push(i);
    }
    while(!stk.empty()){
        answer[stk.top()] = -1;
        stk.pop();
    }
    for(int i{0}; i<N; i++){
        cout << answer[i] << ' ';
    }
    return 0;
}