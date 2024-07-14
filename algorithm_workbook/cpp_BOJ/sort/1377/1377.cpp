#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    vector<pair<int, int>> vec(N);

    for(int i{0}; i<N; i++){
        cin >> vec[i].first;
        vec[i].second = i;
    }

    sort(vec.begin(), vec.end());
    int MAX = 0;
    for(int i{0}; i<N; i++){
        if(MAX < vec[i].second - i){
            MAX = vec[i].second - i;
        }
    }

    cout << MAX + 1;
    return 0;
}