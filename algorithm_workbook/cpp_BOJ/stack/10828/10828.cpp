#include <iostream>
#include <algorithm>
#include <stack>
#include <string>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    stack<int> stk;
    int rpt;
    cin >> rpt;

    for(int i{0}; i<rpt; i++){
        string cmd;
        cin >> cmd;

        if(cmd == "push"){
            int tmp;
            cin >> tmp;
            stk.push(tmp);
        }else if (cmd == "top"){
            if(stk.empty()){
                cout << -1 << '\n';
            }else {
                cout << stk.top() << '\n';
            }
        }else if (cmd == "size"){
            cout << stk.size() << '\n';
        }else if (cmd == "pop"){
            if(stk.empty()){
                cout << -1 << '\n';
            }else {
                int tmp;
                tmp = stk.top();
                stk.pop();
                cout << tmp << '\n';
            }
        }else if(cmd == "empty"){
            if(stk.empty()){
                cout << 1 << '\n';
            }else {
                cout << 0 <<'\n';
            }
        }
    }

    return 0;
}