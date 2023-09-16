# include<iostream>
#include <algorithm>

#define INF 987654321
using namespace std;

int graph[101][101];
int n, m;

void floid(){
    for(int k{1}; k<n+1; k++){
        for(int a{1}; a<n+1; a++){
            for(int b{1}; b<n+1; b++){
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]);
            }
        }
    }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int start, end, distance;
    cin >> n;
    cin >> m;
    // 배열 초기화 해줘야함
    for(int i{1}; i<n+1; i++){
        for(int j{1}; j<n+1; j++)
            graph[i][j] = i == j ? 0 : INF;
    }
    // 정점들 입력
    for(int i{0}; i<m; i++){
        cin >> start >> end >> distance;
        graph[start][end] = min(graph[start][end], distance);
    }


    floid();

    for(int i{1}; i <n+1;i++){
        for(int j{1}; j<n+1; j++){
            if(i==j || graph[i][j] ==INF)
                cout << 0 << " ";
            else
                cout << graph[i][j] << " ";
        }
        cout << endl; 
    }
    return 0;
}