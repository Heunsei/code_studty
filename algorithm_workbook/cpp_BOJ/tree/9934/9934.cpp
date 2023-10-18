#include <iostream>
#include <vector>
using namespace std;

//1<=k<=10
//2^k
int input[10024];
int k;
vector<int> arr[10];
void insertTree(int depth,int start, int end) {
	
	if (start >= end) {
		return;
	}
    // 중간값이 트리의 부모노드
	int mid = (start + end) / 2;
	// vector에 push_back
	arr[depth].push_back(input[mid]);
	// 왼쪽으로 반 , 오른쪽으로 반 들어가기(분할정복)
	insertTree(depth + 1, start, mid);
	insertTree(depth + 1, mid+1, end);

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	cin >> k;
	
	int num;
	int idx = 0;
	// 입력 받으면서 배열에 저장
	while (cin >> num) {
		input[idx++] = num;
	}

	insertTree(0,0, idx);
	// 깊이 k만큼 k에 있는 배열들을 모두 출력
	for (int i = 0; i < k; i++) {
		for (auto o : arr[i]) {
			cout << o << ' ';
		}
		cout << '\n';
	}
	return 0;
}