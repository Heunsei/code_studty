#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;
int n;
long long result = 0;

int cmp(const pair<ll, ll> a, const pair<ll, ll> b){
    // a가 b보다 작으면 a가 앞으로 간다
    return a.second < b.second;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    vector<ll> trees(5);
    vector<ll> grow(5);
    vector<pair<ll, ll>> to_cut;
    
    for(int i{0}; i<n; i++){
        int a;
        std::cin >> a;
        trees[i] = a;
    }

    for (int i{0}; i<n; i++){
        int a;
        std::cin >> a;
        grow[i] = a;
    }
    
    for(int i{0}; i<n; i++){
        to_cut.push_back({trees[i], grow[i]});
    }
    
    std::sort(to_cut.begin(), to_cut.end(), cmp);

    for(int i{0}; i<n; i++){
        result += to_cut[i].first + to_cut[i].second * i;
    }
    cout << result;
    return 0;
}