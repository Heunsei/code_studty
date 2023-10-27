#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// n개의 아케인스톤
// i번째 퀘스트를 진행하면 i번째 아케인스톤을 얻을 수있음
int n, k;
vector<long long> quest;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> k;
    for(int i{0}; i<n; i++){
        int a;
        std::cin >> a;
        quest.push_back(a);
    }

    int i = 0;
    long long int sum = 0;

    std::sort(quest.begin(), quest.end());
    
    for(long long int num : quest){
        // 정렬해놓고 얻은 아케인 스톤만큼 곱하기
        sum += num * (long long int)i;
        if (i<k) i++;
    }

    cout << sum ;
    return 0;
}