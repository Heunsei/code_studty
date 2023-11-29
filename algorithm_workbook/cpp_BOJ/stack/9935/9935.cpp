#include <iostream>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    string str;
    string bomb;
    stack<char> stk;
    string result;
    cin >> str >> bomb;

    for(int i{0}; i<str.length(); i++){
        stk.push(str[i]);
        if (str[i] == bomb[bomb.length() - 1] && stk.size() >= bomb.length()){
            string temp;
            while(temp.length() != bomb.length()){
                temp.push_back(stk.top());
                stk.pop();
            }
            reverse(temp.begin(), temp.end());
            if (temp.compare(bomb) != 0) {
                for(int i = 0; i < temp.length(); i++) stk.push(temp[i]);
            }
        }
    }

    while(!stk.empty()){
        result.push_back(stk.top());
        stk.pop();
    }
    reverse(result.begin(), result.end());
    if(result.empty()) cout << "FRULA";
    else cout << result;
}