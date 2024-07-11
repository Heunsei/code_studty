#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string input_value;
    cin >> input_value;
    vector<int> vec(input_value.size(),0);
    for(int i{0}; i<input_value.size(); i++){
        vec[i] = stoi(input_value.substr(i,1));
    }

    for(int i{0}; i<input_value.length(); i++){
        int MAX = i;
        for(int j {i+1}; j<input_value.length(); j++){
            if(vec[j] > vec[MAX]){
                MAX = j;
            }
        }
        if(vec[i] < vec[MAX]){
            int temp = vec[i];
            vec[i] = vec[MAX];
            vec[MAX] = temp;
        }
    }
    for(int i{0}; i<vec.size(); i++){
        cout << vec[i];
    }

    return 0;
}