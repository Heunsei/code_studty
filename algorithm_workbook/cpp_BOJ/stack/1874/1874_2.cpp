#include <iostream>
#include <vector>
#include <stack>

// 스택 수열.
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N;
    cin >> N;
    vector<int> input_value(N,0);
    vector<char> output_value;

    for(int i{0}; i<N; i++){
        cin >> input_value[i];
    }

    stack<int> stk;
    int stk_value = 1;
    bool result = true;

    for(int i{0}; i < input_value.size(); i++){
        int to_find = input_value[i];
        if(to_find >= stk_value){
            // 같을때 까지, 1,2,3,4 까지 
            while (to_find >= stk_value){
                stk.push(stk_value++);
                output_value.push_back('+');
            } // 4는 출력 해야하니까
            stk.pop();
            output_value.push_back('-');
        }else{
            // 스택에 들어있는 top값이 만약 찾아야할 값보다 크다면
            // 출력 불가능한 수열이므로 NO출력 후 종료
            int top = stk.top();
            stk.pop();
            if(top > to_find){
                result = false;
                cout << "NO";
                break;
            }else{
                output_value.push_back('-');
            }
        }
    }

    if (result){
        for (auto i : output_value){
            cout << i << '\n';
        }
    }

    return 0;
}