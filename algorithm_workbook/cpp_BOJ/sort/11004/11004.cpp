#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;
    cin >> N >> K;

    vector<int> vec(N);
    for(int i{0}; i<N; i++){
        cin >> vec[i];
    }
    sort(vec.begin(), vec.end());
    cout << vec[K-1];
    return 0;
}