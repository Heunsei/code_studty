#include <algorithm>
#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    int arr[1000001];
    int N;
    std::cin >> N;
    for(int i{0}; i<N; i++){
        std::cin >> arr[i];
    }

    sort(arr, arr+N);

    for(int i{0}; i<N; i++){
        std::cout << arr[i] << '\n';
    }
}