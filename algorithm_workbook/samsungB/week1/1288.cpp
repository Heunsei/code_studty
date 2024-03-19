#include <iostream>
#include <string>

using namespace std;
int main(){
    int T;
    std::cin >> T;
    // 자리수를 기록할 비트로 만든 숫자
    // 반복문을 돌릴 필요가 없이 자리수만 비교하면 되니까 연산을 줄일 수 있다
    int testCase = (1 << 10) - 1;
    for (int i{1}; i <= T; i++){
        int temp;
        cin >> temp;
        int visited {0};
        int count {0};
        while (true){
            string curValue = to_string(temp * (++count));
            for (char c : curValue){
                int num = c -'0';
                visited |= (1 << num);
            }
            if (visited == testCase){
                break;
            }
        }
        cout << '#' << i << " " << count * temp << '\n';
    }

}