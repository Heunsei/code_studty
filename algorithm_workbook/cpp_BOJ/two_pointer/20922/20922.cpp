#include <iostream>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int arr[200000];
    int cnt[100001];

    int N, K;
    cin >> N >> K;

    for (int i{0}; i<N; i++){
        cin >> arr[i];
    }

    int i = 0;
    int j = 0;
    int result = 0;

    // 전부다 확인할 필요없이 i와 j만 움직일때 그 위치의 값만 확인하면 되는것
    while (j<N){
        // 
        if (cnt[arr[j]] != K){
            cnt[arr[j]]++;
            j++;
        }else {
            cnt[arr[i]]--;
            i++;
        }
        result = max(result, j-i);
    }
    cout << result << "\n";
    return 0;
}