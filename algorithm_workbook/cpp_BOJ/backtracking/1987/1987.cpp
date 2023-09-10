#include <iostream>
#include <algorithm>

using namespace std;

int R, C, res = 0;
char A[21][21];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };
bool visit[26];

void dfs(int n, int x, int y) {
    res = max(res, n);

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
        if (visit[A[nx][ny] - 'A']) continue;

        visit[A[nx][ny] - 'A'] = true;
        dfs(n + 1, nx, ny);
        visit[A[nx][ny] - 'A'] = false;
    }
} 

void solution() {
    visit[A[0][0] - 'A'] = true;
    dfs(1, 0, 0);

    cout << res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> R >> C;

    for (int i = 0; i < R; i++) {
        string a;
        cin >> a;
        for (int j = 0; j < C; j++) {
            A[i][j] = a[j];
        }
    }

    solution();

    return 0;
}