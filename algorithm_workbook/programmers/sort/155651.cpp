#include <string>
#include <vector>
#include<bits/stdc++.h>

using namespace std;

int maxMin = 1450;

int conTime(string time) {
    int h = stoi(time.substr(0,2));
    int m = stoi(time.substr(3,2));
    return h * 60 + m;
}

int solution(vector<vector<string>> book_time) {
    vector<int> booked (maxMin, 0);
    for(auto time: book_time){
        booked[conTime(time[0])] += 1;
        booked[conTime(time[1]) + 10] -= 1;
    }
    int answer = 0;
    for(int i{1}; i<maxMin; i++){
        booked[i] += booked[i-1];
        answer = max(answer,booked[i]);
    }
    return answer;
}