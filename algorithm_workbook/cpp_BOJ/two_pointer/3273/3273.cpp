#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, x;
    cin >> n;
    vector<int> arr(n,0);

    for (int i{0}; i<n; i++){
        cin >> arr[i];
    }

    cin >> x;
    
    sort(arr.begin(), arr.end());

    int i{0};
    int j{n-1};
    int result{0};

    while(i<j){
        if (arr[i] + arr[j] == x){ 
            result++;
            j--;
        }
        else if (arr[i] + arr[j] > x) j--;
        else if (arr[i] + arr[j] < x) i++;
    }
    cout << result;

    return 0;
}