#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

bool cmpr1(pair<int, int> a, pair<int, int> b){
    return a.second < b.second;
}

bool cmpr2(pair<int, int> a, pair<int, int> b){
    return a.first < b.first;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    cin >> N;
    vector<pair<int, int>> table;
    for(int i{0}; i<N; i++){
        int a,b;
        cin >> a >> b;
        table.push_back(make_pair(a,b));
    }
    sort(table.begin(), table.end(), cmpr2);
    sort(table.begin(), table.end(), cmpr1);

    int str = table[0].first;
    int end = table[0].second;
    int cnt = 1;
    for(int i{1}; i<N; i++){
        if(table[i].first >= end){
            str = table[i].first;
            end = table[i].second;
            cnt++;
        }
    }
    cout << cnt;
}