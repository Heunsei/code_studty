#include <iostream>
#include <vector>

using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<int> arr(N, 0);
    
    for(int i=0; i<N; i++){
        int temp;
        cin >> temp;
        if (i==0){
            arr[i] = temp%M;
        }else{
            arr[i] = arr[i] + temp%M;
        }
    }

    for (auto i : arr){
        cout << i << '\n';
    }

    return 0;
}