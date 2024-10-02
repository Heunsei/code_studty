#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

bool pos_cmpr(int a, int b){
    return a > b;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    vector<int> positive;
    vector<int> negative;
    int N;
    int acc = 0;
    cin >> N;
    for(int i{0}; i<N; i++){
        int tmp;
        cin >> tmp;
        if(tmp > 0){
            positive.push_back(tmp);
        }else{
            negative.push_back(tmp);
        }
    }
    
    sort(positive.begin(), positive.end(), pos_cmpr);
    sort(negative.begin(), negative.end());

    int pos_idx = 0;
    while(pos_idx<positive.size()){
        if(pos_idx == positive.size()-1){
            acc += positive[pos_idx];
            break;
        }
        if(positive[pos_idx] * positive[pos_idx+1] < positive[pos_idx] + positive[pos_idx+1]){
            acc += positive[pos_idx] + positive[pos_idx+1];
        }else{
            acc += (positive[pos_idx] * positive[pos_idx+1]);
        }
        pos_idx+=2;
    }

    int neg_idx = 0;
    while(neg_idx<negative.size()){
        if(neg_idx == negative.size()-1){
            acc += negative[neg_idx];
            break;
        }
        acc += (negative[neg_idx] * negative[neg_idx+1]);
        neg_idx += 2;
    }
    cout << acc;
}