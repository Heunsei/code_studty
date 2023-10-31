#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
vector<string> graph(20);
vector<pair<int,int>> coins;

int main(){
    int N,M;
    std::cin >> N >> M;
    for(int i{0}; i<N; i++){
        string input;
        cin >>  input;
        graph[i].append(input);
    }


    return 0;
}