#include <iostream>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

    string word,boom;
    cin >> word >> boom;
    stack<char> s;
    string ans;
    
    ans.reserve(1000000); // 미리 할당해둠으로서 시간복잡도를 줄임
    for(int i = 0; i < word.length(); i++){
        s.push(word[i]); // 스택에 넣음
        if(word[i] == boom[boom.length()-1] && s.size() >= boom.length()){
            string tmp;
            for(int j = 0; j < boom.length(); j++){
                tmp.push_back(s.top());
                s.pop();
            }
            reverse(tmp.begin(),tmp.end());
            if(tmp.compare(boom) != 0){
                for(int i = 0; i < tmp.length(); i++) s.push(tmp[i]);
            }
        }
    }

    // 스택에 남은 원소들을 ans에 넣음
    while(!s.empty()){
        ans.push_back(s.top());
        s.pop();
    }
    reverse(ans.begin(),ans.end()); 
    if(ans.empty()) cout << "FRULA"; 
    else cout << ans;
}