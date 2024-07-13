#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // 테이프의 길이 L
    int N, L;
    int sol {1};
    cin >> N >> L;
    vector<int> vec(N, 0);

    for(int i{0}; i<N; i++){
        cin >> vec[i];
    }

    sort(vec.begin(), vec.end());

    int str {0};
    int end {N-1};
    int pos = vec[str];
    while(str<end){
        if(pos + L > vec[str+1]){
            str++;
        } else {
            pos = vec[str+1];
            sol++;
            str++;
        }
    }
    cout << sol;
    return 0;
}