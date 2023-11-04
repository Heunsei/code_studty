#include <iostream>
using namespace std;

int N, M;
int acc[1025][1025] = {0,};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    // N+1 x N+1 크기의 원소가 0으로 차있는 벡터생성

    for(int i{1}; i<=N; i++){
        for(int j{1}; j<=N; j++){
            int tmp;
            cin >> tmp;
            // 배열의 합을 누적해서 저장하는 방식
            // x1, y1, 부터 x2, y2까지 직사각형 모양으로 누적합을 구할때
            // 왼쪽부분, 위쪽부분을 지우고 겹쳐지는 i-1, j-1부분을 한번 더 빼준다
            acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1] + tmp;
        }
    }

    for (int i{0}; i<M; i++){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int result = acc[x2][y2] - acc[x2][y1-1] - acc[x1-1][y2] + acc[x1-1][y1-1];
        cout << result << "\n";
    }
    return 0;
}