#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int N, K;
	int sum[100'001] = { 0, };
	int answer = -2147483647;
	cin >> N >> K;

	for (int i = 1; i <= N; i++) {
		int temp;
		cin >> temp;
		sum[i] = sum[i - 1] + temp;
	}

	for (int i = K; i <= N; i++) {
		answer = max(answer, sum[i] - sum[i - K]);
	}

	cout << answer;

	return 0;
}
