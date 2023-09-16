#include <iostream>
#include <algorithm>
using namespace std;
 
#define INF 987654321
#define ARR_SIZE 100 + 1 
int n, m;
int arr[ARR_SIZE][ARR_SIZE];
int from, to, weight;
 
void floyd_warshall() {
    for (int i = 1; i <= n; i++)             // i vertex를 거치는 경우
        for (int j = 1; j <= n; j++)         // from vertex
            for (int k = 1; k <= n; k++)     // to vertex
                if (arr[j][i] != INF && arr[i][k] != INF)        
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k]);
}
 
int main(){
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {        // vectex table 초기화
        for (int j = 1; j <= n; j++) {
            arr[i][j] = INF;
        }
    }
    for (int i = 0; i < m; i++) {    // from vertex에서 to vertex 입력, 가중치 입력
        cin >> from >> to >> weight;
        if (arr[from][to] > weight) 
            arr[from][to] = weight;
    }
    floyd_warshall();
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if ( i == j || arr[i][j] == INF)
                cout << 0 << " ";
            else
                cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
