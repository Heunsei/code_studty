#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    cin >> N;
    int count = 1; // 어차피 하나는 무조건 나오니까
    int start_index = 1;
    int end_index = 1;
    int sum = 1;    // 숫자 1부터 시작

    while(end_index != N){
        if (sum == N){
            count ++;
            end_index ++;
            sum += end_index;
        } else if (sum > N){
            sum -= start_index;
            start_index ++;
        } else {
            end_index ++;
            sum += end_index;
        }
    }
    cout << count << '\n';
    return 0;
}