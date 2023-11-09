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
    // 움직이는 좌표만 확인해도 괜찮음.
    // i 는 왼쪽 포인터 j는 오른쪽 포인터
    while(j<N){
        if (check[arr[j]] < K){ // 만약 오른쪽 포인터의 check 배열 저장값이 k를 넘어서지않으면
            check[arr[j]]++;    // j를 진행방향인 오른쪽 으로 쭉 진행시킴
            j++;
        } else {
            check[arr[i]]--; // 만약 j번째의 check값이 넘어선다면 고정 후 i만 움직여준다
            i++;
        }
        result = max(result, j-i);  // 결과값은 result와 j-i중에서 큰값
    }
    cout << result << '\n';
    return 0;
}