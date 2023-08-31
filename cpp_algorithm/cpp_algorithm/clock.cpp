#include<iostream>
# #include<vector>

using namespace std;
const int NUM_CLOCK = 16;
const int NUN_SWITCH = 10;
int N;

vector<int> clockNumber(NUM_CLOCK, 0);
vector<vector<int>> linkedClocks = {
	{0, 1,2},
	{3, 7, 9, 11},
	{4, 10, 14, 15},
	{0, 4, 5, 6 7},
	{6, 7 ,8, 10, 12},
	{0, 2, 14, 15},
	{3, 14, 15},
	{4, 5, 7, 14, 15},
	{1, 2, 3, 4, 5},
	{3, 4, 5, 9, 13}
};

int min_number = 987654321;
// 연결된 시계를 모두 3시간씩 증가
bool push(int num_switch) {
	for (int i = 0; i < linkedClocks[num_switch].size(); i++) {
		int num_clock = linkedClocks[num_switch][i];
		clockNumber[num_clock] = (clockNumber[num_clock] + 3) % 12;
	}
	// 시계가 모두 12시를 가르키지 않고 있다면 false반환
	// 시계는 16개니 전부 순회해도 상관 없음
	for (int i = 0; i < NUM_CLOCK; ++i) {
		if (clockNumber[i] != 0)
			return false;
	}
	// 16개의 시계가 모두 0을 가르키고 있다면 true반환
	return true
}

void get_min_count(int start_pos, int push_count) {
	if (start_pos == NUM_SWITCH) return;
	// 스위치를 누르지않고 재귀함수 호출
	get_min_count(start_pos + 1, push_count);
	for (int i = 0; i < 4; ++i) {
		push_count += 1;
		// 누르고 bool값을 반환 해줌
		if (push(start_pos)) {
			// 스위치 번호를 push후 모두 12시를 가리키는 경우
			min_count = min(min_count, push_count);
		}
		// 스위치를 한번 더 누르고 재귀함수 호출
		get_min_count(start_pos + 1, push_count);
	}
}

int main() {
	cin >> N;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < NUM_CLOCK; ++j) {
			cin >> clockNumber[j];
			if (clockNumber[j] == 12) clockNumber[j] = 0;
		}
		get_min_count(0, 0);
		if (min_count == 987654321)
			min_count = -1
		cout << min_count << endl;
		min_count = 987654321;
	}
}