#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    bool result = true;
    cin >> n;
    vector<int> input_value(n,0);
    vector<char> output_value;
    
    for(int i {0}; i<n; i++){
        cin >> input_value[i];
    }

    stack<int> stk;
    int stk_value = 1;

    for(int i {0}; i< input_value.size(); i++){
        int curreunt_value = input_value[i];

        if(curreunt_value >= stk_value){
            while(curreunt_value>= stk_value){
                stk.push(stk_value++);
                output_value.push_back('+');
            }
            stk.pop();
            output_value.push_back('-');
        } else {
            int top = stk.top();
            stk.pop();
            if(top > curreunt_value){
                cout << "NO";
                result = false;
                break;
            } else {
                output_value.push_back('-');
            }
        }
    }

    if(result){
        for(auto i : output_value){
            cout << i << '\n';
        }
    }

    return 0;
}