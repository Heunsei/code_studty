// 좋은 수
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N;
    std::vector<long long> arr(N, 0);
    for (int i{0}; i<N; i++){
        std::cin >> arr[i];
    }
    
    sort(arr.begin(), arr.end());
    int start_index = 0;
    int end_index = 0;
    int check_index = 1;
    int cnt = 0;
    
    while (check_index < N){
        if (arr[start_index] + arr[end_index] == arr[check_index]){
            cnt++;
        }
        if (arr[start_index] + arr[end_index] > arr[check_index]){
            end_index --;
        }else if (arr[start_index] + arr[end_index] < arr[check_index]){
            start_index++;
        }      
    }
}