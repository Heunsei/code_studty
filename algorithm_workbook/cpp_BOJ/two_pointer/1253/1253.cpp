// 좋은 수
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    cin >> N;
    std::vector<long long> arr(N, 0);
    for (int i{0}; i<N; i++){
        std::cin >> arr[i];
    }
    
    sort(arr.begin(), arr.end());   // 편한 비교를 위한 정렬

    int cnt = 0;
    for(int chk{0}; chk<N; chk++){
        int i = 0;
        int j = N - 1;
        long long find = arr[chk];
        while (i < j){
            if (arr[i] + arr[j] == find){
                if (i != chk && j != chk){
                    cnt ++;
                    break;
                }else if (i==chk){
                    i++;
                }else{
                    j--;
                }
            }else if(arr[i] + arr[j] > find){
                j--;
            }else{
                i++;
            }
        }
    }
    cout << cnt;
    return 0;    
}