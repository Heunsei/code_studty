#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;

// https://dev-astra.tistory.com/330
int n, m, x;
long long cnt[1001];
long long sum, ans;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for(int i = 0; i < n; i++)
    {
        cin >> x;
        sum += x;
        cnt[sum % m]++;
    }

    for(int i = 0; i <= m; i++)
    {
        ans += cnt[i] * (cnt[i] - 1) / 2;
    }

    cout << ans + cnt[0];
}