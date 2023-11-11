// 회문
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void checkString(string& str){
    auto i = str.begin();  // 포인터 시작점
    auto j = str.end()-1;  // 포인터 종료지점
    int type = 0;
    int canDelete = true;
    while (i<=j){
        if (i==j){
            cout << type << '\n';
            return;
        }
        // cout << "i: " << *i << " j: " << *j << '\n';
        if(*i == *j){   // 둘의 값이 같다면 포인터를 중앙쪽으로 배치
            i++;
            j--;
        }
        else{   // 둘의 값이 다르다면 한번옮겨보고 결정해야함
            if (canDelete){ // 바꿀수있는 기회가 있다면 한번씩 옮겨보고 다음으로 진행
                auto next_i = i+1;
                auto next_j = j-1;
                auto save_i = i;
                auto save_j = j;
                if (*next_i == *j){ // 분기 두개를 모두 확인해야함
                    canDelete = false;
                    i+=2;
                    j--;
                    type = 1;
                    while (i<j){
                        if (*i==*j){
                            j--;
                            i++;
                        }else if (i+1 == j || j-1 == i){
                            
                        }
                        else{
                            type = 2;
                        }
                        if (type==1){
                            cout << type << '\n';
                            return;
                        }else break;
                    }
                }
                i = save_i;
                j = save_j;
                if (*next_j == *i){
                    canDelete = false;
                    j-=2;
                    i++;
                    type = 1;
                    while (i<j){
                        if (*i==*j){
                            j--;
                            i++;
                        }
                        else if (i+1 == j || j-1 == i){
                            cout << type << '\n';
                            return;
                        }
                        else{
                            type = 2;
                        }
                        cout << type << '\n';
                        return;
                    }
                }
                if (*next_j != *i || *next_i != *j) {
                    cout << 2 << '\n';
                    return;
                }
            } else {    // 바꿀수도 없는데 다르다? 2를 출력하고 종료
                cout << '2' << '\n';
                return;
            }
        }
    }
    cout << type << '\n';
    return;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    cin >> N;
    for (int i{0}; i<N; i++){
        string temp;
        cin >> temp;
        checkString(temp);
    }
    return 0;
}