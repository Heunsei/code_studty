// BOJ : 1253 좋다
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    int N;      // N개의 수
    cin >> N;
    std::vector<long long> arr(N, 0);
    for (int i{0}; i<N; i++){
        std::cin >> arr[i];
    }
    
    sort(arr.begin(), arr.end());   // 정렬

    int cnt = 0;
    for(int chk{0}; chk<N; chk++){
        int i = 0;          // 양쪽 끝에서 비교
        int j = N - 1;
        long long find = arr[chk];
        while (i < j){
            if (arr[i] + arr[j] == find){   // i,j의 합이 find와 같을 때
                if (i != chk && j != chk){  // 찾아야할 좌표랑 같으면 안됌
                    cnt ++;
                    break;
                }else if (i==chk){          // i가 같다면 i의 진행방향으로
                    i++;
                }else{                      // j가 같다면 j의 진행방향으로
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