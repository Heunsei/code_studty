#include <iostream>
#include <cstring>
#include <string>
#include <set>
 
using namespace std;
 
int T, ans, p;
int a[4][4];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
bool c[10000000];
int idx[10000000];
 
void dfs(int x, int y, int num, int cnt)
{
    if (cnt == 7) {
        if (c[num] == 0) {
            c[num] = 1;
            idx[p++] = num;
            ans++;
        }
        return;
    }
    for (int k = 0; k < 4; k++) {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (nx >= 0 && nx < 4 && ny >= 0 && ny < 4)
            // 자릿수를 10을 곱하면서 1의 자리에 a[nx][ny] 값을 넣어줌
            dfs(nx, ny, num * 10 + a[nx][ny], cnt + 1);
    }
}
 
int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    register int i, j;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        ans = p = 0;
        for (i = 0; i < 4; i++)
            for (j = 0; j < 4; j++)
                cin >> a[i][j];
        for (i = 0; i < 4; i++)
            for (j = 0; j < 4; j++)
                dfs(i, j, a[i][j], 1);
        for (i = 0; i < p; i++) c[idx[i]] = 0;
        cout << '#' << tc << ' ' << ans << '\n';
    }
    return 0;
}