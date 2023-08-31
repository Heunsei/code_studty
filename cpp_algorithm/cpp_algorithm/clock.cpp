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
// ����� �ð踦 ��� 3�ð��� ����
bool push(int num_switch) {
	for (int i = 0; i < linkedClocks[num_switch].size(); i++) {
		int num_clock = linkedClocks[num_switch][i];
		clockNumber[num_clock] = (clockNumber[num_clock] + 3) % 12;
	}
	// �ð谡 ��� 12�ø� ����Ű�� �ʰ� �ִٸ� false��ȯ
	// �ð�� 16���� ���� ��ȸ�ص� ��� ����
	for (int i = 0; i < NUM_CLOCK; ++i) {
		if (clockNumber[i] != 0)
			return false;
	}
	// 16���� �ð谡 ��� 0�� ����Ű�� �ִٸ� true��ȯ
	return true
}

void get_min_count(int start_pos, int push_count) {
	if (start_pos == NUM_SWITCH) return;
	// ����ġ�� �������ʰ� ����Լ� ȣ��
	get_min_count(start_pos + 1, push_count);
	for (int i = 0; i < 4; ++i) {
		push_count += 1;
		// ������ bool���� ��ȯ ����
		if (push(start_pos)) {
			// ����ġ ��ȣ�� push�� ��� 12�ø� ����Ű�� ���
			min_count = min(min_count, push_count);
		}
		// ����ġ�� �ѹ� �� ������ ����Լ� ȣ��
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