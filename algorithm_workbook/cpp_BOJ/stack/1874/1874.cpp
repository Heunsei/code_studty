#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    int N;
    cin >> N;
    int result = true;
    vector<int> A(N,0); // N개를 0으로 초기화
    vector<char> save_char;

    for(int i{0}; i<N; i++){
        cin >> A[i];
    }

    stack<int> stk;
    int position = 1;

    for(int i {0}; i < A.size(); i++){
        int cur = A[i];
        // 현재값이 position보다 크다면
        if (cur >= position){
            // 첫값이 4라면 1,2,3,4 는 + 한뒤 4를 빼서 -를 넣어줘야함
            while(cur >= position){
                stk.push(position++);
                save_char.push_back('+');
            }
            stk.pop();
            save_char.push_back('-');
        }else{
            int top = stk.top();
            stk.pop();
            if(top > cur){
                cout << "NO";
                result = false;
                break;
            }else{
                save_char.push_back('-');
            }
        }
    }
    
    if (result){
        for(auto i : save_char){
            cout << i << '\n';
        }
    }
    return 0;
}