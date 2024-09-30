#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N, M;   // 강의의 갯수, 블루레이의 갯수
    cin >> N >> M;
    vector<int> video (N+1);
    int max_len = 0;    // 아무리 작아도 블루레이의 길이는 얘부터 시작
    int acc = 0;        // 누적값을 활용해 이분탐색

    for(int i{0}; i<N; i++){
        cin >> video[i];
        if(max_len < video[i]){
            max_len = video[i];
        }
        acc += video[i];
    }
    // max_len과 acc를 왔다갔다 올리면서 범위를 축소
    while(max_len <= acc){
        int middle = (max_len + acc) / 2;
        int sum = 0;
        int count = 0;
        for (int i{0}; i<N; i++){
            if(sum+video[i] > middle){ // 중앙값 보다 커지면 카운트를 올리고 누적값 재계산
                count++;
                sum = 0;
            }
            sum += video[i];
        }
        if(sum != 0){
            count++;
        }
        if(count <= M){  // count가 동일하다면 최소길이를 찾아야하니 -1 진행
            acc = middle - 1;
        }else{
            max_len = middle + 1;
        }
    }
    cout << max_len;
}