#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n, w, l;
    // 트럭의 숫자, 다리의 길이, 최대하중
    cin >> n >> w >> l;
    int current_w = 0;
    int res = 0;
    vector<pair<int, int>> wait_t;
    queue<int> cur_t;

    for(int i{0}; i<n; i++){
        int temp;
        cin >> temp;
        wait_t.push_back({temp, w});
    }

    int cur_ptr = 0;

    while(true){
        // 기존 트럭 관리
        if(!cur_t.empty()){
            bool isPop = false;
            int out_truck;
            for(int i {cur_t.front()}; i<=cur_t.back(); i++){
                wait_t[i].second -= 1;
                if(wait_t[i].second <= 0){
                    isPop = true;
                    out_truck = i;
                }
            }
            if(isPop){
                current_w -= wait_t[cur_t.front()].first;
                cur_t.pop();
            }
        }

        // 새로 진입하는 트럭을 관리
        if(wait_t[cur_ptr].first + current_w <= l && cur_ptr < n && cur_t.size() <= w){
            current_w += wait_t[cur_ptr].first;
            cur_t.push(cur_ptr);
            // wait_t[cur_ptr].second -= 1;
            cur_ptr++;
        }
        res++;
        // cout << res << " : " << current_w << '\n';
        if(cur_ptr >= n-1 && cur_t.empty()){
            break;
        }
    }
    cout << res;

}
