#include <iostream>
#include <vector>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);

    int N,j;
    cin >> N;
    vector<int> vec(N,0);

    for(int i{0}; i<N; i++){
        cin >> vec[i];
    }

    for(int i{1}; i<N; i++){
        int key = vec[i];
        for(j = i-1; j>=0; j--){
            if(vec[j] > key){
                vec[j+1] = vec[j];
            }else break;
        }
        vec[j+1] = key;
    }

    int add = vec[0];
    for(int i{1}; i<N;i++){
        int tmp = vec[i];
        vec[i] = vec[i-1] + tmp;
        add += vec[i];
    }

    cout << add;
    return 0;
}