// 특성값이 0에 가까운 두 용액을 만들기
#include <iostream>
#include <vector>

using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N;
    cin >> N;
    vector<int> arr(N, 0);

    for (int i{0}; i<N; i++){
        cin >> arr[i];
    }

    int i = 0;      // arr의 양쪽 끝에서 탐색
    int j = N-1;
    int result = abs(arr[i] + arr[j]);
    pair<int,int> position = {arr[i], arr[j]}; 

    while(i < j){
        int tmp = arr[i] + arr[j];
        if (abs(tmp) < result){
            result = abs(tmp);
            position = {arr[i] , arr[j]};
        }
        if (tmp < 0){
            i++;
        }else {
            j--;
        }
    }

    int a = position.first;
    int b = position.second;
    (a > b) ? cout << b << " " << a : cout << a << " " << b;

    return 0;
}