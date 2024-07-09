#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    vector<int> vec(N,0);

    for (int i{0}; i<N; i++){
        cin >> vec[i];
    }

    for(int i{0}; i<N-1; i++){
        for (int j{0}; j < N - 1 - i ;j++){
            if(vec[j]>vec[j+1]){
                int tmp = vec[j];
                vec[j] = vec[j+1];
                vec[j+1] = tmp;
            }
        }
    }

    for(auto i : vec){
        cout << i << '\n';
    }
    
    return 0;
}