#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, M;
    int count = 0;
    cin >> N >> M;
    vector<int> arr(N, 0);

    for (int i{0}; i<N; i++){
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());    
    int start_index = 0;
    int end_index = N-1;

    while (start_index < end_index){
        long sum = arr[start_index] + arr[end_index];
        if(sum == M){
            count ++;
            end_index--;
            start_index++;
        }
        else if (sum > M){
            end_index--;
        }
        else if (sum < M){
            start_index++;
        }
    }
    cout << count << '\n';
    return 0;
}