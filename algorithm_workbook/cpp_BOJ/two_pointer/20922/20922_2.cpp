#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int arr[200000];
    int check[100'001];

    int N, K;
    cin >> N >> K;
    for (int i{0}; i<N; i++){
        cin >> arr[i];
    }

    int i = 0;
    int j = 0;
    int result = 0;

    while(j<N){
        if (check[arr[j]] < K){
            check[arr[j]]++;
            j++;
        } else {
            check[arr[i]]--;
            i++;
        }
        result = max(result, j-i);
    }
    cout << result << '\n';
    return 0;
}